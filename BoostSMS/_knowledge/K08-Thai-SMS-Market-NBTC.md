# K08 · Thai SMS Market & NBTC Regulation

> **TL;DR (EN):** Thailand's SMS market is regulated by NBTC (National Broadcasting and Telecommunications Commission). All bulk SMS must use registered Sender IDs, observe 08:00–21:00 send window for promotional, and provide opt-out. Three operators dominate routing — AIS, TrueMove H, dtac — each with own anti-spam filters. SMS pricing in Thailand: ฿0.20–0.80/message depending on volume + sender type. Market size: ~10B SMS/year, mostly OTP + transactional.
>
> **สรุป (TH):** ตลาด SMS ไทยอยู่ใต้ NBTC ทุก bulk SMS ต้องขึ้น Sender ID, ส่งโปรเฉพาะ 8–21 น., มี opt-out 3 operator หลัก: AIS, TrueMove H, dtac แต่ละเจ้ามี filter ของตัวเอง ราคา: ฿0.20–0.80/SMS ตาม volume + sender ตลาด ~10,000 ล้าน SMS/ปี ส่วนใหญ่ OTP + transactional

---

## 1. NBTC (National Broadcasting and Telecommunications Commission)

### หน่วยงาน
- **กสทช.** = คณะกรรมการกิจการกระจายเสียง กิจการโทรทัศน์ และกิจการโทรคมนาคมแห่งชาติ
- ตั้งเมื่อปี 2553
- ดูแล: ใบอนุญาต, spectrum, consumer protection, content

### บทบาทกับ SMS
- รับ complaint จากผู้บริโภค
- กำกับ operator (AIS, dtac, True)
- บังคับ Sender ID registration
- ปรับ + ระงับ sender ที่ผิด

---

## 2. กฎสำคัญสำหรับ SMS Marketing

### ⏰ Time Window
- **Promotional/Marketing SMS:** 08:00–21:00 เท่านั้น
- **OTP / Transactional:** 24 ชม
- **Holiday/Religious days:** บางวันห้ามแม้ในเวลา

### 📛 Sender ID Registration
- ต้องขึ้นทะเบียนกับ AIS, dtac, True
- Sender Name = alphanumeric, 11 ตัวอักษร
- ใช้ชื่อแบรนด์จริง — ห้ามใช้ใกล้กับแบรนด์อื่น
- กระบวนการ approve: 7–14 วัน
- ค่าธรรมเนียม: ฿1,000–฿5,000/sender/ปี (เปลี่ยนตามค่าย)

### ✅ Opt-out Requirement
- ทุก promotional SMS ต้องมี opt-out
- "พิมพ์ STOP เพื่อเลิกรับ" หรือ "Reply STOP"
- ต้อง process ภายใน 24 ชม

### 📜 Content Rules
- ❌ ห้ามหลอกลวง / fake offer
- ❌ ห้ามขายสินค้าผิดกฎหมาย
- ❌ ห้ามเนื้อหา 18+ (กับ list ทั่วไป)
- ❌ ห้ามแอบใช้ชื่อหน่วยงานอื่น
- ❌ ห้าม phishing link

### 🔒 PDPA Integration
- ต้องมี consent ก่อนส่ง marketing
- เก็บ proof of consent (timestamp, source)
- ดู [[K14-Compliance-AntiSpam]] เพิ่ม

---

## 3. โทษ (Penalties)

| ฝ่าฝืน | โทษ |
|---|---|
| Send without consent | ปรับ ฿20,000–฿200,000 + per case |
| Spam (complaint > X) | Sender ระงับชั่วคราว/ถาวร |
| Phishing / scam | คดีอาญา + ปรับ |
| Outside time window | Sender warning → ระงับ |
| ผิด PDPA | ปรับเพิ่ม ฿5M สูงสุด |

> **Reality:** Repeat offender อาจโดน **blacklist ทั้ง 3 operator** = หมดธุรกิจ

---

## 4. 🏢 3 Operators ของไทย

### AIS (Advanced Info Service)
- Market share: ~45%
- Brand: AIS, AIS Fibre
- SMS routing: หลายเส้น (premium/standard)
- Sender ID approval: ผ่าน AIS Business
- **Pro:** กว้าง, ความเร็วดี
- **Con:** spam filter เข้ม

### TrueMove H (True Corporation)
- Market share: ~35%
- Brand: TrueMove H, TrueOnline
- SMS via True Business
- **Pro:** routing เร็วใน Bangkok
- **Con:** filter เปลี่ยนบ่อย

### dtac (Total Access Communication)
- Market share: ~15–20%
- Brand: dtac
- หลัง merge กับ True เป็น **dtac-True (TrueMove H operator)** ปี 2566
- ใน practice = ใช้ infrastructure True

> **Note 2026:** Effectively มี 2 operator (AIS + True/dtac merged) + NT (National Telecom = TOT+CAT)

---

## 5. SMS Routing & Pricing

### Route Types

| Route | Cost | Quality | Use Case |
|---|---|---|---|
| **Premium / Direct** | ฿0.50–฿0.80 | สูงสุด | OTP, Banking |
| **Standard** | ฿0.30–฿0.50 | สูง | Transactional |
| **Bulk** | ฿0.20–฿0.30 | กลาง | Marketing |
| **Grey route** | ฿0.10–฿0.20 | ต่ำ | ❌ ห้าม (เลี่ยง operator) |

### Volume Discount
- < 10,000/เดือน: rate full
- 10,000–100,000: −10%
- 100,000–1M: −20%
- > 1M: −30% หรือ negotiate

### BoostSMS Pricing Context
ดู [[../02-Packages-Pricing]] — 9 packages ตั้งแต่ trial → enterprise+

---

## 6. ตลาด SMS ไทย (Market Size)

### 📊 Numbers (2024–2025 estimate)
- Total SMS volume: ~10 พันล้าน SMS/ปี
- A2P (Application-to-Person) market: ฿3,500–฿5,000 ล้าน/ปี
- Marketing SMS: ~30%
- Transactional: ~40%
- OTP: ~30%
- Growth: 5–8%/ปี (gradual, stable)

### 📈 Trends
- Marketing SMS **ลดลง** ทุกปี (LINE replace)
- OTP / Transactional **เพิ่มขึ้น** (banking, e-commerce)
- A2P revenue stable เพราะ price premium ขึ้น

---

## 7. Industry Verticals ที่ใช้ SMS เยอะ

### 🏦 Banking & Fintech (Top user)
- OTP login + transaction
- Balance alert
- Loan/Credit promo
- KBank, SCB, BBL, Krungsri — heavy senders

### 🛒 E-commerce
- Lazada, Shopee, JD Central
- Order confirmation, shipping, abandon cart

### 📞 Telco
- TrueMove, AIS internal — package promo

### 🏥 Healthcare
- Appointment reminder
- Lab result ready

### 🛍 Retail
- Loyalty alert
- Flash sale

### 🛫 Travel
- Booking confirmation
- Flight update
- Hotel reminder

---

## 8. Anti-spam Filters (Operator Level)

### AIS Filter Patterns (observed)
- คำต้องห้าม: "ฟรี" + "!" + URL ในข้อความสั้น
- Sender ID ไม่ approved → block
- Volume spike > threshold → throttle
- Same content จาก sender เดิม > N ครั้ง → flag

### True/dtac Filter
- Similar logic
- Latency optimization vs filter strict
- บางช่วงเวลา filter เข้มขึ้น (เช่น เทศกาล)

### วิธี Maintain Deliverability
- ✅ ใช้ approved sender ID
- ✅ Vary content (template ละกัน)
- ✅ Throttle send rate
- ✅ Avoid trigger words ("ฟรี!!!" "ด่วน!!!")
- ✅ มี proper opt-out
- ✅ Clean list (remove bounce)

---

## 9. ปฏิทินสำคัญสำหรับ SMS Marketer ไทย

| เดือน | กิจกรรม | SMS Volume |
|---|---|---|
| ม.ค. | ปีใหม่, วันเด็ก | สูงต้นเดือน |
| ก.พ. | ตรุษจีน, Valentine | สูง |
| มี.ค. | ผัก/นมแม่ | กลาง |
| เม.ย. | สงกรานต์ (13–15) | **สูงสุด** |
| พ.ค. | วันแรงงาน | กลาง |
| มิ.ย. | วันพ่อแห่งชาติ (อังกฤษ) | กลาง |
| ก.ค. | วันเข้าพรรษา | ต่ำ |
| ส.ค. | วันแม่ (12) | **สูง** |
| ก.ย. | เปิดเทอม | กลาง |
| ต.ค. | กินเจ, ออกพรรษา | กลาง |
| พ.ย. | ลอยกระทง, Black Friday | **สูง** |
| ธ.ค. | ปีใหม่, คริสต์มาส | **สูงสุด** |

---

## 10. ผู้เล่นหลักในตลาด A2P SMS ไทย

### Operator-led
- AIS Business SMS
- True Business SMS

### Local Aggregators (B2B SMS)
- **Thaibulksms** — market leader, longest track record
- **Hashlinks** — multi-channel
- **ThaiSMS / SMS Premium / SMS Master** — various brands
- **SMS Live / Boost SMS / BoostSMS** ⭐ — our product

### Global Players (Thailand presence)
- **Twilio** (US, programmatic)
- **MessageBird/Bird** (NL)
- **Vonage** (UK)
- **Plivo** (US)
- **Infobip** (Croatia, strong APAC)
- **Sinch** (Sweden)

ดูเทียบ feature → [[K12-Competitor-Landscape]]

---

## 🔗 อ่านต่อ

- Sender Name detail → [[K09-Sender-Name-Thailand]]
- Compliance → [[K14-Compliance-AntiSpam]]
- Deliverability → [[K13-Deliverability-DLR]]
- Competitors → [[K12-Competitor-Landscape]]

## 📚 Resources

- NBTC: https://www.nbtc.go.th
- กฎหมาย: พ.ร.บ.กิจการโทรคมนาคม
