#!/usr/bin/env python3
"""One-way mirror: Claude Code memory -> Obsidian vault ("30 Claude Memory").

Self-healing display names — NO hardcoded dict to maintain. Each memory file's
Thai node name is resolved in this order:
  1) `.display-names.json` sidecar (curated Thai names; edit there, not here)
  2) its title in MEMORY.md  ( "- [Title](file.md)" )  -> readable automatically
  3) the English filename stem (+ a warning in the log so it can be curated later)

So a brand-new memory is never "broken": it shows up with its index title until
someone (optionally) gives it a prettier Thai name in the sidecar.

Source of truth stays English at ~/.claude-warp/.../memory/ — edit there, never in the vault.
The vault copy is disposable: this script wipes and rewrites "30 Claude Memory" each run.
"""
import json
import re
import sys
import traceback
from datetime import datetime
from pathlib import Path

SRC = Path.home() / ".claude-warp/projects/-Users-aexgee/memory"
DST = Path.home() / "SecondBrain/30 Claude Memory"
SIDECAR = SRC / ".display-names.json"
LOG = Path.home() / "Library/Logs/secondbrain-sync.log"

INDEX_SRC = "MEMORY.md"            # canonical index filename
INDEX_DST = "ดัชนีความจำ"          # its Thai node name in the vault
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")  # [Title](file.md)
WIKI_RE = re.compile(r"\[\[([^\]]+?)\]\]")            # [[target]] or [[target|alias]]


def collapse(s: str) -> str:
    """Separator/case-insensitive key so [[cmux]], reference_cmux, ccgram-telegram all match."""
    return re.sub(r"[-_\s]", "", s.lower())


def alias_keys(stem: str):
    """Keys a body wikilink might use to refer to this memory: full slug + prefix-stripped."""
    keys = {collapse(stem)}
    for pre in ("feedback_", "project_", "reference_"):
        if stem.startswith(pre):
            keys.add(collapse(stem[len(pre):]))
    return keys


def log(msg: str) -> None:
    line = f"{datetime.now():%F %T} [py] {msg}"
    print(line)
    try:
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except Exception:
        pass  # never let logging break the sync


def sanitize(name: str) -> str:
    """Make a string safe as a macOS filename (no path separators / colons)."""
    return name.replace("/", "-").replace(":", "-").strip()


def memory_md_titles(src_dir: Path) -> dict:
    """Map 'stem' -> human title from MEMORY.md's '- [Title](stem.md)' lines."""
    titles = {}
    idx = src_dir / INDEX_SRC
    if not idx.is_file():
        return titles
    for m in LINK_RE.finditer(idx.read_text(encoding="utf-8", errors="replace")):
        title, target = m.group(1).strip(), Path(m.group(2)).name
        titles.setdefault(target[:-3] if target.endswith(".md") else target, title)
    return titles


def build_resolver(src_dir: Path):
    """Return (resolve_fn, fallback_list). resolve_fn: stem -> Thai display name."""
    curated = {}
    if SIDECAR.is_file():
        try:
            curated = {k: v for k, v in json.loads(SIDECAR.read_text(encoding="utf-8")).items()
                       if not k.startswith("_")}
        except Exception as e:
            log(f"WARN: could not parse {SIDECAR.name}: {e}")
    titles = memory_md_titles(src_dir)
    fallbacks = []

    def resolve(stem: str) -> str:
        if stem == "MEMORY":
            return INDEX_DST
        if stem in curated:
            return sanitize(curated[stem])
        if stem in titles:                       # self-healing path
            fallbacks.append(stem)
            return sanitize(titles[stem])
        fallbacks.append(stem)
        log(f"WARN: no display name for '{stem}' — used English stem; add it to {SIDECAR.name}")
        return stem

    return resolve, fallbacks


def main() -> int:
    if not SRC.is_dir():
        log(f"ERROR: source missing {SRC}")
        return 1
    DST.mkdir(parents=True, exist_ok=True)

    resolve, _ = build_resolver(SRC)
    md_files = sorted(p for p in SRC.glob("*.md") if p.is_file())

    # full stem -> "Display.md" map, used to rewrite the index links
    name_map = {p.stem: f"{resolve(p.stem)}.md" for p in md_files}

    # alias index: any slug a body might use -> the canonical stem (so inline
    # [[english_slug]] links can be retargeted to the Thai-renamed mirror file).
    alias_index = {}
    for stem in name_map:
        if stem == "MEMORY":
            continue
        for k in alias_keys(stem):
            alias_index.setdefault(k, stem)

    def fix_wikilinks(content: str) -> str:
        """Retarget [[english_slug]] -> [[Thai Display|english_slug]] in note bodies
        so the memory graph actually connects in Obsidian. Unknown slugs are left
        untouched (they may be intentional 'to-be-written' links)."""
        def repl(m):
            inner = m.group(1)
            left, sep, alias = inner.partition("|")
            target = left.split("#", 1)[0].split("^", 1)[0].strip()
            stem = alias_index.get(collapse(target))
            if not stem:
                return m.group(0)
            display = name_map[stem][:-3]
            if display == target:
                return m.group(0)
            shown = alias.strip() if sep else target
            return f"[[{display}|{shown}]]"
        return WIKI_RE.sub(repl, content)

    # wipe the mirror (it is disposable; canonical data lives in SRC)
    for f in DST.glob("*"):
        if f.is_file():
            f.unlink()

    written = 0
    for src_file in md_files:
        content = src_file.read_text(encoding="utf-8", errors="replace")
        if src_file.name == INDEX_SRC:
            # rewrite "- [Title](stem.md)" -> "- [[Display|Title]]" so the hub keeps
            # its graph edges AND survives parentheses like "(COO)" that break md-links.
            def to_wikilink(m):
                title, target = m.group(1).strip(), Path(m.group(2)).name
                display = name_map.get(target[:-3], None)
                if not display:
                    return m.group(0)
                return f"[[{display[:-3]}|{title}]]"
            content = LINK_RE.sub(to_wikilink, content)
        content = fix_wikilinks(content)
        (DST / name_map[src_file.stem]).write_text(content, encoding="utf-8")
        written += 1

    # surface English-stem leftovers (those with neither sidecar nor index title)
    _, fallbacks = build_resolver(SRC)
    english = [s for s in name_map if name_map[s][:-3] == s and s != "MEMORY"]
    log(f"synced {written} files -> {DST.name}"
        + (f"; {len(english)} still English-named: {english}" if english else "; all named"))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        log("FATAL:\n" + traceback.format_exc())
        sys.exit(1)
