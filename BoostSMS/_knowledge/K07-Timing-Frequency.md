# K07 · Timing & Frequency Best Practices

> **TL;DR (EN):** SMS timing matters more than email — recipients see it immediately, so wrong-time delivery = annoyance. Best windows for Thailand: 10:00–11:00, 13:00–14:00, 18:00–20:00. NEVER send before 8:00 or after 21:00 (NBTC enforced 21:00 cutoff for promotional SMS). Frequency cap: 2–4 promo SMS/month per contact; sequential SMS within a campaign min 24h apart.
>
> **สรุป (TH):** SMS timing สำคัญกว่า email — เห็นทันที ส่งผิดเวลา = รำคาญ ช่วงดี: 10:00–11:00, 13:00–14:00, 18:00–20:00 **ห้ามส่งก่อน 8:00 หรือหลัง 21:00** (กฎ NBTC) ความถี่: 2–4 ครั้ง/เดือน/คน, SMS ในแคมเปญเดียวกัน ห่างกันอย่างน้อย 24 ชม

---

## 1. Time of Day — เวลาส่ง SMS ที่ดีที่สุด

### 🇹🇭 Thai Mobile Behavior Pattern

```
06:00 - 08:00  📈 ตื่น/เดินทาง — engagement กลาง
08:00 - 10:00  📈 ทำงาน early — engagement กลาง
10:00 - 11:00  ⭐ Coffee break — peak 1
11:00 - 12:00  📊 Pre-lunch — กลาง
12:00 - 13:00  📈 Lunch — กลาง (engaged แต่กิน)
13:00 - 14:00  ⭐ After lunch — peak 2
14:00 - 17:00  📉 ทำงาน — ต่ำ
17:00 - 18:00  📈 เลิกงาน — กลาง
18:00 - 20:00  ⭐ Evening — peak 3 (สูงสุด)
20:00 - 21:00  📊 ก่อนนอน — กลาง
21:00 - 06:00  ❌ ห้ามส่ง (NBTC)
```

### Industry-Specific Windows

| Industry | Best Times |
|---|---|
| F&B / Restaurant | 11:00–12:00 (lunch), 17:00–18:30 (dinner) |
| Retail / E-commerce | 12:00–14:00, 18:00–20:00 |
| Banking / Finance | 09:00–11:00, 14:00–16:00 (working hours) |
| Beauty / Wellness | 10:00–12:00, 19:00–21:00 |
| Travel | Friday 16:00–19:00, Saturday morning |
| Education | 17:00–20:00 |
| Healthcare appointment | 1 day before at 14:00, 2h before |

---

## 2. Day of Week

### Thai Pattern

```
Mon    📊 ดีปานกลาง (start of week, busy)
Tue    ⭐ ดีที่สุด
Wed    ⭐ ดีที่สุด
Thu    ⭐ ดี (esp. promo "Thursday treat")
Fri    📈 ดี (weekend prep)
Sat    📊 กลาง (relaxed, but distracted)
Sun    📉 ต่ำ (family time)
```

### Special Days

- **เงินเดือนออก (25th–31st):** spike for big-ticket promo
- **เงินเดือนกลาง (10th–15th):** good for everyday promo
- **วันเด็ก, แม่, พ่อ:** themed campaigns
- **วันหวยออก (1, 16):** F&B + retail spike
- **เทศกาล (สงกรานต์, ตรุษจีน):** plan 7 days ahead

---

## 3. กฎหมาย — NBTC Time Restrictions

### 📜 Official Hours
- **ห้ามส่ง SMS โฆษณา:** 21:00–08:00
- **OTP / Transactional:** ส่งได้ตลอด 24 ชม
- **ฝ่าฝืน:** ปรับ + sender ID ถูกระงับ

> **Note:** บางครั้ง NBTC ยืดเป็น 22:00 — เช็คล่าสุดทุก quarter

### ❌ ห้ามส่ง
- วันสำคัญทางศาสนา (เช้ามืด)
- วันพระใหญ่
- หลังเหตุการณ์ disaster (etiquette)

---

## 4. Frequency — ความถี่ที่ลูกค้ารับได้

### 📊 Frequency Tolerance

| ความถี่ | ลูกค้าทั่วไปรับได้? |
|---|---|
| 1 ครั้ง/เดือน | ✅ ทุกคน |
| 2 ครั้ง/เดือน | ✅ ส่วนใหญ่ |
| 1 ครั้ง/สัปดาห์ | ⚠️ ต้อง value สูง |
| 2 ครั้ง/สัปดาห์ | ❌ opt-out spike |
| Daily | 🚫 unless transactional |

### Tier ตาม Engagement

| Segment | Max SMS/เดือน |
|---|---|
| VIP / Loyal | 4–6 |
| Active | 2–4 |
| Casual | 1–2 |
| At-risk | 1 ครั้ง (win-back) |
| Dormant | 1 ครั้ง/quarter |

---

## 5. Frequency Capping (กลไก suppression)

### 💡 Rule of Thumb
- **Per-day cap:** max 1 SMS/contact/day (ยกเว้น critical: OTP)
- **Per-week cap:** max 2 SMS/contact/week
- **Per-month cap:** max 4–6 SMS/contact/month

### Implementation
```
ก่อนส่งทุกครั้ง check:
1. เบอร์นี้ได้รับ SMS ใน 24h หรือยัง? (skip ถ้าใช่ ยกเว้น OTP)
2. ครบ cap เดือนหรือยัง?
3. อยู่ใน opt-out list?
4. กำลังเป็น recipient ของ active drip campaign?
```

---

## 6. Send Time Optimization (STO)

### 🤖 AI-driven Timing
- Track click time ต่อ user
- Send next time at predicted optimal hour
- Twilio, MoEngage, Braze support

### Manual Heuristics
- ลูกค้าซื้อตอน lunch → ส่ง 11:30
- ลูกค้าซื้อตอนเย็น → ส่ง 18:00
- ไม่รู้ → ใช้ default peak (10:00, 13:00, 19:00)

### Throttling
- ส่ง 10,000 SMS ใน 30 นาที (ไม่ใช่ทีเดียว) → ลด carrier filter risk
- BoostSMS support throttling rate config

---

## 7. Sequential Campaign Pacing

### Welcome Drip
```
Day 0  09:00  → Welcome SMS
Day 1  10:00  → How-to tip
Day 3  18:00  → First-purchase incentive
Day 7  10:00  → Survey/feedback
Day 14 18:00  → Re-engagement
Day 30 19:00  → Loyalty intro
```

**กฎ:** ห่างอย่างน้อย 24 ชม ระหว่าง SMS ในแคมเปญเดียวกัน

### Flash Sale Pacing
```
T-24h:  Pre-launch tease
T-0:    Launch (peak time)
T+12h:  Mid-sale reminder
T+22h:  Last-call (1h before end)
```

### Cart Abandonment Sequence
```
+2h:   "ตะกร้ายังรอ"
+24h:  + ส่วนลด 10%
+72h:  + ส่วนลดเพิ่ม / last chance
```

---

## 8. Frequency vs Opt-out Curve

```
Opt-out
Rate
  3% │                      🔴
     │                  🔴
  2% │              🔴
     │          🟡
  1% │      🟡
     │  🟢
  0% │🟢
     └───────────────────────────
       1  2  3  4  5  6  7  8
       SMS/month per contact
```

**Sweet spot:** 2–4 SMS/เดือน → opt-out ต่ำ + engagement ดี

---

## 9. Anti-pattern Timing

❌ **ส่ง 21:30 "เพราะคนเล่นมือถือก่อนนอน"** → NBTC ฟัน
❌ **ส่ง 6:00 "เพราะคนตื่น"** → annoying + NBTC
❌ **ส่ง 12:30 "ลูกค้ากำลังกิน"** → annoying
❌ **ส่ง วันอาทิตย์เช้า** → family time
❌ **ส่งทุกวัน** → opt-out fast
❌ **ส่ง SMS หลายอันใน 1 ชม** → spam vibe

---

## 10. Special Triggers — เวลาส่ง

### Cart Abandonment
- +30 min, +24h, +72h

### Birthday
- เช้าวันเกิด 09:00 (emotional)

### Appointment
- 24h before: 14:00
- 2h before: 2h ก่อน

### Renewal / Subscription
- 30 วัน, 7 วัน, 1 วัน ก่อน expire

### OTP
- Immediate (< 5 sec)

---

## 🔗 อ่านต่อ

- ประเภทแคมเปญ → [[K04-Campaign-Types]]
- Compliance → [[K14-Compliance-AntiSpam]]
- ทำ A/B test เวลา → [[K15-AB-Testing-SMS]]
- Thai NBTC → [[K08-Thai-SMS-Market-NBTC]]
