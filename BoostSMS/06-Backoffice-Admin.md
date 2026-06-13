# 06 — Backoffice (Admin Panel)

URL: https://backoffice.boost-sms.com/

## Menu Structure

| หมวด | เมนู |
|------|------|
| แดชบอร์ด | ภาพรวม · CEO · การเงิน · ซัพพอร์ต · ปฏิบัติการ · CTO |
| จัดการ | ผู้ใช้งาน · คำสั่งซื้อ · SMS · ชื่อผู้ส่ง · แพ็กเกจ · โค้ดส่วนลด · แคมเปญ · รายได้ |
| ระบบ | ตั้งค่า (Roles) · ประวัติการใช้งาน (Audit Logs) |

## Dashboard Stats (1-19 พ.ค. 2026)

- **SMS วันนี้:** 138 (-76.1% vs yesterday)
- **สลิปรอตรวจ:** มีค้าง
- **ธุรกรรมล่าสุด:**
  - Chadaporn Jamkao: ฿9,844 × 2 (ปฏิเสธ)
  - กฤตติยา ถิ่นปรุ: ฿9,844 (ปฏิเสธ)
  - กหฟด ฟหกดฟหดก: ฿374.5 (อนุมัติ)
  - Thanisorn Mangkorn: ฿374.5 (อนุมัติ)

## ผู้ใช้ใหม่ล่าสุด

| ชื่อ | อีเมล | สมัคร | เครดิต |
|------|------|------|--------|
| กหฟด ฟหกดฟหดก | thanisorn.m@thunder.in.th | 2026-05-18 | 900 |
| Chadaporn Jamkao | chadaporn.j@thunder.in.th | 2026-05-18 | 100 |
| เกวลิน ปะวะลัง | beamkewalin14@gmail.com | 2026-05-15 | 100 |

## Audit Log (กิจกรรมล่าสุด)

- `admin.login`
- `discount_code.deactivate`
- `discount_code.create`
- (วันที่ 19 พ.ค.)

## Backoffice Shortcuts

| งาน | path |
|-----|------|
| จัดการผู้ใช้ | `/users` |
| ตรวจสลิป | `/orders?status=pending_verification` |
| บันทึก SMS | `/sms` |
| แพ็กเกจ | `/packages` |
