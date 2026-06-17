---
name: ai-orchestrator
description: One-click multi-AI pipeline at ~/ai-orchestrator/ with /ai-loop skill. Routes jobs across Claude Max (claude -p), ChatGPT Plus (codex exec), and any web AI (Chrome MCP). Built 2026-04-30.
type: project
originSessionId: 0f03386f-e7a6-475f-9c21-fd6f5e11a928
---
**Trigger:** `/ai-loop` skill in Claude Code (visible in skill list as `ai-loop`).

**Layout:**
- `~/.claude/skills/ai-loop/SKILL.md` — orchestrator instructions
- `~/ai-orchestrator/pipeline.ts` — Bun runner for `claude` / `codex` / `bash` providers
- `~/ai-orchestrator/drivers/neomake.md` — Chrome MCP playbook (proven selectors, 2026-04-30)
- `~/ai-orchestrator/drivers/web.md` — generic Chrome MCP playbook
- `~/ai-orchestrator/jobs.yaml` — default job spec
- `~/ai-orchestrator/.session.jsonl` — resumable log (skip jobs already done)
- `~/ai-orchestrator/out/<run-id>/` — outputs

**Providers:** `claude` (Max sub), `codex` (Plus sub — needs codex CLI ≥0.125), `bash`, `neomake` (Chrome MCP), `web` (Chrome MCP).

**Why:** User wanted single click → loop AI tasks across services without re-typing prompts each time. Subscriptions only (no API key cost).

**How to apply:** When user wants to add automation that hits multiple AI tools, extend this — add a new driver in `drivers/` or a new `provider` branch in `pipeline.ts`. Don't reinvent. For new web AIs, just add `provider: web` job entries with `url:` and `steps:`.

**Known:** codex 0.118 doesn't work with ChatGPT account (needs ≥0.125). Upgrade via `npm i -g @openai/codex`. Veo flags person likeness in ref images — log policy violation and retry on Seedance/Kling.
