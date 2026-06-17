---
name: qa_ezxchange
description: "QA/security test of EasyExchange web app (ezxchange.trippyn.cc) — bilingual Apple-styled report, 4 critical findings"
metadata: 
  node_type: memory
  type: project
  originSessionId: cf811b34-0f9d-4728-b4d7-9b11e88205ab
---

QA + light security test of **EasyExchange** currency-exchange web app at `ezxchange.trippyn.cc` (Next.js + tRPC + Ant Design + Cloudflare), done 2026-05-31 via Chrome MCP as user `tamayuki`.

**Verdict: NOT ready for production.** 19 findings (4 critical / 5 high / 6 medium / 4 low).

Critical: **(1)** Turnstile CAPTCHA submits a hardcoded test token `XXXX.DUMMY.TOKEN.XXXX`, no iframe — bot gate disabled. **(2)** `exchange.getRate` returns `maxAmount: null` — entered ฿99,999,999,999 accepted, no upper limit. **(3)** Zero security headers (no CSP/HSTS/X-Frame-Options…), leaks `X-Powered-By: Next.js`. **(4)** Validation client-side only; disabled submit re-enabled via DevTools fires; amount field accepts `<script>` string (not proven to execute).

Real tRPC endpoints found: `auth.session`, `exchange.getRate`, `notification.list` (GET 200); `auth.login/logout/refresh`, `exchange.create/cancel`, `notification.markRead` (mutations).

Deliverable: bilingual TH/EN (toggle in-file), Apple-typography report at `/tmp/ezx-report/EasyExchange-QA-Report.html` (self-contained, screenshots embedded). Built via `/tmp/ezx-report/build.py`; copy refined by a 4-lens critique workflow (TH voice / EN voice / accuracy / tone). Related: [[กติกา - โหมดแฮกเกอร์|feedback_vibe_hacker_mode]], [[โปรไฟล์ - สาย Security|user_security_interest]].
