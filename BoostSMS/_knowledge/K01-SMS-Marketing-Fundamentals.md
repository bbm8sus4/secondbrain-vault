# K01 · SMS Marketing Fundamentals

> **TL;DR (EN):** SMS is the most reliable mass-communication channel — 98% open rate, 90% read within 3 minutes, no algorithm, no inbox spam, no app install required. The catch: it's expensive per message (฿0.20–0.80 in TH), highly constrained (160 char EN / 70 char TH), and abused-to-spam easily. Use SMS for **urgent, valuable, transactional** moments — not "weekly newsletters".
>
> **สรุป (TH):** SMS = ช่องทางที่ **อ่านแน่นอนที่สุด** — 98% เปิด, 90% อ่านใน 3 นาที, ไม่มี algorithm คั่น, ไม่ต้องลง app ข้อเสีย: แพงต่อข้อความ (฿0.20–0.80), จำกัด 70 ตัวอักษรไทย/160 อังกฤษ ใช้กับ **moment ที่เร่งด่วน, มี value, transactional** ห้ามใช้ส่ง newsletter รายสัปดาห์

---

## 1. SMS คืออะไร (ใน 2026)

**SMS = Short Message Service** — เกิดปี 1992 ส่งข้อความแรก "Merry Christmas"

ใน 2026 SMS ยังเป็นช่องทางที่:
- **Universal** — โทรศัพท์ทุกเครื่องรับได้ ไม่ต้อง app, ไม่ต้องเน็ต
- **Trusted** — คนเปิดอ่าน 98% ภายใน 3 นาที
- **Unmediated** — ไม่มี algorithm คั่น (Facebook, IG, LINE มีหมด)
- **Sovereign** — แบรนด์ควบคุม sender name + content เอง

---

## 2. ทำไม SMS ยังไม่ตาย (ในยุค LINE / IG / TikTok)

### 📊 The Numbers

| Metric | SMS | Email | LINE Broadcast | Push |
|---|---|---|---|---|
| Open rate | **98%** | 21% | 50–70% | 5–25% |
| Read in 3 min | **90%** | < 30% | varies | varies |
| Click-through rate | **19%** | 2.5% | 4–7% | 2–6% |
| ต้องลง app | ❌ ไม่ต้อง | ❌ | ✅ ต้องมี LINE | ✅ ต้องลง app + allow |
| ต้องมี internet | ❌ | ✅ | ✅ | ✅ |

> **ที่มา:** Twilio State of Customer Engagement 2024, Salesforce Marketing Cloud benchmark

### 💡 Key Insight
> SMS ไม่ใช่ **ช่องโปรโมท** แต่เป็น **ช่องการันตีการอ่าน**

ใช้ SMS เมื่อ "ลูกค้าต้องเห็น" ไม่ใช่ "อยากให้เห็น"

---

## 3. ข้อเสียที่ต้องเข้าใจ

| ข้อเสีย | ผล |
|---|---|
| **แพง** ฿0.20–฿0.80/SMS | ไม่เหมาะ mass cheap content |
| **160 ตัวอักษร (EN), 70 (TH)** | เขียนยาก ต้องคัด |
| **No multimedia** (ใน SMS ปกติ) | รูป/video ต้องใช้ link |
| **Spam liability** | กฎหมาย + NBTC + opt-out |
| **No 2-way trust** (พิมพ์เบอร์ปลอมง่าย) | ลูกค้าระแวง |
| **Read once and delete** | ลูกค้าไม่กลับมาดู (vs email/LINE) |

---

## 4. SMS Use Cases ที่เวิร์ก

### ✅ ใช้ดี
1. **OTP / 2FA** — Banking, login, verify
2. **Order confirmation** — "คำสั่งซื้อ #1234 พร้อมส่ง"
3. **Delivery notification** — "Package ถึงสาขาแล้ว"
4. **Appointment reminder** — "พรุ่งนี้ 14:00 น. นัดหมอ"
5. **Flash sale (12h window)** — "ลด 50% ถึง 23:59 วันนี้"
6. **Abandoned cart recovery** — "ตะกร้ายังรอคุณอยู่ ฿xxx"
7. **Loyalty alert** — "แต้ม 2,500 จะหมดอายุ 31 ส.ค."
8. **Emergency / urgent** — Service outage, security alert

### ❌ ใช้แย่
1. **Weekly newsletter** — ใช้ email/LINE
2. **Long-form content** — ตัดออกหมด
3. **Cold outreach mass** — สเปม + ผิดกฎ
4. **Re-marketing low-intent** — ROI ลบ
5. **เนื้อหา branding ทั่วไป** — เปลือง

---

## 5. SMS Marketing Funnel

```
   📱 Acquire opt-in        ← ✅ Consent (PDPA)
        ↓
   🎯 Welcome SMS (60s)     ← ✅ First impression
        ↓
   💡 Value-driven SMS      ← Discount, alert, exclusive
        ↓
   🛒 Convert / Action       ← Click link, redeem
        ↓
   📊 Measure (DLR, CTR, conv)
        ↓
   ♻️ Optimize segments
```

---

## 6. ROI ของ SMS Marketing

### 📊 Industry Benchmark (Twilio 2024)
- **ROI:** $71 returned per $1 spent (avg)
- **Conversion rate:** 29% (เทียบกับ email 4–6%)
- **CTR:** 19%
- **Cost per conversion:** $1.50–$5

### 🎯 บริบทไทย
- SMS ต้นทุน ฿0.30/ข้อความ
- หากใช้ส่ง offer ที่ converted 5%
- ฿0.30 ÷ 0.05 = **฿6 ต่อ conversion**
- ถ้า basket size = ฿800 + margin 30% = **฿240 profit** → ROI = 40x

---

## 7. SMS Marketing 5 Principles

### 1️⃣ Permission First (Opt-in)
- ห้ามส่งโดยไม่มี consent — ผิดกฎหมาย (PDPA)
- ใช้ double opt-in ถ้าเป็นไปได้

### 2️⃣ Value Per Message
- ทุก SMS ต้อง "คุ้มค่าเปิด"
- ถ้าลูกค้ารู้สึก "ทำไมส่งมา" = บาด trust

### 3️⃣ Brevity (ความสั้น)
- ตัดทุกคำที่ไม่จำเป็น
- ขึ้นต้นด้วย action/value

### 4️⃣ Identifiable Sender
- ใช้ Sender Name ที่จดจำ ("EasySlip" ไม่ใช่ "+66xxx")
- ใส่ brand ต้นข้อความ

### 5️⃣ Always-Easy Opt-out
- "พิมพ์ STOP เพื่อเลิกรับ"
- ลูกค้าออกง่าย = trust สูง

---

## 8. SMS ในอนาคต (2026+)

### 📱 RCS (Rich Communication Services)
- "SMS 2.0" — รองรับรูป, video, button, carousel
- Google + Apple support
- ค่อย ๆ replace SMS ในตลาดเริ่มต้น (US, EU)
- ไทยยังไม่แพร่หลาย

### 🤖 AI-Personalized SMS
- LLM generate copy per user
- Smart timing (ส่งเมื่อ user น่าจะเปิด)

### 🔗 Conversational SMS / 2-way
- ลูกค้าตอบกลับได้ → chatbot auto-reply
- Twilio Conversations, MessageBird Inbox

### 📊 Number-as-Identity
- เบอร์ = identifier ผูก WhatsApp + LINE + SMS
- Multi-channel orchestration

---

## 🔗 อ่านต่อ

- เทียบช่อง → [[K02-Channel-Comparison]]
- เขียน SMS ให้ดี → [[K03-SMS-Copywriting]]
- ประเภทแคมเปญ → [[K04-Campaign-Types]]
- ตลาดไทย → [[K08-Thai-SMS-Market-NBTC]]
