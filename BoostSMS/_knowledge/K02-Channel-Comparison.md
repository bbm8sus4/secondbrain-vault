# K02 · Channel Comparison — SMS vs Email vs LINE vs RCS vs Push

> **TL;DR (EN):** No single channel wins everything. SMS = guaranteed read + urgent. Email = long-form + low cost. LINE OA = engagement + Thai-native. Push = app-engaged users only. RCS = the future but limited reach. The right strategy uses 3–4 channels in orchestration: SMS for must-read, LINE for engage, email for content, push for app users.
>
> **สรุป (TH):** ไม่มีช่องไหนชนะทุกอย่าง — SMS = อ่านแน่ + เร่งด่วน, Email = ยาว + ถูก, LINE = engage + คนไทย, Push = คนใช้แอป, RCS = อนาคต กลยุทธ์ที่ดีใช้ **3–4 ช่องประสานกัน** ไม่ใช่เลือกอันเดียว

---

## 1. ตารางเปรียบเทียบ (Quick Reference)

| มิติ | SMS | Email | LINE OA | Push (App) | RCS |
|---|---|---|---|---|---|
| **Open rate** | 98% | 20–25% | 50–70% | 5–25% | 80%+ |
| **CTR เฉลี่ย** | 19% | 2.5% | 4–7% | 2–6% | 25%+ |
| **Read in 3 min** | 90% | 30% | 50% | varies | 70% |
| **ต้องลง app** | ❌ | ❌ | ✅ LINE | ✅ | ❌ |
| **ต้องมี internet** | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Multimedia** | ❌ | ✅ | ✅ | ⚠️ | ✅ |
| **Long-form** | ❌ | ✅ | ⚠️ | ❌ | ⚠️ |
| **2-way chat** | ⚠️ | ✅ | ✅ | ❌ | ✅ |
| **ต้นทุน/ข้อความ TH** | ฿0.30 | ฿0.001 | ฿0.06–0.30 | ฿0 | TBD |
| **Mass send** | ✅ | ✅ | ⚠️ จำกัด/แพ็ก | ✅ | ⚠️ |
| **Personal feel** | สูง | ต่ำ | กลาง | ต่ำ | สูง |
| **Algorithm risk** | ❌ ไม่มี | ⚠️ spam folder | ⚠️ ลด reach | ⚠️ OS throttle | ❌ |
| **Thailand reach** | 99% | 60% (อายุ 25+) | 95% | 70% (smartphone) | < 5% |

---

## 2. แต่ละช่องเหมาะกับ moment ไหน

### 📲 SMS — Must-read moments
- OTP / 2FA
- Order confirmation
- Delivery tracking
- Appointment reminder
- Time-critical promo (flash sale 12h)
- Service alert / emergency
- Payment reminder
- Loyalty point expiry

### 📧 Email — Educate + Content
- Welcome series (3–5 emails)
- Newsletter รายสัปดาห์/เดือน
- Product launches (รายละเอียดยาว)
- Receipts + invoices
- Re-engagement (inactive 90 วัน)
- Survey + feedback
- Educational content

### 💚 LINE OA — Engagement + Thai Daily Life
- Rich menu interactive
- Sticker-based engagement
- 2-way customer service
- Personalized chat
- Loyalty card (EasyCRM)
- Group community
- Mini-game / quiz

### 🔔 Push Notification — Already-engaged Users
- In-app behavior alerts
- Real-time events (livestream start)
- Personalized recommendations
- Geolocation-triggered offers
- Cart abandonment (ถ้าลงแอป)

### 💬 RCS — SMS but Rich (อนาคต)
- เหมือน SMS แต่ใส่ button, carousel
- ดี US/EU แล้ว ไทย < 5%
- Watch this space

---

## 3. Channel Cost Comparison (ส่ง 1,000 ข้อความ)

| Channel | ต้นทุน |
|---|---|
| Email | ฿1 (Mailchimp/SendGrid) |
| Push notification | ฿0 (in-app) |
| LINE Broadcast (Standard plan) | ~฿60–฿150 |
| SMS (BoostSMS) | ~฿200–฿800 |
| RCS | TBD (ยังไม่ standard ในไทย) |

> **Trade-off:** ถูก = reach กว้าง แต่ open rate ต่ำ | แพง = reach แน่นอน

---

## 4. ใช้ทุกช่องอย่างไร — Orchestration Strategy

### 🎯 Channel Mix Recommendation

```
            Awareness               Conversion
                ↓                       ↓
            Social Ads      ───→    SMS (urgent)
                                       ↑
            Email content   ←─── LINE OA engage
                                       ↑
            Blog / SEO      ←─── Push (re-engage)
```

### 🧠 Rule of Thumb
- **SMS first** สำหรับ urgent + must-action
- **LINE OA** สำหรับ relationship + 2-way
- **Email** สำหรับ content + long-form
- **Push** สำหรับ already-active user

### 🔁 Multi-channel Sequence ตัวอย่าง

**Flash Sale Campaign**
1. Day -3: Email teaser
2. Day -1: LINE OA broadcast (preview)
3. Day 0, 09:00: **SMS** "เริ่มแล้ว! ลด 50% ถึง 23:59"
4. Day 0, 18:00: **Push** "เหลือ 5 ชม!"
5. Day 0, 23:00: **SMS** "เหลือ 1 ชม สุดท้าย!"
6. Day +1: Email summary

→ ใช้แต่ละช่องตามจุดแข็ง

---

## 5. SMS vs LINE OA — เลือกอย่างไรในไทย

ปัญหาทั่วไปของ SME ไทย: "มี LINE OA แล้ว ทำไมต้องใช้ SMS อีก?"

| สถานการณ์ | LINE หรือ SMS? |
|---|---|
| ลูกค้า follow LINE OA แล้ว | **LINE** (ฟรี/ถูก, รูปได้) |
| ลูกค้าไม่ follow LINE | **SMS** (รู้แค่เบอร์ก็ส่งได้) |
| Urgent + must-read | **SMS** (open rate 98% เสมอ) |
| OTP / Banking | **SMS** (LINE บล็อก OTP) |
| ลูกค้าซื้อครั้งแรก | **SMS** (ยังไม่ add LINE) |
| Promo + content ยาว | **LINE** (rich content) |
| Re-engage หลังไม่ active 6 เดือน | **SMS** (LINE message ถูกบล็อก/mute) |

> **Best practice:** ใช้ **ทั้งสอง** — LINE = day-to-day, SMS = critical moments

---

## 6. Email vs SMS — เลือกอย่างไร

| ปัจจัย | Email | SMS |
|---|---|---|
| Content ยาว | ✅ | ❌ |
| ต้นทุน | ต่ำมาก | สูง |
| Open rate | 20–25% | 98% |
| ไม่อ่าน → ไม่ลบ | ✅ (ดูภายหลัง) | ❌ (อ่านแล้วลบ) |
| Mobile-first market | บ่อยครั้ง ignore | ใช้ดี |
| คนไทย < 30 ปี | ใช้น้อย | universal |
| คนไทย 40+ | ดี | ดีกว่า LINE |
| B2B | ดีกว่า | ใช้บ้าง |

> **Insight:** ในไทย Email ใช้ได้ดีกับ B2B และคนทำงาน อายุ 30+ — ไม่เหมาะกับ Gen Z

---

## 7. RCS Cheat Sheet (อนาคตของ SMS)

| คุณสมบัติ | SMS | RCS |
|---|---|---|
| ตัวอักษร | 70/160 | ไม่จำกัด |
| รูปภาพ | ❌ | ✅ |
| Video | ❌ | ✅ |
| Carousel | ❌ | ✅ |
| Button (CTA) | ❌ | ✅ |
| Read receipt | ❌ | ✅ |
| Typing indicator | ❌ | ✅ |
| Verified sender | ⚠️ | ✅ |

**ในไทย:**
- AIS, dtac, TrueMove รองรับบางส่วน
- iOS 18+ เริ่ม support
- คาดว่า penetration > 30% ภายใน 2027

> BoostSMS อนาคต: สนใจ integrate RCS เมื่อ Thai operator standard ออก

---

## 8. Channel Decision Framework

```
ถามตัวเอง 3 ข้อ:

1. ลูกค้าต้องอ่านในกี่นาที?
   → < 5 นาที: SMS
   → < 1 ชม: SMS / Push
   → < 24 ชม: LINE / Push
   → ไม่เร่ง: Email

2. Content ยาวแค่ไหน?
   → < 70 ตัว: SMS
   → 70–500 ตัว: SMS / LINE
   → > 500 ตัว: Email / LINE rich

3. ลูกค้าเป็นใคร?
   → ไม่เคยติดต่อ + รู้แค่เบอร์: SMS
   → Follow LINE: LINE
   → ลง app: Push
   → Subscribe: Email
```

---

## 🔗 อ่านต่อ

- พื้นฐาน SMS → [[K01-SMS-Marketing-Fundamentals]]
- ประเภทแคมเปญ → [[K04-Campaign-Types]]
- เขียนให้ดี → [[K03-SMS-Copywriting]]
