# K09 · Sender Name / Sender ID — Thailand

> **TL;DR (EN):** Sender Name (alphanumeric, max 11 chars) is what shows up as "from" on the recipient's phone. In Thailand, all bulk SMS senders must register the Sender Name with each operator (AIS, True/dtac). Approval takes 7–14 days; rules forbid impersonation, generic words like "BANK", and special characters. The Sender Name is brand-critical — recipients ignore unknown senders.
>
> **สรุป (TH):** Sender Name = ชื่อแสดงเป็น "จาก" ในมือถือลูกค้า ขีดจำกัด 11 ตัวอักษร อัลฟ่านิวเมอริก ในไทย bulk SMS ทุกตัวต้องขึ้นทะเบียนกับแต่ละ operator (AIS, True/dtac) ใช้เวลา approve 7–14 วัน ห้ามแอบอ้าง ห้ามใช้คำกลาง ๆ ("BANK") ห้ามอักขระพิเศษ Sender Name = brand asset — ลูกค้าเมิน sender ที่ไม่รู้จัก

---

## 1. Sender Name คืออะไร

```
┌────────────────────────────────┐
│  EasySlip                     │ ← Sender Name (11 chars)
│  10:23 AM                      │
│                                │
│  เครดิตคงเหลือ 2,500 ตรวจสลิป │
│  ผ่าน LINE OA ของคุณ           │
│                                │
└────────────────────────────────┘
```

**Sender Name** (a.k.a. **Sender ID**, **Alpha Sender**, **Origin Address**) =
ข้อความที่แสดงเป็นผู้ส่งบนมือถือผู้รับ — แทนที่จะเป็นเบอร์โทร

---

## 2. Naming Rules (กฎตั้งชื่อ)

### ✅ ที่อนุญาต
- A–Z, a–z, 0–9
- ความยาว 3–11 ตัวอักษร
- Mix ตัวพิมพ์ใหญ่/เล็กได้
- ตัวเลขผสมได้

### ❌ ที่ไม่อนุญาต
- ช่องว่าง (บางค่าย OK, ส่วนใหญ่ห้าม)
- อักขระพิเศษ: !@#$%^&*()
- ภาษาไทย (Thai script)
- Generic words: "BANK", "SHOP", "PROMO", "DELIVERY"
- คำเลียนแบบแบรนด์อื่น
- คำที่ทำให้ confuse กับ official entity
- ชื่อสั้นเกิน (< 3 ตัว)

### 🆔 ตัวอย่างที่ใช้ได้

| Brand | Sender Name |
|---|---|
| EasySlip Co. | `EasySlip` |
| BoostSMS | `BoostSMS` |
| Thunder | `Thunder` หรือ `Thunder-AI` |
| ห้างฯ Lazada | `Lazada` |
| KBank | `K-Plus` หรือ `KBank` |
| 7-Eleven | `7Eleven` |
| Grab | `GrabTH` |

### ❌ ตัวอย่างที่ไม่ผ่าน

| ❌ Bad | ทำไม |
|---|---|
| `BANK` | generic |
| `Free!` | special char |
| `อีซี่สลิป` | Thai script |
| `EasySlip2024` | ผ่าน character แต่ดูสะเปะ |
| `Lazada-VN` | คล้ายแบรนด์อื่น |

---

## 3. กระบวนการขึ้นทะเบียน

### Step 1: เลือก Operator ที่จะส่งหา
- ต้องขึ้น **แยกกัน** ทุกค่าย (AIS, True, dtac)
- แต่ละ operator มี form + เอกสาร

### Step 2: เตรียมเอกสาร
- ✅ หนังสือรับรองบริษัท (อายุ < 3 เดือน)
- ✅ บัตร ปชช. กรรมการ
- ✅ ใบ ภพ.20 (VAT registration)
- ✅ Sample SMS content
- ✅ Use case description
- ✅ Privacy Policy URL
- ✅ Authorization letter (ถ้าใช้ aggregator)

### Step 3: ส่งฟอร์ม + รอ approve
- AIS: 7–10 วันทำการ
- True: 10–14 วันทำการ
- dtac: ~10 วันทำการ (now merged)

### Step 4: ทดสอบส่ง
- ส่ง SMS test ไป operator แต่ละค่าย
- Verify sender name แสดงถูก
- Verify DLR กลับ

### Step 5: Live & Maintain
- ค่าบำรุง sender (ต่ออายุ) ทุกปี ~฿1,000–฿5,000/sender/operator
- Update ถ้าเปลี่ยน use case
- Renew ก่อนหมดอายุ

---

## 4. Sender Name Strategy — กลยุทธ์

### 🎯 Brand-aligned (แนะนำ)
- ใช้ชื่อแบรนด์ตรง ๆ
- ลูกค้าจำได้ทันที
- ตัวอย่าง: `Thunder`, `EasySlip`, `BoostSMS`

### 🔗 Multi-purpose vs Dedicated
- **Multi-purpose:** ใช้ Sender Name เดียวสำหรับทุก SMS
  - ✅ ง่าย, จำง่าย
  - ❌ Mix OTP + promo = trust ปนกัน
- **Dedicated:** แยก Sender Name ตาม use case
  - `Thunder-OTP` (OTP only)
  - `Thunder` (transactional)
  - `Thunder-Promo` (marketing)
  - ✅ Trust แยก
  - ❌ ค่าใช้จ่ายเพิ่ม, ขึ้นทะเบียนหลาย

### 🌐 Geographic
- บางแบรนด์มี `BrandTH`, `BrandSG`, `BrandMY`
- ใช้เมื่อมีหลายตลาด

---

## 5. การใช้ Numeric Sender (ทางเลือก)

### Long Code
- เบอร์โทรปกติ (เช่น 02-xxx-xxxx)
- ไม่ต้องขึ้นทะเบียน Sender Name
- ❌ ดูเหมือนคน + spam อาจถูก block

### Short Code
- เบอร์สั้น 4–6 หลัก (เช่น 4567)
- เช่าจาก operator แพง (฿20,000–฿100,000/เดือน)
- ใช้กับ 2-way SMS, voting, contests
- ไม่ค่อยใช้ใน B2C marketing

> **Best practice:** ใช้ Sender Name (alpha) ทุกครั้งที่ทำได้ — looks brand, trust ดีกว่า

---

## 6. Sender Trust Hierarchy

```
ลูกค้าเปิดอ่าน SMS แค่ไหน?

  Brand Name ที่จำได้   →  ⭐⭐⭐⭐⭐ 98%+ open
  Sender Name ใกล้แบรนด์ →  ⭐⭐⭐⭐ 85%
  Sender Name ไม่รู้จัก  →  ⭐⭐⭐ 60%
  เบอร์ปกติ              →  ⭐⭐ 40%
  เบอร์ต่างประเทศ        →  ⭐ 15%
  Spam-flagged          →  ❌ ส่งไม่ถึง
```

---

## 7. ปัญหาที่พบบ่อย

### 😱 Sender Name ถูก Reject
**สาเหตุที่พบบ่อย:**
- คำใกล้แบรนด์อื่น (ตัวอย่าง: `BankPro` คล้ายธนาคาร)
- Generic words
- เอกสารไม่ครบ
- Use case description คลุมเครือ

**แก้:**
- ทำ name unique เฉพาะแบรนด์
- ส่งเอกสารครบ
- ระบุ use case ชัด

### 🚫 Sender ถูก Block (หลัง approve)
**สาเหตุ:**
- Volume spike กระทันหัน
- Spam complaint
- Content trigger filter

**แก้:**
- ติดต่อ operator account manager
- Provide proof of consent
- Adjust content

### 🐌 SMS Delay
**สาเหตุ:**
- Route ผิด (premium vs bulk)
- Operator queue สูง
- Throttling activated

**แก้:**
- ใช้ premium route สำหรับ OTP
- Distribute send rate

---

## 8. Multi-Sender Strategy ตัวอย่าง

### กรณี EasySlip / Thunder Solution

| Sender Name | Use Case |
|---|---|
| `EasySlip` | Transactional (เครดิต, balance) |
| `EasySlip-OTP` | OTP login |
| `Thunder-AI` | Marketing โปรโมต (BoostSMS) |
| `BoostSMS` | BoostSMS internal (notification users) |
| `BANKTECH` | Technical alert (banking-related) |

**ทำไมแยก?**
- ลูกค้า trust ต่อ use case
- ถ้า marketing โดน throttle → OTP ไม่กระทบ
- Compliance ง่ายขึ้น

---

## 9. International Sender ID

ถ้าส่ง SMS ไปต่างประเทศ:

| ประเทศ | Sender ID Rules |
|---|---|
| ไทย | Alpha 11 char, register |
| Singapore | Alpha (IMDA register) |
| Malaysia | Alpha (operator register) |
| Indonesia | OTP only on shortcode |
| US/Canada | Numeric only (10DLC, toll-free) |
| UK | Alpha 11 char, register |
| EU | Mostly alpha, country-specific |
| China | Numeric only, strict route |
| India | DLT registration mandatory |

> ส่งข้ามประเทศ = แต่ละประเทศแยก register

---

## 10. Quick Reference Checklist

### ก่อนเลือก Sender Name
- [ ] เป็นชื่อแบรนด์ของจริง (ไม่แอบอ้าง)
- [ ] 3–11 ตัวอักษร
- [ ] A–Z, 0–9 เท่านั้น
- [ ] ไม่ generic ("SHOP", "BANK")
- [ ] ตรวจไม่ซ้ำกับ existing sender
- [ ] อ่านง่าย, จำได้ง่าย

### ก่อนขึ้นทะเบียน
- [ ] เตรียมเอกสารบริษัทครบ
- [ ] Sample SMS content
- [ ] Privacy policy public URL
- [ ] Use case ชัด
- [ ] เผื่อเวลา 14 วัน

### ระยะ Live
- [ ] Test ทุก operator
- [ ] Monitor DLR
- [ ] Renew ก่อนหมดอายุ
- [ ] อัพเดต use case ถ้าเปลี่ยน

---

## 🔗 อ่านต่อ

- Thai market context → [[K08-Thai-SMS-Market-NBTC]]
- Compliance → [[K14-Compliance-AntiSpam]]
- Deliverability → [[K13-Deliverability-DLR]]
- Competitor sender practices → [[K12-Competitor-Landscape]]
