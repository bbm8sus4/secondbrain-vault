---
name: Graphify skill installed
description: Knowledge-graph skill for Claude Code — turns any folder into queryable graph. v0.9.17 (upgraded 2026-07-17), first vault graph = EasySlip at ~/Code/secondbrain-graphs/easyslip.
type: reference
originSessionId: 7be13753-0760-437b-8848-7dfe6cb9ca55
---
**Installed:** 2026-05-03 (`pipx install graphifyy`). **Upgraded 2026-07-17: 0.6.8 → 0.9.17** — skill ใหม่ 678 บรรทัด + `references/` 8 ไฟล์, sync ครบ 3 harness (`~/.claude`, `~/.claude-warp`, `~/.claude-cmux` — เวอร์ชันต้องตรงกันเสมอ, ดู [[Harness split — เคยพัง|feedback_memory_harness_split]]). Backups: `SKILL.md.bak-0.6.8` ใน .claude และ .claude-cmux. Rollback: `pipx install --force graphifyy==0.6.8` + คืน .bak.

**Trigger:** `/graphify <path>` (+ `--wiki --obsidian --update --mode deep`), `query "<question>"`, `path "A" "B"`, `explain "X"`, `graphify merge-graphs` (รวมกราฟข้าม KB), `graphify export obsidian|html|wiki|svg`. ใหม่ใน 0.9.x: graph health check, shrink-guard (#479), query fast-path, FalkorDB.

**SecondBrain graphs (workspace นอก vault กัน auto-sync):** `~/Code/secondbrain-graphs/<kb>/graphify-out/` — ทุกอันมี graph.html + graph.json + GRAPH_REPORT.md + obsidian/ (เปิดเป็น vault แยก) + wiki/ (ยกเว้น merged ไม่มี wiki). สร้างครบ 3 แบรนด์ + merged เมื่อ 2026-07-17.
- **easyslip** — 13 ไฟล์ (3 PDF) → 66 nodes / 129 edges / 9 communities. God node #1 = สัญญา SCCN MOU. คำถาม AMBIGUOUS ค้าง: Easyslip Gateway (easy-kbank-lb) เป็นเส้น direct-KBank หรือ Thunder cross-billed?
- **thunder-solution** — 17 ไฟล์ (HTML reports + 1 PDF MOU) → 84 nodes / 117 edges / 11 communities. God node = Thunder Solution Co./MOU KBank.
- **boostsms** — dedup แล้ว 45 text + 12 img (จาก 119; ตัด logo/svg + ไฟล์ซ้ำด้วย content-hash) → 237 nodes / 379 edges / 18 communities. หมายเหตุ: รูป BoostSMS-01..08 เป็น logo variant → cluster เป็นเกาะเดี่ยว 8 ก้อน (noise ยอมรับได้).
- **merged** — custom cross-brand merge (`~/Code/secondbrain-graphs/merge_crossbrand.py`, ไม่ใช่ `graphify merge-graphs` built-in เพราะตัวนั้นแค่ prefix แยกเกาะ ไม่เชื่อม). เติมเส้น `same_entity_as` ข้ามแบรนด์ผ่าน ANCHORS map → 387 nodes / 647 edges / 22 bridges / 12 shared entities. **ผล: community c2 (companies+dashboards) กับ c5 (API pricing+cost) เป็นก้อนผสม 3 แบรนด์.** cross-brand link ทั้งหมดมาจาก bridge ที่ seed เอง (แต่ละ KB extract แยกกัน จึงไม่มี organic cross-edge). แก้ ANCHORS แล้วรัน script ซ้ำเพื่อเพิ่ม/ปรับ bridge.
- Session limit เคยตัดกลางคัน (2pm) — chunk เขียนลงดิสก์ไปแล้วเช็คก่อน re-dispatch เฉพาะที่ขาด (ประหยัด ไม่รันซ้ำ).

**นำเข้า Obsidian vault แล้ว (2026-07-17):** `~/SecondBrain/_KnowledgeGraphs/{EasySlip,Thunder,BoostSMS,_Merged-CrossBrand}/` — 845 notes + 4 graph.canvas + `หน้าหลัก.md` index. Workspace `~/Code/secondbrain-graphs/` ยังเป็น source of truth. **กติกาสำคัญตอน re-sync เข้า vault: copy แค่ `*.md` + `graph.canvas` — อย่า copy `.obsidian/` ของกราฟเข้ามา (จะทับ setting vault หลักพัง).** โฟลเดอร์ `_` ขึ้นต้น เรียงบนสุด แยกจาก PARA. หมายเหตุ: ตอนนี้ 845 ไฟล์นี้จะเข้า auto-sync + git push ทุกรอบ (ผู้ใช้เลือกเอาเข้า vault เอง แม้ขัดกติกา "graph นอก vault" เดิม).

**How to apply:**
- มีกราฟแล้ว → คำถามเกี่ยวกับ KB นั้นให้ `graphify query` ก่อน ไม่ต้องอ่านไฟล์ดิบ (ต้อง cd เข้า workspace dir ก่อน — graph.json อยู่ relative กับ cwd)
- ไฟล์ใน KB เปลี่ยน → `--update` (re-extract เฉพาะไฟล์ที่เปลี่ยน, มี SHA256 cache)
- **ห้าม set GEMINI_API_KEY/MOONSHOT_API_KEY** ตอนรันบน vault — ข้อมูลธุรกิจต้องอยู่ใน Claude เท่านั้น
- **Privacy caveat:** อย่ารันบนโฟลเดอร์ที่มี customer data/PII/secrets โดยไม่มี `.graphifyignore` (detect ข้าม sensitive ให้ระดับหนึ่ง — EasySlip run ข้าม 3 ไฟล์เอง)
- อย่า copy GRAPH_REPORT.md เข้า scan root ของ KB — ไม่งั้นรอบ `--update` ถัดไปมันจะถูกดูดเข้ากราฟเอง (self-reference noise)
