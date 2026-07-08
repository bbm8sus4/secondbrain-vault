# 📋 Google Forms — Claude AI Workshop

สร้างเมื่อ: 2026-06-30 13:08 (Asia/Bangkok)
บัญชี: bobbysomporn@gmail.com

## ฟอร์มที่ใช้ได้ (คู่ล่าสุด)

### 1. แบบสอบถามเจ้าของธุรกิจ — Needs Analysis
- **แก้ไข:** https://docs.google.com/forms/d/1oEUefpyYqe1MQPpbwyM_lrkzReq02ZaETM50rUf-bvw/edit
- **ส่งให้ตอบ:** เปิดจากปุ่ม "Send" ในหน้า edit (responderUri ต้องเปิด Forms API ก่อนถึงดึงผ่าน CLI ได้)

### 2. แบบสำรวจผู้เรียน — Pre-training Survey
- **แก้ไข:** https://docs.google.com/forms/d/1ekrJsyjnlVluHixcDwyJy0AcTnwO9vuYYfzfkw81G7o/edit
- **ส่งให้ตอบ:** เปิดจากปุ่ม "Send" ในหน้า edit

> Published URLs ทั้ง 2 ใบแสดงอยู่ในแท็บ Web App ที่เปิดไว้แล้ว (หน้า "✅ สร้างฟอร์มเรียบร้อย")

## Duplicate ที่ต้องลบเอง

doGet ถูก trigger 2 ครั้ง ทำให้มีฟอร์มเกินมา 2 ใบ — clasp token ไม่มีสิทธิ์ลบให้
ไปลบเองที่ https://drive.google.com (search "Claude AI Workshop"):
- `1hLEg4Jmh8dp6zQvo8PWRgIJwJ-c5LRxMNOmxjD5bAMI` (ผู้เรียน — duplicate)
- `1mLALx74_5yf0i51LlJuI_1E72vBhT4iED-NqTaecJgo` (เจ้าของ — duplicate)

## Apps Script project

- Editor: https://script.google.com/d/1r5GYtrTrwvdmfF6EKlbmg-9iHT-zVC_rg2yqo-e7u0pj_8Xk3aRitrsc/edit
- Local clasp dir: `clasp-deploy/`
- ถ้าจะรันใหม่ → ใช้ Web App URL หรือเปิด editor แล้ว Run `createBothForms`

## แบบฟอร์มอาหาร (เบรก + กลางวัน) — เพิ่ม 2026-07-08
- **ฟอร์ม:** เลือกอาหารเบรก & อาหารกลางวัน — Claude AI Workshop
- **กรอก:** https://docs.google.com/forms/d/18DiJbVkwo2v4q51CVoC4c1uwLXJ4NyHlTuvsiHX8UIc/viewform
- **แก้ไข:** https://docs.google.com/forms/d/18DiJbVkwo2v4q51CVoC4c1uwLXJ4NyHlTuvsiHX8UIc/edit
- source: `5_แบบฟอร์มอาหาร_Catering_AppsScript.gs` · deploy: `catering-form-deploy/`
