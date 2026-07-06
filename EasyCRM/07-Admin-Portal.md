---
title: "07 · Admin Portal (ระบบหลังบ้าน)"
type: entity
source: "EasyCRM/_assets/EasyCRM-Guide.html (brand KB session 2026-06)"
source_date: 2026-06-13
imported: 2026-06-13T22:49:35
last_verified: 2026-07-06
status: live
tags: [easycrm, brand]
---

# 07 · Admin Portal (ระบบหลังบ้าน)

> **URL หลัก:** https://easycrm-two.vercel.app/login

## 7 โมดูลหลักที่แอดมินใช้ประจำวัน

ภาพรวม · ปฏิทินนัด · จัดการลูกค้า · Onboarding · บริการลูกค้า · จัดการปัญหา · ประวัติการเงิน

---

## 1. ภาพรวม (Dashboard)
**URL:** `easycrm-two.vercel.app/dashboard`

- รายได้รวม · รายได้เดือนนี้ · รายได้วันนี้
- สถิติงบประมาณ Paid vs Trial
- ลูกค้าทั้งหมด · จ่ายแล้ว · ทดลองใช้
- Onboarding ค้างอยู่ · นัดหมายวันนี้ · ปัญหาเปิดอยู่
- เปรียบเทียบ vs เดือนก่อน + % เติบโต
- กรอง: ช่วงเวลา / ประเภทธุรกิจ / แหล่งที่มา + Export CSV

## 2. ปฏิทินนัดลูกค้า (Calendar)
**URL:** `easycrm-two.vercel.app/calendar`

- มุมมอง: วัน · สัปดาห์ · เดือน · ปี · List
- แยกตาราง MIZTEEN · OLIVE · SUPPORT เป็นคอลัมน์
- สถิติ: นัดทั้งหมด, วันนี้, สัปดาห์นี้, รอติดตาม, สำเร็จ
- **Conversion Rate** — สัดส่วนนัดที่ปิดดีล
- ค้นหา · กรอง · พิมพ์ · Export

## 3. จัดการลูกค้า (Customer Management)
**URL:** `easycrm-two.vercel.app/customers`

- ตารางรวม: ชื่อ · เบอร์ · แพ็กเกจ · วันลงทะเบียน · สถานะเชื่อมต่อ
- กด **"รูปตา"** → ดูรายละเอียดทั้งหมด
- รายละเอียดมี: ข้อมูลธุรกิจ TH/EN, ผู้ดูแล, LINE OA, ประวัติการนัด, เอกสาร & การเงิน
- กรอง: ชื่อ/LINE OA, แพ็กเกจ, สถานะ + เพิ่มลูกค้าใหม่

## 4. Onboarding
**URL:** `easycrm-two.vercel.app/onboarding`

- ติดตาม 5 Phases: ยืนยันการขาย → Kick-off → Setup → กราฟิก → ฝึกอบรม
- สถานะ: ค้าง · เกินกำหนด · สำเร็จแล้ว
- กรองตาม Role: CSM · Specialist · Designer
- กดปุ่ม **"เสร็จ"** ปิดงานแต่ละข้อ
- เห็น Progress ของแต่ละลูกค้า (เช่น 2/5 PHASES)

## 5. บริการลูกค้า (Customer Service)
**URL:** `easycrm-two.vercel.app/service`

- ติดตามวันหมดอายุ & ปัญหารายๆ
- กรอง: ใช้งานสด · ใกล้หมดอายุ · หมดอายุแล้ว

## 6. จัดการปัญหา (Issue Tracker)
**URL:** `easycrm-two.vercel.app/issues`

- บันทึก: หัวข้อปัญหา · ความสำคัญ · สถานะ
- Tab "จัดการ Feedback" สำหรับฟีดแบ็คลูกค้า

## 7. จัดการแพ็กเกจ (Package Manager)
**URL:** `easycrm-two.vercel.app/packages`

- การ์ดสรุป Trial · Starter · Plus · Premium · Enterprise
- แก้ไขราคา/สลิป/Admin/Tier · เปิด-ปิดใช้งาน

## 8. ประวัติการเงิน (Finance)
**URL:** `easycrm-two.vercel.app/finance`

- รายได้ยืนยันแล้ว · ใบเสนอราคา · สลิปทั้งหมด
- Tab: สลิปทั้งหมด · ใบเสนอราคา · ใบกำกับ/ภบบ · สรุปยอด

---

## เครื่องมือเสริม

| โมดูล | คำอธิบาย |
|---|---|
| **จัดเก็บเอกสาร** | Drive Link, Google Docs ของลูกค้าแต่ละราย |
| **Media Stock** | คลังภาพ Rich Menu, Banner, Logo |
| **คู่มือ CRM (Manual)** | 4 ชุด: เมนูจัดการ, EasyCRM, LINE OA, Thunder Bot |
| **ตั้งค่าระบบ** | โปรไฟล์, จัดการผู้ใช้, ประวัติการใช้งาน, สิทธิ์เข้าถึง |

## URL summary

- Login: `/login`
- Dashboard: `/dashboard`
- Calendar: `/calendar`
- Customers: `/customers`
- Onboarding: `/onboarding`
- Service: `/service`
- Issues: `/issues`
- Packages: `/packages`
- Finance: `/finance`
- Register (public): `/register`
