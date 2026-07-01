# Meeting — ปรับปรุงระบบและแผนงาน BoostSMS

- **วันที่:** 2026-07-01
- **หัวข้อ:** AIS Provider Transition + Infra Roadmap + Finance/Compliance
- **สถานะ:** เริ่มเปลี่ยน provider กรกฎาคม 2569

---

## 1. เปลี่ยน Provider → AIS (เริ่ม ก.ค. 2569)

### Workflow
- ใช้แนวคิด **LeanFlow** — สั้นที่สุด บริหารจากหลังบ้าน (Back-office)
- ดาวน์โหลดไฟล์เป็น **CSV / Excel / PDF** เพื่อส่งให้ AIS ตามรอบ

### Data Handling
- **AIS ไม่เก็บข้อมูลลูกค้า** — ข้อมูลทั้งหมดอยู่ที่เรา
- ยึดหลัก data sovereignty ฝั่ง BoostSMS

### User Experience
- ต้องมี **Progress Bar** ให้ลูกค้าเห็นสถานะการทำงานของระบบ

### Redundancy
- เตรียมแผน **สลับท่อส่ง AIS ↔ Dtac** กรณีเกิดปัญหา เพื่อรักษาความต่อเนื่อง

---

## 2. Infrastructure Development

- **Speed Optimization:** เพิ่มท่อส่งเป็น **2 เส้น** เพื่อให้ส่ง OTP เร็วขึ้น
- **Internal Pipeline:** เราต้องบริหารจัดการท่อส่งเอง เพื่อประสิทธิภาพสูงสุด
- **Reporting:** ปรับ format รายงานให้สอดคล้องกับของ AIS

---

## 3. Finance & Policy

### ต้นทุนและ Margin
- **ต้นทุนจาก AIS:** 0.29 บาท / SMS
- **เป้าหมาย 500,000 SMS:** 155,150 บาท (หักลบส่วนต่าง 3% ตามเงื่อนไข)

### Credit & Refund
- **Call back ที่มีปัญหา:** นำมาคืนเครดิตให้ลูกค้า
- **Log System:** ต้องมีบันทึก log การคืนเครดิต + รายการทางการเงินที่ชัดเจน
- **Compliance:** นโยบายคืนเงินต้องรัดกุม สอดคล้องกับระเบียบ **กสทช.**

---

## 4. Action Items

### บอม — แบบฟอร์มกรอกข้อมูลลูกค้า (AIS Onboarding)
- นำเงื่อนไข AIS มาวิเคราะห์และแยกขั้นตอน
- จัดทำเอกสาร **"แบบฟอร์มการกรอกข้อมูลสำหรับลูกค้า"**
  - เน้น **Lean** — สั้น กระชับ ไม่ถามซ้ำ ไม่ถามฟิลด์ที่ไม่ต้องใช้
  - **ใช้งานง่าย** — flow ตรง ลูกค้ากรอกจบภายในครั้งเดียว
- บันทึกงานนี้ลง Obsidian ให้ project BoostSMS ✅ (ไฟล์นี้)

### CRM System — เพิ่มฟีเจอร์ดูแลลูกค้าใน BoostSMS
- เพิ่ม **ระบบ CRM** เข้าไปเป็นฟีเจอร์ใน BoostSMS
- จุดประสงค์: ให้ทีมและลูกค้ามีเครื่องมือดูแล relationship + ประวัติ + ติดตามผลได้ในแพลตฟอร์มเดียว
- ต้องขยาย scope + เขียน content เพิ่ม (spec / requirement / user story)
- ประเด็นที่ต้องคุยต่อ:
  - overlap กับ [[../../EasyCRM/หน้าหลัก|EasyCRM]] มั้ย? (แยก product หรือ shared component?)
  - อยู่ใน package ไหน (Trial ให้ใช้มั้ย? หรือ paid-only?)
  - impact กับ [[../02-Packages-Pricing]] และ [[../03-Sales-Commission]]

---

## Related
- [[../01-Overview]]
- [[../02-Packages-Pricing]]
- [[../06-Backoffice-Admin]]
- [[../_knowledge/K08-Thai-SMS-Market-NBTC]]
