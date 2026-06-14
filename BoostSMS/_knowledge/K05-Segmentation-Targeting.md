# K05 · Segmentation & Targeting

> **TL;DR (EN):** SMS is expensive per message, so segmentation is the #1 ROI lever. The fastest wins: send only to active/recent customers (drop dormant), separate by lifecycle stage (new vs returning vs at-risk), and remove non-converters from promotional lists. Even a simple 3-segment split (Active / Lapsed / VIP) can triple ROI vs blasting all contacts.
>
> **สรุป (TH):** SMS แพง → segmentation คือ **lever ROI อันดับ 1** วินเร็วสุด: ส่งให้คน active เท่านั้น (ตัด dormant), แยกตาม lifecycle (ใหม่/กลับมา/at-risk), เอาคนไม่ convert ออกจาก list โปร แค่แบ่ง 3 กลุ่มง่าย ๆ (Active/Lapsed/VIP) ROI พุ่ง 3 เท่าทันที vs ส่งหว่าน

---

## 1. ทำไม Segmentation สำคัญที่สุดใน SMS

### 💰 Math
- ส่งหว่าน 10,000 คน × ฿0.30 = ฿3,000 → 1% convert = 100 คน → ฿30/conv
- ส่งกลุ่ม targeted 2,000 คน × ฿0.30 = ฿600 → 8% convert = 160 คน → **฿3.75/conv**

**ROI ดีขึ้น 8x** จากการ segment

### 🎯 SMS = Permission Medium
- ลูกค้าให้ permission ไว้ใจ
- ส่งของไม่ relevant = ผิด trust = unsubscribe
- ทุก SMS = chance ที่ลูกค้าจะ opt-out

---

## 2. Segmentation Layers

### 🔹 Layer 1: Demographic
- Age range (Gen Z, Millennial, Gen X, Boomer)
- Gender
- Location (กทม vs ตจว, จังหวัด)
- Language

### 🔹 Layer 2: Behavioral
- Purchase history (RFM, ดู [[../../EasyCRM/_knowledge/K02-RFM-Segmentation|RFM]])
- Last activity date
- Browse/cart abandonment
- App engagement

### 🔹 Layer 3: Lifecycle Stage
- New (สมัคร 0–30 วัน)
- Active (transact ใน 90 วัน)
- Loyal (transact > 5 ครั้ง/ปี)
- At-risk (ไม่ transact 60–90 วัน)
- Lapsed (ไม่ transact > 90 วัน)
- Dormant (> 180 วัน)

### 🔹 Layer 4: Preference
- Categories ที่ซื้อบ่อย
- Channel preference (SMS vs LINE)
- Frequency tolerance

### 🔹 Layer 5: Predictive
- Predicted CLV
- Churn probability
- Next-best-action

---

## 3. 5 Segments ที่ทุก SME ควรมี (Minimum)

### 1️⃣ 🌟 VIP / Loyal (top 10–20%)
- High value, high frequency
- ส่ง: exclusive offer, early access, premium content
- ความถี่: ปานกลาง (2–4 ครั้ง/เดือน)

### 2️⃣ ✅ Active (กลาง 50–60%)
- ซื้อล่าสุด 30–90 วัน
- ส่ง: relevant promo, loyalty alerts
- ความถี่: 1–2 ครั้ง/สัปดาห์

### 3️⃣ ⚠️ At-risk (10–20%)
- ห่างไป 60–90 วัน
- ส่ง: win-back, ส่วนลดพิเศษ
- ความถี่: 1 ครั้ง/สัปดาห์ ใน window

### 4️⃣ 💤 Lapsed (10–20%)
- ห่างไป > 90 วัน
- ส่ง: re-engagement campaign, big offer
- ความถี่: 1–2 ครั้ง/เดือน

### 5️⃣ 👋 New (สมัคร < 30 วัน)
- ลูกค้าใหม่
- ส่ง: welcome drip, education
- ความถี่: 1 ครั้ง/สัปดาห์ (sequence)

---

## 4. RFM สำหรับ SMS (เร็วสุด)

ใช้ RFM 3×3×3 = 27 segments → ตัดเหลือ 5 กลุ่มหลัก

| RFM Code | Segment | SMS Strategy |
|---|---|---|
| 333, 332, 323 | 🏆 Champions | Exclusive perk |
| 322, 232, 222 | ⭐ Loyal | Cross-sell upsell |
| 311, 211 | 🌱 New / Promising | Welcome + helpful |
| 233, 133 | ⚠️ At-risk High Value | Personal win-back |
| 111, 112 | 💤 Lost | Mass re-engagement |

> รายละเอียด RFM เต็ม ๆ → [[../../EasyCRM/_knowledge/K02-RFM-Segmentation]]

---

## 5. Behavioral Triggers (Real-time Segmentation)

### Browse abandonment
- Trigger: ดู product 3+ ครั้ง ใน 7 วัน แต่ไม่ซื้อ
- SMS: "เห็นว่าสนใจ [item] — ลด 10% โค้ด: BROWSE"

### Cart abandonment
- Trigger: ใส่ตะกร้า → ไม่ checkout ใน 2h
- SMS sequence: 2h, 24h, 72h

### Browse history
- Trigger: ดู category X ใน 30 วันล่าสุด
- SMS: ส่ง promo ของ category X

### Price drop alert
- Trigger: item ในตะกร้า/wishlist ลดราคา
- SMS: "[item] ที่คุณสนใจ ลดเหลือ ฿xxx!"

### Restock alert
- Trigger: item ที่คนสนใจ out of stock → กลับมามี
- SMS: "[item] กลับมาแล้ว!"

---

## 6. Exclusion Lists (สำคัญพอ ๆ กับ Include)

### ❌ ใครต้อง exclude
- พึ่ง opt-out (forever)
- รับ SMS อื่นใน 24h (anti-fatigue)
- ซื้อสินค้านี้แล้วใน 7 วัน (ไม่ส่งโปรเดิมซ้ำ)
- คนที่อายุไม่ตรง (เช่น ส่งโปรเด็ก ไม่ส่งคนแก่)
- เบอร์ที่ DLR fail 3+ ครั้งติด (เบอร์ตาย)
- คนที่ใช้ภาษาอื่น (ไม่ส่ง Thai SMS ให้ลูกค้าเวียดนาม)

### 🛡 Suppression List Management
- Permanent: opt-out, fraud, complaint
- Temporary: recent contact, in-progress order, vacation mode

---

## 7. Test & Control Groups (Holdout)

> **กฎ:** ไม่มีกลุ่ม control = ไม่รู้จริงไหมว่าได้ผล

### Holdout Strategy
- เก็บ **5–10%** ของ target group ไว้ ไม่ส่ง SMS
- เปรียบเทียบ:
  - Conversion ของ sent vs holdout
  - Incremental revenue
  - ROI true

### ตัวอย่าง
- ส่ง 9,500 คน → Convert 8% = 760 conversions
- Holdout 500 คน → Convert ปกติ 2% = 10 conversions
- **Incremental:** 760 − (8% × 0 control adj) → 6% × 10,000 = 600 จริง
- ส่งเพิ่ม conv 600 vs ส่ง spam 760 — แม่นยำขึ้น

---

## 8. Personalization Levels

| Level | ตัวอย่าง | Implementation |
|---|---|---|
| Level 0 | "[Brand] Promo ลด 20%" | ส่งหว่าน |
| Level 1 | "[Brand] คุณ[ชื่อ] ลด 20%" | merge ชื่อ |
| Level 2 | "[Brand] คุณ[ชื่อ] ลด 20% หมวด[category]" | + interest |
| Level 3 | "[Brand] คุณ[ชื่อ] เหลือ ฿[amount] ใช้ลด [item]" | + behavior |
| Level 4 | AI generated copy per user | LLM + history |

> **ROI lift:** Level 0→1 +30%, Level 1→2 +50%, Level 2→3 +100%

---

## 9. Tools & Implementation

### Manual segmentation (เริ่มต้น)
- Excel/Sheets: filter RFM, age, recency
- Export → upload to BoostSMS

### Semi-automated
- BoostSMS dashboard filter: "ลูกค้าซื้อใน 30 วัน + ยอด > ฿1,000"
- Save as audience → reuse

### Fully automated (Advanced)
- CDP (Customer Data Platform)
- Real-time triggers
- API integration
- Predictive scoring

---

## 10. Anti-patterns

❌ **"ส่งทุกคนเหมือนกันหมด"** — ROI ต่ำที่สุด
❌ **"แบ่ง 30 segments"** — ซับซ้อนเกิน ดูแลไม่ไหว
❌ **"ใช้ list เก่า > 1 ปี"** — เบอร์ตายเยอะ, opt-out implicit
❌ **"ไม่มี exclusion list"** — ส่งซ้ำ → opt-out spike
❌ **"ไม่มี holdout"** — ไม่รู้ ROI จริง

---

## 🔗 อ่านต่อ

- RFM เต็ม → [[../../EasyCRM/_knowledge/K02-RFM-Segmentation|RFM Segmentation]]
- ประเภทแคมเปญ → [[K04-Campaign-Types]]
- วัดผล → [[K06-SMS-Metrics-KPIs]]
- A/B test → [[K15-AB-Testing-SMS]]
