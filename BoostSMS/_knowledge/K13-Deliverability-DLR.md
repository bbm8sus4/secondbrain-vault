---
source: agent synthesis 2026-07-06
last_verified: 2026-07-06
status: live
---

# K13 · Deliverability & DLR — ทำไม SMS ส่งไม่ถึง

> **TL;DR (EN):** "Sent" ≠ "Delivered". A DLR (Delivery Report) is the operator's receipt confirming the handset actually got the message. Standard SMPP statuses: DELIVRD, UNDELIV, EXPIRED, REJECTD, ACCEPTD, UNKNOWN. In Thailand the top delivery killers are: unregistered Sender ID (operator hard-block), content-based spam filters at AIS/True-dtac, invalid/recycled numbers, and phones off past validity period. Healthy benchmark: **delivery rate > 95%** on clean lists via direct routes. Monitor per-operator, use seed numbers, and treat a sudden drop on one operator as a filter/route incident.
>
> **สรุป (TH):** "ส่งแล้ว" ไม่เท่ากับ "ถึงมือ" — DLR คือใบตอบรับจาก operator ว่าข้อความเข้าเครื่องจริง สถานะหลัก: DELIVRD, UNDELIV, EXPIRED, REJECTD สาเหตุส่งไม่ถึงในไทยอันดับต้น ๆ: Sender ID ไม่ได้ขึ้นทะเบียน (โดน block), spam filter ของ AIS/True-dtac, เบอร์ตาย/เบอร์เปลี่ยนมือ, เครื่องปิดเกิน validity period เป้าที่ดี: **delivery rate > 95%** บน list สะอาด + direct route ต้อง monitor แยกราย operator ถ้า drop ที่ค่ายเดียว = filter/route มีปัญหา

---

## 1. DLR คืออะไร (Delivery Report)

### เส้นทางของ SMS 1 ข้อความ

```
Platform → Aggregator → SMSC (operator) → เสาสัญญาณ → มือถือ
   ▲                        │
   └──────── DLR ◀──────────┘
        (ใบตอบรับย้อนกลับ)
```

- **Submit** = platform ส่งเข้า operator สำเร็จ (แค่ "รับเรื่อง")
- **DLR** = operator ยืนยันปลายทาง — ถึงเครื่อง / ไม่ถึง / รอ
- DLR กลับมาช้าได้ตั้งแต่ **ไม่กี่วินาที → หลายชั่วโมง** (เครื่องปิด = รอจนเปิด)

> **จุดที่คนเข้าใจผิดบ่อยสุด:** report "Sent 100%" ไม่ได้แปลว่าลูกค้าได้รับ 100% — ต้องดู **Delivered** เท่านั้น

---

## 2. สถานะ DLR มาตรฐาน (SMPP Standard)

| Status | ความหมาย | Final? | ทำอะไรต่อ |
|---|---|---|---|
| **DELIVRD** | ถึงมือถือแล้ว | ✅ Final | นับเป็น delivered |
| **ACCEPTD** | operator รับแล้ว รอส่งต่อ | ⏳ ชั่วคราว | รอ status ถัดไป |
| **ENROUTE** | กำลังเดินทางใน network | ⏳ ชั่วคราว | รอ |
| **UNDELIV** | ส่งไม่ได้ (เบอร์ผิด/ตาย/block) | ✅ Final | เช็ค error code, เอาออกจาก list ถ้าเบอร์ตาย |
| **EXPIRED** | เกิน validity period (เครื่องปิดนาน) | ✅ Final | retry แคมเปญหน้า, ดู pattern |
| **REJECTD** | operator ปฏิเสธ (filter/sender ไม่ approve) | ✅ Final | เช็ค sender + content ทันที |
| **DELETED** | ถูกลบก่อนถึง | ✅ Final | หายาก — สอบ route |
| **UNKNOWN** | ไม่รู้สถานะ | ❓ | เจอเยอะ = สงสัย grey route |

### Error Codes
- นอกจาก status ยังมี **error code** ราย operator/aggregator (เช่น absent subscriber, call barred, handset busy)
- แต่ละ vendor ใช้รหัสไม่เหมือนกัน — ต้องขอ mapping table จาก aggregator ที่ใช้

---

## 3. Metrics ที่เกี่ยวข้อง

```
Submitted 100%
   └─ Accepted 99%        (operator รับ)
        └─ Delivered 96%  ← ตัวจริงที่ต้องดู
        └─ Failed 3%      (UNDELIV + REJECTD + EXPIRED)
```

| Metric | สูตร | เป้า |
|---|---|---|
| **Delivery rate** | Delivered ÷ Submitted | > 95% |
| **Failure rate** | Failed ÷ Submitted | < 5% |
| **DLR latency** | เวลาจาก submit → DLR final | ส่วนใหญ่ < 1 นาที |
| **Pending > 24h** | ค้างไม่ final | ควรใกล้ 0 |

> Delivery rate เชื่อมกับ KPI ภาพรวม → ดู [[K06-SMS-Metrics-KPIs]]

---

## 4. 🇹🇭 สาเหตุที่ SMS ส่งไม่ถึงในไทย

### 1️⃣ Sender ID ไม่ได้ขึ้นทะเบียน (ตัวการอันดับ 1)
- AIS / True-dtac **hard-block** sender ที่ไม่ approve → REJECTD ยกแคมเปญ
- Sender approve ค่ายเดียว แต่ส่งทุกค่าย = ถึงแค่ค่ายเดียว
- ดูขั้นตอนขึ้นทะเบียน → [[K09-Sender-Name-Thailand]]

### 2️⃣ Content Filter ของ Operator
- คำ trigger: "ฟรี!!!", "ด่วน!!!", link แปลก ๆ ในข้อความสั้น
- ส่ง template เดิมซ้ำ volume สูง → โดน flag
- ช่วงเทศกาล filter มักเข้มขึ้น
- รายละเอียด filter ราย operator → [[K08-Thai-SMS-Market-NBTC]]

### 3️⃣ เบอร์ปลายทางมีปัญหา
- เบอร์ยกเลิก / เบอร์เวียนกลับมาขายใหม่ (recycled)
- เบอร์พิมพ์ผิด format (ไม่ใช่ 66xxxxxxxxx)
- MNP (ย้ายค่ายเบอร์เดิม) — route ผิดค่ายถ้า aggregator ไม่ lookup

### 4️⃣ เครื่องปิด / นอกพื้นที่
- SMSC จะ retry ตาม **validity period** (ปกติ 24–72 ชม)
- เกินกำหนด → EXPIRED

### 5️⃣ Route คุณภาพต่ำ (Grey Route)
- ราคาถูกผิดปกติ = มักอ้อม operator → DLR ปลอม (ตอบ DELIVRD ทั้งที่ไม่ถึง)
- สังเกต: delivery รายงานสวยแต่ CTR ต่ำผิดปกติ / OTP ลูกค้าบอกไม่ได้รับ

### 6️⃣ ผู้รับ block เอง
- iOS/Android filter ข้อความจากคนไม่รู้จัก, app กรอง spam (เช่น Whoscall)
- ข้อความ "ถึงเครื่อง" (DELIVRD) แต่ตกถัง junk — DLR ตรวจไม่เห็นชั้นนี้

---

## 5. Validity Period

- ค่าที่ platform กำหนดว่า SMSC จะพยายามส่งนานแค่ไหนก่อนตีเป็น EXPIRED
- **Marketing:** ตั้งสั้น (เช่น 6–12 ชม) — โปรหมดเขตแล้วส่งถึงทีหลัง = เสียเครดิตฟรี + ลูกค้างง
- **OTP:** ตั้งสั้นมาก (5–15 นาที) — OTP เก่าถึงช้าไร้ประโยชน์
- **Transactional:** 24–48 ชม ได้

---

## 6. Monitoring ที่ควรทำ

### Dashboard ขั้นต่ำ
- Delivery rate **แยกราย operator** (AIS / True-dtac / NT) — รวมกันจะมองไม่เห็นปัญหารายค่าย
- Failure breakdown ราย status (UNDELIV vs REJECTD vs EXPIRED บอกคนละโรค)
- Trend รายวัน/รายแคมเปญ

### Seed Number Testing
- มีซิมทดสอบครบทุกค่าย (AIS, True, dtac เดิม, NT)
- ส่งเข้าซิมจริงก่อนยิงแคมเปญใหญ่ — เช็คว่า sender แสดงถูก, ลิงก์กดได้, ไม่โดน filter

### Alert Rules (ตัวอย่าง)
| เงื่อนไข | สัญญาณ |
|---|---|
| Delivery < 90% ในแคมเปญ | route หรือ list มีปัญหา |
| REJECTD spike ที่ค่ายเดียว | sender/content โดน filter ค่ายนั้น |
| EXPIRED สูงผิดปกติ | ส่งเวลาไม่เหมาะ หรือ list เก่ามาก |
| DELIVRD 100% เป๊ะตลอด | น่าสงสัย grey route / fake DLR |

---

## 7. Checklist เพิ่ม Deliverability

- ✅ ใช้ Sender ID ที่ approve ครบทุก operator
- ✅ ใช้ direct/standard route — เลี่ยง grey route เด็ดขาด
- ✅ Clean list สม่ำเสมอ: ตัดเบอร์ UNDELIV ซ้ำ ≥ 2–3 ครั้ง
- ✅ เลี่ยง trigger words + vary template → ดู [[K03-SMS-Copywriting]]
- ✅ Throttle send rate อย่ายิง spike ก้อนเดียว
- ✅ ส่งในเวลา 08:00–21:00 ตามกฎ → ดู [[K07-Timing-Frequency]]
- ✅ ตั้ง validity period ให้เหมาะกับประเภทข้อความ
- ✅ ทดสอบ seed number ก่อนแคมเปญใหญ่ทุกครั้ง
- ✅ เก็บ DLR log ไว้ตอบ dispute ลูกค้า ("ส่งจริงไหม")

---

## 🔗 อ่านต่อ

- KPI ภาพรวม → [[K06-SMS-Metrics-KPIs]]
- Operator filter + ตลาดไทย → [[K08-Thai-SMS-Market-NBTC]]
- Sender Name registration → [[K09-Sender-Name-Thailand]]
- Compliance (โดน block เพราะผิดกฎ) → [[K14-Compliance-AntiSpam]]
