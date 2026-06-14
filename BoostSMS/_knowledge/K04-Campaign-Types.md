# K04 · SMS Campaign Types

> **TL;DR (EN):** SMS campaigns fall into 5 archetypes — Promotional (revenue), Transactional (functional), OTP (security), Drip/Sequence (nurture), Trigger-based (behavior). Each has different success metrics, regulatory treatment, and ROI profile. Most SME mistakes come from treating all SMS as "broadcasts" — the highest-ROI usage is trigger-based (cart abandon, expiring point, missed appointment).
>
> **สรุป (TH):** SMS แคมเปญแบ่งเป็น 5 ประเภท — Promotional / Transactional / OTP / Drip / Trigger-based แต่ละแบบมี KPI ต่างกัน, กฎหมายต่างกัน, ROI ต่างกัน SME ส่วนใหญ่ผิดที่ส่งแบบ "broadcast หว่าน" — แต่ที่ ROI สูงสุดจริง ๆ คือ **trigger-based** (cart abandon, แต้มจะหมด, นัดพรุ่งนี้)

---

## 1. 5 Archetypes Overview

| Type | Goal | Frequency | ROI |
|---|---|---|---|
| 🎯 **Promotional** | สร้าง revenue | สัปดาห์/เดือน | กลาง |
| 📦 **Transactional** | แจ้งสถานะ | per event | สูง (ลด ticket) |
| 🔐 **OTP / 2FA** | Security | per login | จำเป็น |
| 💧 **Drip / Sequence** | Nurture | sequence | สูง |
| ⚡ **Trigger-based** | Behavior response | event-driven | **สูงที่สุด** |

---

## 2. 🎯 Promotional Campaign

### ลักษณะ
- ส่งหา list กว้าง
- มี offer/discount/event
- ต้อง opt-in มาก่อน (PDPA)

### ตัวอย่าง
```
[Brand] วันเด็ก ลด 50% เด็ก + แม่
ถึง 14 ม.ค. เท่านั้น
ดูดีล: s.brand/jan
STOP=เลิกรับ
```

### Best Practices
- ✅ Segment list (อย่าส่งทุกคน)
- ✅ มี deadline ชัดเจน
- ✅ ความถี่ไม่เกิน 1–2 ครั้ง/สัปดาห์
- ✅ ทดสอบเวลาส่ง

### KPI
- Delivery rate > 95%
- CTR > 10%
- Conversion > 2%
- Opt-out rate < 1%

### ❌ ข้อผิดพลาดที่พบบ่อย
- ส่งทุกวัน → opt-out พุ่ง
- ไม่ใส่ deadline → urgency น้อย
- Generic offer สำหรับทุกคน → conversion ต่ำ

---

## 3. 📦 Transactional SMS

### ลักษณะ
- ส่งตาม event ของลูกค้า (ออเดอร์, ชำระเงิน)
- "Service message" ตามกฎหมาย NBTC = ไม่ต้องขอ opt-in marketing
- Open rate สูงสุด (99%+) เพราะลูกค้าคาดหวัง

### ตัวอย่าง
```
[Shop] ออเดอร์ #1234 ยืนยันแล้ว
฿1,490 ส่งภายใน 3 วัน
Track: s.shop/t1234
```

### Use Cases
- Order confirmation
- Payment received
- Shipping notification
- Delivery update
- Refund processed
- Account update
- Booking confirmation

### KPI
- Delivery rate > 98%
- Customer satisfaction
- Reduce inbound support calls

### 💡 ROI Insight
Transactional SMS ลด support ticket ได้ 30–50% — ROI มาจาก cost saving ไม่ใช่ revenue

---

## 4. 🔐 OTP / 2FA SMS

### ลักษณะ
- One-Time Password
- Time-sensitive (5–10 นาที)
- Sender ต้อง dedicated (อย่าผสมกับ promo)

### ตัวอย่าง
```
รหัสยืนยัน [Brand]: 472193
ใช้ภายใน 5 นาที ห้ามแชร์
```

### Best Practices
- ✅ ไม่ใส่ link (security)
- ✅ ระบุชัดว่า "ห้ามแชร์"
- ✅ Expiry time
- ✅ Dedicated sender ID
- ✅ Fallback channel (LINE, voice call)

### ❌ ห้าม
- ใส่ marketing message ใน OTP SMS
- Long delay (> 30 วินาที) → fraud risk
- ใช้ sender ID เดียวกับ promo (mix sender = lose trust)

### Cost Optimization
- OTP มักแพงกว่า marketing SMS (premium route)
- ใช้ multi-provider failover
- Voice call fallback ถ้า SMS ส่งไม่ถึง

---

## 5. 💧 Drip / Sequence Campaign

### ลักษณะ
- ลำดับ SMS หลายอัน ตามเวลา
- เป้าหมาย: nurture, education, conversion

### ตัวอย่าง Welcome Drip
```
Day 0: ยินดีต้อนรับ! รับ ฿100 ส่วนลด → [link]
Day 1: คู่มือใช้ครั้งแรก → [link]
Day 3: 3 ทริคจากลูกค้าคนอื่น → [link]
Day 7: ส่วนลดสำหรับคำสั่งซื้อที่ 2 → [link]
Day 14: ครบ 2 สัปดาห์! รีวิวให้เรา → [link]
```

### Best Practices
- ✅ Spread evenly (อย่ายัด 3 SMS ใน 1 วัน)
- ✅ Each SMS ต้อง standalone value
- ✅ Stop logic (ถ้าซื้อแล้ว ข้าม drip)
- ✅ Test ทั้ง sequence

### Common Sequences
- Welcome (sign-up → first purchase)
- Onboarding (first purchase → 2nd)
- Re-engagement (inactive 30/60/90 วัน)
- Birthday (1 wk before → birthday → 1 wk after)
- Post-purchase (delivery → review → loyalty)

---

## 6. ⚡ Trigger-based / Behavioral

### ลักษณะ
- ส่งตาม **action** หรือ **inaction** ของลูกค้า
- Highly relevant → ROI สูงสุด

### Top 5 Triggers ที่ ROI ดี

#### 1. 🛒 Cart Abandonment
```
[Shop] ตะกร้าคุณยังรอ
฿2,499 + ฟรีส่งวันนี้
ดูตะกร้า: s.shop/c
```
- Send: 30 min, 24h, 72h หลัง abandon
- Conversion: 15–30% (สูงมาก)

#### 2. 💎 Loyalty Point Expiry
```
[Brand] แต้ม 2,000 จะหมด 30 มิ.ย.
แลกของรางวัล: s.brand/r
```
- Send: 30, 14, 7, 1 วันก่อนหมดอายุ
- Drive redemption + return visit

#### 3. 🔄 Re-engagement (Win-back)
```
คิดถึงคุณ! กลับมา 7 วันนี้
ลด 20% โค้ด WELCOMEBACK
s.brand/back
```
- Send: 30, 60, 90 วันหลัง active ล่าสุด

#### 4. 🎂 Birthday
```
[Brand] สุขสันต์วันเกิด!
รับฟรี [item] ภายใน 7 วัน
แสดง SMS ที่ร้าน
```
- Sending day = birthday + 7 day reminder
- Highest emotional response

#### 5. 📅 Appointment Reminder
```
นัดพรุ่งนี้ 14:00 น.
ที่ [location]
เลื่อนได้ที่ [phone]
```
- Send: 24h ก่อน + 2h ก่อน
- ลด no-show 40%+

---

## 7. Hybrid Campaign (รวมหลายแบบ)

ตัวอย่าง: **Flash Sale Campaign**

| ขั้น | Type | Timing |
|---|---|---|
| 1 | Promotional broadcast | T-24h: "พรุ่งนี้ flash sale" |
| 2 | Promotional broadcast | T-0: "เริ่มแล้ว!" |
| 3 | Promotional broadcast | T+12h: "เหลือ 6 ชม" |
| 4 | Trigger (cart abandon) | T+15h–18h: "ตะกร้ารอคุณ" |
| 5 | Transactional | T+24h: "ขอบคุณ ออเดอร์ยืนยัน" |
| 6 | Drip (post-purchase) | T+48h: "เคล็ดลับใช้ [item]" |

---

## 8. Campaign Type Decision Matrix

```
ถาม: เกิดอะไรขึ้นที่ลูกค้า?

📦 มีออเดอร์/transaction
   ↓
   Transactional SMS

🔐 ต้องการ verify / security
   ↓
   OTP SMS

⚡ ลูกค้าทำ (หรือไม่ทำ) บางอย่าง
   ↓
   Trigger-based SMS

💧 ลูกค้าเพิ่งสมัคร → ต้อง educate
   ↓
   Drip sequence

🎯 มี offer ใหม่ ต้องการ broadcast
   ↓
   Promotional SMS
```

---

## 9. ROI Hierarchy

```
   📊 ROI สูง                    📊 ROI ต่ำ
        ↑                              ↓

  Trigger-based (cart, expiry, birthday)
        ↑
  Transactional (lifecycle moments)
        ↑
  Drip (welcome series)
        ↑
  Promotional (segmented)
        ↑
  Promotional (mass broadcast) ← เริ่มต้นที่นี่แล้วต่อยอด
```

> **Lesson:** SME ที่เพิ่งเริ่มมักทำ Promotional broadcast ก่อน → ค่อย ๆ migrate ขึ้นไปทาง Trigger-based เมื่อ data + automation พร้อม

---

## 🔗 อ่านต่อ

- เขียนแต่ละประเภท → [[K03-SMS-Copywriting]]
- Segment ก่อนส่ง → [[K05-Segmentation-Targeting]]
- วัดผล → [[K06-SMS-Metrics-KPIs]]
- ส่งเวลาไหนดี → [[K07-Timing-Frequency]]
