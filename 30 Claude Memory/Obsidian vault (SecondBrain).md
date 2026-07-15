---
name: reference-obsidian-vault
description: "Obsidian vault \"SecondBrain\" — PARA structure, entrypoint, rules, auto-sync, read-only folders, active projects index"
metadata: 
  node_type: memory
  type: reference
  originSessionId: ea98f00f-3f56-4b4b-8e67-303a3f505331
---

# Obsidian Vault — SecondBrain

**Path:** `~/SecondBrain` · **Entrypoint:** `หน้าหลัก.md` (อ่านก่อนเสมอ)
**AI access:** mcp-obsidian → `~/SecondBrain`

## โครงสร้าง (PARA + extras)
- `00 Inbox/` — โน้ตใหม่ที่ยังไม่จัด (default location สำหรับโน้ตใหม่ทั้งหมด)
- `01 Projects/` — โปรเจกต์ที่มี deadline
- `02 Areas/` — งานต่อเนื่อง
- `03 Resources/` — playbook, แผนที่ความรู้ (`แผนที่ - โปรเจกต์/กติกา/คู่มือ/Security.md`)
- `04 Archive/` — จบแล้ว
- `05 Meeting/`, `06 Task/`, `10 Daily/`
- `20 Rules/กติกาการทำงาน.md` — กติกาที่ AI ต้องอ่านก่อนลงมือ
- `30 Claude Memory/` — **READ-ONLY mirror** จาก `~/.claude-warp/projects/-Users-aexgee/memory/` (sync ทุก 30 นาที, ชื่อไฟล์ต้นทางอังกฤษ → แปลงเป็นไทยในนี้)
- `40 Meeting Notes/` — **READ-ONLY mirror** จาก repo `meeting-notes` (sync ทุก 30 นาที)

## โฟลเดอร์โปรเจกต์ (มี `หน้าหลัก.md` + ไฟล์ 01-09 ในแต่ละโฟลเดอร์)
- `BoostSMS/` · `EasyBOT/` · `EasyCRM/`

## กติกา (จาก `20 Rules/กติกาการทำงาน.md`)
1. **ห้ามสร้างโน้ตซ้ำ** — ค้นก่อนเสมอ ถ้ามีให้อัพเดตของเดิม
2. โน้ตใหม่ไม่รู้เก็บไหน → `00 Inbox/` เท่านั้น
3. เชื่อมโน้ตด้วย `[[wikilink]]` ถ้าเกี่ยวข้อง
4. ห้ามแก้ไฟล์ใน `30 Claude Memory/` — แก้ที่ต้นทาง `~/.claude-warp/projects/-Users-aexgee/memory/`
5. งานเสร็จ → log ลง daily หรือ project note ทุกครั้ง
6. ตอบไทยสั้น ลงท้าย "ครับ"
7. Mass-send: pacing 3-5s+, snapshot, dedup ก่อน resume — ดู [[กติกา - ส่งข้อความหมู่ต้องช้า|feedback-broadcast-pacing]]
8. Cloudflare deploy: stable URL only — ดู [[กติกา - Deploy ใช้ stable URL|feedback-deploy-link]]

## ระบบ Auto-sync
- `~/bin/sync-memory-to-vault.py` — memory → vault ทุก 30 นาที (มี mapping ชื่อไฟล์อังกฤษ↔ไทย)
- `~/bin/telegram-vault-capture.py` — forward Telegram → `00 Inbox/Telegram <วันที่>.md` ภายใน 1 นาที
- Codex CLI "จำ/บันทึก" → เขียนลง `00 Inbox/` (ตั้งใน `~/.codex/AGENTS.md`)

## Active Projects (จาก `หน้าหลัก.md` + `แผนที่ - โปรเจกต์.md`)
- Thunder Solution (slip verify + LINE chatbot, ฿125M) — [[โปรเจกต์ - Thunder Solution|project-thunder-solution]]
- EasyBOT Finance — [[โปรเจกต์ - EasyBOT Finance|project-easybot-finance]]
- Friday AI (Telegram bot, repo `my-ai-bot`)
- ccgram (คุม Claude/Codex จาก Telegram, repo `cmux-telegram`)
- Dashboard รายจ่าย Thunder/EasySlip
- สรุปประชุมอัตโนมัติ — [[โปรเจกต์ - สรุปประชุมอัตโนมัติ|project-meeting-notes]]
- OCR Bot — [[โปรเจกต์ - OCR Bot|project-ocr-bot]]
- AI Orchestrator — [[โปรเจกต์ - AI Orchestrator|project-ai-orchestrator]]
- คู่มือ ChatGPT (signup สำหรับ trainee)

## เลิกทำแล้ว
- Invoice Hub — เลิก 2026-04-29 — [[โปรเจกต์ - Invoice Hub (เลิกแล้ว)|project-invoice-hub]]

## How to apply
- ก่อนเขียนโน้ตใหม่ลง vault: grep ชื่อ/topic ก่อน ถ้าเจอ → อัพเดต ไม่สร้างใหม่
- ถามเรื่องโปรเจกต์/กติกา → อ่าน `หน้าหลัก.md` + `แผนที่ - *.md` ก่อนเสมอ
- จะแก้ memory → แก้ที่ `~/.claude/projects/-Users-aexgee/memory/` (ไม่ใช่ใน vault) แล้วรอ sync
