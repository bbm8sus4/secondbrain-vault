---
source: agent synthesis 2026-07-06
last_verified: 2026-07-06
status: live
---

# K14 · Compliance & Anti-Spam — PDPA, Opt-in/Opt-out, NBTC

> **TL;DR (EN):** SMS marketing in Thailand sits under two regimes: **NBTC** (telecom rules — registered Sender ID, 08:00–21:00 promo window, mandatory opt-out) and **PDPA** (data protection — marketing SMS needs valid consent, revocable anytime, with proof kept). Practical rule: no consent record = don't send. Every promo message carries opt-out; STOP must be honored fast and permanently. Transactional/OTP messages don't need marketing consent but must not smuggle in promo content. US reference: TCPA (per-message statutory damages) shows how expensive spam can get.
>
> **สรุป (TH):** SMS marketing ไทยโดนกำกับ 2 ชั้น: **กสทช. (NBTC)** — Sender ID ต้องขึ้นทะเบียน, ส่งโปรได้ 8–21 น., ต้องมี opt-out และ **PDPA** — ส่ง marketing ต้องมี consent ที่ถูกต้อง ถอนได้ตลอด และเก็บหลักฐานไว้ กติกาง่าย ๆ: **ไม่มีหลักฐาน consent = ห้ามส่ง** ทุกข้อความโปรต้องมีช่องทางเลิกรับ พิมพ์ STOP แล้วต้องหยุดจริงและถาวร ส่วน OTP/transactional ไม่ต้องใช้ marketing consent แต่ห้ามแอบยัดโปรมาด้วย

---

## 1. ภาพรวม — กติกา 2 ชั้นของไทย

```
                 SMS Marketing ไทย
                        │
        ┌───────────────┴───────────────┐
   NBTC / กสทช.                      PDPA
   (กติกาช่องทาง)                 (กติกาข้อมูล)
   - Sender ID ขึ้นทะเบียน         - Consent ก่อนส่ง marketing
   - เวลา 08:00–21:00              - สิทธิถอน consent
   - ต้องมี opt-out                - เก็บ proof of consent
   - ห้ามเนื้อหาหลอกลวง            - โทษปกครอง + อาญา
```

- ผิดฝั่ง NBTC → sender โดน warning/ระงับผ่าน operator
- ผิดฝั่ง PDPA → โทษปรับทางปกครอง + ความเสี่ยงคดี
- รายละเอียดฝั่ง NBTC/ตลาด → [[K08-Thai-SMS-Market-NBTC]]

---

## 2. PDPA กับ SMS Marketing

### หลักการ
- **PDPA** (พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562, บังคับใช้เต็มมิ.ย. 2565)
- เบอร์โทร = ข้อมูลส่วนบุคคล → การส่ง SMS marketing = การ "ใช้" ข้อมูล ต้องมีฐานทางกฎหมาย
- สำหรับ direct marketing ฐานที่ปลอดภัยและใช้กันเป็นหลักคือ **consent**

### Consent ที่ใช้ได้ต้อง…
| เงื่อนไข | หมายถึง |
|---|---|
| **Freely given** | ไม่บังคับพ่วง — ห้าม "ต้องรับ SMS โปรถึงจะสมัครได้" |
| **Specific** | บอกชัดว่าส่งอะไร (ข่าวสาร/โปรโมชั่น ทาง SMS) |
| **Informed** | รู้ว่าใครส่ง เอาข้อมูลไปทำอะไร |
| **Unambiguous** | ต้อง opt-in เอง — ❌ pre-ticked checkbox ใช้ไม่ได้ |
| **Revocable** | ถอนได้ง่ายเท่าตอนให้ — และถอนแล้วต้องหยุดจริง |

### Proof of Consent (ต้องเก็บ)
- ใครให้ consent (เบอร์/ลูกค้า ID)
- ให้เมื่อไหร่ (timestamp)
- ให้ผ่านช่องทางไหน (ฟอร์มสมัคร, POS, LINE, เว็บ)
- ข้อความ consent เวอร์ชันที่เห็นตอนนั้น
> เวลาลูกค้า complaint หรือ regulator ถาม — **หลักฐานชุดนี้คือเกราะ**

### สิ่งที่ทำไม่ได้
- ❌ ซื้อ list เบอร์มาส่ง (ไม่มี consent กับเรา = ผิดตั้งแต่ต้น)
- ❌ เอาเบอร์จาก transaction เก่ามา blast โปรโดยไม่เคยขอ consent marketing
- ❌ ส่งต่อ/แชร์ list ให้บริษัทในเครือโดย consent ไม่ครอบคลุม

### โทษ PDPA
- ปรับทางปกครองสูงสุด **฿5,000,000** ต่อกรณี
- บางฐานความผิดมีโทษอาญา (จำคุก/ปรับ)
- + ความเสียหายทางแบรนด์ ซึ่งมักแพงกว่าค่าปรับ

---

## 3. Marketing vs Transactional — เส้นแบ่งสำคัญ

| ประเภท | ต้องมี marketing consent? | เวลา | ต้องมี opt-out? |
|---|---|---|---|
| **Promotional** (โปร/ข่าวสาร) | ✅ ต้องมี | 08:00–21:00 | ✅ ทุกข้อความ |
| **Transactional** (ยืนยันออเดอร์, นัดหมาย, แจ้งเตือนบริการ) | ❌ ใช้ฐานสัญญา/บริการ | 24 ชม | แนะนำมี |
| **OTP** | ❌ | 24 ชม | ไม่ต้อง |

> ⚠️ **กับดักคลาสสิก:** เอาข้อความ transactional มา "พ่วงโปร" — "ออเดอร์จัดส่งแล้ว! ลด 20% ครั้งหน้า โค้ด…" → กลายเป็น marketing ทันที ต้องใช้เกณฑ์ marketing เต็ม (consent + เวลา + opt-out)

---

## 4. Opt-out — ข้อบังคับ ไม่ใช่ option

### ขั้นต่ำที่ต้องทำ
- ทุก promotional SMS มีวิธีเลิกรับที่ชัด: "พิมพ์ STOP เพื่อเลิกรับ" / เบอร์กด *137 (ช่องทางกลางของ operator ไทยสำหรับเลิก SMS ค่าย) / link จัดการ preference
- Process ให้เร็ว — ตามแนวปฏิบัติไทยคือ **ภายใน 24 ชม** ยิ่งทันทียิ่งดี
- ปลดแล้ว = **ถาวร** เก็บลง suppression list (blacklist) กันส่งซ้ำจากทุกแคมเปญ
- ❌ ห้ามส่ง SMS "ยืนยันการเลิกรับ" เพิ่มอีกหลายข้อความ

### Suppression List Hygiene
- ทุกช่องทาง opt-out (STOP, call center, LINE, email) ต้องไหลลง list เดียวกัน
- Import list ใหม่ทุกครั้ง → เช็คชน suppression list ก่อนส่งเสมอ
- Opt-out rate เป็น health metric → ดู [[K06-SMS-Metrics-KPIs]]

---

## 5. Sender Name & Compliance

- Sender ID ที่ขึ้นทะเบียน = ตัวระบุความรับผิด — complaint ทั้งหมดวิ่งกลับมาที่ sender นั้น
- ใช้ sender ปลอม/เลียนแบรนด์อื่น = โดนทั้ง operator ban + ความผิดฐานหลอกลวง
- Sender โดน complaint สะสม → operator ระงับ = ทุกแคมเปญใต้ชื่อนั้นตายหมด (รวม OTP)
- **นัยยะเชิงธุรกิจ:** sender name คือ asset ที่ต้องรักษาประวัติให้สะอาด — แยก sender สำหรับ OTP กับ marketing เพื่อไม่ให้ marketing complaint ลาก OTP ล่มไปด้วย
- รายละเอียดการขึ้นทะเบียน → [[K09-Sender-Name-Thailand]]

---

## 6. เนื้อหาที่ห้าม (Content Rules)

- ❌ หลอกลวง / เงื่อนไขโปรไม่ตรงจริง
- ❌ สินค้า/บริการผิดกฎหมาย (พนัน, ยาไม่ขึ้นทะเบียน ฯลฯ)
- ❌ แอบอ้างหน่วยงานรัฐ / ธนาคาร / แบรนด์อื่น
- ❌ Phishing link, ลิงก์ย่อที่ปลายทางไม่ตรงกับที่บอก
- ❌ เนื้อหา 18+ ไปยัง list ทั่วไป
- ภาษาที่ดูเป็น spam ("ฟรี!!!", "รับเงินทันที") แม้ไม่ผิดตรง ๆ ก็เพิ่ม complaint + โดน filter → ดู [[K03-SMS-Copywriting]]

---

## 7. 🌍 อ้างอิงต่างประเทศ (เทียบเคียง)

| กติกา | ประเทศ | จุดเด่นที่ควรรู้ |
|---|---|---|
| **TCPA** | 🇺🇸 US | ค่าเสียหาย **$500–$1,500 ต่อข้อความ** — class action SMS spam มีมูลค่าหลักร้อยล้าน; ต้องมี prior express written consent |
| **GDPR + ePrivacy** | 🇪🇺 EU | consent มาตรฐานสูง, soft opt-in ได้เฉพาะลูกค้าเดิม + สินค้าใกล้เคียง + opt-out ทุกข้อความ |
| **CASL** | 🇨🇦 Canada | opt-in เข้มระดับต้น ๆ ของโลก, โทษถึง C$10M |
| **Spam Act 2003** | 🇦🇺 Australia | consent + identify sender + unsubscribe ทุกข้อความ |

> ใช้เป็น benchmark: มาตรฐาน "ขั้นต่ำไทย + วินัยแบบ EU" = ปลอดภัยทุกตลาด และเป็นจุดขายให้ลูกค้า enterprise ได้

---

## 8. ✅ Compliance Checklist (ใช้ก่อนยิงทุกแคมเปญ)

### ก่อนส่ง
- [ ] ทุกเบอร์ใน list มี consent record (ใคร/เมื่อไหร่/ช่องทาง)
- [ ] เช็คชน suppression list แล้ว
- [ ] Sender ID approve ครบทุก operator
- [ ] เวลา schedule อยู่ใน 08:00–21:00 (โปรโมชั่น)
- [ ] เนื้อหาไม่เข้าข่ายต้องห้าม + เงื่อนไขโปรตรงจริง
- [ ] มีข้อความ opt-out ชัดเจน

### หลังส่ง
- [ ] Process opt-out ภายใน 24 ชม → เข้า suppression list ถาวร
- [ ] Monitor complaint / opt-out rate (เกิน ~1% ต่อแคมเปญ = สัญญาณเตือน)
- [ ] เก็บ log การส่ง + DLR ไว้ตอบ dispute → ดู [[K13-Deliverability-DLR]]

---

## 🔗 อ่านต่อ

- ตลาดไทย + กฎ NBTC ละเอียด → [[K08-Thai-SMS-Market-NBTC]]
- Sender Name registration → [[K09-Sender-Name-Thailand]]
- เขียน copy ให้ไม่ดู spam → [[K03-SMS-Copywriting]]
- เวลา + ความถี่ที่ถูกกฎ → [[K07-Timing-Frequency]]
- Deliverability (ผลของการทำผิดกฎ) → [[K13-Deliverability-DLR]]
