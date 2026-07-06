---
title: Thunder Solution — Overview
type: entity
brand: Thunder Solution
source:
  - 30 Claude Memory/โปรเจกต์ - Thunder Solution.md
  - Thunder Solution/Revenue/2569-01-to-05 Revenue Report.md
  - Thunder Solution/หน้าหลัก.md
source_date: 2026-06-12
imported: 2026-07-06T00:00:00
last_verified: 2026-07-06
status: live
tags: [thunder-solution, overview, business-model, thunder-group]
---

# 01 · Thunder Solution Overview

## บริษัทคืออะไร

**บริษัท ธันเดอร์ โซลูชั่น จำกัด** (Thunder Solution Co., Ltd. · ขอนแก่น) — ธุรกิจ **ตรวจสอบสลิปโอนเงิน (slip verification)** + **LINE chatbot** ให้ e-commerce / ร้านค้าออนไลน์ไทย

Thunder Group มี 2 แบรนด์:
- **Thunder Solution** — จับลูกค้า enterprise/รายใหญ่ (Thunder BOT, Thunder API, Flex)
- **[[../EasySlip/หน้าหลัก|EasySlip]]** — จับ SMB (Easy Bot, EasySlip API)

## Business model

- รายได้หลักจาก 2 ช่องทาง: **slip verification API** (คิดตามจำนวนสลิป) + **LINE chatbot** (subscription)
- **Pre-paid billing cycle:** margin ช่วงต้นเดือนจะติดลบ −40 ถึง −50% เสมอ แล้วฟื้นปลายเดือน — **เป็นเรื่องปกติ อย่าตีเป็นวิกฤต**
- Unit economics ระดับกลุ่ม: **margin ~82% ต่อสลิป** (รายได้ ~19 สตางค์ / ต้นทุน ~3 สตางค์) — snapshot 8 พ.ค. 2569
- Volume: ~2M สลิป/วัน (~16M ใน 8 วัน) — snapshot 8 พ.ค. 2569
- ฐานลูกค้ากลุ่ม ~67K users · active แค่ **16%** → โอกาส re-engagement ใหญ่มาก

## เป้ารายได้ปี 2569

- **เป้าทั้งกลุ่ม ฿125M/ปี** — แบ่ง Thunder ~฿55M + EasySlip ~฿70M
- YTD ม.ค.–พ.ค. ทั้งกลุ่ม: ฿51.0M (40.8% ของเป้า) → ต้องเฉลี่ย ฿10.57M/เดือนใน 7 เดือนที่เหลือ
- Thunder brand พ.ค. 2569: ฿5.11M (+10.4% MoM) = **44.3% ของรายได้กลุ่ม**
- รายละเอียด: [[Revenue/2569-01-to-05 Revenue Report|Revenue Report ม.ค.–พ.ค. 2569]]

## Product mix (snapshot 8 พ.ค. 2569)

| Product | ตำแหน่ง | ARPU |
|---|---|---:|
| Thunder BOT | ฐานลูกค้าใหญ่สุด (53K) แต่ ARPU ต่ำสุด | ฿120 |
| Thunder API | ลูกค้า VIP · โต +326% ม.ค.→พ.ค. (PMF signal) | ฿826 |
| Thunder Flex | minor product | — |

รายละเอียดสินค้า → [[02-Products-Services]]

## Dashboard & Backoffice

- Master Dashboard: `https://master-dashboard-eight-nu.vercel.app/` (`/today` · `/overview` · `/thunder` · `/easyslip`)
  - ⚠️ MoM% หน้า `/today` เป็น naive (เทียบ 8 วัน vs 30 วัน) — ใช้ค่าหน้า per-product แทน
- Executive report: `https://thunder-revenue-report.pages.dev/`
- API backoffice: `https://backoffice-developer.thunder.in.th/`
- LINE Bot backoffice: `https://old.thunder.in.th/`

## หน้าที่เกี่ยวข้อง

- [[02-Products-Services]] — สินค้า/บริการ + Corporate API + Gen QR
- [[03-Revenue-Commission]] — รายได้ + ค่าคอมเซลส์ Corporate API
- [[หน้าหลัก]] — brand index
