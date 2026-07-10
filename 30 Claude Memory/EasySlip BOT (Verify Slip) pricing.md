---
name: reference-easyslip-bot-pricing
description: Pointer to EasySlip BOT (Verify Slip) pricing — 11 packages × 4 durations (1/3/6/12 mo) with margin analysis. No discount for longer terms.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 40e7b7c3-fe83-40e7-a1e8-f75f794f5180
---

# EasySlip BOT (Verify Slip) — Pricing + Margin

ข้อมูลเต็มอยู่ใน Obsidian: `~/SecondBrain/EasySlip/Documents/bot-verify-slip-packages.md`

คนละสินค้ากับ [[EasySlip API pricing + margin|EasySlip API]] — BOT มี UI + จัดการสาขา + บอทตรวจสลิปอัตโนมัติ ทุกแพ็กรองรับ 10 สาขา

## What's there
- **11 แพ็กเกจ** (Start → Premium-4): ฿99–฿14,000/เดือน, ฿/สลิป 0.247 → 0.093
- **4 รอบสัญญา:** 1 / 3 / 6 / 12 เดือน — ราคา/สลิปเท่ากันทุกรอบ
- ตาราง quick-cost (× 0.11) + GP% ทุกแพ็ก ทุกรอบ
- ตารางขาดทุนสะสมถ้า Others 100% สำหรับ Premium-2/3/4
- Sales playbook + เงื่อนไข MOU แนะนำสำหรับรอบยาว

## Key facts ที่ต้องจำ

1. **ไม่มีส่วนลดรอบยาวเลย** — 3/6/12 เดือน = ราคา × N + สลิป × N (เว็บแสดง "ประหยัดไป ฿0.00 / 0%" ตลอด)
2. **Quick cost rule:** ต้นทุน = สลิป × **0.11** บ. (worst case Others 100%)
3. **Premium-2 ถึง Premium-4 ขาดทุนถ้า Others 100%** — ราคา/สลิป (0.100, 0.095, 0.093) ต่ำกว่า cost 0.11
4. **Premium-4 รอบ 12 เดือน + Others 100% = ขาดทุน ฿30,000/contract** — เซ็นแล้วถอยไม่ได้
5. **MOU ต้อง lock K-source ≥ 50%** ถ้าจะปิด Premium-2+ รอบ 6/12 เดือน

## Sales commission tier (proposed, pattern เดียวกับ Thunder API)
- GP% ≥ 60% → 15% (Start, Basic, Starter)
- 50–60% → 12% (Beginner, Silver, Gold, Diamond, Premium-1)
- 40–50% → 7% (Premium-2, Premium-3, Premium-4)

## Commission Excel ที่ทำไว้ใน Documents/ (3 ไฟล์)

1. **`easyslip-bot-sales-commission.xlsx`** — BOT คอม **flat 10%** ทุกแพ็ก ทุกรอบ (1/3/6/12mo) — 4 quadrants ใน sheet เดียว
2. **`easyslip-api-sales-commission.xlsx`** — API คอม tiered 5/7/12/15% (Thunder API style), 1mo + 12mo
3. **`easyslip-api-commission-cost-analysis.xlsx`** — API คอม Thunder Corp style, 2 ตาราง (X 0.11 + X 0.077) มี Cost/Profit/Margin/Net column ครบ

**คอมที่เลือกใช้:**
- BOT = flat 10% (เหมือน Thunder BOT, สินค้าราคา/สลิปเท่ากันเป๊ะกับ Thunder BOT)
- API = tiered 5/7/12/15% ตาม GP% (เหมือน Thunder API)

## Related
- [[EasySlip API pricing + margin|reference_easyslip_api_pricing]] — สินค้าหลัก API (คนละ pricing structure)
- [[Kbank API pricing + cross-billing|reference_kbank_api_pricing]] — ฝั่ง cost ที่ใช้คำนวณ margin
- [[Thunder Corporate API commission (MOU)|reference_thunder_corporate_commission]] — Thunder Corporate API commission model
