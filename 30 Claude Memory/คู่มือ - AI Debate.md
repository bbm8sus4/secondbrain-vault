---
name: ai-debate-harness
description: "Local multi-model debate tool (~/ai-debate/debate.py, wrapper `aidebate`) — Codex+Gemini+Claude propose→critique→synthesize for best-result answers. Includes the tricky headless CLI flags for each agent."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3a5d81b7-445f-40cc-abd6-c986b4fafda9
---

Built 2026-06-04 to satisfy "อยากให้ AI คุยกันเอง เพื่อผลลัพธ์ดีที่สุด". **Rewritten 2026-06-11** (robustness + features). Cloud subs by default — fits [[feedback_no_local_ai]]; Typhoon (local Ollama) is opt-in via `--typhoon` per user decision (its answers were visibly weaker — the panel itself criticized them).

**Tool:** `~/ai-debate/debate.py` (wrapper `~/ai-debate/aidebate`). 3 rounds: (1) Codex+Gemini+Claude propose in parallel → (2) anonymized cross-critique (drafts labeled Expert A/B/C to cut brand bias + identity confusion) → (3) judge synthesizes (default Claude).
- Run: `aidebate "question"` · flags: `--fast`/`--no-critique`, `--typhoon` (health-checks Ollama first, skips if down), `--judge claude|gemini|codex`, `--timeout SECS`, `-f FILE` (long prompts; stdin pipe also works), `--copy` (pbcopy final answer).
- Resilience: each model call retries once on failure (not on timeout); failed models are dropped from later rounds with a visible ⚠ and the debate continues; critique failure falls back to that model's Round-1 answer; live progress lines `✓ Gemini (38s)` / `✗ Codex (...)` per round.
- Transcripts: history at `~/ai-debate/debates/YYYYMMDD-HHMMSS.md` + latest always at `~/ai-debate/last_debate.md`.
- Demo (50-person ChatGPT rollout decision) ran 265s; cross-critique caught real errors a single model kept (stale "GPT-4o quota", Team→Business rename, "Go has ads" myth) — proving the quality lift.

**Headless one-shot invocations (verified 2026-06-11, macOS — these flags are non-obvious):**
- **Codex:** `codex exec --skip-git-repo-check --ephemeral --color never -o <tempfile> "PROMPT" </dev/null` — `-o/--output-last-message FILE` writes ONLY the final agent message (no more stdout-noise heuristics); needs the trust flag or it blocks; reads stdin (redirect from /dev/null). **Known failure mode: expired ChatGPT auth → exit 1 with "access token could not be refreshed" on stderr → fix with `codex login`** (this is what silently produced empty Codex answers in the old script).
- **Gemini CLI:** `GEMINI_CLI_TRUST_WORKSPACE=true gemini -p "PROMPT" -o text` — needs the trust env (or `--skip-trust`) or it refuses; strip "Ripgrep is not available" warning.
- **Claude Code:** `claude -p "PROMPT"` — clean output, works as-is (even spawned from inside a Claude session).
- **Typhoon:** Ollama API `localhost:11434/api/generate`, model `scb10x/typhoon2.1-gemma3-12b`; health-check `GET /api/tags`.
- macOS has no `timeout`; use `perl -e 'alarm shift; exec @ARGV' SECS cmd...` or python `subprocess(..., timeout=)`.

**Installed agent CLIs:** codex `/opt/homebrew/bin/codex`, gemini `/opt/homebrew/bin/gemini`, claude `~/.local/bin/claude`. **Antigravity** (`agy`/`antigravity`) is a GUI IDE app (`/Applications/Antigravity.app`, Gemini-powered, config under `~/.gemini/antigravity*`) — NOT a headless terminal agent, so it can't join the terminal debate; its multi-agent lives inside its own app.

Related: alternative for free-form "living team" chat = hcom / OpenAgents (see session research). [[reference_cmux]]
