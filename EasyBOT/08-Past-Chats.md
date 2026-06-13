# 08 — Past & Future Chats

> แชทเก่าที่กรองจาก session_log + ระบบ auto-capture ต่อจากนี้

## โครงสร้าง

- `_chats/2026-04.md` — แชทเดือน เม.ย. (เริ่ม EasyBOT Finance discovery + partner agreements)
- `_chats/2026-05.md` — พ.ค. (cost-tracker integration, QA, content marketing)
- `_chats/2026-06.md` — มิ.ย. เป็นต้นไป (auto-append จาก SessionEnd hook)

## ระบบ auto-capture

`~/.claude/hooks/summarize-session.sh` (SessionEnd hook) ถูกแก้แล้ว — ถ้า detect คำว่า `EasyBOT` / `easybot.finance` / `finance-webapp` ใน session summary จะ append บรรทัดสรุปเข้าไฟล์ `_chats/YYYY-MM.md` อัตโนมัติ (เดือนตามวันที่ session end)

**Keywords ที่ trigger:**
- `EasyBOT` (case-insensitive)
- `easybot.finance`
- `finance-webapp`
- `easybot-finance-cockpit`

**ที่ exclude (ไม่ใช่ EasyBOT):**
- `EasyBot Affiliate` ← LINE OA broadcast เก่าที่จริงๆ คือของ EasySlip
- `EasySlip`

## วิธีดูแลแชท

- ไฟล์เป็น Markdown ธรรมดา — แก้/ลบ/เพิ่ม comment ได้เสรี
- แต่ละบรรทัดมี format: `- YYYY-MM-DD HH:MM — <session_id>: <topic>: <summary>`
- ใช้ Obsidian search ค้นได้ ใช้ graph view ดูความเกี่ยวข้องได้
