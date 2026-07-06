---
title: EasySlip — Overview
type: entity
brand: EasySlip
source:
  - 30 Claude Memory/โปรเจกต์ - Thunder Solution.md
  - 30 Claude Memory/Kbank API pricing + Easy×Thunder cross-billing.md
  - EasySlip/Revenue/2569-01-to-05 Revenue Report.md
  - EasySlip/หน้าหลัก.md
source_date: 2026-06-12
imported: 2026-07-06T00:00:00
last_verified: 2026-07-06
status: live
tags: [easyslip, overview, slip-verification, api, thunder-group]
---

# 01 · EasySlip Overview

## แบรนด์คืออะไร

**บริษัท อีซี่สลิป จำกัด** (สำนักงานใหญ่ · 629 หมู่ 6 ต.บ้านเป็ด อ.เมืองขอนแก่น จ.ขอนแก่น 40000) — แบรนด์ฝั่ง **SMB** ของ Thunder Group ทำธุรกิจ **ตรวจสอบสลิปโอนเงิน (slip verification)** สำหรับร้านค้าออนไลน์/e-commerce ไทย

Thunder Group = [[../Thunder Solution/หน้าหลัก|Thunder Solution]] (enterprise) + **EasySlip** (SMB)

## สินค้า

| สินค้า | ตำแหน่ง |
|---|---|
| **EasySlip API** | ⭐ STAR product ของทั้งกลุ่ม — ARPU ฿986 · MRR ~฿2.5M (snapshot 8 พ.ค. 2569) · 97.5% ของรายได้แบรนด์ |
| **EasySlip BOT** (Verify Slip) | บอทตรวจสลิป + UI + จัดการสาขา (ทุกแพ็กรองรับ 10 สาขา) — สินค้ารอง |
| **BoostSMS** | SMS marketing (flat ~฿13K/5 เดือน — dormant) · KB แยกที่ [[../BoostSMS/หน้าหลัก|BoostSMS]] |

สินค้าใต้บริษัทเดียวกัน: [[../EasyCRM/หน้าหลัก|EasyCRM]] (Loyalty/CRM)

## ขนาดธุรกิจ (ม.ค.–พ.ค. 2569)

- รายได้แบรนด์ พ.ค.: **฿6.42M** (+19.0% MoM) = **55.7% ของกลุ่ม** (ใหญ่กว่า Thunder)
- EasySlip API ตัวเดียว = **54.3% ของรายได้ทั้งกลุ่ม** (พ.ค.) — โตทุกเดือน ไม่มีถดถอย
  - (memory snapshot 8 พ.ค. ระบุ "60% ของ group revenue" — ตัวเลขต่างกันตามวิธีวัด/ช่วงเวลา ⚠️ ต้อง verify ถ้าจะใช้อ้างอิงทางการ)
- เป้าปีของแบรนด์: **~฿70M** จากเป้ากลุ่ม ฿125M
- ⚠️ **Concentration risk** — รายได้กระจุกที่ EasySlip API ตัวเดียว และลูกค้า top-1 ฝั่ง top-up = 31% ของยอดเติม 6 เดือน (ดู [[03-Contracts-Revenue]])

## ความสัมพันธ์กับ Thunder (สำคัญ)

- Easy ใช้ KBank Slip Verification API ผ่าน 2 ทาง: **ผ่าน Thunder ~94.7%** (~12.5M ครั้ง/เดือน) · ตรง KBank แค่ 5.3% (ข้อมูล ธ.ค. 2568)
- Thunder cross-bill Easy: K2K × 0.04 flat + Others × 0.11 flat + VAT 7% — Thunder ได้ margin บน K2K
- ทุกการวิเคราะห์ margin/cost ของ Easy ต้องนับเงิน **฿1.05M+/เดือน** ที่จ่าย Thunder
- รายละเอียด: [[../Thunder Solution/Reports/kbank-api-pricing-and-easy-thunder-crossbilling|KBank pricing + cross-billing]]

## Dashboard

- Master Dashboard: `https://master-dashboard-eight-nu.vercel.app/easyslip`
- Executive report: `https://thunder-revenue-report.pages.dev/`

## หน้าที่เกี่ยวข้อง

- [[02-API-Pricing-Packages]] — ราคา + margin ทุกแพ็กเกจ (API + BOT)
- [[03-Contracts-Revenue]] — สัญญา + รายได้ + วิเคราะห์ลูกค้า top-up
- [[หน้าหลัก]] — brand index
