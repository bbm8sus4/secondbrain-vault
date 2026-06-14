# K03 · SMS Copywriting — เขียน 70 ตัวอักษรให้คุ้ม

> **TL;DR (EN):** SMS encoding is the hidden tax: 160 characters in plain English (GSM-7), but only **70 characters in Thai** (UCS-2 Unicode). Every Thai vowel/tone mark counts. Best SMS opens with a hook (brand + benefit) in the first 30 chars (preview window), uses one clear CTA, includes a short URL, and ends with opt-out. Avoid emojis (forces UCS-2 even in English).
>
> **สรุป (TH):** SMS ไทยมีแค่ **70 ตัวอักษร** ต่อข้อความ (อังกฤษ 160) — เพราะใช้ Unicode UCS-2 รูปแบบ SMS ที่ดี: เปิดด้วย hook (แบรนด์ + ประโยชน์) ใน 30 ตัวแรก (ตัวอย่างใน preview) มี CTA ชัด 1 อัน + short URL + opt-out ห้ามใช้ emoji (ทำให้แม้ภาษาอังกฤษกลายเป็น UCS-2 → ตัวสั้นลง)

---

## 1. ขีดจำกัดตัวอักษร (Character Limits)

### Encoding Standards

| Encoding | ใช้กับ | ต่อ 1 SMS | Concatenated (2+ SMS) |
|---|---|---|---|
| **GSM-7** | English + basic Latin | 160 | 153 ต่อ SMS |
| **UCS-2** (Unicode) | Thai, Chinese, Arabic, emoji | **70** | **67 ต่อ SMS** |

### ทำไม Thai ใช้ 70 ตัว?
- ภาษาไทยต้องใช้ Unicode UCS-2 (16-bit ต่อตัว)
- SMS payload = 140 bytes
- 140 bytes ÷ 2 = **70 ตัวอักษร**

### นับยังไง?
- พยัญชนะ 1 ตัว = 1 อักขระ
- สระ (เ◌, ◌ิ, ◌ู, ◌ำ) = 1 อักขระ
- วรรณยุกต์ (◌่, ◌้) = 1 อักขระ
- ช่องว่าง = 1 อักขระ
- 1 emoji = 1–2 อักขระ (ขึ้นกับ encoding)

### ตัวอย่างนับ
```
"สวัสดี" = 6 อักขระ (ส + ◌ + ว + ◌ + ส + ดี... )
จริง ๆ = ส, ว, ◌ั, ส, ด, ี = 6 ตัว
```

> **เทียบ:** "Hello" = 5 ตัวใน GSM-7 / "สวัสดี" = 6 ตัวใน UCS-2 (แต่ใช้ pool 70 ไม่ใช่ 160)

---

## 2. การคิดราคาตามจำนวน Segment

| ภาษา | 1 SMS | 2 SMS (concat) | 3 SMS |
|---|---|---|---|
| English | 160 | 161–306 | 307–459 |
| Thai | 70 | 71–134 | 135–201 |

> **ระวัง:** ถ้าใส่ emoji 1 ตัวในข้อความอังกฤษ → กลายเป็น UCS-2 ทันที = 70 ตัว ไม่ใช่ 160

> ตัวอย่าง "Hi! ใช้โค้ด WELCOME10 ลด 10%" = ไทย + อังกฤษผสม → UCS-2 = 70 ตัว/SMS

---

## 3. โครงสร้าง SMS ที่ดี (Anatomy)

```
[BRAND] [HOOK]: [VALUE]. [CTA]. [URL]
                                      [OPT-OUT]
```

### ตัวอย่าง (Thai)
```
[Thunder] ดีลด่วน! ลด 50% เฉพาะคืนนี้
ใช้โค้ด NIGHT50 → s.th/x4f
พิมพ์ STOP เพื่อเลิกรับ
```
- Brand: Thunder
- Hook: ดีลด่วน! ลด 50%
- Specificity: เฉพาะคืนนี้
- Code: NIGHT50
- URL: s.th/x4f (short)
- Opt-out: พิมพ์ STOP

**นับ:** ~95 ตัว = 2 segments

---

## 4. หลัก 5 ข้อของ SMS Copywriting

### 1️⃣ Brand แรกสุด (Identify yourself ในขั้นแรก)
- ❌ "ลด 50% วันนี้!!" (ใครส่ง??)
- ✅ "[EasySlip] ลด 50% วันนี้"

### 2️⃣ Value ก่อน Context
- ❌ "ขอบคุณที่ใช้บริการ ขอเรียนแจ้งว่าโปรของเรา..."
- ✅ "ลด 30% ใช้ก่อน 31 พ.ค."

### 3️⃣ 1 CTA เท่านั้น
- ❌ "ดูเว็บ + ดาวน์โหลดแอป + โทรเรา 02-xxx"
- ✅ "ดูดีล: s.th/x4f"

### 4️⃣ Specific Number
- ❌ "ลดเยอะมาก!"
- ✅ "ลด ฿299" หรือ "ลด 50%"

### 5️⃣ Urgency เมื่อจำเป็น (อย่าฟุ่มเฟือย)
- ❌ "ด่วน! โอกาสสุดท้าย!! รีบเลย!!!" ← spam vibe
- ✅ "ถึง 23:59 วันนี้" ← specific deadline

---

## 5. Hook Patterns ที่เวิร์ก (Templates)

### 🎯 Promotional
- "[Brand] ลด 30% โค้ด: SAVE30 → [link]"
- "ดีลด่วน 24 ชม: [item] เหลือ ฿xxx [link]"
- "[Brand] VIP only: 1 แถม 1 ถึง [date]"

### 📦 Transactional
- "ออเดอร์ #1234 พร้อมส่งวันนี้ → [tracking link]"
- "[Brand] เครดิตคงเหลือ ฿xxx · ใช้ก่อน [date]"
- "นัดหมายพรุ่งนี้ 14:00 ที่ [location]"

### 🔐 OTP / Verification
- "รหัสยืนยัน: 472193 ห้ามแชร์ใคร"
- "[Brand] รหัสล็อกอิน: 8472 (ใช้ภายใน 5 นาที)"

### 💌 Engagement / Loyalty
- "[Brand] แต้ม 2,000 จะหมด 31 ส.ค. → แลก: [link]"
- "ครบรอบ 1 ปี! รับฟรี [item] → [link]"

### 🚨 Alert
- "[Bank] มีการล็อกอินใหม่ ถ้าไม่ใช่คุณ โทร 02-xxx"
- "[Brand] บริการหยุด 22:00–02:00 (บำรุงรักษา)"

---

## 6. คำที่ควรหลีกเลี่ยง (Spam Trigger Words)

| ❌ คำที่ทำให้รู้สึก spam | ✅ ใช้แทน |
|---|---|
| ฟรี!!! รีบเลย!! | ลดวันนี้ · ฟรีค่าส่ง |
| ด่วนมาก!!! | ถึง 23:59 |
| รับเงินทันที | รับ ฿500 ผ่าน QR |
| โอกาสครั้งเดียว | สิทธิ์เฉพาะคุณ ถึง [date] |
| คลิกเลย!!! | ดูดีล: [link] |
| !!! เครื่องหมายเยอะ | ใช้แค่ ! เดียว |
| ตัวพิมพ์ใหญ่ทั้งหมด | ปกติ |

---

## 7. URL Strategy

### ✅ Short URL ที่ดี
- `s.boostsms.co/x4f`
- `easyslip.co/promo`
- `bit.ly/3xY7zQ` (สากล)

### ❌ Long URL ที่แย่
- `https://www.example.com/promo/summer-sale-2026/?utm_source=sms&utm_medium=...`

### Best Practices
- Custom branded short URL (`s.brand.com`) > Bitly (trust สูงกว่า)
- Track ผ่าน UTM parameters
- ใส่ rel="noreferrer" ที่ landing page

---

## 8. Opt-out (สิ่งที่ต้องมี — กฎหมาย)

ทุก SMS marketing **ต้องมี** opt-out:

### ✅ ที่ใช้กันในไทย
- "พิมพ์ STOP เพื่อเลิกรับ"
- "Reply STOP to unsubscribe"
- "หยุดรับ พิมพ์ NO"

### Best Practices
- ต้องประมวลผลทันที (1 SMS = ปลดทันที)
- ไม่ตอบกลับ "ยืนยันลบรายชื่อ" (ส่ง SMS เพิ่ม = ผิดวัตถุประสงค์)
- เก็บ blacklist ไม่ส่งซ้ำ

> ดู [[K14-Compliance-AntiSpam]] เพิ่ม

---

## 9. SMS Copy A/B Testing Ideas

ตัวอย่างที่ทดสอบได้:

| Variant A | Variant B |
|---|---|
| "ลด 50%" | "ลด ฿500" |
| Deadline | No deadline |
| CTA "Click" | CTA "Shop now" |
| Brand ต้น | Brand ท้าย |
| Emoji | No emoji |
| Numeric short URL | Custom branded URL |
| Personalization (ชื่อ) | Generic |
| 1 segment | 2 segments (รายละเอียดเพิ่ม) |

> วัด: CTR, conversion rate, opt-out rate

---

## 10. ตัวอย่าง SMS ที่ดี (Real Patterns)

### ☕ ร้านกาแฟ Loyalty
```
[CafeMew] เก็บครบ 8 แก้วแล้ว!
ฟรี Latte ที่ร้าน ถึง 30 มิ.ย.
แสดง SMS นี้ที่เคาน์เตอร์
พิมพ์ STOP เพื่อเลิกรับ
```
**~95 ตัว = 2 segments**

### 🛒 E-commerce Cart Abandonment
```
[Shop] ตะกร้าคุณยังรอ
฿2,499 + ฟรีส่ง วันนี้
ดูตะกร้า: s.shop/c4r
STOP=เลิกรับ
```
**~60 ตัว = 1 segment**

### 🏥 Appointment Reminder
```
[คลินิก] นัดพรุ่งนี้ 14:00
หมอสมหวัง ห้อง 302
เลื่อนนัด: 02-123-4567
```
**~55 ตัว = 1 segment**

### 🔐 OTP
```
รหัสยืนยัน BoostSMS: 482915
ห้ามแชร์ ใช้ภายใน 5 นาที
```
**~55 ตัว = 1 segment**

---

## 🔗 อ่านต่อ

- ประเภทแคมเปญ → [[K04-Campaign-Types]]
- Compliance → [[K14-Compliance-AntiSpam]]
- ทดสอบ → [[K15-AB-Testing-SMS]]
