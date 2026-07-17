---
type: community
cohesion: 0.70
members: 5
---

# Easyslip Gateway Infra

**Cohesion:** 0.70 - tightly connected
**Members:** 5 nodes

## Members
- [[stats JSON Endpoint (currentgaugeshistorylimiter, refresh 1s)]] - concept - Documents/easyslip-gateway-summary.pdf
- [[Critical Security Finding Auth Token in Query String]] - rationale - Documents/easyslip-gateway-summary.pdf
- [[Easyslip Gateway (easy-kbank-lb — rate-limited proxyLB บน cluster jetder.com)]] - concept - Documents/easyslip-gateway-summary.pdf
- [[Easyslip Gateway — Live Dashboard Summary (PDF, สำรวจ 1 พ.ค. 2026)]] - document - Documents/easyslip-gateway-summary.pdf
- [[Token Bucket Rate Limiter (sustained 20 reqs, burst 50, window 5s)]] - concept - Documents/easyslip-gateway-summary.pdf

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Easyslip_Gateway_Infra
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Thunder Group & Brands]]
- 2 edges to [[_COMMUNITY_Business Overview & Docs]]

## Top bridge nodes
- [[Easyslip Gateway — Live Dashboard Summary (PDF, สำรวจ 1 พ.ค. 2026)]] - degree 6, connects to 1 community
- [[Easyslip Gateway (easy-kbank-lb — rate-limited proxyLB บน cluster jetder.com)]] - degree 6, connects to 1 community