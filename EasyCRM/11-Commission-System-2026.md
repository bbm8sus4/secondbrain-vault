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
