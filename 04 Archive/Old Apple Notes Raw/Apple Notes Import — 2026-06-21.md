---
title: Apple Notes Import — 2026-06-21 (post-triage manifest)
type: archive
source: Apple Notes app (70 notes export)
source_date: 2026-06-21
imported: 2026-06-21
ingested: 2026-06-21T14:30
last_verified: 2026-06-21
status: archived
tags: [archive, import, manifest, apple-notes]
related:
  - "[[index]]"
  - "[[log]]"
---

# Apple Notes Import — 2026-06-21 (post-triage manifest)

> Record ของ 70 Apple Notes ที่ import เข้า vault เมื่อ 2026-06-21 13:56 และ triage จบในวันเดียวกัน 14:30
> ไฟล์ทั้งหมดถูกย้ายไปที่เหมาะสมแล้ว — record นี้ไว้ตรวจสอบย้อนหลัง

## Workflow (ที่ทำ)
1. **Export**: `osascript` + pandoc HTML→markdown (script: `/tmp/notes_export/export.py`)
2. **Image extraction**: base64 inline → ไฟล์จริง 40 images
3. **Categorize**: by title pattern → 8 categories
4. **Triage**: 3 tier (high/medium/low) — ดู `[[log]]` วันที่ 2026-06-21

## ปลายทางสุดท้ายของ 70 notes

| ต้นทาง (Apple Notes category) | จำนวน | ปลายทาง |
|---|---|---|
| Customers & Projects | 6 | 1 → `01 Projects/HUG COMPANY/` (SRS) · 1 → `03 Resources/People/` (บ๊อบ) · 1 → `Thunder Solution/Documents/` (API Gen QR) · 2 → `04 Archive/Old Planning/` (Easy Exchange, บ้านแชร์) · 1 → `01 Projects/KuanGolf/` (Vendor Quote) + raw → `04 Archive/Old Apple Notes Raw/` |
| Prompt Library | 31 | `03 Resources/Prompt Library/` + README index |
| Daily & Weekly Logs | 15 | 14 → `04 Archive/Old Job Logs/` · 1 (COO Daily Log) → `02 Areas/` |
| Roles & JD | 7 | 5 → `03 Resources/People/Job Descriptions/` + README · 2 ("ที่ทำงานเดิม") → `04 Archive/Old Job Logs/` |
| POS & LINE | 5 | `04 Archive/Old Job POS/` |
| Code Snippets | 3 | `04 Archive/Old Snippets/` |
| Docs & Compliance | 2 | `03 Resources/Compliance/` |
| Todo | 1 | `04 Archive/Old Job Logs/` |
| **รวม** | **70** | |

## Attachments
- 40 รูปย้ายจาก `_attachments/` ใน Apple Notes folder ไปที่ vault root `_attachments/`
- เหตุผล: wiki-link `[[_attachments/...]]` resolve จาก vault root → ใช้ได้ทุกหน้าใน vault

## ของที่ถูก deprecate
- README ต้นฉบับมี link ไปไฟล์ original locations ใน `00 Inbox/Apple Notes/<category>/` — link เหล่านั้น **เสียทั้งหมด** เพราะไฟล์ถูกย้าย
- จะใช้ทำอะไร? — แค่ตรวจ provenance: ถ้าไฟล์ไหนมี `source: Apple Notes #N` ที่ frontmatter → match กับ `note_index` ของไฟล์นั้น
