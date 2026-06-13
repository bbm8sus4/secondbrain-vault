---
name: EasyBOT Finance (easybot.finance)
description: Multi-tenant SaaS finance dashboard. Path mapping + stack + phase status.
type: project
originSessionId: 509744bf-2efa-45b2-a1e2-901ec3359d4a
---
**Local path:** `/Users/aexgee/Desktop/EasyBOT/finance-webapp`
(Folder name `finance-webapp` does NOT match repo name `easybot-finance-cockpit` — easy to miss in search.)

**Aliases user may use:** "EasyBOT Finance", "easybot.finance", "finance cockpit", "easybot-finance-cockpit"

**URLs:**
- Live: https://easybot.finance
- Pages: https://easybot-finance.pages.dev
- GitHub: https://github.com/bbm8sus4/easybot-finance-cockpit

**Stack:** Cloudflare Pages + D1 + R2, vanilla JS ES modules + Chart.js (no build step), Clerk auth, Paddle billing, Resend email, Sentry, PostHog, Gemini 2.5 Flash AI.

**Layout:**
- `index.html` — SPA shell + CSP
- `app.js` — frontend logic (~5,200 lines, module split in progress)
- `styles.css` — design system (CSS custom props)
- `functions/api/` — Pages Functions (state.js, insight.js, public-config.js, ai-threads*)
- `migrations/` — D1 schema (numbered, idempotent)
- `tests/` — Playwright

**Menus:** Overview, Compare, Goals, Portfolio, Subscriptions, AI Insight, Backoffice, Cost Master.

**Phase status (per ACTION_ITEMS.md):**
- Phase 0 Foundation ✅
- Phase 1 Auth + Multi-tenancy (Clerk + workspace isolation) 🟡 next
- Phase 2 Billing / Phase 3 Polish / Phase 4 Hardening ⏳

**Why:** User is solo COO building toward launch. Path is non-obvious so memory must hold the mapping.

**How to apply:** When user says any of the aliases above, go straight to the path. Don't search, don't clone. If user scopes a chat to a specific menu (e.g. "ทำ Overview เท่านั้น"), respect that boundary strictly.

**Knowledge base (Obsidian):** ทุกข้อมูล EasyBOT (ไม่ใช่แค่ Finance Webapp) → `~/SecondBrain/EasyBOT/` — มี knowledge base (หน้าหลัก + 01-Overview, 02-Finance-Webapp, 03-Organization, 04-Marketing-Content, 05-Partnerships-Legal, 06-Research-Strategy, 07-Design-Assets, 08-Past-Chats), `_source/` symlink → `~/Desktop/Business/EasyBOT/`, `_chats/YYYY-MM.md` (SessionEnd hook auto-append). ดู [[feedback-easybot-obsidian]]
