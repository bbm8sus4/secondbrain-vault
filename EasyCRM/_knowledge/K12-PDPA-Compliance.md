# K12 · PDPA Compliance (สำหรับ Loyalty / CRM)

> **TL;DR (EN):** PDPA = Thailand's Personal Data Protection Act, enforced since June 2022. Modeled after GDPR. Any business storing customer data (name, phone, LINE ID, purchase history) must (1) get explicit consent, (2) state purpose, (3) honor data subject rights, (4) appoint DPO if scale exceeds threshold, (5) report breaches within 72h. Fines: up to ฿5M criminal + ฿5M administrative + civil damages.
>
> **สรุป (TH):** PDPA = พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล ไทย บังคับใช้ มิ.ย. 2565 เลียนแบบ GDPR ของ EU ใครเก็บข้อมูลลูกค้า (ชื่อ, เบอร์, LINE ID, ประวัติซื้อ) ต้อง (1) ขอ consent ชัด, (2) บอกวัตถุประสงค์, (3) เคารพสิทธิ์ลูกค้า, (4) แต่ง DPO ถ้า scale ใหญ่, (5) แจ้ง breach ใน 72 ชม โทษ: รวมสูงสุดเกิน ฿15M + แพ่ง

---

## 1. PDPA คืออะไร

**Personal Data Protection Act พ.ศ. 2562** (Thai PDPA)
- ประกาศ: 27 พ.ค. 2562
- บังคับใช้เต็ม: 1 มิ.ย. 2565
- ผู้บังคับใช้: สำนักงานคุ้มครองข้อมูลส่วนบุคคล (PDPC)
- โมเดล: GDPR (EU) แต่ปรับให้เข้ากับบริบทไทย

---

## 2. ข้อมูลส่วนบุคคล (Personal Data) คืออะไร

### ข้อมูลทั่วไป (General Personal Data)
- ชื่อ-นามสกุล
- เลขบัตรประชาชน
- เบอร์โทรศัพท์
- อีเมล
- ที่อยู่
- **LINE ID / LINE User ID**
- **เลขบัญชีธนาคาร** (จากสลิป!)
- ประวัติการซื้อ
- IP address, cookie ID, device ID

### ข้อมูลอ่อนไหว (Sensitive Personal Data)
- เชื้อชาติ ศาสนา ความคิดเห็นทางการเมือง
- พฤติกรรมทางเพศ
- ประวัติอาชญากรรม
- ข้อมูลสุขภาพ
- ข้อมูลพันธุกรรม biometric
- → **ต้อง consent แยกชัดเจน + ระวังพิเศษ**

> **EasyCRM context:** ข้อมูลที่เก็บ = general personal data (LINE ID, name, phone, purchase history) ไม่ใช่ sensitive — แต่ยังต้องทำตาม PDPA ครบ

---

## 3. ฐานทางกฎหมาย (Legal Basis) 7 ข้อ

| ฐาน | EN | ใช้เมื่อ |
|---|---|---|
| 1. **Consent** | ความยินยอม | ขอชัดเจน, ถอนได้ |
| 2. **Contract** | สัญญา | จำเป็นต่อการปฏิบัติสัญญา |
| 3. **Legal obligation** | กฎหมายกำหนด | เช่น ใบกำกับภาษี |
| 4. **Vital interest** | ปกป้องชีวิต | กรณีฉุกเฉิน |
| 5. **Public interest** | ผลประโยชน์สาธารณะ | ภาครัฐ |
| 6. **Legitimate interest** | ประโยชน์โดยชอบ | บริษัทใช้พอเหมาะ, ไม่ละเมิด |
| 7. **Research/Statistic** | วิจัย/สถิติ | มีมาตรการคุ้มครอง |

> **สำหรับ Loyalty program:** มักใช้ **Consent + Contract + Legitimate Interest**

---

## 4. สิทธิ์ของเจ้าของข้อมูล (Data Subject Rights) 8 ข้อ

ลูกค้ามีสิทธิ์ขอ:

| สิทธิ์ | EN |
|---|---|
| 1. ขอข้อมูลที่บริษัทเก็บ | Right to access |
| 2. ขอแก้ไขข้อมูล | Right to rectification |
| 3. ขอลบข้อมูล | Right to erasure (right to be forgotten) |
| 4. ขอจำกัดการใช้ | Right to restrict processing |
| 5. ขอย้ายข้อมูลไปที่อื่น | Right to data portability |
| 6. คัดค้านการใช้ | Right to object |
| 7. เพิกถอน consent | Right to withdraw consent |
| 8. ร้องเรียน PDPC | Right to lodge complaint |

> **EasyCRM ต้องตอบสนองภายใน 30 วัน**

---

## 5. หน้าที่ของผู้ใช้ EasyCRM (ผู้ควบคุมข้อมูล)

### ก่อนเก็บข้อมูล (Pre-collection)
- ✅ ทำ **Privacy Policy** ให้ลูกค้าอ่าน
- ✅ ขอ consent ชัดเจน — ไม่ใช่ pre-checked box
- ✅ บอกวัตถุประสงค์, ระยะเวลาเก็บ, สิทธิ์ผู้ให้ข้อมูล

### ระหว่างเก็บ (Processing)
- ✅ ใช้ตามวัตถุประสงค์ที่แจ้งเท่านั้น
- ✅ เก็บ minimum necessary
- ✅ มี security (encryption, access control)
- ✅ จำกัดการแชร์ third party

### หลังเก็บ (Post-processing)
- ✅ ลบเมื่อพ้นวัตถุประสงค์
- ✅ ตอบสนองคำขอลูกค้าใน 30 วัน
- ✅ แจ้ง breach ภายใน 72 ชม

### ถ้าธุรกิจใหญ่ (เงื่อนไข)
- ✅ แต่งตั้ง **DPO** (Data Protection Officer)
- ✅ ทำ **DPIA** (Data Protection Impact Assessment) ก่อนเก็บข้อมูลที่ risk สูง
- ✅ ทำ **Record of Processing Activities (RoPA)**

---

## 6. ข้อความ Consent ที่ดี (ตัวอย่างสำหรับ EasyCRM)

```
✅ ตัวอย่างที่ถูกต้อง

ฉันยินยอมให้ [ชื่อร้าน] เก็บและใช้ข้อมูลส่วนบุคคล
(ชื่อ, เบอร์โทร, LINE ID, ประวัติการซื้อ)
เพื่อวัตถุประสงค์ดังนี้:

☐ ให้บริการสะสมแต้มและสมาชิก (จำเป็น)
☐ ส่งโปรโมชั่นและข่าวสารผ่าน LINE (ทางเลือก)
☐ วิเคราะห์พฤติกรรมเพื่อพัฒนาสินค้า (ทางเลือก)

ระยะเวลาเก็บ: ตราบที่เป็นสมาชิก + 5 ปีหลังยกเลิก
ฉันมีสิทธิ์ขอเข้าถึง/แก้ไข/ลบข้อมูล โดยติดต่อ
[email] หรือ [LINE OA]

[ ] ฉันได้อ่านและยอมรับ Privacy Policy
[ปุ่ม "ยืนยัน"]   [ปุ่ม "ยกเลิก"]
```

❌ **ตัวอย่างผิด:**
- Pre-checked checkbox
- "การลงทะเบียน = ยอมรับ" (implied consent)
- ไม่บอกวัตถุประสงค์ชัด
- รวม consent ทุกอย่างใน 1 checkbox

---

## 7. โทษ (Penalties)

| ประเภท | สูงสุด |
|---|---|
| **โทษทางอาญา** | จำคุก 6 เดือน–1 ปี + ปรับ ฿500,000–฿1,000,000 |
| **โทษปกครอง** | ปรับ ฿1M–฿5M |
| **โทษทางแพ่ง** | ค่าเสียหาย + ค่าปรับเชิงลงโทษ 2 เท่า |

> **Note:** SME ที่ทำผิด PDPA จริง ๆ มักโดน **โทษปกครอง** ก่อน — แต่ถ้า breach รุนแรงและไม่แจ้ง = อาญา

---

## 8. PDPA Checklist สำหรับร้านค้าใช้ EasyCRM

- [ ] มี Privacy Policy บนหน้าลงทะเบียน
- [ ] Consent checkbox ไม่ pre-checked
- [ ] แยก consent **จำเป็น** vs **marketing**
- [ ] บอกวัตถุประสงค์ที่ใช้ข้อมูลชัดเจน
- [ ] บอกระยะเวลาเก็บ
- [ ] บอกช่องทางติดต่อ (email/LINE OA)
- [ ] มี process รับคำขอลูกค้า (access/delete)
- [ ] มี process แจ้ง breach
- [ ] Train พนักงานพื้นฐาน PDPA
- [ ] ถ้าใหญ่ (> X สมาชิก) — แต่ง DPO

---

## 9. GDPR — เปรียบเทียบเร็ว

| | PDPA (TH) | GDPR (EU) |
|---|---|---|
| บังคับใช้ | 1 มิ.ย. 2565 | 25 พ.ค. 2561 |
| Penalty max | ~฿15M รวม | €20M หรือ 4% global revenue |
| Scope | ในไทย / ขายให้คนไทย | ใน EU / ขายให้คน EU |
| DPO required | conditions | conditions |
| Breach notification | 72h | 72h |
| Subject rights | 8 rights | 8 rights |

> ใช้แทนกันได้ใน 80% — ถ้าทำ GDPR compliant แล้ว PDPA จะใกล้เคียง

---

## 10. ⚠️ Sensitive Points สำหรับ EasyCRM

### 🔍 LINE User ID
- = personal data ภายใต้ PDPA
- เก็บได้ แต่ต้อง consent + วัตถุประสงค์ชัด

### 💳 ข้อมูลสลิป (EasySlip integration)
- เลขบัญชี = personal data
- ต้องบอกว่าเก็บเพื่อ verify เท่านั้น
- ห้ามใช้ทำ marketing ภายนอก

### 📊 RFM segmentation / behavior analysis
- = "automated decision-making" ภายใต้ PDPA
- ลูกค้ามีสิทธิ์รู้ logic + คัดค้าน
- แนะนำ: ใส่ใน Privacy Policy ว่ามีการ profile

### 🤝 Sub-processor (Subdomain `.easy-crm.co`)
- EasyCRM = data processor
- ร้านค้า = data controller
- ต้องมี **Data Processing Agreement (DPA)** ระหว่างทั้งสอง

---

## 🔗 อ่านต่อ

- ข้อมูล RFM ที่เก็บ → [[K02-RFM-Segmentation]]
- กลไก Loyalty → [[K04-Loyalty-Program-Types]]
- Audit ด้าน security → [../../../qa_easycrm_security|EasyCRM security audit] (ถ้ามี)

## 📚 Resources

- PDPC official: https://www.pdpc.or.th
- Thai PDPA full text: https://www.ratchakitcha.soc.go.th
- GDPR text: https://gdpr.eu
