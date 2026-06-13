---
name: feedback-easybot-obsidian
description: EasyBOT info ทุกอย่างต้อง save/lookup ใน ~/SecondBrain/EasyBOT/ (Obsidian) — ไม่ใช่ memory เปล่าๆ. EasyBOT ≠ EasySlip
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 71f4b0dd-89f2-43f1-883c-44845fb20d47
---

ข้อมูลเกี่ยวกับ **EasyBOT** ทุกประเภท (product specs, finance webapp, partner agreements, marketing content, research, design, decisions, แชทที่ทำเกี่ยวกับโปรเจกต์นี้) ต้องไปลงที่ Obsidian folder `~/SecondBrain/EasyBOT/`

**Why:** ผู้ใช้สั่งวันที่ 2026-06-11 ว่า "เอาทุกอย่างที่เกี่ยวกับ EasyBOT ไปใส่ไว้ในนี้... เอาไฟล์ทั้งหมด และประแชทเก่า ทุก ๆ และอนาคตต่อ ๆ ไปด้วย" — Obsidian = single source of truth สำหรับ EasyBOT (ค้นได้ง่าย, link ภายในได้, ใช้ผ่านมือถือ/ทุก device). **EasyBOT ≠ EasySlip** — คนละธุรกิจ ห้ามจำสับ

**How to apply:**
- มีข้อมูล EasyBOT ใหม่เข้ามา → append/create note ใน `~/SecondBrain/EasyBOT/` (kebab-case ชื่อไฟล์ + อัปเดต `หน้าหลัก.md` ถ้าเพิ่มไฟล์ใหม่)
- มีคำถามเรื่อง EasyBOT → ค้น `~/SecondBrain/EasyBOT/` ก่อนเสมอ
- ต้นทางไฟล์ (docx/pdf/xlsx/code) → อยู่ที่ `~/Desktop/Business/EasyBOT/` และ symlink เข้า vault ที่ `~/SecondBrain/EasyBOT/_source/`
- โครงไฟล์ปัจจุบัน: หน้าหลัก, 01-Overview, 02-Finance-Webapp, 03-Organization, 04-Marketing-Content, 05-Partnerships-Legal, 06-Research-Strategy, 07-Design-Assets, 08-Past-Chats
- แชท EasyBOT (past + future) → `_chats/YYYY-MM.md` — SessionEnd hook ที่ `~/.claude/hooks/summarize-session.sh` auto-append เข้าให้ตามเดือนเมื่อ detect คำว่า EasyBOT/easybot.finance/finance-webapp/easybot-finance-cockpit
- Memory เก็บแค่ pointer (ดู [[project_easybot_finance]]) — เนื้อหาจริงอยู่ใน Obsidian
- ระวัง: vault sync mirror memory → Obsidian แต่ EasyBOT folder = native Obsidian (แก้ที่นี่ตรงๆ ได้เลย ไม่ต้องผ่าน memory)
- **ห้ามสับสน:** "EasyBot Affiliate" ใน LINE OA broadcast เก่า = จริงๆ คือ EasySlip — อย่าเหมารวมเข้า EasyBOT
