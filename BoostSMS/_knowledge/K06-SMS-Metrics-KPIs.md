# K06 · SMS Metrics & KPIs

> **TL;DR (EN):** Track 4 metric families — Delivery (DLR rate), Engagement (CTR), Conversion (revenue/action), and Health (opt-out, bounce). The single most-overlooked metric is **opt-out rate** — even 0.5%/campaign compounds to 50%+ list loss per year. Aim: delivery > 95%, CTR > 10%, conversion > 2%, opt-out < 1%.
>
> **สรุป (TH):** วัด 4 กลุ่ม — Delivery, Engagement, Conversion, Health ตัวที่คนมองข้ามมากสุดคือ **opt-out rate** — 0.5%/แคมเปญ ทบกัน 1 ปี = 50%+ list หาย เป้า: delivery > 95%, CTR > 10%, conversion > 2%, opt-out < 1%

---

## 1. กรอบ 4 มิติของ SMS KPI

```
            Delivery ──┐
                        │
Conversion ◀───── SMS ────▶ Engagement
                        │
                Health ─┘
```

| มิติ | คำถาม |
|---|---|
| **Delivery** | SMS ถึงเบอร์ปลายทางจริงไหม? |
| **Engagement** | ลูกค้าคลิกไหม? |
| **Conversion** | ทำให้ขายได้ไหม? |
| **Health** | List แข็งแรงไหม? |

---

## 2. 📡 Delivery Metrics

### Delivery Rate (DLR)
```
= SMS ที่ถูก deliver / SMS ที่ส่ง × 100
```
- **Excellent:** > 97%
- **Good:** 95–97%
- **Acceptable:** 90–95%
- **Red flag:** < 90% → operator routing problem หรือ list ไม่ดี

### Submission Rate
```
= SMS ที่ถูก submit ไปยัง operator / SMS ทั้งหมด
```
- ปกติ > 99%
- < 99% = ผิดที่ system (sender ID, format)

### Time to Deliver
- **Transactional/OTP:** < 5 วินาที (acceptable < 30s)
- **Promotional:** < 60 วินาที (acceptable < 5 นาที)

### Carrier-level Breakdown
แยกตาม operator:
- AIS: %
- TrueMove H: %
- dtac: %

ถ้า delivery rate ของ operator หนึ่งต่ำผิดปกติ = ปัญหา routing ฝั่ง operator

---

## 3. 👆 Engagement Metrics

### CTR (Click-Through Rate)
```
= clicks / delivered SMS × 100
```
- **Excellent:** > 20%
- **Good:** 10–20%
- **Average:** 5–10%
- **Red flag:** < 5% → copy/offer ไม่ดี

> **เทียบ:** Email CTR เฉลี่ย 2.5% — SMS ดีกว่า 4–8 เท่า

### Click Time Distribution
- 30% คลิกใน 5 นาทีแรก
- 60% คลิกใน 1 ชม
- 90% คลิกใน 24 ชม

### Click-to-Open
N/A สำหรับ SMS (ไม่ track open ได้)

---

## 4. 💰 Conversion Metrics

### Conversion Rate
```
= conversions / delivered SMS × 100
```
- **Excellent:** > 5%
- **Good:** 2–5%
- **Average:** 1–2%
- **Red flag:** < 0.5%

### Revenue per Message (RPM)
```
= total revenue / SMS sent
```
- ใช้ benchmark กับ SMS cost
- ต้องสูงกว่า cost อย่างน้อย 5x

### Cost per Conversion
```
= total SMS cost / conversions
```
- เทียบกับ AOV และ margin

### ROAS (Return on Ad Spend)
```
= revenue from campaign / SMS cost
```
- **Excellent:** > 10x
- **Good:** 5–10x
- **Average:** 2–5x
- **Red flag:** < 2x (อาจขาดทุน)

### Attribution Models
- **Last-click:** SMS clicked → conversion (overstate SMS)
- **First-touch:** SMS first → eventual conversion (understate)
- **Multi-touch:** weighted (best)
- **Holdout (incremental):** sent vs control → true ROI

---

## 5. ❤️ Health Metrics

### Opt-out Rate (สำคัญที่สุด!)
```
= opt-outs / delivered SMS × 100
```
- **Healthy:** < 0.5%
- **Warning:** 0.5–1%
- **Red flag:** > 1% → ปรับ strategy ทันที

### 💡 Compound Effect
```
ส่ง 12 แคมเปญ/ปี × opt-out 0.5%/แคมเปญ
= ~6% list loss/ปี

ถ้า 2% opt-out/แคมเปญ × 12 = 24%/ปี → 1/4 list หาย
```

### Bounce Rate (เบอร์ตาย)
```
= SMS ที่ส่งไม่ถึง (permanent error) / ส่งทั้งหมด × 100
```
- **Healthy:** < 2%
- **Action:** ลบ list ที่ bounce 3+ ครั้งติดออก

### Spam Complaint
- ปกติยาก track ใน SMS (ไม่มีปุ่ม spam)
- แต่ NBTC complaint = serious → sender ban

### Block Rate by Carrier
- AIS, dtac, TrueMove แต่ละเจ้ามี anti-spam filter
- ถ้า submission ok แต่ delivery ต่ำ = carrier block
- Action: เปลี่ยน sender, ลด volume, fix content

---

## 6. SMS KPI Dashboard

| KPI | เป้า | ทำได้ | สถานะ |
|---|---|---|---|
| Delivery rate | > 95% | 97% | ✅ |
| CTR | > 10% | 8% | ⚠️ |
| Conversion rate | > 2% | 3.2% | ✅ |
| ROAS | > 5x | 8.5x | ✅ |
| Opt-out rate | < 0.5% | 0.3% | ✅ |
| Bounce rate | < 2% | 1.1% | ✅ |
| Cost per conversion | < ฿15 | ฿9.40 | ✅ |

---

## 7. Industry Benchmarks (Twilio + Salesforce 2024)

| Industry | Delivery | CTR | Conversion |
|---|---|---|---|
| Retail / E-commerce | 96% | 15% | 3.5% |
| Banking / Fintech | 98% | 22% | 4.2% |
| Healthcare | 95% | 18% | 5.1% |
| Restaurants / F&B | 94% | 12% | 2.8% |
| Travel | 97% | 19% | 3.9% |
| Education | 95% | 14% | 3.2% |

### Thai-specific (BoostSMS observation)
- Delivery: 92–95% (ต่ำกว่าโลกนิดหน่อยเพราะ filter NBTC)
- CTR: 6–10% (ต่ำกว่าโลกเพราะ link click on mobile ยาก)
- Conversion: 1–3% (ลูกค้าไทยลังเลกว่า)

---

## 8. Funnel Analysis

```
Send 10,000 SMS
   ↓ Delivery 95%
9,500 delivered
   ↓ CTR 10%
   950 clicked
   ↓ Landing page bounce 30%
   665 engaged
   ↓ Add to cart 40%
   266 carted
   ↓ Checkout 60%
   159 purchased
```

→ Overall conversion = 159/10,000 = **1.6%**
→ AOV ฿800 = ฿127,200 revenue
→ Cost = 10,000 × ฿0.30 = ฿3,000
→ **ROAS = 42x** 🎯

### Where to optimize?
- Delivery 95→97%: +200 delivered → +3 sales
- CTR 10→15%: +475 clicked → +8 sales
- LP bounce 30→20%: +95 engaged → +2 sales
- **Best lever:** CTR (copy/timing) — +8 sales = 5% lift

---

## 9. Vanity Metrics — อย่ายึด

| ❌ Vanity | ทำไมไม่ดี |
|---|---|
| Total SMS sent | ส่งเยอะไม่ใช่ดี |
| Subscribers ทั้งหมด | ไม่บอก active |
| "Reach" | ไม่บอกผล |
| Click count | ไม่บอก quality |

> **กฎ:** ทุก vanity ต้องคู่กับ outcome metric — sends + conversions, subs + engaged subs

---

## 10. Reporting Cadence

### Daily
- Delivery rate
- Opt-out alerts (spike?)
- Failed campaigns

### Weekly
- Campaign performance review
- CTR + conversion trends
- Segment performance

### Monthly
- List health (active, bounce, opt-out trends)
- ROI/ROAS
- Channel mix optimization

### Quarterly
- Strategic review
- Audience evolution
- A/B test learnings

---

## 🔗 อ่านต่อ

- Deliverability deep-dive → [[K13-Deliverability-DLR]]
- A/B test → [[K15-AB-Testing-SMS]]
- Segment เพื่อเพิ่ม conversion → [[K05-Segmentation-Targeting]]
