---
name: project-friday-bot
description: "Friday AI Telegram bot — knowledge base / \"brain\" stored in Obsidian at ~/SecondBrain/Friday/. Monthly recaps, theme deep-dives, technical reference."
metadata: 
  node_type: memory
  type: project
  originSessionId: c8ad000e-5c89-4989-bbc3-c6fc65814ab3
---

# Friday Bot — Knowledge Base

**Source code**: `~/my-ai-bot/` (Cloudflare Worker, D1 SQLite `my-ai-bot-db`)
**Knowledge base**: `~/SecondBrain/Friday/` (Obsidian — Friday's own "brain")

## โครงสร้าง Obsidian
- `~/SecondBrain/Friday/README.md` — index + technical reference + business context (people, brands)
- `~/SecondBrain/Friday/Monthly Recaps/` — สรุปเดือนรวม (`YYYY-MM ภาษาไทย.md`)
- `~/SecondBrain/Friday/Themes/` — รายงานละเอียดต่อหมวด business
- `~/SecondBrain/Friday/_assets/` — HTML renders for print/share

## ที่บันทึกแล้ว
- **2026-05 พฤษภาคม** — Monthly recap แรก (151 weekly + 426 daily summaries → 150k chars Markdown)
  - 6 themes แยกไฟล์: Thunder Ops · EasySlip+Finance · EasyBOT+Marketing · Product+Dev · EasyCRM+Sales+HR · SHIFT+Talk to Bob
  - HTML render ใน `_assets/`

## วิธีเพิ่ม recap เดือนถัดไป
1. Pull summaries จาก D1: `SELECT ... FROM summaries WHERE summary_date BETWEEN ...` (ดูตัวอย่างใน README)
2. แยกตาม chat_title → group เป็น themes
3. ใช้ parallel agents ดึง detail ตามหมวด
4. ประกอบเป็น `Monthly Recaps/YYYY-MM <ภาษาไทย>.md` + Themes แยกไฟล์
5. Update Friday/README.md ให้ link ใหม่

**Why**: User ต้องการให้ Friday bot มี "สมอง" ของตัวเองที่บันทึกแยกจาก memory ของ user หลัก เพื่อให้ AI tool ที่จะมาช่วยจัดการ Friday ในอนาคต (หรือ Friday เวอร์ชันใหม่) อ่านได้ในที่เดียว.

**How to apply**: เวลา user ถามถึงสรุปงาน/เหตุการณ์เดือน xxx ของทีม Thunder/EasySlip/EasyBOT/EasyCRM/BoostSMS/SHIFT — เช็คใน `~/SecondBrain/Friday/Monthly Recaps/` ก่อน ถ้ามีอ่านได้เลย ถ้าไม่มี ต้อง pull จาก D1 + สังเคราะห์ใหม่.

Related: [[โปรเจกต์ - OCR Bot|project_ocr_bot]], [[โปรเจกต์ - EasyCRM|project_easycrm]], [[โปรเจกต์ - EasyBOT Finance|project_easybot_finance]], [[โปรเจกต์ - BoostSMS|project_boostsms]], [[โปรเจกต์ - Thunder Solution|project_thunder_solution]], [[โปรเจกต์ - Second Brain|project_second_brain]]
