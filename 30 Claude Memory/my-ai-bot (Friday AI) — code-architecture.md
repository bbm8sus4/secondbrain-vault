---
name: project_my_ai_bot
description: "my-ai-bot (Friday AI) technical reference — Cloudflare Worker Telegram bot architecture, DB, cron, multi-user roles"
metadata: 
  node_type: memory
  type: project
  originSessionId: 523d3065-5a4e-4bfa-b668-afb1db462f4b
---

**my-ai-bot (Friday AI)** — Telegram bot, technical reference. Codebase/history in the repo; this is the non-obvious architecture map.

- **Type:** Cloudflare Worker, single-file `src/index.js` (~3500 lines)
- **DB:** D1 SQLite, migrations in `migrations/` (currently 0001-0014)
- **Cron:** Every 3h → `proactiveAlert`, `proactiveInsightAlert`, `summarizeAndCleanup`
- **AI:** Gemini 2.5 Flash via direct API call (`askGemini` helper)
- **Telegram:** Bot API with callback queries (inline keyboards), `sendTelegramWithKeyboard`
- **Key tables:** messages, commitments, memories, summaries, file_cache, bot_messages, alerts, group_registry, allowed_users
- **Multi-user:** Role-based access (boss=full, member=limited, null=rejected). `getUserRole()`, `MEMBER_COMMANDS`, `MEMBER_CALLBACKS` sets. `/allow`, `/revoke`, `/users` commands. `handleMemberChat` = simplified AI (flash model, no actions)
- **Proactive Alert v2:** JSON output format, dedup via topic_fingerprint, urgency scoring (critical/high/medium/low), per-group gathering with priority_weight, real-time urgent alerts via regex, boss feedback learning
- **Callback format:** `pa:<mode>:<chatId>:<alertId>` where mode = s/d/h/x
- **Multi-instance:** Wrangler envs (`[env.daisy]`). `BOT_NAME` env var replaces hardcoded "Friday". `BOSS_NICKNAMES` env var (JSON array) for `detectBossMention`. Deploy: `deploy:all`, `db:migrate:all`
- **Syntax check:** `node -c src/index.js` (no test suite)

Friday bot's knowledge base (recaps/themes) lives in Obsidian — see [[โปรเจกต์ - Friday Bot|project_friday_bot]].
