---
title: SecondBrain — Vault Index
type: index
status: live
last_verified: 2026-06-21
maintained_by: agent (per [[WIKI]])
tags: [index, vault, catalog]
---

# SecondBrain — Vault Index

> Catalog ของทุกหน้า wiki ที่สำคัญ จัดตาม PARA + Brand
> Agent อ่านก่อนตอบคำถามใหญ่ · อัพเดตเมื่อสร้าง/ลบ/ย้ายหน้าใหญ่
> ดูกฎที่ [[WIKI]]

## หน้าหลัก
- [[หน้าหลัก]] — entry point มี active work index + map ภาพรวม

## 20 Rules — Schema (กฎ wiki)
- [[WIKI]] — master schema · last_verified: 2026-06-21
- [[WIKI - Ingest Playbook]] — วิธีรับ source · last_verified: 2026-06-21
- [[WIKI - Query Playbook]] — วิธีตอบ + ratchet · last_verified: 2026-06-21
- [[WIKI - Lint Playbook]] — health check checklist · last_verified: 2026-06-21
- [[WIKI - Page Templates]] — frontmatter + template · last_verified: 2026-06-21
- [[กติกาการทำงาน]] — กติกาเก่า (ยังใช้ได้)
- [[คู่มือ vault]] — คู่มือ vault เก่า

## 01 Projects (มี deadline)
- [[01 Projects/KuanGolf/README|KuanGolf]] — Thunder Solution's golf scoring app · ก๊วนกอล์ฟไทย · LINE-native
  - [[01 Projects/KuanGolf/Brand Strategy Brain|Brand Strategy Brain]] — 7 ส่วน Business→USP
  - [[01 Projects/KuanGolf/Strategic Analysis|Strategic Analysis]] — COO assessment + paths
  - [[01 Projects/KuanGolf/Research Demand — Report|Research Demand Report]]
  - [[01 Projects/KuanGolf/Product|Product]]
  - [[01 Projects/KuanGolf/Marketing|Marketing]]
  - [[01 Projects/KuanGolf/Website & Tech|Website & Tech]]
  - [[01 Projects/KuanGolf/FAQ — Live|FAQ — Live]]
  - [[01 Projects/KuanGolf/llms.txt mirror|llms.txt mirror]]
  - [[01 Projects/KuanGolf/Vendor Quote — Taatuu x Easy Design Studio|Vendor Quote]] · imported 2026-06-21

## 02 Areas (ต่อเนื่อง)
- _(ยังไม่มี — เพิ่มเมื่อเริ่ม area งาน)_

## 03 Resources
- [[03 Resources/แผนที่ - โปรเจกต์|แผนที่ - โปรเจกต์]] — index project ทั้งหมด
- [[03 Resources/แผนที่ - กติกา|แผนที่ - กติกา]]
- [[03 Resources/แผนที่ - คู่มือ|แผนที่ - คู่มือ]]
- [[03 Resources/แผนที่ - Security|แผนที่ - Security]]
- [[03 Resources/คู่มือ - Claude Skills สำหรับ COO|คู่มือ - Claude Skills สำหรับ COO]]
- [[03 Resources/คู่มือ - ภาษาไทยสไลด์ผู้บริหาร|คู่มือ - ภาษาไทยสไลด์ผู้บริหาร]]
- [[03 Resources/คู่มือ - สไลด์ HTML ปิดบังตัวเลข|คู่มือ - สไลด์ HTML ปิดบังตัวเลข]]
- `03 Resources/AI Workshops/`
- `03 Resources/Accounting/`
- `03 Resources/COO/`
- `03 Resources/People/`
- `03 Resources/Tools/`

## 04 Archive
- _(เพิ่มเมื่อโอนของจาก projects)_

## Brand KBs (per-brand knowledge base)

### Thunder Solution
- [[Thunder Solution/หน้าหลัก]] — slip verification + LINE chatbot · เป้าปี ฿125M
- `Thunder Solution/Reports/` · `Documents/` · `Marketing/`

### EasySlip
- [[EasySlip/หน้าหลัก]] — slip verification API
- `EasySlip/Documents/`

### EasyCRM
- [[EasyCRM/หน้าหลัก]] · 9 detail pages 01-09 · LINE OA + Loyalty/CRM

### BoostSMS
- [[BoostSMS/หน้าหลัก]] · 9 detail pages 01-09 · SMS marketing platform

### EasyBOT
- [[EasyBOT/หน้าหลัก]] · 8 detail pages 01-08 · AI product + finance webapp

### Friday
- [[Friday/README|Friday]] · Telegram bot บน Cloudflare Worker (repo: my-ai-bot)
- Monthly recaps · weekly summaries · themes

## 00 Inbox (raw, รอจัด)
- [[00 Inbox/Apple Notes/README|Apple Notes import]] · 70 notes · 8 categories · 2026-06-21
  - `Customers & Projects/` · `Daily & Weekly Logs/` · `Docs & Compliance/`
  - `POS & LINE/` · `Prompt Library/` · `Roles & JD/` · `Code Snippets/` · `Todo/`
- [[00 Inbox/2026-06-11 ทดสอบระบบ Second Brain]]
- [[00 Inbox/_vault-health]]

## 10 Daily
- [[10 Daily/...|Daily notes]] (auto)
- `2026-06-21.md` (root, อาจย้ายเข้า 10 Daily)

## 30 Claude Memory (auto-mirror, read-only)
- `30 Claude Memory/MEMORY.md` — index ทุก memory pointer
- ห้ามแก้ที่นี่ — แก้ที่ต้นทาง `~/.claude-warp/projects/-Users-aexgee/memory/`

## 40 Meeting Notes (auto-sync, read-only)
- จาก repo `bbm8sus4/meeting-notes` · sync ทุก 30 นาที

---

## วิธีอัพเดต index นี้

1. หลัง ingest ใหญ่ → เพิ่ม/ย้ายบรรทัด section ที่เหมาะ
2. หลัง lint → fix bullet ที่ชี้ไปหน้าที่ถูกลบ/ย้าย
3. ใส่ `last_verified:` เป็น date ของหน้าจริง (ไม่ใช่ของ index)
4. ถ้า section ยาวเกิน 30 รายการ → แตกเป็น sub-page แล้ว link มา
