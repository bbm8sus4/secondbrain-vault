---
brand: Thunder Solution
type: pricing-commission
product: Thunder Corporate API (MOU)
captured: 2026-06-19
updated: 2026-06-19
excel: thunder-corporate-api-commission.xlsx
---

# Thunder Corporate API — Sales Commission Model (MOU)

แพ็กเกจ Enterprise ที่ขายผ่าน MOU (ไม่ใช่แพ็กเกจมาตรฐานบนเว็บ) ลูกค้าเลือกจำนวนสลิปได้ตามต้องการ

📊 **ไฟล์ Excel ใช้จริง:** [thunder-corporate-api-commission.xlsx](thunder-corporate-api-commission.xlsx)
- 4 sheets: Summary / 1 Month / 12 Month / Per-Slip Detail
- มีคำอธิบาย inline ในแต่ละ sheet (ไม่ต้องเปิดสลับ)

---

## 1. โครงสร้างราคา

- **ราคาขาย flat: 0.125 บ./สลิป** ทุก tier
- ลูกค้าเลือก 100k → 1M สลิป/เดือน (10 tiers: Coperate A–J)
- มีตัวเลือกสัญญา 1 เดือน หรือ 12 เดือน (volume × 12)

## 2. ต้นทุน 2 scenarios

| Scenario | Cost/สลิป | GP/สลิป | GP% |
|---|---:|---:|---:|
| **A** Other-source 100% | 0.110 | 0.015 | **12.0%** |
| **B** Mix blend (~30/70 K/Other) | 0.077 | 0.048 | **38.4%** |

## 3. แนะนำเรทค่าคอมเซลส์

| Scenario | แนะนำ | เหตุผล | Net margin หลังคอม |
|---|---|---|---|
| **A** (cost 0.11) | **3% revenue** | margin บาง 12% — เกิน 5% บริษัทเหลือกำไร <5% ไม่คุ้ม opex | ~9% |
| **B** (cost 0.077) | **8% revenue** | margin หนา 38.4% — ให้แรงได้ จูงใจปิดดีลใหญ่ | ~30% |

ทางเลือก: คิดเป็น % ของ GP แทน revenue
- A @ 25% ของ GP ≈ 3% revenue
- B @ 20% ของ GP ≈ 7.7% revenue

---

## 4. ตารางค่าคอม / 1 เดือน

| Pkg | Slips | Price | Comm A (3%) | Comm B (8%) |
|---|---:|---:|---:|---:|
| A | 100,000 | 12,500 | 375 | 1,000 |
| B | 200,000 | 25,000 | 750 | 2,000 |
| C | 300,000 | 37,500 | 1,125 | 3,000 |
| D | 400,000 | 50,000 | 1,500 | 4,000 |
| E | 500,000 | 62,500 | 1,875 | 5,000 |
| F | 600,000 | 75,000 | 2,250 | 6,000 |
| G | 700,000 | 87,500 | 2,625 | 7,000 |
| H | 800,000 | 100,000 | 3,000 | 8,000 |
| I | 900,000 | 112,500 | 3,375 | 9,000 |
| J | 1,000,000 | 125,000 | 3,750 | 10,000 |

## 5. ตารางค่าคอม / 12 เดือน

| Pkg | Slips/ปี | Price/ปี | Comm A (3%) | Comm B (8%) |
|---|---:|---:|---:|---:|
| A | 1,200,000 | 150,000 | 4,500 | 12,000 |
| B | 2,400,000 | 300,000 | 9,000 | 24,000 |
| C | 3,600,000 | 450,000 | 13,500 | 36,000 |
| D | 4,800,000 | 600,000 | 18,000 | 48,000 |
| E | 6,000,000 | 750,000 | 22,500 | 60,000 |
| F | 7,200,000 | 900,000 | 27,000 | 72,000 |
| G | 8,400,000 | 1,050,000 | 31,500 | 84,000 |
| H | 9,600,000 | 1,200,000 | 36,000 | 96,000 |
| I | 10,800,000 | 1,350,000 | 40,500 | 108,000 |
| J | 12,000,000 | 1,500,000 | 45,000 | 120,000 |

---

## 6. คำอธิบายช่องในตาราง (Field Guide)

| ช่อง | สูตร | ความหมาย / ตัวอย่าง Coperate J |
|---|---|---|
| Package | — | ระดับแพ็กเกจ MOU (Coperate A → J) ตามจำนวนสลิปที่ลูกค้าซื้อ |
| Slips/period | base × ตัวคูณ (1 หรือ 12) | จำนวนสลิปทั้งหมดในรอบสัญญา · J = 1,000,000 (1mo) / 12,000,000 (12mo) |
| Price/period | Slips × 0.125 | รายได้รวมที่ EasySlip รับ · J = 125,000 (1mo) / 1,500,000 (12mo) |
| Cost (A) | Slips × 0.11 | ต้นทุนรวมที่จ่าย KBank · J = 110,000 (1mo) / 1,320,000 (12mo) |
| GP (A) | Price − Cost | กำไรขั้นต้น Scenario A · J = 15,000 (1mo) / 180,000 (12mo) |
| Comm @3% | Price × 0.03 | ค่าคอมเซลส์ Scenario A · J = 3,750 (1mo) / 45,000 (12mo) |
| Net GP (A) | GP − Comm | กำไรสุทธิหลังหักคอม · J = 11,250 (1mo) / 135,000 (12mo) |
| Cost (B) | Slips × 0.077 | ต้นทุน mix blend · J = 77,000 (1mo) / 924,000 (12mo) |
| GP (B) | Price − Cost | กำไรขั้นต้น Scenario B · J = 48,000 (1mo) / 576,000 (12mo) |
| Comm @8% | Price × 0.08 | ค่าคอมเซลส์ Scenario B · J = 10,000 (1mo) / 120,000 (12mo) |
| Net GP (B) | GP − Comm | กำไรสุทธิหลังหักคอม · J = 38,000 (1mo) / 456,000 (12mo) |

## 7. ค่าคอมต่อสลิป (สำหรับ tier นอกตาราง)

| รายการ | Scenario A | Scenario B |
|---|---:|---:|
| ราคาขาย/สลิป | 0.125 | 0.125 |
| ต้นทุน/สลิป | 0.110 | 0.077 |
| GP/สลิป | 0.015 | 0.048 |
| **ค่าคอม/สลิป** | **0.00375** | **0.010** |
| Net GP/สลิป | 0.01125 | 0.038 |

**ตัวอย่างใช้งาน:** ลูกค้าซื้อ 250,000 สลิป (นอกตาราง)
- Scenario A: ค่าคอม = 250,000 × 0.00375 = **937.50 บ.** · บริษัทเหลือ 2,812.50 บ.
- Scenario B: ค่าคอม = 250,000 × 0.01 = **2,500 บ.** · บริษัทเหลือ 9,500 บ.

---

## 8. Sales Playbook (6 ขั้นตอน)

| Step | ทำอะไร |
|---|---|
| 1 | เช็คก่อน: ลูกค้า traffic เป็น K-src/Other เท่าไร — ถ้าไม่รู้ → ใช้ Scenario A safe |
| 2 | ถาม budget ลูกค้า → ดูว่าตรงกับ Coperate ตัวไหน |
| 3 | อ่านช่อง Comm ของ Scenario ที่ใช้ → คือยอดที่เซลส์จะได้ |
| 4 | ดูช่อง Net GP → ดูว่าบริษัทเหลือกำไรเท่าไรหลังจ่ายเซลส์ |
| 5 | ถ้าใช้ Scenario B ต้องเขียนใน MOU: ลูกค้ารับประกัน K-src ≥ 30% |
| 6 | ถ้า tier ลูกค้านอกตาราง (เช่น 250k สลิป) → ใช้ Per-Slip Detail คูณเอง |

---

## 9. ข้อควรระวัง (Trade-off)

### Scenario A — cost 0.11 (Other 100%)
- ถ้าคิดเรทคอมเกิน 5% net margin ติดลบเมื่อรวม opex
- เหมาะถ้ารู้แน่ว่าลูกค้า traffic เป็น Other-source เกือบทั้งหมด
- ราคา flat 0.125 ที่ขายเหนือ cost แค่ 0.015 — sensitive มาก

### Scenario B — cost 0.077 (mix blend)
- **ต้อง lock traffic mix ใน MOU** ไม่งั้นถ้าลูกค้าใช้ Other มากกว่าคาด cost จะทะลุ 0.077 = margin หาย
- ระบุใน MOU: "ลูกค้ารับประกัน K-source ≥ 30% ของ traffic หรือ EasySlip มีสิทธิ์ปรับราคา"
- ถ้าทำได้ scenario นี้คุ้มทั้งสองฝ่าย เซลส์ได้แรง บริษัทได้ margin 30%

### ทั่วไป
- ราคา flat 0.125 ไม่ใช่ tier discount — แพ็กใหญ่ไม่ได้กำไรเพิ่ม % ต่างจาก Web Pricing
- Net GP ≠ Net Profit — ยังไม่หัก opex (server, dev, support, sales operation) ~10–20%
- ตัวเลขไฟล์เป็นราคา flat ตาม MOU ไม่ได้แยก excl/incl VAT — ปรึกษาบัญชีก่อนใช้คำนวณงบ

---

## Related
- [[../../EasySlip/Documents/api-pricing-packages|EasySlip API public pricing — margin matrix]]
- [[kbank-api-pricing-and-easy-thunder-crossbilling|KBank cost + Thunder cross-billing]]
- [[../บันทึกข้อตกลงการใช้บริการ_API_Slip_Verification_อีซี่สลิป|MOU KBank PDF]]
