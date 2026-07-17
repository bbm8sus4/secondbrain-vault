---
type: community
cohesion: 0.20
members: 10
---

# KBank Pricing & Sales Playbook

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[Corporate Flat Pricing 0.125slip]] - rationale - Reports/thunder-corporate-api-sales-commission.md
- [[Corporate Sales Playbook]] - rationale - Reports/thunder-corporate-api-sales-commission.md
- [[Cost Scenario A (Other-source 100%)]] - rationale - Reports/thunder-corporate-api-sales-commission.md
- [[Cost Scenario B (Mix blend 3070)]] - rationale - Reports/thunder-corporate-api-sales-commission.md
- [[KBank]] - concept - Reports/kbank-api-pricing-and-easy-thunder-crossbilling.md
- [[KBank-source Tiered Pricing]] - rationale - Reports/kbank-api-pricing-and-easy-thunder-crossbilling.md
- [[Kbank Slip Verification API Pricing]] - document - Reports/kbank-api-pricing-and-easy-thunder-crossbilling.md
- [[Others-source Flat Pricing]] - rationale - Reports/kbank-api-pricing-and-easy-thunder-crossbilling.md
- [[Reduce Others-slip Cost Strategy]] - rationale - Reports/kbank-api-pricing-and-easy-thunder-crossbilling.md
- [[Sales Commission Model]] - rationale - Reports/thunder-corporate-api-sales-commission.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KBank_Pricing__Sales_Playbook
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_BNI Pitch & Platform]]

## Top bridge nodes
- [[Kbank Slip Verification API Pricing]] - degree 3, connects to 1 community
- [[Corporate Flat Pricing 0.125slip]] - degree 2, connects to 1 community