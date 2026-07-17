---
name: Graphify skill installed
description: Knowledge-graph skill for Claude Code — turns any folder into queryable graph. v0.9.17 (upgraded 2026-07-17), first vault graph = EasySlip at ~/Code/secondbrain-graphs/easyslip.
type: reference
originSessionId: 7be13753-0760-437b-8848-7dfe6cb9ca55
---
**Installed:** 2026-05-03 (`pipx install graphifyy`). **Upgraded 2026-07-17: 0.6.8 → 0.9.17** — skill ใหม่ 678 บรรทัด + `references/` 8 ไฟล์, sync ครบ 3 harness (`~/.claude`, `~/.claude-warp`, `~/.claude-cmux` — เวอร์ชันต้องตรงกันเสมอ, ดู [[Harness split — เคยพัง|feedback_memory_harness_split]]). Backups: `SKILL.md.bak-0.6.8` ใน .claude และ .claude-cmux. Rollback: `pipx install --force graphifyy==0.6.8` + คืน .bak.

**Trigger:** `/graphify <path>` (+ `--wiki --obsidian --update --mode deep`), `query "<question>"`, `path "A" "B"`, `explain "X"`, `graphify merge-graphs` (รวมกราฟข้าม KB), `graphify export obsidian|html|wiki|svg`. ใหม่ใน 0.9.x: graph health check, shrink-guard (#479), query fast-path, FalkorDB.

**SecondBrain graphs (workspace นอก vault กัน auto-sync):** `~/Code/secondbrain-graphs/<kb>/graphify-out/`
- **easyslip** — built 2026-07-17 จาก `~/SecondBrain/EasySlip` (13 ไฟล์ รวม 3 PDF): 66 nodes / 129 edges / 9 communities. God node #1 = สัญญา SCCN MOU. เปิด `graphify-out/obsidian/` เป็น vault แยกใน Obsidian (75 notes + graph.canvas), `wiki/index.md` = agent entry point. มีคำถาม AMBIGUOUS ค้าง: Easyslip Gateway (easy-kbank-lb) เป็นเส้น direct-KBank หรือ Thunder cross-billed?
- ต่อไป: Thunder Solution, BoostSMS → แล้ว `merge-graphs` หา cross-brand connections.

**How to apply:**
- มีกราฟแล้ว → คำถามเกี่ยวกับ KB นั้นให้ `graphify query` ก่อน ไม่ต้องอ่านไฟล์ดิบ (ต้อง cd เข้า workspace dir ก่อน — graph.json อยู่ relative กับ cwd)
- ไฟล์ใน KB เปลี่ยน → `--update` (re-extract เฉพาะไฟล์ที่เปลี่ยน, มี SHA256 cache)
- **ห้าม set GEMINI_API_KEY/MOONSHOT_API_KEY** ตอนรันบน vault — ข้อมูลธุรกิจต้องอยู่ใน Claude เท่านั้น
- **Privacy caveat:** อย่ารันบนโฟลเดอร์ที่มี customer data/PII/secrets โดยไม่มี `.graphifyignore` (detect ข้าม sensitive ให้ระดับหนึ่ง — EasySlip run ข้าม 3 ไฟล์เอง)
- อย่า copy GRAPH_REPORT.md เข้า scan root ของ KB — ไม่งั้นรอบ `--update` ถัดไปมันจะถูกดูดเข้ากราฟเอง (self-reference noise)
