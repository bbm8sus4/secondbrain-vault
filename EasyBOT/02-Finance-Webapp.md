---
title: "02 — EasyBOT Finance Webapp"
type: entity
source: "~/Desktop/Business/EasyBOT/ via _source symlink (brand KB session 2026-06)"
source_date: 2026-06-13
imported: 2026-06-13T22:49:35
last_verified: 2026-07-06
status: live
tags: [easybot, brand]
---

# 02 — EasyBOT Finance Webapp

> Multi-tenant SaaS finance dashboard บน edge — Cloudflare Pages + D1 + Clerk + Paddle + Gemini
> Live: **https://easybot.finance** · Pages: https://easybot-finance.pages.dev

## Path / Repo

- **Local:** `~/Desktop/Business/EasyBOT/07_Development/finance-webapp/`
  (vault symlink: `_source/07_Development/finance-webapp/`)
- **GitHub:** https://github.com/bbm8sus4/easybot-finance-cockpit
- ⚠️ ชื่อ folder `finance-webapp` ≠ ชื่อ repo `easybot-finance-cockpit` — search ยาก ให้ใช้ path ตรง

## Aliases ที่ user อาจใช้

"EasyBOT Finance", "easybot.finance", "finance cockpit", "easybot-finance-cockpit"

## Stack

| Layer | Tool | หมายเหตุ |
|---|---|---|
| Hosting | Cloudflare Pages | Edge, free tier เยอะ, integrate กับ D1 |
| Frontend | Vanilla JS + ES modules + Chart.js | ไม่มี build step |
| Database | Cloudflare D1 (SQLite) | Serverless, auto backup |
| Auth | Clerk | Email + Google OAuth, 10K MAU free |
| Billing | Paddle | Merchant of Record |
| Email | Resend | |
| Errors | Sentry | |
| Analytics | PostHog | |
| AI | Google Gemini 2.5 Flash | |
| CI/CD | GitHub Actions + Playwright | Test-gated deploy |

## Layout

- `index.html` — SPA shell + CSP
- `app.js` — frontend logic (~5,200 บรรทัด, module split in progress)
- `styles.css` — design system (CSS custom props)
- `functions/api/` — Pages Functions (state.js, insight.js, public-config.js, ai-threads*)
- `migrations/` — D1 schema (numbered, idempotent)
- `tests/` — Playwright

## เมนู

Overview · Compare · Goals · Portfolio · Subscriptions · AI Insight · Backoffice · Cost Master

## Phase (ตาม ACTION_ITEMS.md)

- Phase 0 Foundation ✅
- Phase 1 Auth + Multi-tenancy (Clerk + workspace isolation) 🟡 **next**
- Phase 2 Billing ⏳
- Phase 3 Polish ⏳
- Phase 4 Hardening ⏳

## Strengths (จาก ai-loop synthesis 2026-06-07)

จุดแกร่งจริง = **forward-looking FP&A** (cash forecast + scenario, variance attribution, proactive alerts) ไม่ใช่ table-stakes features

## ข้อควรระวัง deploy

- ใช้ stable URL `easybot.finance` หรือ `easybot-finance.pages.dev` เท่านั้น — **ห้ามแชร์ per-commit hash URL** ดู [[กติกา - Deploy ใช้ stable URL]]
- Lighthouse perf gate = 80 (เคยติด 55) — ต้องผ่านก่อน deploy
- Playwright 55/55 ต้องเขียว

## Source files

- `_source/07_Development/finance-webapp/` (code, README, ACTION_ITEMS, SECURITY)
- `_source/02_Finance_and_Trackers/` (Excel + Python builders ของ Finance Sheets เวอร์ชันก่อนเป็น webapp)
