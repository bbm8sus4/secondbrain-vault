---
name: maw-setup
description: "maw-js (multi-agent tmux orchestrator) installed 2026-06-12 — install quirks, oracle convention, known traps, full-power config"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1afef197-b113-45e4-b27f-a09bb4d1766e
---

maw v26.5.21 installed 2026-06-12 (user accepted security risk, wants full power). Studied repo at /tmp/maw-js-study. Dev: Nat Weerawan (@nazt, Thai), bus factor 1, alpha churn.

**Install:** `curl -fsSL https://raw.githubusercontent.com/Soul-Brews-Studio/maw-js/main/install.sh | bash` — direct `bun add -g github:...` FAILS (`@maw-js/sdk@workspace` unresolvable). If binary vanishes (#531): `bunx -p github:Soul-Brews-Studio/maw-js maw doctor`.

**Config:** `~/.config/maw/maw.config.json` — node `macbook-aexgee`, port 3456, default cmd `claude --dangerously-skip-permissions`, codex pattern `--dangerously-bypass-approvals-and-sandbox`. ghq root = `~/Code` (repos at `~/Code/github.com/<owner>/<repo>`).

**Oracle convention:** wake target `foo` resolves repo `<ghq>/github.com/bbm8sus4/foo-oracle`. Org dir must match gh login (bbm8sus4), else needs `--all-local`. Test oracle: `maw-playground`.

**Traps verified:**
- `--task` string becomes tmux window name → dots (`.`) break tmux target syntax ("can't find pane"). Keep task slugs dot-free; real prompt goes in `-p`.
- `-p` on wake = one-shot print mode (claude exits after). For persistent agent: `maw wake <name>` bare (interactive), then `maw hey <name> "msg"`.
- `--continue` in command pattern kills fresh oracles ("No conversation found to continue" → agent dead). Removed from config.
- Broken wakes poison `~/.maw/snapshots/*.json` (rehydrate retries bad window) + leave stillborn worktrees in `<oracle>/agents/`. Fix: rm snapshot, `git worktree remove --force`, kill session, re-wake.

**Working loop:** `maw wake X` → `maw hey X "task"` → `tmux capture-pane -t '01-X' -p` or `maw peek`. Serve: `maw serve` (binds 127.0.0.1 when no peers), UI installed → http://localhost:3456/federation_2d.html. Cost API `/api/costs/daily` parses ~/.claude/projects JSONL with hardcoded API rates (notional — user is on Max 20x, not real spend).

**QA pass 2026-06-12 (all verified working):**
- serve runs under launchd `com.maw.serve` (~/Library/LaunchAgents/com.maw.serve.plist, KeepAlive+RunAtLoad, logs ~/.maw/logs/serve*.log). Kill-respawn tested. **UI 404 after `maw ui install` until serve restarts** (`launchctl kickstart -k gui/$UID/com.maw.serve`).
- maw-heal hook sourced in ~/.zshrc (copy at ~/.maw/maw-heal.sh, MAW_HEAL_SILENT=1) — auto-restores binary (#531).
- **`-e codex` silently ran claude** until engines defined: config now has `engines.{claude,codex}` + exact `commands.{claude,codex}` keys — `resolveEngine` matches exact engine name only (globs like `codex-*` are window-name patterns, not engine names; no ENGINE_SEED fallback at runtime).
- hey to worktree agent: target window agent name, e.g. `maw hey maw-playground-codex-qa "..."`.
- Codex side blocked by revoked refresh token (`codex login` needed — recurring issue); maw delivery itself verified into codex UI. Codex first-boot dialogs (update prompt, hooks trust) need one-time tmux send-keys answers.

Related: [[คู่มือ - Cmux|cmux]] (GUI alternative, stable), [[โปรเจกต์ - ccgram Telegram|ccgram-telegram]].
