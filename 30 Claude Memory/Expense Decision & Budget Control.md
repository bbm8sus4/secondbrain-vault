---
name: project_expense_control
description: Expense Decision & Budget Control — SME expense-approval + budget/cash MVP. Next 16 + Supabase. Repo bbm8sus4/expense-control.
metadata: 
  node_type: memory
  type: project
  originSessionId: a4255932-5801-4bc1-bd9e-e14577c47f05
---

Production-ready MVP built 2026-07-14: **ประเมินค่าใช้จ่ายก่อนอนุมัติ → กันงบ → จ่ายจริง → คุมเงินสด** (ไม่ใช่ ERP/บัญชีเต็ม).

- **Source:** `~/Code/expense-control` · GitHub `bbm8sus4/expense-control` (private, `main`).
- **Stack:** Next.js **16** (App Router, Turbopack, `src/proxy.ts` = middleware — renamed in v16; `cookies()`/`params` async), TS strict, Tailwind 4, shadcn/ui, Supabase (Postgres+Auth+Storage+RLS), Zod, Recharts. Thai-first, THB, Asia/Bangkok.
- **Money engine = DB, not client:** every money mutation goes through SECURITY DEFINER SQL functions (`approve_expense_request`, `record_expense_payment`, `cancel_expense_request`, `adjust_budget`, `transfer_budget`, `create_cash_adjustment`, `increase_approval`…) with row locks + audit_logs. `budget_balances` view = source of truth for committed/actual/available. Invariants: approve=commit (no cash move), pay=release+actual (no double-count), over-pay blocked, underspend auto-released, cash balance = Σ cash_transactions.
- **Schema/source of truth:** `supabase/migrations/0001_schema … 0005_storage` + `supabase/seed.sql`. Apply via `supabase db push`.
- **Status: Supabase NOT provisioned yet** (user chose "scaffold migrations first"). To go live: create Supabase project → set 3 env vars (`.env.example`) → push migrations+seed → sign up → click "ตั้งเป็นผู้ดูแล" (`claim_admin()`, one-time first admin) → Vercel deploy.
- **Tests:** `pnpm test` (rule engine, 11 cases) + `tests/db/invariants.sql` (7 blocks, verified green on Postgres 17). Rule engine = transparent, explainable, no AI (`lib/finance/recommendation.ts`).
- Roles: requester/reviewer/approver/finance_admin (multi-role). RLS per `organization_id`; cash/payments/audit read gated to approver+finance.

Related: [[Vercel commit-author block|feedback_vercel_commit_author]] (git email already bobbysomporn@gmail.com ✓), [[กติกา - Deploy ใช้ stable URL|feedback_deploy_link]].
