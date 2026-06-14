# K06 · Loyalty Program Metrics & KPIs

> **TL;DR (EN):** Track 4 metric families — Engagement (active member %, redemption rate), Economic (incremental sales, CLV uplift), Health (earn:burn ratio, point liability), and Sentiment (NPS, referral). The single most important loyalty KPI is **incremental revenue per member** — if members don't spend more than non-members, your program is just a cost.
>
> **สรุป (TH):** วัด 4 กลุ่ม — Engagement, Economic, Health, Sentiment ตัวสำคัญที่สุดคือ **รายได้เพิ่มต่อสมาชิก** ถ้าสมาชิกไม่ใช้จ่ายมากกว่าคนทั่วไป loyalty program ก็แค่ "ค่าใช้จ่าย" ไม่ใช่ ROI

---

## 1. กรอบ 4 มิติของ KPI Loyalty

```
                Engagement ──┐
                              │
Sentiment ◀──── Loyalty ────▶ Economic
                              │
                  Health ────┘
```

| มิติ | คำถาม |
|---|---|
| **Engagement** | สมาชิก active แค่ไหน? |
| **Economic** | ทำเงินเพิ่มจริงไหม? |
| **Health** | โปรแกรมแข็งแรงไหม? |
| **Sentiment** | ลูกค้ารักไหม? |

---

## 2. 📊 Engagement Metrics

### Active Member Rate
```
= (สมาชิกที่ทำธุรกรรมใน period / สมาชิกทั้งหมด) × 100
```
- **Benchmark:** 40–60% (90 วัน), 25–35% (30 วัน) สำหรับ B2C SME
- **Red flag:** < 20% = โปรแกรมโดน lock-in แต่ไม่ใช้งาน

### Redemption Rate
```
= แต้มที่ถูกแลก / แต้มที่ถูกออก × 100
```
- **Benchmark:** 25–45% (Bond Loyalty Report)
- **Red flag:** < 10% = catalog ไม่ดึงดูด หรือสะสมยากเกินไป
- **Sweet spot:** 30–40%

### Earn:Burn Ratio
```
= แต้มที่ออก / แต้มที่แลก
```
- **Healthy:** ใกล้ 1:1 (ระยะยาว)
- **Inflation:** > 2:1 (ออกเยอะแลกน้อย → liability บวม)

### Repeat Purchase Frequency
- **Benchmark:** สมาชิก > non-member 30–50%

---

## 3. 💰 Economic Metrics

### Incremental Revenue (สำคัญที่สุด)
```
= รายได้จากสมาชิก − รายได้ที่คาดว่าจะได้ถ้าไม่มี loyalty
```
> **Test methodology:** A/B test กลุ่มสมาชิก vs control (non-member matched cohort)

### Member CLV vs Non-member CLV
```
CLV uplift % = (CLV member − CLV non-member) / CLV non-member × 100
```
- **Good loyalty program:** uplift > 25%
- **World class:** > 50% (Starbucks 3–5x)

### Program ROI
```
ROI = (Incremental gross profit − Program cost) / Program cost
```
- **Acceptable:** > 2x
- **Good:** > 4x
- **World class:** > 7x

### Cost per Active Member
```
= ต้นทุนโปรแกรม / Active members
```
- ใช้ benchmark กับ CLV — ต้องน้อยกว่า CLV/5

---

## 4. ❤️ Health Metrics

### Point Liability (สำคัญในบัญชี)
```
= แต้มคงค้างทั้งหมด × มูลค่าต่อแต้ม
```
> **ทำไมสำคัญ:** ต้องบันทึกเป็น liability ในงบการเงิน (IFRS 15) — โตเร็วโดยไม่ระวัง = หนี้ก้อนใหญ่

**กลยุทธ์ลด liability:**
- กำหนดอายุแต้ม (point expiry) — ทั่วไป 12–24 เดือน
- Burn campaign — "ดับเบิลแต้มถ้าแลกในเดือนนี้"
- Tier-based expiry (Platinum ไม่หมดอายุ)

### Breakage Rate
```
= แต้มที่หมดอายุ / แต้มที่ออก × 100
```
- **Healthy:** 15–25%
- **Red flag:** > 40% = ลูกค้ารู้สึกถูกเอาเปรียบ
- **Too low:** < 5% = แต้มแลกง่ายเกิน → ROI ของโปรแกรมต่ำ

### Member Acquisition Cost
```
= ค่า marketing สมัครสมาชิก / สมาชิกใหม่
```

### Churn Rate
```
= สมาชิกที่หายไปใน period / สมาชิกที่เริ่ม period × 100
```
- ดู [[K13-Retention-Churn]] เพิ่ม

---

## 5. 💬 Sentiment Metrics

### NPS (Net Promoter Score)
```
"จะแนะนำให้เพื่อนใช้บริการนี้ไหม?" (0–10)
NPS = % Promoters (9–10) − % Detractors (0–6)
```
- **Excellent:** > 70 (Apple, Starbucks)
- **Good:** 30–70
- **OK:** 0–30
- **Bad:** < 0

### Referral Rate
```
= ลูกค้าใหม่จากการแนะนำ / ลูกค้าใหม่ทั้งหมด × 100
```
- **Benchmark:** สมาชิก loyalty referral rate ควรสูงกว่า non-member 2–3x

### CSAT (Customer Satisfaction)
- "Rate การใช้งานโปรแกรม 1–5"
- **Good:** > 4.0

### Member Tier Progression Rate
- % สมาชิก Green ที่เลื่อนเป็น Silver ภายใน 6 เดือน
- ถ้าต่ำ < 15% = threshold สูงเกินไป

---

## 6. Dashboard ที่ EasyCRM ควรโชว์

| Top KPIs (เห็นทันที) | Drill-down |
|---|---|
| 🟢 Active Members 30d | by tier, by cohort |
| 💰 Incremental Revenue | by segment (RFM) |
| 🔄 Redemption Rate | by reward type |
| 📈 Member CLV uplift | by tenure |
| ⚠️ Point Liability | aging breakdown |

---

## 7. KPI ทำลายโปรแกรม (Vanity Metrics — อย่าวัดอย่างเดียว)

| ❌ Vanity | ทำไมไม่ดี |
|---|---|
| จำนวนสมาชิกทั้งหมด | ไม่บอก active หรือ engaged |
| แต้มทั้งหมดที่ออก | ขายเยอะ ออกเยอะ ไม่ใช่ insight |
| Likes / Followers | ไม่ correlate กับ revenue |
| App download | ดาวน์โหลดแล้วลบทิ้งก็ได้ |

> **กฎ:** ทุก vanity metric ต้องคู่กับ "engagement metric" — สมาชิก = active member, app download = DAU

---

## 8. Benchmark สรุป (Industry — ค้าปลีก/F&B ไทย)

| Metric | Bad | OK | Good | Excellent |
|---|---|---|---|---|
| Active member % (90d) | < 20% | 20–40% | 40–60% | > 60% |
| Redemption rate | < 10% | 10–25% | 25–45% | > 45% |
| CLV uplift vs non-member | < 10% | 10–25% | 25–50% | > 50% |
| Program ROI | < 1x | 1–3x | 3–6x | > 6x |
| NPS | < 0 | 0–30 | 30–60 | > 60 |
| Tier progression (Green→Silver) | < 10% | 10–20% | 20–35% | > 35% |

---

## 🔗 อ่านต่อ

- คำนวณ CLV → [[K03-Customer-Lifetime-Value]]
- ลด churn → [[K13-Retention-Churn]]
- เลือก reward strategy → [[K04-Loyalty-Program-Types]]
