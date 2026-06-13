---
name: Security audit findings — 2026-04-29 (3 production systems)
description: Attacker-mindset audit of Friday AI (CF Worker), Invoice Control Hub (NestJS+Prisma monorepo, pre-deploy), Telegram OCR Bot (FastAPI on Cloud Run). Self-directed audit applying Bandit-derived edge-case discipline. Findings prioritized critical → high → medium.
type: project
originSessionId: a4b8f59d-a5ce-4b36-8841-d300a1cb3ac2
---
Audit run on 2026-04-29 by 3 parallel subagents + adversarial cross-check. Triggered by user's "vibe code hacker" mode — applying OverTheWire Bandit lessons (filename edge cases, content-type trust, hidden state) to the user's actual production code.

## Status (updated 2026-04-30 — DEPLOY COMPLETE for Friday + Sigma; Daisy paused)

- **Friday AI: ✅ FULLY SECURED IN PROD** — code commits 85f521d + 333661f + c3578df pushed. Wrangler secret set. Telegram setWebhook updated with secret_token. Verified: forged POST → 401, valid POST → 200. Worker version 767bc494.
- **Sigma AI: ✅ FULLY SECURED IN PROD** — same patch + secret + setWebhook. Verified 401/401/200. Worker version fc812519.
- **Daisy AI: 💤 PAUSED 2026-04-30 (per user request)** — cron emptied, Worker dormant, secrets+D1 preserved. To resurrect see inline comments in `wrangler.toml` near `[env.daisy.triggers]`. Webhook secret is set on Daisy but `setWebhook` was NOT done since user wanted it disabled — token never pasted in chat.
- **C2-siblings (tk:del, cl:del): ✅ CODE-PATCHED + DEPLOYED** to Friday + Sigma.
- **C3, C4, C5 (Invoice Hub): WON'T FIX** — project deprecated by user 2026-04-29.

## Tokens exposure note (2026-04-30)
Friday and Sigma bot tokens were pasted in conversation chat to enable setWebhook. Tokens are still valid. **Recommend rotation via @BotFather → /mybots → bot → API Token → Revoke** if user is concerned about chat-log exposure. After rotation, run `wrangler secret put TELEGRAM_BOT_TOKEN` for that env + setWebhook again with new token + same TELEGRAM_WEBHOOK_SECRET.

## NEW findings from adversarial sweep (2026-04-30) — not yet patched

**C6 — Memory IDORs in `src/handlers/memory.js`:**
- Line 274: `UPDATE memories SET priority = ? WHERE id = ?` — no user_id filter
- Line 303: `DELETE FROM memories WHERE id = ?` — no user_id filter
- Line 442: `UPDATE memories SET priority = 'warm' WHERE id = ?` — no user_id filter
- Line 468: `UPDATE memories SET priority = 'hot' WHERE id = ?` — no user_id filter
- Line 495: `DELETE FROM memories WHERE id IN (...)` — no user_id filter
- Same shape as C2 — members can mutate boss's memories. Memories table likely has user_id column (verify via migration 0003_create_memories.sql) → fix is `AND user_id = ?` filter, NOT boss-only (memories are per-user feature).

**Schema gap — `tasks` table:**
- Migration 0020_extend_tasks.sql added `created_by_id`, `assignee_id` columns but `handleTaskCommand` INSERT does not populate them. All current tasks have NULL ownership.
- Quick fix applied today: boss-only on mutating tk: actions.
- Proper fix (future session): wire `created_by_id` on INSERT, allow non-boss to mutate only own tasks (`WHERE created_by_id = ? OR assignee_id = ?`).

**Calendar gap — `/cal add` open to all members:**
- Members can run `/cal add ประชุม ...` and create events on the boss's single shared Google Calendar.
- Quick fix applied today: only `cl:del:` callback gated boss-only.
- Proper fix (future session): boss-only on `handleCalAdd` (and arguably the entire `/cal` command outside read-only listings).

## 🔴 CRITICAL — fix-today list

### Friday AI (in production now)

**C1. No Telegram webhook secret validation** [CODE-PATCHED — needs deploy]
- File: `src/index.js:56-69`
- Exploit: anyone who learns the Worker URL (`*.workers.dev/`) can POST forged Telegram updates with `from.id = BOSS_USER_ID`. Bot will trust them — fire any handler including `/allow <attacker_id>`, `/send`, `/delete`.
- Fix: `wrangler secret put TELEGRAM_WEBHOOK_SECRET` + register via `setWebhook?secret_token=...` + reject in `fetch()` when header doesn't match.
- Effort: 5 min.

**C2. IDOR on `del:` callback**
- Files: `src/handlers/delete.js:47-78`, `src/index.js:109`
- Exploit: `MEMBER_CALLBACKS` whitelists `del:`, but `handleDeleteCallback` never checks ownership. Any member can press `del:aa` (delete-all-groups) and wipe bot messages in groups they're not in.
- Fix: gate with `callbackQuery.from.id === Number(env.BOSS_USER_ID)` (mirrors `handleDeleteCommand:5`), OR remove `del:` from `MEMBER_CALLBACKS`.
- Effort: 2 min.

### Invoice Control Hub (NOT YET DEPLOYED — fix before first prod push)

**C3. OAuth + IMAP credentials stored as plaintext**
- Files: `apps/api/src/modules/mailbox/mailbox.service.ts:106, 140-141, 153-154`
- Issue: column names say `encryptedAccessToken`, `encryptedRefreshToken`, but `TOKEN_ENCRYPTION_KEY` is in `.env` and never imported anywhere. Tokens written raw.
- Exploit: any DB read access (Supabase compromise, backup leak, SQL injection in another module, rogue admin) yields full OAuth tokens for every connected mailbox + raw IMAP passwords.
- Fix: `crypto.createCipheriv('aes-256-gcm', TOKEN_ENCRYPTION_KEY, iv)` wrapper applied on every write/read of mailbox creds.
- Effort: 1-2 hours (needs code + migration + re-encrypt existing rows).

**C4. OAuth callback `state` is unsigned**
- Files: `apps/api/src/modules/mailbox/mailbox.controller.ts:39-68`, `mailbox.service.ts:46`
- Issue: `state` param is plain base64url-encoded JSON containing `userId`, `organizationId`. No HMAC, no nonce, no session binding.
- Exploit: attacker forges `state` so victim's OAuth `code` exchanges into attacker's org → attacker reads victim's mailbox. Or reverse: attacker links own mailbox under victim's org.
- Fix: HMAC-sign `state` with server secret + bind to single-use server-side nonce (Redis, 10-min TTL). Reject unrecognized state.
- Effort: 30 min.

**C5. JWT accepted from `?token=` query string**
- File: `apps/api/src/modules/auth/strategies/jwt.strategy.ts:11`
- Exploit: JWTs leak via web server logs, browser history, Referer headers, link-sharing. Combined with 24h expiry + no revocation = leaked token is 24h skeleton key.
- Fix: remove the query extractor; only accept `Authorization: Bearer`.
- Effort: 1 line.

---

## 🟠 HIGH — fix this week

### Friday AI
- **Cross-user file/cache disclosure** — `fc:` and `rl:` callbacks (`src/handlers/read.js:240-359, 564+`) lookup by `cacheId` only, no `chat_id` filter → member B reads member A's PDF summaries. Add `AND chat_id = ?`.
- **No rate limit on member Gemini chat** — `handleMemberChat` (`src/index.js:502`) has no rate cap → cost abuse. Add `isRateLimited` to mention/DM path.
- **API 500 leaks error details** — `src/handlers/api.js:254` returns `err?.message` to client. Replace with generic message.

### Invoice Hub
- **JWT_SECRET fallback to `'dev-secret'`** — `auth.module.ts:17`, `jwt.strategy.ts:15`. If env unset, app silently uses known weak secret. Fix: throw at bootstrap if missing.
- **No `helmet`/CSP at app layer** — `apps/api/src/main.ts`. Direct API access (dev/staging) unprotected. `app.use(helmet())` with strict CSP.
- **`Content-Disposition: inline` with email-supplied MIME** — `invoices.controller.ts:44-64`. Malicious email sender embeds SVG/HTML → stored XSS. Force `attachment` for non-PDF/image, whitelist mime.
- **Auth login lacks app-level rate limit** — only nginx limits `/api/auth/`. Add `@Throttle({ limit: 5, ttl: 60000 })` to `AuthController.login`.
- **Extraction endpoint unbounded body** — `extraction.controller.ts`. Add Zod max length, ReDoS protection.

### OCR Bot
- **Container runs as root** — both Dockerfiles. Pillow/poppler RCE = root inside container. Add `USER app` (uid 1001).
- **HEIC magic byte check is no-op** — `app/core/constants.py:64-65` matches only `\x00\x00\x00`. Most files satisfy. Fix: search for `ftyp` box at offset 4 + heic/heix/mif1 brand.
- **Webhook secret not enforced in dev/staging** — `app/api/routes/webhook.py:31`. If env empty, endpoint accepts any POST. Make required everywhere.

---

## 🟡 MEDIUM — track in issue tracker

**Friday AI:**
- `BOSS_NICKNAMES` substring match → false positives ("bob" matches "bobcat", "W" matches any word with w). Word-boundary regex.
- `tk:` task callbacks lack `user_id` filter → members can mark/delete boss's tasks.
- Gemini key passed via `?key=` query param → may leak in error logs. Move to `x-goog-api-key` header.

**Invoice Hub:**
- Filename sanitizer doesn't strip NUL, leading dashes, RTL override (`‮`).
- `sortBy` from query lacks whitelist → low-risk DoS, schema leak via error.
- Self-role-change not blocked (last-admin lockout risk).
- No failed-login lockout counter.
- `dashboard.controller` missing `@Roles` guard → MAILBOX_OWNER sees org-wide stats.

**OCR Bot:**
- Per-user rate limit keyed on Telegram-controlled `user_id` — if webhook secret missing, attacker rotates IDs to bypass.
- TIFF allowed (high-mem decompression risk before bomb-cap fires).
- `/health/deep` returns raw exception text.

---

## ✅ DONE WELL (defense already in place)

- **All 3 systems**: SQL injection class is closed (Prisma everywhere in Hub, prepared statements + `.bind()` in Friday, ORM/parameterized in OCR). No raw concat anywhere.
- **Friday AI**: SSRF defense (`isPrivateUrl`) is comprehensive — RFC1918, link-local, metadata, IPv6 ULA, manual-redirect re-validation. Recently hardened (commit b3435c8).
- **Friday AI**: Telegram WebApp auth uses correct HMAC-SHA-256 over sorted params, 24h window, boss-only check on dashboard API.
- **Friday AI**: D1 multi-instance isolation — separate database_id per env in wrangler.toml.
- **Friday AI**: HTML escaping in alerts — `esc()` on all user-name interpolations.
- **OCR Bot**: webhook secret uses `hmac.compare_digest` (constant-time).
- **OCR Bot**: Gemini key via `x-goog-api-key` header (not query string).
- **OCR Bot**: bot token scrubbed from exception messages.
- **OCR Bot**: local downloads use `uuid4()` filename — Telegram filename never touches FS path. Path traversal structurally impossible.
- **OCR Bot**: production refuses to launch without required env vars.
- **Invoice Hub**: every read/write filters by `organizationId` from JWT — no IDOR holes in API services.
- **Invoice Hub**: bcrypt cost-12 for passwords.
- **Invoice Hub**: production Docker is hardened — `read_only`, `cap_drop: ALL`, `no-new-privileges`, non-root `appuser`.
- **Invoice Hub**: nginx adds HSTS/X-Frame/X-Content-Type/Referrer-Policy + 5/min on auth.
- **Invoice Hub**: Swagger auto-disabled in production.
- **Invoice Hub**: `.env` correctly gitignored, only `.env.*.example` committed.
- **Invoice Hub**: ValidationPipe + Zod on mutating endpoints.
- **Invoice Hub**: NO file-upload endpoints, NO `exec/spawn/eval` — entire shell-injection class is N/A.

---

## Standing Orders that fired during this audit

- **SO#13 Recon-first**: started by mapping all 3 codebases before any code-reading.
- **SO#2 Aggressive parallelism**: 3 audits ran concurrent — saved ~5 min.
- **SO#14 Edge state hunting**: every category checked is an edge case (filename quirks, content-type vs magic, race conditions, ID vs ownership).
- **SO#16 Verify memory before acting**: memory said `src/index.js` was 3500 lines — actually 543 (refactored). Adjusted approach.

## Resume / next session pickup

When user returns to this:
1. Start with the 5 criticals (~3 hours total to fix all).
2. Run `npm audit` / `pnpm audit` on all 3 — not done in this audit.
3. Run `gitleaks` or `trufflehog` against all 3 repos for committed secrets in history.
4. Adversarial second pass — re-audit Friday after webhook-secret fix to confirm no other paths into the handler bypass it.
