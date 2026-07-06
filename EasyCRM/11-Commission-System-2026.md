---
title: "ระบบค่าคอมมิชชั่น EasyCRM 2026"
type: entity
source: "EasyCRM/_assets/EasyCRM_Commission_Update_Summary_For_Secretary_Marketing.pdf + Google Sheet Final_EasyCRM_Commission"
source_date: 2026-06-24
imported: 2026-06-24T22:48:26
last_verified: 2026-07-06
status: live
tags: [easycrm, brand]
---

# ระบบค่าคอมมิชชั่น EasyCRM 2026

> สรุประบบคำนวณค่าคอมทีมขาย EasyCRM · อัปเดต 2026-06-24

## ไฟล์ปัจจุบัน (ใช้จริง)

**Google Sheets: `Final_EasyCRM_Commission`** — สร้างเองด้วยมือ (clean, ตัวจริง)
- 4 ชีต: `Rate setting` · `Team setting` · `Sale Record` · `SALES COMMISSION REPORT`
- เลิกใช้ไฟล์เก่า `EasyCRM-Commission-System-2026.xlsx` (8 ชีต รก) — เก็บไว้เป็น backup เฉยๆ

---

## ชีต 1 · Rate setting (อัตราค่าคอมตามแพ็กเกจ)

| คอลัมน์ | คือ | ชนิด |
|---|---|---|
| A แพ็กเกจ | Starter/Plus/Premium/Enterprise A-G | กรอก |
| B ราคารายปี | ราคาก่อน VAT | กรอก |
| C คอม% (ใหม่) | เรตดีลใหม่ | กรอก |
| D ค่าคอม Thb. | `=B×C` | สูตร |
| E คอม% (ต่ออายุ) | เรตต่ออายุ (ครึ่งเรต) | กรอก |
| F ค่าคอม Thb. (ต่ออายุ) | `=B×E` | สูตร |

- ราคา: Starter 15,588 · Plus 23,988 · Premium 35,988 · Enterprise = ใส่ราคาจริงต่อดีล
- **หมายเหตุ:** ปัจจุบันตั้งเรต = 10% ทุกแพ็กเกจ (เดิมแพลน 10/12/15 — ตรวจก่อนใช้จริง)

---

## ชีต 2 · Team setting (สัดส่วนแบ่ง % ต่อคน)

ตาราง 5 คอลัมน์ — % ที่แต่ละคนได้ ตามโหมดการจ่าย:

| ชื่อ (A) | บทบาท (B) | ระหว่างทีม (C) | ภายในทีม (D) | บุคคล (E) |
|---|---|---|---|---|
| MIZTEEN | Sales A | 70% | 35% | 100% |
| OLIVE | Sales B | 70% | 35% | 100% |
| JADI | Marketing | 30% | 30% | 100% |

**3 โหมด (ตารางหมายเหตุแถว 9-12):**
| สถานการณ์ | โหมด | สัดส่วน |
|---|---|---|
| Sales 1 + Marketing (ปกติ) | ระหว่างทีม | 70/30 |
| Sales ปิดเอง | บุคคล | 100 |
| Sales 2 + Marketing (นานๆ ที) | ภายในทีม | 35/35/30 |

**บริบทจริง:** 1 Sale/ดีล เป็นหลัก · 70/30 เสมอถ้า Sales 1 คน · 2 sales นานๆ ที

---

## ชีต 3 · Sale Record (บันทึกดีล — หัวใจ)

โครงคอลัมน์ (data เริ่มแถว 4):

| คอล | หัว | ชนิด | สูตร |
|---|---|---|---|
| A | No | สูตร | `=IF(B4="","",ROW()-3)` |
| B | วันที่ | กรอก | |
| C | ไตรมาส | สูตร | `=IF(B4="","","Q"&ROUNDUP(MONTH(B4)/3,0))` |
| D | ชื่อลูกค้า | กรอก | |
| E | ประเภท | dropdown | ใหม่/ต่ออายุ |
| F | การชำระเงิน | dropdown | |
| G | แพ็กเกจ | dropdown | |
| H | ราคาเต็ม | สูตร | `=IF(B4="","",IFERROR(VLOOKUP(G4,'Rate setting'!$A:$B,2,FALSE),0))` |
| I | ส่วนลด % | กรอก | |
| J | รายได้สุทธิ | สูตร | `=IF(B4="","",H4*(1-IF(I4="",0,I4)))` |
| K | จ่ายแบบ | dropdown | ทีม/รายคน |
| L | Sales (คน) | dropdown | จาก `'Team setting'!A3:A5` |
| M | Marketing (คน) | dropdown | จาก `'Team setting'!A3:A5` |
| N | เรต% | สูตร | `=IF(B4="","",IFERROR(VLOOKUP(G4,'Rate setting'!$A:$E,IF(E4="ต่ออายุ",5,3),FALSE),0))` |
| O | รวมค่าคอม 100% | สูตร | `รายได้สุทธิ × เรต%` |
| P | คอม Sales | สูตร | `=IF($O4="","",IF($K4="รายคน",$O4,$O4*70%))` |
| Q | คอม Marketing | สูตร | `=IF($O4="","",IF($K4="รายคน",0,$O4*30%))` |
| R | สถานะจ่าย | dropdown | |

**สูตรแบ่ง % (P, Q) — final:**
- **รายคน** → Sales ได้เต็ม (100%) · Marketing = 0
- **ทีม** → Sales 70% · Marketing 30%
- หัวคอลัมน์ P/Q ใช้ "คอม Sales" / "คอม Marketing" (ไม่ล็อก 70% เพราะ % ไม่คงที่)

---

## ชีต 4 · SALES COMMISSION REPORT (payslip รายคน/ไตรมาส)

รายงานต่อ Sales rep (เช่น Mizteen) — มี header บริษัท EASYSLIP, TOTAL REVENUE, TOTAL COMMISSION

**คอลัมน์ Deductions + Payout (หักส่วนแบ่งทีมการตลาด):**
- **Deductions** = พิมพ์ % ที่หัก ตรงๆ (เช่น `30`)
- **Payout** = `=IF($K16="","",$K16*(1-IF($L16="",0,$L16)/100))`
  (K = Commission Amount · L = Deductions · M = Payout)
- ใส่ 30 → Payout = ค่าคอม × 70%

---

## บทเรียน / decisions

- **เลิก over-engineer** — เจ้าของทำมือเองดีกว่า (8 ชีต → 4 ชีต ทำเอง)
- **dropdown ดึงจาก range** ต้องชี้ `'Team setting'!A3:A5` (เคยเป็น `=#REF!` เลยว่าง)
- **VLOOKUP ชื่อชีตไทย** ต้อง quote: `'Team setting'!` `'Rate setting'!`
- **โหมดต้องตรงคำ** — dropdown "ทีม/รายคน" ต้องตรงกับสูตร IF (เดิม "ทีม" ไม่ตรง "ระหว่างทีม" → ตกไป 100%)
- **คู่มือ HTML:** `~/SecondBrain/EasyCRM/EasyCRM-คอม-v2-คู่มือ.html`

## ที่ยังค้าง / ต้องเช็ค

- [ ] เรต Rate setting = 10% ทุกแพ็กเกจ — ยืนยันว่าตั้งใจ หรือควรเป็น 10/12/15
- [ ] dropdown M (Marketing) อาจกรองให้เหลือเฉพาะคน Marketing (ตอนนี้โชว์ทั้ง 3 ชื่อ)
- [ ] โหมด "ภายในทีม" (35/35/30) — Sale Record มี Sales ช่องเดียว ยังรองรับ 2 sales ไม่เต็ม

---

## 📋 ฟีดแบ็ก Mark (2026-06-25) — คุณวุทธอนุมัติแนวทางแล้ว

> เอกสาร `EasyCRM_Commission_Update_Summary_For_Secretary_Marketing.pdf` (Prepared by Mark)
> สถานะ: อนุมัติแนวทาง · **ทำไฟล์ใหม่ก่อน** แล้วค่อยแก้ชีตจริง

### แก่น: Lead Source เป็นตัวตัดสินการแบ่ง (ไม่ใช่ "ทีม/รายคน")
Marketing ได้ 30% **เฉพาะดีลที่ Lead มาจาก Online/Marketing** — ถ้า Sales หา Lead เอง → Sales 100%

| สถานการณ์ | Lead Source | แบ่ง | Transaction |
|---|---|---|---|
| Marketing หา Lead → Sales ปิด | Online/Marketing | 70/30 | |
| Sales หา + ปิดเอง | Sales Own | 100/0 (ไม่แบ่ง MK) | |
| 2 Sales ช่วยปิด + Marketing | (มี Second Sales) | 35/35/30 | |
| ต่ออายุ | — | เรต 5% แล้วแบ่งตาม source | Renewal |

### คอลัมน์ใหม่ใน Sale Record (ฝั่งคอม)
| ช่อง | ค่าตัวอย่าง | หน้าที่ |
|---|---|---|
| Lead Source | Online / Marketing / Sales Own / Referral | ตัดสิน MK ได้ 30% ไหม |
| Marketing Owner | JADI / ว่าง | คนสร้าง Lead |
| Closer Sales | MIZTEEN / OLIVE | คนปิดดีล |
| Second Sales | ชื่อคนที่ 2 / ว่าง | รองรับ 35/35/30 |
| Payout Type | auto จาก 3 ช่องบน | เลือกวิธีแบ่ง |

### สูตรแบ่งอัตโนมัติ
```
Payout Type = IFS(
  Second Sales<>"","35/35/30",
  AND(Lead Source<>"Sales Own", Marketing Owner<>""),"70/30",
  TRUE,"Sales 100%")
```
- คอม Closer = รวม × (0.35 ถ้า two-sales / 0.7 ถ้า 70-30 / 1 ถ้า 100%)
- คอม Second = รวม × (0.35 ถ้า two-sales / 0)
- คอม Marketing = รวม × (0.3 ถ้ามี MK / 0)

### ปัญหา Report เดิมที่ต้องแก้
- Mizteen ขาดดีล Kintsu · Olive มี Kintsu เกิน · Jadi เลขถูกแต่หัวเป็น Olive/SR002
- **สาเหตุ:** Sale Record ไม่มี Lead Source · Report กรอกเอง ไม่ดึงจาก Sale Record
- **แก้:** Report ทุกคน **ดึงจาก Sale Record อัตโนมัติ** (Source of Truth) ไม่กรอกแยก

---

## 💰 ฝั่งต้นทุน (Cost Model) — phase 2 (จากฟีดแบ็ก Mark)

### ต้นทุนปัจจุบัน (Cost Sheet)
| แพ็กเกจ | ราคาขาย | ต้นทุนสลิป | คอม 10% | รวมในชีต | กำไร | Margin |
|---|---|---|---|---|---|---|
| Starter | 15,588 | 1,980 | 1,559 | 3,539 | 12,049 | 77.3% |
| Plus | 23,988 | 3,696 | 2,399 | 6,095 | 17,893 | 74.6% |
| Premium | 35,988 | 6,600 | 3,599 | 10,199 | 25,789 | 71.7% |

ต้นทุนสลิป = จำนวนสลิป × 0.11 (Starter 18,000 / Plus 33,600 / Premium 60,000)

### ⚠️ Margin จริงหลังต้นทุนแฝง = 28-36% (ไม่ใช่ 70%)
ต้องเพิ่มต้นทุนแฝงใน Cost per Deal: Onboarding/Training · Customer Support · Server/DB · SMS/LINE · Marketing CAC · Sales Expense · Dev Maintenance · Admin/Finance · Risk/Refund (2-5%)

| แพ็กเกจ | ต้นทุนแฝงประมาณ | Margin จริงประมาณ |
|---|---|---|
| Starter | 6,500 | 35.6% |
| Plus | 9,800 | 33.7% |
| Premium | 15,600 | 28.3% |

→ ต้องคุม scope, support, customization ให้ดี

---

## ✅ ขั้นตอนถัดไป (จากฟีดแบ็ก — ยังไม่ทำ)
1. [ ] ทำ Google Sheet เวอร์ชันใหม่ก่อน (ไม่แก้ไฟล์จริงทันที)
2. [ ] เพิ่มช่อง: Lead Source, Marketing Owner, Closer Sales, Second Sales, Payout Type, Slip Volume, Deal Cost Type
3. [ ] สูตรคอมเลือก 70/30, 100%, 35/35/30 อัตโนมัติจาก Payout Type
4. [ ] Report รายคนดึงจาก Sale Record เป็นหลัก (แก้ Mizteen/Olive/Jadi mismatch)
5. [ ] ใส่ต้นทุนแฝงทุกหมวดใน Cost per Deal
6. [ ] ตรวจ 4 ดีลตัวอย่างให้ยอดตรง logic
7. [ ] ส่งคุณวุทธตรวจก่อนใช้แทนไฟล์จริง
