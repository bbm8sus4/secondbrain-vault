# 04 · การเชื่อมต่อ LINE OA

> ⚠️ **ต้องทำบนคอมพิวเตอร์/โน้ตบุ๊กเท่านั้น** — LINE Developers Console ไม่รองรับมือถือ

## ข้อมูลที่ลูกค้าต้องส่งให้แอดมิน

### Messaging API (3 ค่า)
ดึงจาก LINE Developers Console
- Channel ID
- Channel Secret
- Channel Access Token

### LINE Login (2 ค่า)
- Channel ID
- Channel Secret

ส่งครบทั้งหมดให้แอดมิน → ทีมตั้งค่าระบบสมาชิกให้ทันที

## 2 กรณีการเชื่อมต่อ Messaging API

### กรณีที่ 1 — ยังไม่ได้เปิด Messaging API
ทีมแอดมิน EasyCRM **เข้าไปตั้งค่าให้ได้ทั้งหมด** แล้วโอนสิทธิ์ผู้ให้บริการกลับให้ลูกค้าเมื่อเสร็จ — ลูกค้าไม่ต้องทำเอง

### กรณีที่ 2 — ลูกค้าเปิด Messaging API ไว้แล้ว
ลูกค้าต้องเข้า **LINE OA Manager** + **LINE Developers Console** ดึงค่า Channel ID/Secret/Access Token ด้วยตัวเอง

### ⚠️ กรณีพิเศษ
ถ้าลูกค้า **ไม่ใช่ผู้สร้างบัญชีผู้ให้บริการเดิม** ต้องติดต่อคนที่เปิด Messaging API ตอนแรกก่อน — ระบบ LINE ไม่อนุญาตให้คนอื่นเข้าถึงโดยไม่มีสิทธิ์

## สร้างช่องเพิ่มไม่ได้? (Provider เต็ม)

ลูกค้ามอบสิทธิ์ระดับ **"แอดมิน"** ในส่วน **Roles** ของ LINE Developers Console ให้ทีม EasyCRM ที่ระดับผู้ให้บริการ → ทีมงานสร้างช่องในนามลูกค้าได้

**วิดีโอวิธีเพิ่มแอดมิน LINE OA:**
https://www.youtube.com/watch?v=wuo4sIydVts

## Callback URL pattern

```
<store>.easy-crm.co/api/portal/auth/line/callback
```

ตัวอย่าง: `day-hotel.easy-crm.co/api/portal/auth/line/callback`
