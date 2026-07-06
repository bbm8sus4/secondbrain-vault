---
title: EasySlip — Contracts & Revenue
type: resource
brand: EasySlip
source:
  - EasySlip/Contracts/INDEX.md
  - EasySlip/Contracts/2569-03-31_SCCN_x_Easyslip_Slip-Verification-API.md
  - EasySlip/Revenue/2569-01-to-05 Revenue Report.md
  - EasySlip/Revenue/EasySlip API - วิเคราะห์ลูกค้า Top-up 6 เดือน.md
source_date: 2026-07-02
imported: 2026-07-06T00:00:00
last_verified: 2026-07-06
status: live
tags: [easyslip, contracts, revenue, topup, churn, sccn]
---

# 03 · EasySlip — Contracts & Revenue

## 1. สัญญา (Contracts)

ทะเบียนสัญญาทั้งหมด: [[Contracts/INDEX|Contracts INDEX]] — เกณฑ์: ทุกสัญญา/MOU/SLA ของ EasySlip เก็บที่ `Contracts/` เป็น verbatim markdown + PDF ต้นฉบับคู่กัน

### สัญญา Active (ณ 26 มิ.ย. 2569 มี 1 ฉบับ)

**[[Contracts/2569-03-31_SCCN_x_Easyslip_Slip-Verification-API|SUPER COCONUT (SCCN) × EasySlip — Slip Verification API]]** (ลงนาม 31 มี.ค. 2569)
- ค่าบริการ **0.125 บ./รายการ (incl VAT)** · billing แบบ **Use First, Pay Later** (รายเดือนตามรอบปฏิทิน)
- ฟรี 1,000 สลิป/ร้านใหม่ (อายุ 60 วัน) · SLA uptime **99.9%/เดือน**
- อายุสัญญา 1 เม.ย. 2569 – 30 มี.ค. 2570 · **ต่ออายุอัตโนมัติ 1 ปี**
- ผู้ลงนาม: นายวัชรินทร์ แก้วม่วง (EasySlip) × นายจิตตวัฒน์ จิตสำรวย (SCCN) · เชื่อมระบบ Super rOS

## 2. รายได้ ม.ค.–พ.ค. 2569

รายงานเต็ม: [[Revenue/2569-01-to-05 Revenue Report|Revenue Report ม.ค.–พ.ค. 2569]]

| Month | EasySlip Brand (฿) | MoM |
|---|---:|---:|
| ม.ค. | 4,976,692 | — |
| ก.พ. | 5,244,288 | +5.4% |
| มี.ค. | 5,325,680 | +1.6% |
| เม.ย. | 5,391,009 | +1.2% |
| **พ.ค.** | **6,417,845** | **+19.0%** |

- EasySlip API = 97.5% ของแบรนด์ (พ.ค.) = 54.3% ของทั้งกลุ่ม — โตทุกเดือน
- EasySlip BOT: ฿145K–201K/เดือน (+13.6% YTD) · BoostSMS: flat ~฿12.9K → ต้องตัดสินใจ reprice หรือ kill

## 3. วิเคราะห์ลูกค้า Top-up 6 เดือน (ม.ค.–มิ.ย. 2569)

รายงานเต็ม + dashboard: [[Revenue/EasySlip API - วิเคราะห์ลูกค้า Top-up 6 เดือน|EasySlip API — วิเคราะห์ลูกค้า Top-up 6 เดือน]]

### ตัวเลขหลัก
- ยอดเติมรวม **฿33.64M** · 6,371 รายการ · ลูกค้า 1,250 คน · โต **+45%** (ม.ค. ฿4.79M → มิ.ย. ฿6.95M)
- เติมซ้ำ 63.8% · median ฿1,500/ครั้ง · จังหวะเติมจริง median 11 วัน

### การกระจุกตัว (ความเสี่ยงอันดับ 1)
- **Gini = 0.888** · Top 1% ของลูกค้า = **50% ของรายได้** · Top 10% = 81%
- **บัญชี #1 คนเดียว = ฿10.4M = 31%** ของยอดเติมทั้งหมด
- ฉากเสี่ยง: whale หายไป = รายได้ปีหาย ~฿19–26M

### Churn & Segment
- นิยาม churn = เงียบเกิน **60 วัน** (98% ของการเติมซ้ำเกิดใน 60 วัน)
- Lapsed (เคยประจำแล้วเลิก) 173 คน ฿1.14M = retention problem · เติมครั้งเดียวแล้วหาย 225 คน = onboarding problem
- RFM 7 กลุ่ม: VIP 122 คน = **80% ของรายได้**
- Cohort churn แย่ลงเรื่อยๆ: ม.ค. 38% → มี.ค. 54% = คุณภาพ acquisition เดือนหลังตก

### คาดการณ์
- ก.ค. 2569: ฿6.6–7.5M · ทั้งปี 2569: **~฿75–83M** (อย่า commit 86M+)

## หน้าที่เกี่ยวข้อง

- [[01-Overview]] · [[02-API-Pricing-Packages]] · [[หน้าหลัก]]
- ฝั่ง Thunder: [[../Thunder Solution/03-Revenue-Commission|Thunder Revenue & Commission]]
