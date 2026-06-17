---
name: Telegram OCR Bot
description: Thai/English OCR bot (PDF + image) deployed on Google Cloud Run in asia-southeast1 — stack details and deploy quirks
type: project
originSessionId: d2769089-4496-4454-918d-a4d902e3b2e2
---
# telegram-ocr-bot (OCR - BOT in Telegram, used in group "OCR Tools - Easyslip")

**Deployment target:** Google Cloud Run (NOT Railway, NOT Fly, NOT a VPS)
- Project: `bobsanchez`
- Service: `ocr-bot-api`
- Region: `asia-southeast1`
- URL: https://ocr-bot-api-702369193047.asia-southeast1.run.app
- Webhook path: `/telegram/webhook`
- Deploy command: `gcloud builds submit --tag asia-southeast1-docker.pkg.dev/bobsanchez/ocr-bot/app:latest --region=asia-southeast1 .` then `gcloud run services update ocr-bot-api --region=asia-southeast1 --image=…`
- **No git-based auto-deploy** — `git push` alone does nothing; you must rebuild and update the service manually.
- Memory: 2 GiB (bumped from 1 GiB after OOMs during parallel preprocessing on 10-page PDFs).
- `--max-instances=1` to avoid 2 instances racing on the same update.
- Request timeout: 300s. Cloud Run CPU is throttled outside active requests by default — do not spawn `asyncio.create_task` and return 200 immediately, the task will be CPU-starved.
- **Database (since 2026-04-28):** Cloud SQL Postgres 15, instance `ocr-bot-db` (db-f1-micro, asia-southeast1-c). Connection via Unix socket `/cloudsql/bobsanchez:asia-southeast1:ocr-bot-db` — Cloud Run service has `--add-cloudsql-instances` set, no VPC connector needed. DB `ocr_bot`, user `ocrbot`. Replaced the old Supabase free-tier project after it got deleted (NXDOMAIN, not just paused) and silently killed startup on 2026-04-28.
- **Secrets (since 2026-04-28):** All sensitive env vars now in Secret Manager, not plain Cloud Run env: `database-url`, `db-password`, `telegram-bot-token`, `telegram-webhook-secret`, `gemini-api-key`, `redis-url`. Cloud Run service account `702369193047-compute@developer.gserviceaccount.com` has `roles/secretmanager.secretAccessor` on each.

**Stack (reality, not what the README used to say):**
- FastAPI + aiogram 3, single process (`uvicorn app.main:app`). No Celery, no separate worker — Celery was removed in commit `fc467ff` and the OCR pipeline runs inline in the webhook request handler.
- OCR: Gemini 2.5 Pro via REST (`app/services/ocr/gemini_provider.py`). API key sent in `x-goog-api-key` header, never in the URL.
- PDF: pdf2image + poppler → OpenCV preprocessing → Gemini per page. Pages are preprocessed and OCR'd in parallel with `asyncio.to_thread` + `asyncio.gather(..., return_exceptions=True)` and a `Semaphore(3)` so a failed page becomes a warning instead of killing the whole job.
- Postgres (SQLAlchemy async) for jobs/users/pages **and** rate limit + dedup (since 2026-04-28 — Redis was removed). Atomic INSERT…ON CONFLICT via `app/services/ratelimit_service.py`.
- Dedup TTL: 600s (shorter TTLs let Telegram webhook retries slip past).
- **No Redis.** The `redis>=5.0.0` dep, `redis_url` setting, and Upstash binding were removed on 2026-04-28 after Upstash Redis (`magical-toad-68578.upstash.io`) got NXDOMAIN'd alongside the Supabase outage. Postgres handles everything Redis used to.

**Known stale files to ignore / clean if seen:**
- `docker/Dockerfile.worker`, `railway.toml`, `app/worker.py`, `app/tasks/` — should not exist. If they reappear, the audit missed a revert.

**Why:** I spent an entire afternoon (2026-04-09) re-diagnosing this stack because memory had no record of Cloud Run. The PDF processing also kept timing out because the handler was synchronous. Don't forget either fact.

**How to apply:** When the user mentions OCR bot / "OCR - BOT" / easyslip PDF problems, default to Cloud Run commands (`gcloud run services …`, `gcloud logging read …`) in `asia-southeast1`, not Railway/Fly. When diagnosing "bot doesn't reply", check Cloud Run request-timeout + OOM first, then Telegram `getWebhookInfo`.
