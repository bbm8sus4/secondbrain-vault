---
name: reference-kbank-api-pricing
description: "Kbank Slip Verification API pricing (tiered for KBank-source, flat 0.11 for Others) + Thunder→Easy cross-billing formula. Use to verify monthly bills, compute true cost per entity, and check intercompany margin."
metadata: 
  node_type: memory
  type: reference
  originSessionId: d116a431-29e0-4032-a2df-cd3d34f19dd0
---

# Kbank Slip Verification API — Pricing & Cross-billing

**บันทึกใน Obsidian:** `~/SecondBrain/Thunder Solution/Reports/kbank-api-pricing-and-easy-thunder-crossbilling.md`

## Kbank pricing (effective ม.ค. 2569)

**KBank-source slips** (KBank→KBank, KBank→Other): **tiered**
- 1–1M: 0.04 · 1M–3M: 0.035 · 3M–5M: 0.030 · 5M+: 0.025

**Others-source slips** (Other→KBank, Other→Other): **flat 0.11**

→ verified ตรงเป๊ะกับบิล EASY ทุกเดือน และ THUNDER ตั้งแต่ ม.ค. 2569 เป็นต้นไป
→ THUNDER ธ.ค. 2568 ยังราคาเก่า (สูงกว่า ~884K)

## Thunder → Easy cross-billing formula

- **K2K** (Kbank-source) × **0.04** flat (ไม่มี tier discount)
- **Others** × **0.11** flat
- + VAT 7%

→ Thunder ได้ margin บน K2K (pay Kbank ที่ tier ขั้นสูง 0.025–0.035 แต่เก็บ Easy 0.04)
→ Others เป็น pass-through ไม่มี margin

## Volume insight (ธ.ค. 2568)

Easy ใช้ Kbank API ผ่าน 2 ทาง:
- ผ่าน Thunder: ~12.5M ครั้ง/เดือน (**94.7%**)
- ตรง Kbank: ~696K (5.3%)

→ Easy depends on Thunder ~95% ทุกการวิเคราะห์ margin/cost ของ Easy ต้องนับ ฿1.05M+/เดือนที่จ่าย Thunder

## What this overturns

AIDEBATE รอบแรก (ก่อนรู้สูตร) ผิดประเด็นหลัก:
- ❌ "ไม่มี tier" — มีตั้งแต่ ม.ค. 2569
- ❌ "THUNDER ธ.ค. ส่วนเกิน 915K คือ setup fee" — คือราคาเก่า
- ❌ "เรท 0.074" — เป็น mix ของ 0.04 + 0.11
- ❌ "เจรจาลดเรท" — ลดไปแล้ว

## Real levers
1. Push ลูกค้าให้สแกนจาก KBank app → ลด Others slip (แพง 2.75×)
2. ทบทวน margin Thunder→Easy (intercompany fairness)
3. Verify บิลทุกเดือนด้วยสูตรนี้ → ทวงถ้าไม่ตรง
4. ขอราคาใหม่ effective ย้อนหลังถึง ธ.ค. 2568 → ทวง 884K
