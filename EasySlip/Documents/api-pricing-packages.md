---
brand: EasySlip
type: pricing
product: EasySlip API
source: easyslip.com (public pricing page)
captured: 2026-06-19
updated: 2026-06-19
---

# EasySlip API — Public Pricing & Margin Analysis

ราคาที่ EasySlip ขายลูกค้าปลายทาง + วิเคราะห์ gross margin ตาม traffic mix

---

## 1. ตารางแพ็กเกจราคาขาย (จากเว็บสาธารณะ)

| Package | ราคา/เดือน | จำนวนสลิป | เฉลี่ย/สลิป (incl VAT) | เฉลี่ย/สลิป (excl VAT) |
|---|---:|---:|---:|---:|
| Tester | ฟรี 7 วัน | 50 | — | — |
| Start | ฿99 | 250 | 0.396 | 0.370 |
| Basic | ฿350 | 1,000 | 0.350 | 0.327 |
| Starter | ฿700 | 2,500 | 0.280 | 0.262 |
| Beginner | ฿1,200 | 4,500 | 0.267 | 0.250 |
| Silver | ฿1,500 | 6,000 | 0.250 | 0.234 |
| Gold | ฿3,500 | 17,500 | 0.200 | 0.187 |
| Diamond | ฿5,000 | 35,000 | 0.143 | 0.134 |
| Premium 1 | ฿10,000 | 75,000 | 0.133 | 0.124 |
| Premium 2 | ฿30,000 | 230,000 | 0.130 | 0.121 |
| Premium 3 | ฿40,000 | 320,000 | 0.125 | 0.117 |

---

## 2. ต้นทุน KBank (จาก MOU 8 ม.ค. 2568)

**KBank-source (KBank→KBank & KBank→Other) — tiered:**
- 1 – 1M: 0.04 บ./รายการ (excl VAT)
- 1M – 3M: 0.035
- 3M – 5M: 0.03
- **5M+: 0.025** ← EasySlip อยู่ tier นี้ (volume 250M/ปี)

**Other-source (Other→KBank & Other→Other):** **0.11** บ./รายการ flat (excl VAT)

ดู: [[../../Thunder Solution/Reports/kbank-api-pricing-and-easy-thunder-crossbilling|KBank API cost detail + Thunder cross-billing]]

---

## 3. Gross Margin ตาม Traffic Mix (excl VAT)

**Cost blend ที่ scale ปัจจุบัน (5M+ tier):**

| Mix (K-src/Other) | Cost/สลิป |
|---|---:|
| 100/0 | 0.025 |
| **80/20** | **0.042** |
| **70/30** | **0.0505** |
| **60/40** | **0.059** |
| 50/50 | 0.0675 |
| 0/100 | 0.11 |

**Margin Table (% ของ revenue):**

| แพ็ก | ขาย/สลิป | 100/0 | **80/20** | **70/30** | **60/40** | 50/50 | 0/100 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Start ฿99 | 0.370 | 93% | **89%** | **86%** | **84%** | 82% | 70% |
| Basic ฿350 | 0.327 | 92% | **87%** | **85%** | **82%** | 79% | 66% |
| Starter ฿700 | 0.262 | 90% | **84%** | **81%** | **77%** | 74% | 58% |
| Beginner ฿1,200 | 0.250 | 90% | **83%** | **80%** | **76%** | 73% | 56% |
| Silver ฿1,500 | 0.234 | 89% | **82%** | **78%** | **75%** | 71% | 53% |
| Gold ฿3,500 | 0.187 | 87% | **78%** | **73%** | **68%** | 64% | 41% |
| Diamond ฿5,000 | 0.134 | 81% | **69%** | **62%** | **56%** | 50% | 18% |
| Premium 1 ฿10,000 | 0.124 | 80% | **66%** | **59%** | **52%** | 46% | 11% |
| Premium 2 ฿30,000 | 0.121 | 79% | **65%** | **58%** | **51%** | 44% | 9% |
| Premium 3 ฿40,000 | 0.117 | 79% | **64%** | **57%** | **50%** | 43% | 6% |

---

## 4. Business Insight

### Sweet spots
- **70/30 mix = sweet spot ทั้งกระดาน** — ทุกแพ็กกำไร 57–86%, ไม่มีแพ็กหลุดต่ำ 55%
- **SME tier (Start–Gold) ทนทาน** — แม้ mix 50/50 ยังกำไร 64%+
- **กำไรหลักของบริษัทมาจาก SME tier** (margin สูง × ปริมาณรวมเยอะ) แม้ MRR Enterprise = 68% ของบริษัท

### Risk zones
- **Diamond ขึ้นไป + mix แย่กว่า 60/40** = margin ต่ำกว่า 50% → เริ่มเฉียดแดงเมื่อรวม opex
- **Other-source 100%** = Diamond+ **ขาดทุนทั้งบอร์ด** (6–18%)
- ลูกค้า Enterprise รายไหนที่ mix แย่กว่า 60/40 → ควร negotiate uplift หรือเช็ค traffic mix ก่อนปิดดีล

### Margin paradox
- Enterprise = 68% ของ MRR (จาก [[easyslip-business-overview-2568-final|Business Overview 2568]])
- แต่ Enterprise = แพ็กที่ **margin ต่ำสุด**
- กำไรจริงของบริษัทเป็น **blended** — SME อุ้ม Enterprise

### Blended margin ระดับบริษัทปี 2568 (ประมาณ)
- รายได้: ฿38M (ทั้งบริษัท), ฿35.4M (เฉพาะ API)
- ราคา/สลิปเฉลี่ย: 35.4M ÷ 250M = 0.142 บ. (incl VAT) = 0.133 excl
- ถ้า mix จริง 70/30: cost 0.0505 → margin ~62%
- ถ้า mix จริง 50/50: cost 0.0675 → margin ~49%
- **ยังไม่นับ opex** (servers, dev, support, sales) ที่หักจาก gross → net

### Caveat
- **ราคาขายในตารางสมมติลูกค้าใช้เต็ม quota** — จริงๆ ลูกค้าหลายรายใช้ไม่ครบ → effective margin **สูงกว่า** ตัวเลขในตาราง
- ส่วน 95% ของ traffic ที่ผ่าน Thunder Group ใช้ rate flat 0.04 K2K + 0.11 Other (ไม่ได้รับ tier discount ของ KBank) — ทำให้ blended margin จริงต่ำกว่าตารางนี้อีกชั้น ดู [[../../Thunder Solution/Reports/kbank-api-pricing-and-easy-thunder-crossbilling|cross-billing]]

---

## Related
- [[../หน้าหลัก|EasySlip brand index]]
- [[../../Thunder Solution/บันทึกข้อตกลงการใช้บริการ_API_Slip_Verification_อีซี่สลิป|MOU KBank — ต้นทุน API (PDF)]]
- [[../../Thunder Solution/Reports/kbank-api-pricing-and-easy-thunder-crossbilling|KBank pricing + Easy×Thunder cross-billing]]
- [[easyslip-business-overview-2568-final|Business Overview 2568 — MRR Tier breakdown]]
