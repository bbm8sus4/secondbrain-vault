---
name: reference-cmux
description: Cmux — macOS native terminal (libghostty/Swift) for running multiple AI coding agents in parallel. Installed 2026-05-15.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 86333e39-f487-403d-a514-20ec95617ce1
---

**Cmux** (manaflow-ai/cmux) — macOS native terminal app built on libghostty + Swift/AppKit, designed for running multiple AI coding agents (Claude Code, Codex, Cursor, Gemini, Amp, Opencode, Pi, Rovo Dev, Copilot, etc.) in parallel with vertical tabs, split panes, and per-pane notifications. No tmux required.

- **Installed:** 2026-05-15 via `brew tap manaflow-ai/cmux && brew install --cask cmux`
- **App path:** `/Applications/cmux.app`
- **CLI:** `/opt/homebrew/bin/cmux` (version 0.64.6)
- **Auto-update:** via Sparkle — drag-install once, updates itself
- **Source/docs:** https://github.com/manaflow-ai/cmux · https://cmux.com/
- **Config:** reads `~/.config/ghostty/config` for themes/fonts if present (none currently)

**Key features:**
- Vertical tab sidebar shows git branch, PR status, working dir, listening ports, latest notification per workspace
- Blue ring on pane + sidebar highlight when an agent is waiting for input
- Built-in scriptable browser (snapshot a11y tree, click, fill, eval JS) — splits next to terminal so agents can hit dev server directly
- SSH support with remote workspace creation
- `cmux claude-teams` — one-command launch of Claude Code teammate mode, teammates spawn as native splits
- Browser import from Chrome/Firefox/Arc/20+ browsers
- Custom commands via `cmux.json`

**Linked agents already on this Mac:**
- `claude` at `/Users/aexgee/.local/bin/claude` (Claude Code)
- `codex` at `/opt/homebrew/bin/codex` (Codex CLI)

**Update later:** `brew upgrade --cask cmux`

**Related:** [[project-ai-orchestrator]] — Cmux complements `/ai-loop`: ai-loop is a job-spec-driven batch runner across providers, Cmux is the live interactive surface for human-in-the-loop multi-agent work.
