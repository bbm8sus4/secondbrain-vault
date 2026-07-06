#!/usr/bin/env python3
"""Auto-route new files in SecondBrain/00 Inbox/ based on frontmatter rules.

Runs every 3 min via launchd. Rule-based — no AI calls, no surprises.
Web Clipper drops file with `tags: [clippings]` → moved to `03 Resources/Clippings/`.
Other files left in inbox for manual review.

Companion to:
- vault-capture (Telegram → inbox)
- sync-memory-to-vault (memory → vault mirror)
- vault-health (orphan/dead-link scan)

Schema authority: ~/SecondBrain/20 Rules/WIKI.md
"""
import re
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

VAULT = Path.home() / "SecondBrain"
INBOX = VAULT / "00 Inbox"
LOG = VAULT / "log.md"
SKIP_FILES = {"_vault-health.md"}
STABLE_SECONDS = 30  # file must be mtime-stable to be processed

# (regex over frontmatter block, destination subdir, route name)
ROUTES = [
    (re.compile(r"\bclippings\b"), "03 Resources/Clippings", "clippings"),
]


def read_frontmatter(path: Path) -> str:
    """Return frontmatter block content (without --- delimiters), or '' if absent."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    return m.group(1) if m else ""


def classify(path: Path):
    """Return (dest_subdir, route_name) or None."""
    fm = read_frontmatter(path)
    if not fm:
        return None
    # Look at the tags: line only (avoid false positives in body)
    tag_match = re.search(r"^tags:\s*(.*?)(?:^\w|\Z)", fm, re.M | re.DOTALL)
    tag_block = tag_match.group(1) if tag_match else ""
    for pattern, dest, name in ROUTES:
        if pattern.search(tag_block):
            return dest, name
    return None


def update_last_verified(path: Path):
    """Insert or update last_verified: YYYY-MM-DD in frontmatter."""
    text = path.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%d")
    if re.search(r"^last_verified:", text, re.M):
        text = re.sub(
            r"^last_verified:.*$",
            f"last_verified: {today}",
            text, count=1, flags=re.M,
        )
    else:
        text = re.sub(
            r"^---\n(.*?)\n---",
            lambda m: f"---\n{m.group(1)}\nlast_verified: {today}\n---",
            text, count=1, flags=re.DOTALL,
        )
    path.write_text(text, encoding="utf-8")


def strip_frontmatter_wikilinks(path: Path):
    """Web Clipper writes `author: "[[Channel]]"` — a wikilink to a page that will
    never exist, so every clip ships a fresh dead link. Flatten [[X]] / [[X|Y]] to
    plain text inside the frontmatter block only (body links are left alone)."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^(---\n)(.*?)(\n---)", text, re.DOTALL)
    if not m:
        return
    fm = m.group(2)
    new_fm = re.sub(r"\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]", r"\1", fm)
    if new_fm != fm:
        path.write_text(text[: m.start(2)] + new_fm + text[m.end(2):], encoding="utf-8")


def append_log(now: datetime, moves):
    """Insert log entry after the YAML header, before existing entries."""
    if not moves:
        return
    ts = now.strftime("%Y-%m-%d %H:%M")
    lines = [
        f"## [{ts}] auto-ingest | inbox sweep ({len(moves)} file(s))",
    ]
    for title, route, dest in moves:
        lines.append(f"- routed `{title}` → `{dest}` (rule: {route})")
    lines.append("- agent: `~/bin/inbox-auto-ingest.py` (rule-based, no AI)")
    block = "\n".join(lines) + "\n\n"

    existing = LOG.read_text(encoding="utf-8")
    # Find first "## [" and insert before it
    m = re.search(r"^## \[", existing, re.M)
    if m:
        idx = m.start()
        new = existing[:idx] + block + existing[idx:]
    else:
        new = existing.rstrip() + "\n\n" + block
    LOG.write_text(new, encoding="utf-8")


def main():
    if not INBOX.is_dir():
        print(f"inbox not found: {INBOX}", file=sys.stderr)
        return 1
    now = datetime.now()
    cutoff = time.time() - STABLE_SECONDS
    moves = []

    for path in sorted(INBOX.glob("*.md")):
        if path.name in SKIP_FILES:
            continue
        try:
            mtime = path.stat().st_mtime
        except FileNotFoundError:
            continue
        if mtime > cutoff:
            continue  # still being written
        classified = classify(path)
        if not classified:
            continue
        dest_subdir, route_name = classified
        dest_dir = VAULT / dest_subdir
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / path.name
        if dest.exists():
            dest = dest_dir / f"{path.stem} (auto-{now.strftime('%H%M%S')}).md"
        shutil.move(str(path), str(dest))
        try:
            update_last_verified(dest)
        except Exception as e:
            print(f"warn: could not update last_verified for {dest.name}: {e}",
                  file=sys.stderr)
        if route_name == "clippings":
            try:
                strip_frontmatter_wikilinks(dest)
            except Exception as e:
                print(f"warn: could not strip fm wikilinks for {dest.name}: {e}",
                      file=sys.stderr)
        rel_dest = str(dest.relative_to(VAULT))
        moves.append((path.stem, route_name, rel_dest))
        print(f"[{now:%H:%M:%S}] routed: {path.name} -> {rel_dest}")

    if moves:
        try:
            append_log(now, moves)
        except Exception as e:
            print(f"warn: could not append log.md: {e}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
