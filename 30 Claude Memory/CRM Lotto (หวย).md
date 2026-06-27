---
name: project-crm-lotto
description: "CRM Lotto (หวย) — knowledge base ใน Obsidian `~/SecondBrain/CRM หวย/`. รายงานยอดผู้ใช้รายเดือนเป็น Excel จาก Telegram. มี filter rule สำหรับ inactive users."
metadata: 
  node_type: memory
  type: project
  originSessionId: fb0d1932-f031-4fef-8953-f5aa5ce38f6f
---

# CRM หวย (Lotto)

ผู้ใช้รับรายงานยอดเล่นรายเดือนเป็นไฟล์ Excel ผ่าน Telegram (ชื่อไฟล์: `Report_YYYY-MM-DD_HH-MM-SS.xlsx`)

## Knowledge base
`~/SecondBrain/CRM หวย/` (Obsidian vault) — เก็บกฎ/วิธีใช้/รายงานสรุปทั้งหมดที่นี่. **Memory เก็บแค่ pointer**

## โครงสร้างไฟล์รายงาน
- 2 ชีต: `Cover` (ช่วงวันที่) + `Report` (ข้อมูลผู้ใช้)
- 19 คอลัมน์: ชื่อผู้ใช้ / สายรหัส AFF / ยอดฝาก + 4 หมวด × 4 ฟิลด์ (หวย, Slot & Casino, มินิเกม, รวม)
- คอลัมน์สำคัญ: **C = ยอดฝาก, S = ยอดสุทธิรวม**

## Filter rule ที่ตั้งไว้
**C = 0 AND S = 0 → ลูกค้าขาดฝาก + ไม่เล่นในเดือนนั้น**

## Default action (สำคัญ — ทำทุกครั้งโดยไม่ต้องถาม)
ผู้ใช้ส่งไฟล์ `Report_*.xlsx` (Lotto) มาเมื่อไหร่ → **กรองเก็บเฉพาะแถว C=0 AND S=0, ลบที่เหลือทั้งหมด**, save เป็นไฟล์ใหม่ `Report_<date>_inactive_only.xlsx`, รายงานจำนวน inactive ที่ได้.

## Skill ที่ทำงานนี้
`/lotto-report-filter` → `~/.claude/skills/lotto-report-filter/SKILL.md`
รายละเอียดกฎเต็มใน Obsidian: `~/SecondBrain/CRM หวย/เงื่อนไขกรอง - ลูกค้าขาดฝาก.md`

## How to apply
- รายงานใหม่ทุกเดือน → ใช้กฎเดิมกรอง inactive ก่อนคิดสถิติ
- ถ้าผู้ใช้เพิ่มเงื่อนไข/นิยามใหม่ → เพิ่มไฟล์ใน `~/SecondBrain/CRM หวย/` ไม่ใช่ memory

## Note
เนื้อหาเป็นข้อมูลเว็บพนัน (ผิดกฎหมายในไทย). ไม่ทราบบริบทธุรกิจชัด — อาจเป็น investigation / due diligence / ลูกค้าให้ดู. ไม่เกี่ยวข้องกับ EasySlip/Thunder/EasyBOT/EasyCRM/BoostSMS/Friday โดยตรง. ทำตามที่ผู้ใช้สั่งและไม่ตัดสิน
