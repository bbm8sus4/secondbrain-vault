---
name: feedback-apicost-listprice
description: Platform internal usage_cost API returns list price (~100x real cost). Always scrape the HTML table for actual post-Max-sub cost.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 65d75fcf-0782-4ed8-b99a-fdddac4fcf70
---

NEVER use the platform.claude.com internal API `/api/organizations/{org_id}/usage_cost` for cost reporting — it returns **list price** before Max subscription discount, which is ~100x higher than actual cost.

**Why:** First attempt sent a report showing $132.79 instead of $1.33 — user flagged it as completely wrong data. The "Cost" column on the platform HTML page shows the real post-discount cost.

**How to apply:** When building `/apicost` or any cost reporting from Claude Platform, always scrape the HTML table via `chrome_get_web_content(selector: "table")` on platform.claude.com/settings/keys. The internal API `usage_cost` endpoint is only useful if you want raw token counts or list-price-equivalent analysis.
