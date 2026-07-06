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
import json
import re
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path.home() / "SecondBrain"
MEM_SRC = Path.home() / ".claude-warp/projects/-Users-aexgee/memory"   # primary
MEM_EXTRA = [                                                          # merged by sync (keep in step with sync-memory-to-vault.py)
    Path.home() / ".claude/projects/-Users-aexgee/memory",
    Path.home() / ".claude-cmux/projects/-Users-aexgee/memory",
    Path.home() / ".claude-ghostty/projects/-Users-aexgee/memory",
]
MIRROR = VAULT / "30 Claude Memory"
SYNC_LOG = Path.home() / "Library/Logs/secondbrain-sync.log"
REPORT = VAULT / "00 Inbox/_vault-health.md"
ENV_FILE = Path.home() / ".vault-capture.env"

# launchd jobs the vault machinery depends on — alert if any is not loaded
EXPECTED_JOBS = [
    "com.aexgee.memory-vault-sync",
    "com.aexgee.inbox-auto-ingest",
    "com.aexgee.vault-capture",
    "com.aexgee.vault-health",
]

# folders that hold machine state / binaries, not notes to graph-check
SKIP_DIRS = {".git", ".obsidian", ".smart-env", ".trash", "_assets", "_templates"}
# folders whose notes are auto-generated logs — exclude from orphan noise
ORPHAN_EXEMPT = {"_logs", "_source", "_chats", "00 Inbox", "40 Meeting Notes"}
# wiki layer that must carry schema frontmatter (type + last_verified per 20 Rules/WIKI)
FRONTMATTER_DIRS = {"01 Projects", "02 Areas", "03 Resources", "20 Rules",
                    "BoostSMS", "EasyBOT", "EasyCRM", "EasySlip", "Friday", "Thunder Solution"}
# raw-ish content inside those dirs that is exempt from the frontmatter rule
FRONTMATTER_EXEMPT = {"Clippings", "_knowledge", "_scripts", "Files", "Materials",
                      "Meetings", "Documents", "Reports", "Revenue", "Contracts", "Legal"}
STALE_DAYS = 90
REQUIRED_KEYS = ("type", "last_verified")

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


def frontmatter(text: str) -> dict:
    """Cheap YAML-lite: top-level 'key: value' pairs from the leading --- block."""
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km:
            out[km.group(1)] = km.group(2).strip().strip("'\"")
    return out


def memory_source_count() -> int:
    """Unique memory stems across all harness dirs (MEMORY index counted once) —
    must mirror the merge logic in sync-memory-to-vault.py."""
    stems = set()
    for d in [MEM_SRC] + MEM_EXTRA:
        if d.is_dir():
            stems.update(p.stem for p in d.glob("*.md"))
    return len(stems)


def dead_jobs() -> list:
    """launchd jobs from EXPECTED_JOBS that are not currently loaded."""
    try:
        out = subprocess.run(["launchctl", "list"], capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return []  # can't tell — don't false-alarm
    return [j for j in EXPECTED_JOBS if j not in out]


def unpushed_count() -> int:
    try:
        r = subprocess.run(["git", "-C", str(VAULT), "log", "@{u}..HEAD", "--oneline"],
                           capture_output=True, text=True, timeout=10)
        return len([l for l in r.stdout.splitlines() if l.strip()]) if r.returncode == 0 else 0
    except Exception:
        return 0


def telegram_alert(text: str) -> None:
    """Fire-and-forget alert. Tries the vault-capture bot first, falls back to the
    ccgram bot (send-only — safe, no getUpdates conflict). Silent no-op without config."""
    def read_env(path: Path) -> dict:
        cfg = {}
        try:
            for line in path.read_text().splitlines():
                if "=" in line and not line.lstrip().startswith("#"):
                    k, v = line.split("=", 1)
                    cfg[k.strip()] = v.strip()
        except Exception:
            pass
        return cfg

    try:
        token = chat = ""
        for env in (ENV_FILE, Path.home() / ".ccgram/.env"):
            cfg = read_env(env)
            if cfg.get("TELEGRAM_BOT_TOKEN"):
                token = cfg["TELEGRAM_BOT_TOKEN"]
                chat = cfg.get("ALLOWED_USERS", "").split(",")[0].strip()
                break
        if not token or not chat:
            return
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=json.dumps({"chat_id": chat, "text": text}).encode(),
            headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=15)
    except Exception:
        pass  # a broken alert must never break the scan


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
    fm_missing, stale, verify_q = [], [], []
    today = datetime.now()
    report_rel = REPORT.relative_to(VAULT)

    for p in notes:
        rel = p.relative_to(VAULT)
        text = p.read_text(encoding="utf-8", errors="replace")
        body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL).strip()
        if not body:
            empty.append(p)

        # schema frontmatter (type + last_verified) on wiki-layer pages
        if rel.parts[0] in FRONTMATTER_DIRS and not any(part in FRONTMATTER_EXEMPT for part in rel.parts):
            fm = frontmatter(text)
            missing = [k for k in REQUIRED_KEYS if k not in fm]
            if missing:
                fm_missing.append((rel, missing))
            else:
                try:
                    age = (today - datetime.strptime(str(fm["last_verified"])[:10], "%Y-%m-%d")).days
                    if age > STALE_DAYS:
                        stale.append((rel, fm["last_verified"], age))
                except ValueError:
                    fm_missing.append((rel, ["last_verified (รูปแบบวันที่เพี้ยน)"]))

        # standing "needs human verification" queue
        if rel != report_rel and rel.name != "log.md":
            for i, line in enumerate(text.splitlines(), 1):
                if "ต้อง verify" in line:
                    snippet = line.strip().lstrip("-#>* ").strip()
                    verify_q.append((rel, i, snippet[:110]))

        scan = strip_code(text)  # ignore links inside code spans/blocks
        targets = set()
        for m in WIKI_RE.finditer(scan):
            targets.add(norm_target(m.group(1)))
        for m in MD_RE.finditer(scan):
            t = m.group(1)
            if t.startswith(("http://", "https://", "mailto:", "#", "file://", "obsidian://")):
                continue
            targets.add(norm_target(t))

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

    # mirror drift (source = unique stems across ALL harness memory dirs)
    src_count = memory_source_count()
    mir_count = len(list(MIRROR.glob("*.md"))) if MIRROR.is_dir() else 0

    jobs_down = dead_jobs()
    unpushed = unpushed_count()

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
    drift_bad = src_count != mir_count
    hard_issues = bool(dead or empty or drift_bad or jobs_down or unpushed > 5)
    status = "🟡 มีจุดต้องดู" if hard_issues else "🟢 แข็งแรง"
    L.append(f"**สถานะรวม: {status}**\n")

    L.append("## สรุป\n")
    L.append(f"| รายการ | ผล |")
    L.append(f"|---|---|")
    L.append(f"| 🔗 ลิงก์เสีย (dead links) | {len(dead)} |")
    L.append(f"| 🏝️ โน้ตโดดเดี่ยว (orphans) | {len(orphans)} |")
    L.append(f"| 📄 ไฟล์ว่าง/สตับ | {len(empty)} |")
    drift = "ตรงกัน ✅" if not drift_bad else f"⚠️ ไม่ตรง ({src_count} vs {mir_count})"
    L.append(f"| 🔄 memory source ↔ mirror | {src_count} ↔ {mir_count} — {drift} |")
    L.append(f"| ⏱️ sync ล่าสุด (vault commit) | {sync_age} |")
    L.append(f"| ⬆️ commit ยังไม่ push | {unpushed if unpushed else '0 ✅'} |")
    jobs_cell = "ครบ " + str(len(EXPECTED_JOBS)) + " ✅" if not jobs_down else "⚠️ หาย: " + ", ".join(jobs_down)
    L.append(f"| ⚙️ launchd jobs | {jobs_cell} |")
    L.append(f"| 📋 frontmatter ขาด (backlog) | {len(fm_missing)} |")
    L.append(f"| 🕰️ หน้าเก่าเกิน {STALE_DAYS} วัน | {len(stale)} |")
    L.append(f"| ❓ คิวรอ verify | {len(verify_q)} |")
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

    def capped(items, cap, fmt):
        rows = [fmt(x) for x in items[:cap]]
        if len(items) > cap:
            rows.append(f"- …และอีก {len(items) - cap} ไฟล์")
        return rows

    if verify_q:
        L.append("## ❓ คิวรอ verify — ระบบจะทวงทุกวันจนกว่าจะเคลียร์\n")
        L += capped(sorted(verify_q), 30, lambda x: f"- `{x[0]}:{x[1]}` — {x[2]}")
        L.append("")
    if fm_missing:
        L.append(f"## 📋 หน้า wiki ที่ frontmatter ยังไม่ครบ schema (ขาด {'/'.join(REQUIRED_KEYS)})\n")
        L += capped(sorted(fm_missing), 25, lambda x: f"- `{x[0]}` — ขาด {', '.join(x[1])}")
        L.append("")
    if stale:
        L.append(f"## 🕰️ หน้าที่ไม่ได้ verify เกิน {STALE_DAYS} วัน — ควรกลับไปดู\n")
        L += capped(sorted(stale, key=lambda x: -x[2]), 25,
                    lambda x: f"- `{x[0]}` — last_verified {x[1]} ({x[2]} วัน)")
        L.append("")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"vault-health: {len(dead)} dead, {len(orphans)} orphans, {len(empty)} empty, "
          f"mirror {src_count}↔{mir_count}, fm-missing {len(fm_missing)}, stale {len(stale)}, "
          f"verify-q {len(verify_q)}, unpushed {unpushed}, jobs-down {len(jobs_down)} "
          f"→ {REPORT.relative_to(VAULT)}")

    if hard_issues:
        probs = []
        if dead:
            probs.append(f"ลิงก์เสีย {len(dead)}")
        if empty:
            probs.append(f"ไฟล์ว่าง {len(empty)}")
        if drift_bad:
            probs.append(f"mirror ไม่ตรง {src_count}≠{mir_count}")
        if jobs_down:
            probs.append("launchd หาย: " + ", ".join(j.split('.')[-1] for j in jobs_down))
        if unpushed > 5:
            probs.append(f"commit ค้างไม่ push {unpushed}")
        telegram_alert("🩺 Vault Health 🟡 มีปัญหา\n• " + "\n• ".join(probs)
                       + "\nรายละเอียด: 00 Inbox/_vault-health.md")


if __name__ == "__main__":
    main()
