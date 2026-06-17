---
title: Kbank Slip Verification API — Pricing & Easy×Thunder Cross-billing
created: 2026-06-17
tags: [thunder, easyslip, kbank, api-cost, pricing, cross-billing, COO]
brand: [Thunder Solution, EasySlip]
status: working-doc
---

# Kbank Slip Verification API — Pricing & Easy×Thunder Cross-billing

> **บันทึกจากการวิเคราะห์ค่า API Kbank 6 เดือน (ธ.ค. 2568 – พ.ค. 2569)**
> เริ่มจากบิล Kbank → พบว่า Easy ใช้ Thunder เป็นทาง pass-through ~95% ของ volume → ต้องบันทึกโครงสร้างราคาก่อนวิเคราะห์ต่อ

---

## 1. ตารางค่าธรรมเนียม Kbank (ใหม่ — มีผลตั้งแต่ ม.ค. 2569)

> หน่วย: บาท/รายการ (ex-VAT)

### Slip Type: **KBank-source** (KBank→KBank, KBank→Other)
ราคาแบบ **tiered** ตามปริมาณ/เดือน:

| Tier | จำนวนรายการ | ราคา/รายการ |
|---|---|---:|
| 1 | 1 – 1,000,000 | **0.040** |
| 2 | 1,000,001 – 3,000,000 | **0.035** |
| 3 | 3,000,001 – 5,000,000 | **0.030** |
| 4 | 5,000,001 ขึ้นไป | **0.025** |

### Slip Type: **Others-source** (Other→KBank, Other→Other)
ราคา **flat ไม่มี tier**: **0.110**/รายการ

### ข้อสังเกต
- Others slip **แพงกว่า KBank slip 2.75 เท่า** (0.11 vs 0.04 ที่ tier 1)
- **Cost driver หลัก = Others slip** — การผลักลูกค้าให้สแกนจากแอป KBank ลดต้นทุนทันที
- ราคาใหม่นี้เริ่มมีผล **ม.ค. 2569** — บิล ธ.ค. 2568 ของ Thunder ยังใช้ราคาเก่า (สูงกว่า)

### Verify สูตรกับบิลจริง (ตัวอย่าง)
- EASY ธ.ค.: KBank-src 368,736 × 0.04 + Others-src 327,163 × 0.11 = 50,737.37 ✓ (ตรงเป๊ะ)
- EASY ม.ค.: 502,156 × 0.04 + 495,903 × 0.11 = 74,635.57 ✓
- EASY พ.ค.: tier (1M×0.04 + 2M×0.035 + 2M×0.030 + 6.9M×0.025) + 14.87M×0.11 = 1,978,508.54 ✓
- THUNDER ม.ค.: 393,855 + 1,924,361 = 2,318,216.10 ✓

---

## 2. สูตร Cross-billing: **Thunder เรียกเก็บ Easy**

### โครงสร้าง
Thunder ใช้บัญชี Kbank ของตัวเอง รับ slip ของ Easy เข้าระบบ แล้วเรียกเก็บกลับด้วยสูตรของตัวเอง:

| Slip Type | ราคา/รายการ (ex-VAT) | หมายเหตุ |
|---|---:|---|
| **K2K** (KBank-source ทั้งหมด) | **0.040** | flat ทุก tier — **ไม่ pass tier discount ของ Kbank ให้ Easy** |
| **Others** | **0.110** | flat (เท่า Kbank คิด Thunder) |

### การคิดเงิน
1. นับจำนวนรายการตามชนิด (K2K vs Others)
2. คูณราคาตามตารางข้างบน
3. บวก VAT 7%
4. = ยอดที่ Easy ต้องจ่าย Thunder

### Margin ที่ Thunder ได้
- บน **K2K**: Thunder จ่าย Kbank ที่ tier ขั้นสูง (0.025–0.035) แต่เก็บ Easy ที่ 0.04
  - ตัวอย่าง: 5M K2K ของ Easy → Thunder เก็บ Easy 200,000 / Thunder จ่าย Kbank เพิ่ม ~129,000 (ถ้าผสม volume Thunder เอง) → margin ~71K
- บน **Others**: ขาด margin (เท่ากับที่ Kbank คิด) — Thunder pass-through

### ตัวอย่างจริง: บิล ม.ค. 2569 (ใช้บริการ ธ.ค. 2568)
| Slip Type | จำนวน | ราคา | ยอด ex-VAT |
|---|---:|---:|---:|
| Easy slip Kbank | 5,588,585 | 0.04 | 223,543.40 |
| Easy slip Others | 6,886,057 | 0.11 | 757,466.27 |
| **รวม ex-VAT** | **12,474,642** | | **981,009.67** |
| VAT 7% | | | 68,671 |
| **รวมจ่าย (incl VAT)** | | | **฿1,049,680** |

---

## 3. ทำไมถึงสำคัญ: Easy พึ่งพา Thunder สูงมาก

### Volume เปรียบเทียบ (เดือน ธ.ค. 2568)
| ช่องทาง | จำนวนรายการ Easy | % ของรวม |
|---|---:|---:|
| ผ่าน Thunder (ที่ถูก cross-bill กลับ) | 12,474,642 | **94.7%** |
| ตรง Kbank (บัญชี Easy เอง) | 695,899 | 5.3% |
| **รวม Easy ใช้จริง** | **13,170,541** | 100% |

### Implication
- **Easy = ลูกค้ารายใหญ่ของ Thunder ในเชิง infrastructure** ไม่ใช่แค่บริษัทในเครือ
- ถ้า Thunder หยุดให้ใช้ → Easy ต้องไปสร้าง volume เองที่ Kbank → จะตกอยู่ tier 1 (0.04) แทน tier 4 (0.025) = ต้นทุนรวมพุ่งขึ้น
- การประเมิน margin ของ Easy ที่แท้จริงต้องนับ ฿1.05M+/เดือนที่จ่าย Thunder ด้วย
- Thunder รายได้ส่วนนึงมาจาก Easy โดยตรง — **revenue stream ภายในกลุ่ม**

---

## 4. ราคาเก่า (ก่อน ม.ค. 2569) — กรณี THUNDER ธ.ค. 2568

- บิล ธ.ค. = 2,125,556 (ex-VAT)
- ใช้สูตรใหม่ → ควรเป็น 1,240,622
- ส่วนต่าง **884,934** = ราคาเก่าที่ยังไม่ลด

→ **ไม่ใช่ "setup fee" หรือ "ค่าผิดเก็บ"** ตามที่เคยสงสัย เป็นเพียงสัญญาเก่าที่ราคายังไม่ลด

---

## 5. Insight สำหรับการตัดสินใจ

### ที่ต้องเลิกเชื่อ (จากการวิเคราะห์รอบแรก)
- ❌ "Kbank ไม่มี volume tier" → **ผิด** มีตั้งแต่ ม.ค. 2569
- ❌ "Setup fee ฿915K ของ THUNDER ธ.ค. ทวงได้" → **ผิด** คือราคาเก่า
- ❌ "เรท 0.074 บาท/ครั้ง" → **ผิด** เป็น mix ของ 0.04 (Kbank) + 0.11 (Others)
- ❌ "เจรจาให้ลดเรท" → **ลดไปแล้ว** สัญญาปัจจุบันคือผลของรอบเจรจาก่อน

### ที่ควรลงมือทำจริง
1. **ลด Others slip** — push ลูกค้าให้สแกนจาก KBank app เป็นทางหลัก → ประหยัด 2.75× ต่อรายการ
2. **ทบทวน margin Thunder→Easy** — Thunder กิน arbitrage บน K2K tier ที่ Easy เสียโอกาส → ควรกำหนดว่า fair หรือไม่ในกลุ่มเดียวกัน
3. **Verify บิลทุกเดือน** — ใช้สูตรนี้ตรวจ ถ้าบิลไม่ตรงสูตร = ทวง/หัก
4. **ติดตามว่าราคาเก่าของ Thunder จะมีผลย้อนหลังหรือไม่** — ถ้าเจรจาให้ราคาใหม่ effective ตั้งแต่ ธ.ค. 2568 ด้วย = ทวงคืน 884,934 ได้

---

## 6. ข้อมูลที่ยังขาด (รอผู้ใช้ส่ง)

- breakdown internal/external + K2K vs Others ของเดือน ก.พ.–พ.ค. 2569
- ยืนยัน: Easy เก็บ Thunder กลับ (สวนทาง) หรือเป็น one-way?
- บิลของ pay พ.ค. หรือ pay มิ.ย. หายไป 1 เดือน (ยังไม่ตกผลึก)

## 7. ไฟล์ที่เกี่ยวข้อง

- บิล Kbank ต้นฉบับ: `~/Desktop/02 In progress/API Calls Kbank/EASY/*.pdf`, `THUNDER/*.pdf`
- สรุปดิบ + AIDEBATE: `~/Desktop/02 In progress/API Calls Kbank/API_Calls_Kbank_Summary.xlsx` (read-only)
- Reconciliation (กำลังสร้าง): `~/Desktop/02 In progress/API Calls Kbank/API_Calls_Kbank_Reconciliation.xlsx`
- AIDEBATE log: `~/ai-debate/last_debate.md` (ส่วนใหญ่ของ insight ถูก overturn หลังพบสูตรนี้)
- บันทึกข้อตกลง API Slip Verification: `~/SecondBrain/Thunder Solution/บันทึกข้อตกลงการใช้บริการ_API_Slip_Verification_อีซี่สลิป.pdf`
