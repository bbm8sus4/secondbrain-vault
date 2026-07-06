---
title: "07 — Project History"
type: entity
source: "BoostSMS/_assets/ source files (brand KB session 2026-06)"
source_date: 2026-06-13
imported: 2026-06-13T22:49:35
last_verified: 2026-07-06
status: live
tags: [boostsms, brand]
---

# 07 — Project History

## Development Timeline

| วันที่ | รายการ |
|--------|--------|
| 8 ก.ค. 2568 | รับมอบ Source Code ต้นทาง |
| 9-18 ก.ค. 2568 | ปรับปรุง UX/UI + User Flow |
| 14 ก.ค. - 6 ส.ค. 2568 | พัฒนาฟีเจอร์เพิ่มเติม |
| 7-15 ส.ค. 2568 | SIT + UAT |
| 15 ส.ค. 2568 | **ส่งมอบงาน** (Ready for Use) → เข้าสู่ Maintenance Phase |

## UAT Results (15 ส.ค. 2568)

| หัวข้อ | เกณฑ์ | ผล |
|--------|------|-----|
| SMS Delivery Rate | >99% | **99.8%** ✅ |
| System Latency | <200ms | **145ms** ✅ |
| Data Integrity | 100% | **100%** ✅ |
| Critical Bugs | 0 remaining | **Resolved 100%** ✅ |

## Functional Requirements (ผ่านทั้งหมด)

- **ระบบส่ง SMS** (5 functions): ส่ง · ตั้งเวลา · Sender Name · Unicode · คำนวณเครดิต
- **Contact List** (4 functions): CRUD · Import CSV/Excel · Tag/Group · Export
- **Reports & Analytics** (3 functions): Dashboard · รายวัน/เดือน · Export
- **API Integration** (3 functions): SMS API · Auth · OTP
- **Billing & Credit** (2 functions): ซื้อแพ็กเกจ · หักเครดิตอัตโนมัติ
- **Admin Panel** (3 functions): RBAC (Admin/Operator/Viewer) · จัดการลูกค้า · อนุมัติ Sender

## Intellectual Property

- กรรมสิทธิ์โอนจาก **มูน ริทีม จำกัด → อีซี่สลิป จำกัด** โดยสมบูรณ์
- ครอบคลุม: Source code, Config, Build/Deploy scripts, Test suites, DB Schema, Docs, Admin Access
- **ผู้ส่งมอบ:** มหาสมุทร ฉัตรปราการ (DevOps Engineer)
- **ผู้รับมอบ:** วัชรินทร์ แก้วม่วง (CEO, EasySlip)

## Asset Capitalization

| รายการ | จำนวน (บาท) |
|--------|-------------|
| ค่าลิขสิทธิ์ Source Code | 2,000,000 |
| DevOps (15,000 × 100% × 1.25 เดือน) | 18,750 |
| CTO (100,000 × 10% × 1.25 เดือน) | 12,500 |
| **รวมต้นทุนสินทรัพย์** | **2,031,250** |

- **บันทึกเป็น:** สินทรัพย์ไม่มีตัวตน (Intangible Asset)
- **ตัดจำหน่าย:** 3 ปี (36 เดือน)
- **แผน V.2:** Major Refactoring + AI integration

## เอกสารต้นทาง

- `_assets/บันทึกชี้แจงรายละเอียดโครงการและสรุปต้นทุนสินทรัพย์_BoostSMS (2).pdf`
- `_assets/เอกสารรับมอบงานและปิดโครงการ_BoostSMS_Easyslip_ (2).pdf`
- `_assets/เอกสารรับมอบงานและปิดโครงการ_BoostSMS_Easyslip_2.pdf`
- `_assets/docs/BoostSMS_proposal_CI.pdf`
