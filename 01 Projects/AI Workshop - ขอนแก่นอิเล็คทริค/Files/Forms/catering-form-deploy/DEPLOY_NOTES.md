# Catering Form — clasp deploy notes

**สร้างเมื่อ:** 2026-07-08 · โดย clasp (bobbysomporn@gmail.com)
**Project แยกต่างหาก** จากฟอร์มที่มี response แล้ว (ปลอดภัย)

- **scriptId:** `1HAjx4pxb5h-xqTtDiP8wJvtGGjCEzlp_tyQixv_lt4eQMjvqZthTo0_t`
- **Editor:** https://script.google.com/d/1HAjx4pxb5h-xqTtDiP8wJvtGGjCEzlp_tyQixv_lt4eQMjvqZthTo0_t/edit
- **Deployment:** `AKfycbymgdPq2FTbq_nwW_J7xY-a-dwUVn3rcP3yml0I2aKj8_G5kEfifzJ8t3uHuS6QjJPqFA` (@2)
- **ฟังก์ชัน:** `createFoodForm` (สร้าง Google Form อาหารเบรก+กลางวัน)

## ขั้นตอนสุดท้าย (ต้องคลิกเอง 1 ครั้ง — Google บังคับ)
1. เปิด Editor (ลิงก์ข้างบน)
2. (ครั้งแรก) เปิด Apps Script API: https://script.google.com/home/usersettings → ON
3. เลือกฟังก์ชัน `createFoodForm` → กด **Run**
4. Authorize: เลือกบัญชี bobbysomporn → Advanced → Go to project → Allow (สิทธิ์ Forms/Drive)
5. ดูลิงก์ฟอร์มที่ **Execution log** (published URL = ลิงก์ให้ผู้เข้าอบรมกรอก)

## แก้เมนู/เนื้อหาแล้ว push ใหม่
```bash
cd "Files/Forms/catering-form-deploy"
# แก้ Code.gs (array LUNCH/DRINKS/SNACKS/MILK อยู่บนสุด)
clasp push -f
```

⚠️ Code.gs เป็น create-only (ไม่มี clearAllItems/delete) — รันซ้ำ = ได้ฟอร์มใหม่อีกใบ ไม่ทับของเดิม
