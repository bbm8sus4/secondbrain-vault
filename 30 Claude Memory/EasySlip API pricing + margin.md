---
name: reference-easyslip-api-pricing
description: Pointer to EasySlip API public pricing (11 packages) + margin analysis by traffic mix (K-src/Other)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 320932de-4322-4670-92b3-1b38a7e0e0a4
---

# EasySlip API — Pricing + Margin Analysis

ข้อมูลเต็มอยู่ใน Obsidian: `~/SecondBrain/EasySlip/Documents/api-pricing-packages.md`

## What's there
- ราคาขายลูกค้าปลายทาง 11 แพ็กเกจ (Tester → Premium 3): ฿99–฿40,000/เดือน, ฿/สลิป 0.396 → 0.125
- ตารางต้นทุน KBank (tier 0.025–0.04 K-src, flat 0.11 Other)
- **Margin matrix 7 traffic mix** (100/0, 80/20, 70/30, 60/40, 50/50, 0/100) × 10 แพ็ก
- Sweet spot 70/30 mix = ทุกแพ็กกำไร 57–86%
- Risk zone: Diamond+ ที่ Other 100% = ขาดทุน 6–18%
- Margin paradox: Enterprise = 68% ของ MRR แต่ margin ต่ำสุด → SME อุ้ม Enterprise

## Related
- [[Kbank API pricing + cross-billing|reference_kbank_api_pricing]] — ฝั่ง cost + Thunder cross-billing
- [[โปรเจกต์ - EasyBOT Finance|project_easybot_finance]] — งบ EasyBOT
