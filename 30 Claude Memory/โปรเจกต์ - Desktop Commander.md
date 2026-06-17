---
name: Desktop Commander config (hardened)
description: User's Desktop Commander MCP config was hardened on 2026-04-08 with narrow allowed folders, zsh shell, telemetry off. Backup exists for rollback.
type: project
---

Desktop Commander config lives at `~/.claude-server-commander/config.json`.

**Hardened on 2026-04-08** (re-applied — earlier hardening had been reset). Current state:
- `allowedDirectories`: 8 paths — 6 project folders (my-ai-bot, invoice-control-hub, cost-intelligence-platform, ai-tools, telegram-ocr-bot, shift-coffee) + `~/.claude` (Claude Code memory) + `~/.claude-server-commander` (DC's own config). Previously `[]` = full filesystem access.
- `defaultShell`: `/bin/zsh` (was `/bin/sh`)
- `telemetryEnabled`: false (was true)
- `fileReadLineLimit`: 2000, `fileWriteLineLimit`: 500 (already set)
- `blockedCommands`: 33 defaults, unchanged
- DC v0.2.38 has NO blocklist feature — only whitelist via `allowedDirectories`. To exclude a path you must omit it from the allowlist.

**Also patched (2026-04-08):** `dist/tools/schemas.js` `StartProcessArgsSchema.timeout_ms` made optional with default 30000 to fix wrapper validation bug. Note: this lives in npx cache (`~/.npm/_npx/4b4c857f6efdfb61/...`) and will be overwritten if DC re-installs.

**Why:** User wanted balance between convenience and security — block AI access to ~/.ssh, ~/.codex, ~/.config/gh, ~/.config/gcloud, ~/.docker, ~/.railway, ~/Library/Keychains, ~/Library/Messages, and project .env files while keeping active projects fully accessible. User keeps projects directly in $HOME (not in ~/projects/), so each project folder is listed individually. CLI tools (gh, gcloud, docker, ssh) still work because they read credentials themselves via shell — only direct file reads through DC are blocked.

**Backup:** `~/.claude-server-commander/config.json.backup` contains the pre-hardening config (empty allowedDirectories, /bin/sh, telemetry on).

**How to apply:**
- If user says "rollback DC" / "คืนค่า DC" / similar → `cp ~/.claude-server-commander/config.json.backup ~/.claude-server-commander/config.json` then tell user to restart Claude Desktop.
- If user adds a new project folder outside the allowed list and hits permission errors → add the new path to `allowedDirectories` in the config and remind to restart.
- After any config change, Claude Desktop must be restarted for DC to reload.
