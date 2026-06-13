---
name: Invoice Control Hub - DEPRECATED
description: Invoice Control Hub monorepo — DEPRECATED 2026-04-29. User abandoned the project. Do not suggest deploying, fixing, or extending. Skip in any "what should I work on next" prompt.
type: project
originSessionId: a4b8f59d-a5ce-4b36-8841-d300a1cb3ac2
---
## ⚠️ DEPRECATED 2026-04-29

User explicitly abandoned this project. Do **NOT**:
- Suggest deploying
- Fix the security findings from `security_audit_2026-04-29.md` (C3, C4, C5)
- Extend or maintain
- Bring it up as "next step" in roadmap discussions

The audit findings on this codebase are kept as a learning artifact — useful as a reference of "what NOT to do" patterns (plaintext OAuth tokens, unsigned state, JWT in querystring).

---

## Original Project Context (kept for archive only)

## Invoice Control Hub

**Location:** `/Users/aexgee/invoice-control-hub`
**Type:** pnpm monorepo + Turborepo

### Architecture
- **apps/api** — NestJS backend (port 4000, global prefix `/api`)
- **apps/web** — Next.js 14 + Tailwind + shadcn/ui (port 3000)
- **apps/worker** — NestJS BullMQ worker (health port 4001)
- **packages/database** — Prisma (PostgreSQL)
- **packages/types** — Shared TypeScript types
- **packages/config** — Shared config

### Key Features (completed)
- Gmail OAuth mailbox integration (connect/disconnect/sync)
- IMAP support
- AI-powered invoice pipeline: SYNC → FETCH → CLASSIFY → EXTRACT → DEDUP
- Claude AI for classification + extraction (with PDF support)
- S3/MinIO storage for attachments
- PDF/image preview for invoice documents
- Delete invoice, soft-delete mailbox
- Responsive design
- Role-based access (SUPER_ADMIN, FINANCE_ADMIN, DEPARTMENT_OWNER, MAILBOX_OWNER, VIEWER)

### Pages
`/login`, `/dashboard`, `/invoices` (list + detail `[id]`), `/mailboxes`, `/review`, `/audit`, `/settings`

### Database
PostgreSQL via Prisma. Key models: Organization, User, MailboxAccount, EmailMessage, EmailAttachment, Vendor, InvoiceCandidate, Invoice, InvoiceDocument, AuditLog, SystemJob

### Deployment Infrastructure (ready but not yet deployed)
- Docker Compose: dev, staging, prod configs
- Dockerfiles for api, web, worker
- Nginx reverse proxy (TLS, rate-limiting, WebSocket)
- Scripts: `setup-vm.sh`, `deploy.sh`, `migrate.sh`, `backup-postgres.sh`, `healthcheck.sh`, `rollback.sh`
- Systemd service files
- Supports both managed (Supabase+Upstash) and self-hosted (Docker PostgreSQL+Redis)
- Target: DigitalOcean Droplet (Ubuntu 22.04), guide at `infra/deploy/digitalocean-guide.md`
- Deploy path: `/opt/invoice-hub` on server, user `deployer`

### Last Activity (2026-04-04)
- Latest commit: `f3e7eac` — Supabase + Upstash support with backward-compatible local dev
- Cloud migration completed (Supabase + Upstash support added)
- Branch: `main`, clean working tree
- Git remote: `origin/main`

### Next Step
**Production deployment** — needs decisions on:
1. Server provider (DigitalOcean guide ready)
2. Database mode (managed vs self-hosted)
3. Domain name
4. Git remote (needs to be pushed to GitHub for deploy.sh `git pull`)
5. Gmail OAuth credentials (optional for mailbox integration)

**Why:** Project is feature-complete for initial launch, all deployment scripts and infrastructure configs are ready. Just needs actual server provisioning and env configuration.

**How to apply:** When user returns to this project, pick up from deployment decisions above. All code and infra is ready — focus on server setup, secrets generation, and first deploy.
