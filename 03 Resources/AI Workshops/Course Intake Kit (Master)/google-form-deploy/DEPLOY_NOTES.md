# Course Intake Kit — clasp deploy notes

**สร้างเมื่อ:** 2026-07-15 · โดย clasp (bobbysomporn@gmail.com)
**Project แยกต่างหาก** จากฟอร์มขอนแก่นที่มี response แล้ว (ปลอดภัย ไม่แตะของเดิม)

- **scriptId:** `1DBchyJRg8Qr8S8TnrVRsSH9R_puICnJqODrc00JYE9Y-MlGRWAv6MWvB`
- **Editor:** https://script.google.com/d/1DBchyJRg8Qr8S8TnrVRsSH9R_puICnJqODrc00JYE9Y-MlGRWAv6MWvB/edit
- **ฟังก์ชันหลัก:** `createAllForms` — สร้างฟอร์ม MASTER ทั้ง 4 ตัว + log URLs

## สถานะ: รันแล้ว 2026-07-15 — ฟอร์ม MASTER ทั้ง 4 สร้างเสร็จ

ลิงก์ทั้งหมดอยู่ที่ `../FORM_URLS.md`
- **Deployment (Web App):** `AKfycbyMFn1cAHuZmNd6676eiCbp8_siNUkeZvAvDGsFZYAHMzz-17uwU-9Jj-srsuW2qAgb` (@2)
- เปิด exec URL = โชว์ลิงก์ฟอร์ม (ไม่สร้างซ้ำ) · `?action=cleanup` = trash duplicate ชุด 2026-07-15

## กันสร้างซ้ำ

- `createAllForms` ใช้ **LockService + ScriptProperties** — property check เดี่ยวๆ ไม่พอ
  (บทเรียน 2026-07-15: doGet โดน trigger ซ้อน 3 รอบพร้อมกัน ก่อน property ถูกเขียน → ได้ 12 ฟอร์ม
  ต้อง trash ไป 8 · LockService ทำให้ check-then-create เป็น atomic แล้ว)
- ถ้าตั้งใจจะสร้างชุดใหม่จริงๆ → รัน `createAllFormsForce` (ชุดเก่าไม่ถูกลบ ต้องไปลบเองใน Drive)

## ใช้งานต่อลูกค้า 1 ราย

เปิดฟอร์ม MASTER ใน Drive → **ทำสำเนา (Make a copy)** → แก้ในสำเนา:
- รายชื่อแผนก (ตัวเลือกข้อ "แผนก" ทุกฟอร์ม)
- รายการหัวข้อคอร์ส (B1/B2 ฟอร์ม 1 · grid ฟอร์ม 3 — เหลือเฉพาะที่สอนจริง)
- รายการบัญชีบริการ (ฟอร์ม 2) ให้ตรงเครื่องมือที่คอร์สใช้
- ชื่อฟอร์ม: เอา `[MASTER]` ออก ใส่ชื่อบริษัทลูกค้าแทน

**ห้ามส่งฟอร์ม MASTER ให้ลูกค้าตอบตรงๆ** — response จะปนกันทุกราย

## แก้เนื้อหากลางแล้ว push ใหม่

```bash
cd "~/SecondBrain/03 Resources/AI Workshops/Course Intake Kit (Master)/google-form-deploy"
# แก้ Code.gs (TOPICS / DEPARTMENTS อยู่บนสุด)
clasp push -f
# แล้วรัน createAllFormsForce ใน editor ถ้าอยากได้ฟอร์ม MASTER ชุดใหม่
```

⚠️ สคริปต์นี้ create-only — ไม่มี clearAllItems/delete ใดๆ (กติกาเดิม: ห้ามแตะฟอร์มที่มี response)
