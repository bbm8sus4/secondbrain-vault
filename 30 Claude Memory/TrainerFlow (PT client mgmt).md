---
name: project_trainerflow
description: "TrainerFlow — Thai PT client-management web app built from spec, Next.js 16 + Supabase, on GitHub"
metadata: 
  node_type: memory
  type: project
  originSessionId: d02346a8-e0db-4158-82d0-70171f7ae46a
---

TrainerFlow — ระบบบริหารลูกเทรนสำหรับเทรนเนอร์ (trainer + client portals). Built 2026-07-13/14 from `~/Desktop/trainerflow_claude_warp_master_context.md` spec.

- **Repo**: `~/trainerflow` · GitHub `bbm8sus4/trainerflow` (private) · Next.js 16 (App Router, TS strict, Tailwind v4) + Supabase (Auth/Postgres/RLS/Storage).
- **Runs in demo mode with zero credentials** (`DEMO_MODE=true`, in-memory seeded store). Demo logins: trainer โค้ชบ๊อบ + 8 clients, all fictional `*.demo.trainerflow.local`.
- **Architecture**: `DataStore` interface (`repositories/types.ts`) with demo + supabase adapters; `getDataStore()` is the only switch. Session balances = append-only ledger, atomic complete/revert via SECURITY DEFINER RPCs. 3-layer authz (proxy.ts → server guards → RLS). Details in `docs/` (10 files).
- **Status**: all 5 gates green (lint/typecheck/48 tests/build/12 e2e). **Caveats** (see `docs/IMPLEMENTATION_STATUS.md`): local Supabase/pgTAP NOT run (Docker/OrbStack wouldn't start) — run `pnpm supabase start && db reset && test db` on a Docker machine; Supabase adapter compiles but unrun against live DB; `createClient` needs an invite flow before Supabase-mode client creation; rate-limiting + CSP headers pending.
- Built with a team of subagents (SQL, trainer pages, client pages, Supabase adapter). Next feature rec: appointment/renewal reminders. Related: [[โปรเจกต์ - Thunder Solution|project_thunder_solution]] (COO's main business — separate).
