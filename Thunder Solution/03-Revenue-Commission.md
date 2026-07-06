---
title: Thunder Solution — Revenue & Commission
type: resource
brand: Thunder Solution
source:
  - 30 Claude Memory/Thunder Corporate API commission (MOU).md
  - 30 Claude Memory/Kbank API pricing + Easy×Thunder cross-billing.md
  - Thunder Solution/Reports/thunder-corporate-api-sales-commission.md
  - Thunder Solution/Revenue/2569-01-to-05 Revenue Report.md
source_date: 2026-06-19
imported: 2026-07-06T00:00:00
last_verified: 2026-07-06
status: live
tags: [thunder-solution, revenue, commission, mou, kbank, cross-billing]
---

# 03 · Thunder Solution — Revenue & Commission

## 1. รายได้ ม.ค.–พ.ค. 2569 (สรุป)

| Month | Thunder Brand (฿) | MoM |
|---|---:|---:|
| ม.ค. | 4,581,765 | — |
| ก.พ. | 4,615,657 | +0.7% |
| มี.ค. | 4,718,859 | +2.2% |
| เม.ย. | 4,625,039 | −2.0% |
| **พ.ค.** | **5,105,876** | **+10.4%** |

รายงานเต็ม: [[Revenue/2569-01-to-05 Revenue Report|Revenue Report ม.ค.–พ.ค. 2569]]
Insight หลัก: Thunder API คือ growth vector (+326%) · Thunder BOT ถดถอยช้า (−1.9%)

## 2. Corporate API Sales Commission (MOU)

เอกสารหลัก: [[Reports/thunder-corporate-api-sales-commission|Corporate API — Sales Commission Model]] · Excel ที่ทีมเซลส์ใช้จริง: [[thunder-corporate-api-commission.xlsx]] (4 sheets: Summary / 1 Month / 12 Month / Per-Slip Detail มีคำอธิบาย inline ทุก sheet)

### โครงสร้าง
- ราคาขาย **flat 0.125 บ./สลิป** · 10 tiers Coperate A–J (100K → 1M สลิป/เดือน = ฿12,500 → ฿125,000/เดือน)
- สัญญา 1 เดือน หรือ 12 เดือน

### เรทคอมแนะนำ (2 cost scenarios)

| Scenario | Cost/สลิป | GP% | เรทคอม | Net margin หลังคอม |
|---|---:|---:|---|---|
| **A** Other-source 100% | 0.110 | 12.0% | **3% ของ revenue** | ~9% |
| **B** Mix blend ~30/70 | 0.077 | 38.4% | **8% ของ revenue** | ~30% |

- ตัวอย่าง Coperate J: คอม 3,750 บ./เดือน หรือ 45,000 บ./ปี (@3%) · 10,000 บ./เดือน หรือ 120,000 บ./ปี (@8%)
- Tier นอกตาราง: คอม/สลิป = **0.00375** (A) / **0.010** (B)
- มี Sales Playbook 6 ขั้นตอนในเอกสารหลัก

### ความเสี่ยงสำคัญ
⚠️ ใช้ Scenario B ต้อง **lock traffic mix K-source ≥ 30% ใน MOU** — ไม่งั้น cost ทะลุ 0.077 แล้ว margin หาย
⚠️ Net GP ≠ Net Profit — ยังไม่หัก opex ~10–20% · ตัวเลขไม่ได้แยก excl/incl VAT (ปรึกษาบัญชีก่อนใช้ทำงบ)

## 3. ต้นทุน KBank + Thunder→Easy cross-billing

เอกสารหลัก: [[Reports/kbank-api-pricing-and-easy-thunder-crossbilling|KBank pricing + cross-billing]]

### KBank pricing (effective ม.ค. 2569)
- **KBank-source** (tiered): 1–1M: 0.04 · 1M–3M: 0.035 · 3M–5M: 0.030 · 5M+: 0.025
- **Others-source**: flat **0.11**
- Verify ตรงกับบิล EASY ทุกเดือน และ THUNDER ตั้งแต่ ม.ค. 2569 · THUNDER ธ.ค. 2568 ยังราคาเก่า (จ่ายเกิน ~884K)

### สูตร cross-billing Thunder → Easy
- K2K × **0.04 flat** (Thunder ได้ margin เพราะจ่าย KBank ที่ tier 0.025–0.035)
- Others × **0.11 flat** (pass-through ไม่มี margin)
- + VAT 7%
- Easy พึ่ง Thunder **~94.7%** ของ traffic (~12.5M ครั้ง/เดือน ผ่าน Thunder · ตรง KBank แค่ 5.3% — ข้อมูล ธ.ค. 2568)

### คันโยกจริง (real levers)
1. Push ลูกค้าสแกนจากแอป KBank → ลด Others slip (แพงกว่า 2.75×)
2. ทบทวน margin Thunder→Easy (intercompany fairness)
3. Verify บิลทุกเดือนด้วยสูตรนี้ → ทวงถ้าไม่ตรง
4. ⚠️ ต้อง verify — ขอราคาใหม่ effective ย้อนหลังถึง ธ.ค. 2568 เพื่อทวง ~884K (สถานะการทวงล่าสุดไม่มีในแหล่งข้อมูล)

## หน้าที่เกี่ยวข้อง

- [[01-Overview]] · [[02-Products-Services]] · [[หน้าหลัก]]
- ฝั่ง EasySlip: [[../EasySlip/02-API-Pricing-Packages|EasySlip pricing]] · [[../EasySlip/03-Contracts-Revenue|EasySlip contracts & revenue]]
