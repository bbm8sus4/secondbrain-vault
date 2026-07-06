#!/usr/bin/env python3
"""Second Brain health check — the watchdog the vault didn't have.

Scans ~/SecondBrain and writes a Thai report to "00 Inbox/_vault-health.md":
  - dead links      : [[wikilinks]] / [md](links) whose target note doesn't exist
  - orphan notes    : no inbound and no outbound links (hard to ever find again)
  - empty notes     : 0-byte or frontmatter-only stubs
  - mirror drift    : source memory count vs "30 Claude Memory" mirror count
  - sync freshness  : how long since the last vault auto-commit / sync log line
  - recap freshness : newest Friday weekly/monthly recap

Run on demand:  python3 ~/bin/vault-health.py
Or via launchd once a day (see com.aexgee.vault-health.plist).
Read-only except for the single report note it writes.
"""
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path.home() / "SecondBrain"
MEM_SRC = Path.home() / ".claude-warp/projects/-Users-aexgee/memory"
MIRROR = VAULT / "30 Claude Memory"
SYNC_LOG = Path.home() / "Library/Logs/secondbrain-sync.log"
REPORT = VAULT / "00 Inbox/_vault-health.md"

# folders that hold machine state / binaries, not notes to graph-check
SKIP_DIRS = {".git", ".obsidian", ".smart-env", ".trash", "_assets"}
# folders whose notes are auto-generated logs — exclude from orphan noise
ORPHAN_EXEMPT = {"_logs", "_source", "_chats", "00 Inbox", "40 Meeting Notes"}

WIKI_RE = re.compile(r"\[\[([^\]]+?)\]\]")
MD_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)   # fenced code blocks
INLINE_CODE_RE = re.compile(r"`[^`]*`")          # inline code spans


def strip_code(text: str) -> str:
    """Remove code so quoted/example [[links]] (e.g. in docs or the health report) don't count."""
    return INLINE_CODE_RE.sub("", FENCE_RE.sub("", text))


def md_notes():
    """All .md files in the vault, skipping state/binary dirs."""
    out = []
    for p in VAULT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.relative_to(VAULT).parts):
            continue
        out.append(p)
    return out


def norm_target(raw: str) -> str:
    """Strip alias (|...), heading (#...), block (^...) and .md; return basename."""
    raw = raw.split("|", 1)[0].split("#", 1)[0].split("^", 1)[0].strip()
    raw = raw.rstrip("\\")  # escaped pipe in tables: [[name\|alias]] leaves a trailing backslash
    if raw.endswith(".md"):
        raw = raw[:-3]
    return Path(raw).name  # Obsidian resolves wikilinks by basename


def asset_names():
    """Non-.md files in the vault (images, PDF, xlsx, html…) — valid link targets, not graph nodes.
    Index both full name (photo.png) and stem (photo) so extension-less links still resolve."""
    names = set()
    for p in VAULT.rglob("*"):
        if not p.is_file() or p.suffix == ".md":
            continue
        if any(part in SKIP_DIRS for part in p.relative_to(VAULT).parts):
            continue
        names.add(p.name)
        names.add(p.stem)
    return names


def human_age(ts: float) -> str:
    secs = datetime.now(timezone.utc).timestamp() - ts
    if secs < 3600:
        return f"{int(secs/60)} นาทีที่แล้ว"
    if secs < 86400:
        return f"{int(secs/3600)} ชม.ที่แล้ว"
    return f"{int(secs/86400)} วันที่แล้ว"


def main():
    notes = md_notes()
    assets = asset_names()
    by_basename = {}
    for p in notes:
        by_basename.setdefault(p.stem, []).append(p)

    dead, outbound, inbound, empty = [], {}, {}, []

    for p in notes:
        text = p.read_text(encoding="utf-8", errors="replace")
        body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL).strip()
        if not body:
            empty.append(p)

        scan = strip_code(text)  # ignore links inside code spans/blocks
        targets = set()
        for m in WIKI_RE.finditer(scan):
            targets.add(norm_target(m.group(1)))
        for m in MD_RE.finditer(scan):
            t = m.group(1)
            if t.startswith(("http://", "https://", "mailto:", "#", "file://", "obsidian://")):
                continue
            targets.add(norm_target(t))

        rel = p.relative_to(VAULT)
        outbound[rel] = set()
        for t in targets:
            if not t:
                continue
            if t in by_basename:
                outbound[rel].add(t)
                for dst in by_basename[t]:
                    inbound.setdefault(dst.relative_to(VAULT), set()).add(rel)
            elif t in assets:
                pass  # attachment exists — valid link, just not a note-graph edge
            else:
                dead.append((rel, t))

    orphans = []
    for p in notes:
        rel = p.relative_to(VAULT)
        if any(part in ORPHAN_EXEMPT for part in rel.parts):
            continue
        if not outbound.get(rel) and not inbound.get(rel):
            orphans.append(rel)

    # mirror drift
    src_count = len(list(MEM_SRC.glob("*.md"))) if MEM_SRC.is_dir() else 0
    mir_count = len(list(MIRROR.glob("*.md"))) if MIRROR.is_dir() else 0

    # sync freshness (latest vault commit)
    sync_age = "ไม่ทราบ"
    try:
        ct = subprocess.run(["git", "-C", str(VAULT), "log", "-1", "--format=%ct"],
                            capture_output=True, text=True, timeout=10)
        if ct.returncode == 0 and ct.stdout.strip():
            sync_age = human_age(float(ct.stdout.strip()))
    except Exception:
        pass

    # recap freshness
    def newest(d):
        files = list((VAULT / d).glob("*.md")) if (VAULT / d).is_dir() else []
        if not files:
            return "—"
        nf = max(files, key=lambda f: f.stat().st_mtime)
        return f"{nf.stem} ({human_age(nf.stat().st_mtime)})"

    now = f"{datetime.now():%F %T}"
    L = []
    L.append("# 🩺 Vault Health\n")
    L.append(f"> สแกนอัตโนมัติ · {now} · ไฟล์ .md ทั้งหมด {len(notes)}\n")
    status = "🟢 แข็งแรง" if not dead and not empty else "🟡 มีจุดต้องดู"
    L.append(f"**สถานะรวม: {status}**\n")

    L.append("## สรุป\n")
    L.append(f"| รายการ | ผล |")
    L.append(f"|---|---|")
    L.append(f"| 🔗 ลิงก์เสีย (dead links) | {len(dead)} |")
    L.append(f"| 🏝️ โน้ตโดดเดี่ยว (orphans) | {len(orphans)} |")
    L.append(f"| 📄 ไฟล์ว่าง/สตับ | {len(empty)} |")
    drift = "ตรงกัน ✅" if src_count == mir_count else f"⚠️ ไม่ตรง ({src_count} vs {mir_count})"
    L.append(f"| 🔄 memory source ↔ mirror | {src_count} ↔ {mir_count} — {drift} |")
    L.append(f"| ⏱️ sync ล่าสุด (vault commit) | {sync_age} |")
    L.append(f"| 📰 Friday weekly recap ล่าสุด | {newest('Friday/Weekly Recaps')} |")
    L.append(f"| 📰 Friday monthly recap ล่าสุด | {newest('Friday/Monthly Recaps')} |")
    L.append("")

    if dead:
        L.append("## 🔗 ลิงก์เสีย — ชี้ไปโน้ตที่ไม่มีอยู่\n")
        for rel, t in sorted(dead):
            L.append(f"- `{rel}` → `[[{t}]]` (ไม่พบ)")
        L.append("")
    if empty:
        L.append("## 📄 ไฟล์ว่าง/สตับ — ลบหรือเติมเนื้อหา\n")
        for p in sorted(empty):
            L.append(f"- `{p.relative_to(VAULT)}`")
        L.append("")
    if orphans:
        L.append("## 🏝️ โน้ตโดดเดี่ยว — ไม่มีลิงก์เข้า/ออก (หาเจอยาก)\n")
        for rel in sorted(orphans):
            L.append(f"- `{rel}`")
        L.append("")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"vault-health: {len(dead)} dead, {len(orphans)} orphans, {len(empty)} empty, "
          f"mirror {src_count}↔{mir_count} → {REPORT.relative_to(VAULT)}")


if __name__ == "__main__":
    main()
