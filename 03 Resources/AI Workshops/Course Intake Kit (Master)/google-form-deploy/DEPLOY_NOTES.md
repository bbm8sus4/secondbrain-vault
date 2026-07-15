# Course Intake Kit — clasp deploy notes

**สร้างเมื่อ:** 2026-07-15 · โดย clasp (bobbysomporn@gmail.com)
**Project แยกต่างหาก** จากฟอร์มขอนแก่นที่มี response แล้ว (ปลอดภัย ไม่แตะของเดิม)

- **scriptId:** `1DBchyJRg8Qr8S8TnrVRsSH9R_puICnJqODrc00JYE9Y-MlGRWAv6MWvB`
- **Editor:** https://script.google.com/d/1DBchyJRg8Qr8S8TnrVRsSH9R_puICnJqODrc00JYE9Y-MlGRWAv6MWvB/edit
- **ฟังก์ชันหลัก:** `createAllForms` — สร้างฟอร์ม MASTER ทั้ง 4 ตัว + log URLs

## ขั้นตอนสุดท้าย (ต้องคลิกเอง 1 ครั้ง — Google บังคับ authorize)

1. เปิด Editor (ลิงก์ข้างบน)
2. เลือกฟังก์ชัน `createAllForms` → กด **Run**
3. Authorize: เลือกบัญชี bobbysomporn → Advanced → Go to project → Allow (สิทธิ์ Forms/Drive)
4. ดูลิงก์ฟอร์มทั้ง 4 ที่ **Execution log** (มีทั้ง editUrl + publishedUrl)
5. เอาลิงก์มาใส่ `FORM_URLS.md` ในโฟลเดอร์ kit

## กันสร้างซ้ำ (แก้บั๊ก duplicate ของรอบขอนแก่น)

- `createAllForms` มี **property lock** — รันซ้ำ/doGet ยิงซ้ำ จะคืน URL เดิม ไม่สร้างฟอร์มใหม่
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
