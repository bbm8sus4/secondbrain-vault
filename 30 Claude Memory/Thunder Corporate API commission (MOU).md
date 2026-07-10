---
name: reference-thunder-corporate-commission
description: "Pointer to Thunder Corporate API MOU sales commission model (10 Coperate tiers, 2 cost scenarios, recommended rates 3% / 8%)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 320932de-4322-4670-92b3-1b38a7e0e0a4
---

# Thunder Corporate API — Sales Commission (MOU)

Full doc + Excel in Obsidian: `~/SecondBrain/Thunder Solution/Reports/`
- Markdown: `thunder-corporate-api-sales-commission.md`
- Excel (used by sales team): `thunder-corporate-api-commission.xlsx`

## What's there
- **MOU enterprise pricing** — flat 0.125 บ./สลิป (not the web tier discount)
- **10 Coperate tiers** A→J (100k → 1M สลิป/เดือน, ราคา 12,500 → 125,000 บ./เดือน)
- **2 cost scenarios**:
  - A: Other-source 100% → cost 0.110, GP 12%, แนะนำคอม **3%** revenue
  - B: Mix blend 30/70 → cost 0.077, GP 38.4%, แนะนำคอม **8%** revenue
- Commission tables for 1mo + 12mo contracts (J = 3,750 บ./45,000 บ. at 3%; 10,000 บ./120,000 บ. at 8%)
- Per-slip detail for ad-hoc tier (0.00375 / 0.01 บ./สลิป)
- 6-step Sales Playbook + Excel has inline guide on every sheet (no need to flip tabs)

## Key risk
ใช้ Scenario B ต้อง **lock traffic mix K-src ≥ 30% ใน MOU** ไม่งั้น cost ทะลุ 0.077 = margin หาย

## Related
- [[EasySlip API pricing + margin|reference_easyslip_api_pricing]] — Web tier pricing + margin matrix
- [[Kbank API pricing + cross-billing|reference_kbank_api_pricing]] — KBank cost (raw) + Thunder cross-billing
