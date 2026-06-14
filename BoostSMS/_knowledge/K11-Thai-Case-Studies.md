# K11 · Thai SMS Case Studies

> **TL;DR (EN):** Thailand's SMS standouts are mostly transactional + OTP — Banking (KBank, SCB), e-commerce (Lazada, Shopee), telco (AIS, True), and government (Por Tor, Disaster alerts). Pure SMS marketing is being replaced by LINE OA for B2C, but SMS remains dominant for OTP, fraud alerts, and critical notifications. SME usage is still small but growing.
>
> **สรุป (TH):** SMS ในไทยจุดเด่นคือ transactional + OTP — ธนาคาร (KBank, SCB), e-commerce (Lazada, Shopee), telco, ภาครัฐ Marketing SMS ในระดับ B2C ถูก LINE OA แทนที่เยอะ แต่ SMS ยัง dominant สำหรับ OTP, fraud alert, critical notifications SME ใช้น้อย แต่กำลังโต

---

## 1. 🏦 Banking — Heaviest SMS Users in Thailand

### KBank (KPlus)
- OTP สำหรับทุก transaction
- Sender: `K-Plus`, `KPLUS`, `KBANK`
- Volume: เป็น top-3 sender ในไทย
- Use cases:
  - Login OTP
  - Transaction OTP
  - Balance alert
  - Promo (Real-time)
  - Credit card alert

### SCB Easy
- Sender: `SCB-EASY`
- Heavy OTP + transaction confirm
- Real-time fraud alert (innovative ในไทย)

### Bangkok Bank, Krungsri, Krungthai
- Similar pattern
- Lower volume than KBank/SCB

### บทเรียน
- ✅ ธนาคาร = trust channel — ใช้ SMS เป็น authoritative source
- ✅ Sender Name brand = part of brand experience
- ✅ Real-time = lower fraud loss

---

## 2. 🛒 E-commerce — Lazada, Shopee, JD Central

### Lazada Thailand
- Sender: `Lazada`
- Use cases:
  - OTP สำหรับ login
  - Order confirmation
  - Shipping notification
  - Live commerce reminder
  - Flash sale alert

### Shopee Thailand
- Sender: `Shopee`
- Pattern คล้าย Lazada
- เพิ่ม: live streaming alert, coin reward notification

### Performance
- Order confirmation SMS open rate ~99%
- Delivery notification = customer satisfaction driver

### บทเรียน
- ✅ E-commerce ขาด SMS ไม่ได้ (no app push fallback)
- ✅ Order tracking via SMS = standard expectation
- ✅ Flash sale + SMS = revenue spike

---

## 3. 📞 Telco — AIS, True, dtac

### Use Cases
- Package promo
- Data/airtime alert
- Top-up confirmation
- Network outage notification

### Sender Examples
- `AIS`, `AISBiz`, `12CallAIS`
- `TrueMove`, `TrueOnline`
- `dtac` (legacy)

### Volume
- Telco ส่ง SMS ตัวเอง 200M+ /เดือน
- เพื่อ retention + cross-sell

### บทเรียน
- ✅ Telco = ส่งเอง ลูกค้าตัวเอง = no friction
- ✅ Cross-sell SMS works because of pre-existing relationship
- ❌ Heavy SMS spam อาจทำให้ลูกค้า churn

---

## 4. 🚨 Government / Public — Por Tor (ภัยพิบัติ), Hospital

### Disaster Alert (Cell Broadcast)
- ปี 2562 บังคับใช้ระบบ disaster broadcast
- กรณีน้ำท่วม, แผ่นดินไหว
- Override silent mode ของมือถือ

### COVID-19 Alert (2020–2022)
- ภาครัฐใช้ SMS แจ้งผล PCR
- Booking vaccine
- Outbreak alert ในพื้นที่

### Hospital
- Appointment reminder
- Lab result ready
- Prescription pickup

### บทเรียน
- ✅ SMS = trusted government channel
- ✅ Critical alerts ที่ต้องถึงทุกคน

---

## 5. 🛵 Food Delivery — Grab, Foodpanda, LineMan

### Pattern
- Order placed → SMS confirm
- Driver assigned → SMS with driver info
- Out for delivery → SMS
- Delivered → SMS + rate

### Modern Trend
- Push notification เป็นหลัก
- SMS = fallback channel
- Total SMS volume ลดลง (LINE/Push แทนที่)

---

## 6. 🛒 Retail SME ในไทย — กำลังเริ่ม

### กรณี SME ที่ใช้ SMS เริ่มทำ
- ร้านนวด/สปา — Appointment reminder
- คลินิกความงาม — Promotion + follow-up
- ร้านเสริมสวย — Anniversary, birthday
- ร้านอาหารปลายทาง — Loyalty + reservation

### Pattern ทั่วไป
- ส่ง 1–2 ครั้ง/เดือน
- ใช้ aggregator (Thaibulksms, BoostSMS)
- เริ่มจาก promo → ต่อยอด birthday + appointment

### Pain Points
- ไม่รู้ว่าจะส่งให้ใคร (ไม่ม segment)
- กลัวรบกวนลูกค้า
- ไม่มี dashboard วัดผล

> **Opportunity ของ BoostSMS:** Educate SME + provide simple tools

---

## 7. 💎 Case Study เด่น (จากประสบการณ์ตรง)

### Thunder-AI (BoostSMS internal)
- ใช้ SMS แจ้ง credit, sender approval
- Sender: `Thunder-AI`, `EasySlip`, `BANKTECH`
- ดูข้อมูล Master Dashboard → [[../08-Master-Dashboard-Integration]]

### EasySlip
- ใช้ SMS แจ้ง slip verification credit + alert
- Cross-sell BoostSMS

### Major Bank XYZ (anonymized)
- A/B test: Sender `BankXYZ` vs `BANK_XYZ`
- Difference: 8% CTR uplift จากชื่อ readable

---

## 8. คดี / Spam ที่ขึ้นข่าวในไทย

### Loan Spam SMS (ต่อเนื่อง)
- เบอร์โทรศัพท์ปลอมส่ง "เงินกู้ดอกต่ำ"
- NBTC + DES ออก action regular
- บทเรียน: ทำไม sender ID registration สำคัญ

### Phishing SMS แบบ "DHL/ไปรษณีย์"
- Sender ปลอม → ลิงก์ malware
- คนไทยรับเฉลี่ย 5–10/เดือน

### ผลกระทบ
- ลูกค้าระแวง SMS ทั่วไป → CTR ลดลง
- Brand legitimate ต้องใช้ Sender Name ที่ชัด
- Education สำคัญ

---

## 9. Insight — ทำไม Marketing SMS ในไทยน้อยลง

### Causes
1. **LINE OA** ราคาถูกกว่า + interactive
2. **Spam fatigue** จาก loan/scam SMS
3. **PDPA** บังคับ consent ทำลำบาก
4. **NBTC** เข้มงวด sender registration
5. **App push** สำหรับแบรนด์ที่มี app

### Where SMS Still Wins
- ✅ OTP (LINE ไม่ใช่ secure enough)
- ✅ Transactional (operator-mandated)
- ✅ Critical alert (banking, healthcare)
- ✅ Win-back ลูกค้าที่ไม่ follow LINE
- ✅ First-touch (รู้แค่เบอร์)
- ✅ Cross-channel attribution (sender unique)

---

## 10. Opportunity Map สำหรับ BoostSMS

### Underserved Verticals
- **ร้านสปา/นวด/wellness** — appointment, loyalty
- **คลินิกความงาม** — follow-up, promo
- **ร้านอาหารกลาง** — reservation, member
- **อสังหา/รถมือสอง** — visit reminder, follow-up
- **ทันตแพทย์/หมอ private** — recall, reminder
- **โรงเรียน/สถาบันสอน** — class reminder, parent comm
- **ตัวแทนประกัน** — premium due, claim follow-up

### ที่ทำได้ดี (use case + script)
- → ดู [[../04-Funnel-Marketing-Plan]] สำหรับ industry funnel

---

## 🔗 อ่านต่อ

- Global case study → [[K10-Global-Case-Studies]]
- ตลาด Thai overview → [[K08-Thai-SMS-Market-NBTC]]
- คู่แข่ง → [[K12-Competitor-Landscape]]
- Funnel ขาย → [[../04-Funnel-Marketing-Plan]]
