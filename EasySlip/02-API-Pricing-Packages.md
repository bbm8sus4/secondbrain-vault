---
title: EasySlip — API & BOT Pricing Packages
type: resource
brand: EasySlip
source:
  - EasySlip/Documents/api-pricing-packages.md
  - EasySlip/Documents/bot-verify-slip-packages.md
  - 30 Claude Memory/EasySlip API pricing + margin matrix.md
  - 30 Claude Memory/EasySlip BOT (Verify Slip) pricing.md
  - 30 Claude Memory/Kbank API pricing + Easy×Thunder cross-billing.md
source_date: 2026-06-19
imported: 2026-07-06T00:00:00
last_verified: 2026-07-06
status: live
tags: [easyslip, pricing, packages, margin, commission, kbank]
---

# 02 · EasySlip — Pricing Packages (API + BOT)

สองสินค้า **คนละ pricing structure** — เอกสารเต็มอยู่ใน Documents/:
- [[Documents/api-pricing-packages|EasySlip API — Public Pricing & Margin Analysis]]
- [[Documents/bot-verify-slip-packages|EasySlip BOT (Verify Slip) — Packages]]

## 1. EasySlip API (สินค้าหลัก)

- **11 แพ็กเกจ** Tester (ฟรี 7 วัน) → Premium 3: **฿99–฿40,000/เดือน** · ราคา/สลิป **0.396 → 0.125** (incl VAT)
- ต้นทุน KBank (MOU 8 ม.ค. 2568): K-source tiered 0.04 → **0.025** (EasySlip อยู่ tier 5M+ · volume 250M/ปี) · Other-source flat **0.11**
- **Margin matrix ตาม traffic mix** (7 mix × 10 แพ็ก) — อยู่ในเอกสารเต็ม

### Insight หลัก
- **Sweet spot = mix 70/30 (K/Other)** — ทุกแพ็กกำไร 57–86%
- **Risk zone: Diamond ขึ้นไป + Other 100% = ขาดทุน 6–18%**
- **Margin paradox:** Enterprise = 68% ของ MRR แต่ margin ต่ำสุด → กำไรจริงเป็น blended, **SME อุ้ม Enterprise**
- Blended ปี 2568 (ประมาณ): รายได้ API ฿35.4M ÷ 250M สลิป = 0.142/สลิป · mix 70/30 → margin ~62%
- Caveat: ลูกค้าหลายรายใช้ไม่เต็ม quota → effective margin จริง **สูงกว่า** ตาราง · แต่ 95% ของ traffic ผ่าน Thunder ที่เรท flat (ไม่ได้ tier discount) → blended จริงต่ำลงอีกชั้น

## 2. EasySlip BOT (Verify Slip)

- **11 แพ็กเกจ** Start → Premium-4: **฿99–฿14,000/เดือน** · ราคา/สลิป **0.247 → 0.093**
- **4 รอบสัญญา** 1/3/6/12 เดือน — **ไม่มีส่วนลดรอบยาวเลย** (ราคา × N ตรงๆ)
- Quick cost rule: ต้นทุน = สลิป × **0.11** (worst case Others 100%)

### จุดต้องระวัง
- ⚠️ **Premium-2 ถึง Premium-4 ขาดทุนถ้า Others 100%** (ราคา/สลิป 0.100 / 0.095 / 0.093 < cost 0.11)
- ⚠️ **Premium-4 รอบ 12 เดือน + Others 100% = ขาดทุน ฿30,000/contract** — เซ็นแล้วถอยไม่ได้
- MOU ต้อง **lock K-source ≥ 50%** ถ้าจะปิด Premium-2+ รอบ 6/12 เดือน

## 3. ค่าคอมเซลส์ (ที่เลือกใช้)

- **BOT = flat 10%** ทุกแพ็ก ทุกรอบ (เหมือน Thunder BOT) → [[Documents/easyslip-bot-sales-commission.xlsx|easyslip-bot-sales-commission.xlsx]]
- **API = tiered 5/7/12/15% ตาม GP%** (เหมือน Thunder API) → [[Documents/easyslip-api-sales-commission.xlsx|easyslip-api-sales-commission.xlsx]]
- แบบ Thunder Corporate style (2 cost scenarios, มี Cost/Profit/Margin/Net ครบ) → [[Documents/easyslip-api-commission-cost-analysis.xlsx|easyslip-api-commission-cost-analysis.xlsx]]

## เอกสารประกอบอื่นใน Documents/

- [[Documents/easyslip-business-overview-2568-final.pdf|Business Overview 2568 (PDF)]] — MRR tier breakdown
- [[Documents/easyslip-gateway-summary.pdf|Gateway summary (PDF)]]

## หน้าที่เกี่ยวข้อง

- [[01-Overview]] · [[03-Contracts-Revenue]] · [[หน้าหลัก]]
- ฝั่งต้นทุน/คู่เทียบ: [[../Thunder Solution/Reports/kbank-api-pricing-and-easy-thunder-crossbilling|KBank cost + cross-billing]] · [[../Thunder Solution/Reports/thunder-corporate-api-sales-commission|Thunder Corporate commission (สูตรอ้างอิง)]]
