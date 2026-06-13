---
name: project-second-brain
description: "Obsidian SecondBrain vault at ~/SecondBrain — central memory for all AI agents, auto-mirrored from Claude memory, MCP-connected"
metadata: 
  node_type: memory
  type: project
  originSessionId: bfbf0ac2-09c9-4c43-a027-47f3a362d1b4
---

# Second Brain (Obsidian vault)

Set up 2026-06-11. Vault at `~/SecondBrain/` (local, NOT iCloud — iCloud container creation was permission-denied; user buys Obsidian Sync Standard $5/mo instead for mobile sync).

**Structure:** PARA (`00 Inbox`–`04 Archive`) + `10 Daily` + `20 Rules` + `30 Claude Memory` (read-only mirror).

**Memory mirror:** `~/bin/sync-memory-to-vault.sh` → `sync-memory-to-vault.py` copies `~/.claude-warp/projects/-Users-aexgee/memory/` → `30 Claude Memory/` every 30 min via launchd `com.aexgee.memory-vault-sync` (RunAtLoad + StartInterval 1800). One-way: edit memories at source, never in vault. **Vault filenames are THAI** — the .py holds the English→Thai mapping (user wants Thai node names in graph view); new memory files need a mapping entry added or they appear with English names. Vault-native notes are Thai-named too: `หน้าหลัก.md` (Home), `20 Rules/กติกาการทำงาน.md`, `03 Resources/แผนที่ - *.md` (4 MOC hubs linking all memory files).

**MCP:** `mcp-obsidian` (npx, vault-path flavor, read/search) registered in:
- Claude Code user scope (`claude mcp add --scope user obsidian`)
- Claude Desktop `claude_desktop_config.json`

**Rules for agents:** `20 Rules/Operating Rules.md` in vault — no duplicate notes, Title Case filenames, new notes to `00 Inbox/`, log completed work to daily/project notes. [[feedback-deploy-link]] [[feedback-broadcast-pacing]] rules are duplicated there.

**Capture pipelines (added 2026-06-11):**
- Telegram quick-capture: `~/bin/telegram-vault-capture.py` via launchd `com.aexgee.vault-capture` (60s poll) → appends to `00 Inbox/Telegram YYYY-MM-DD.md`, photos to `00 Inbox/แนบ/`. Config `~/.vault-capture.env` — ALLOWED_USERS prefilled from ccgram; **TELEGRAM_BOT_TOKEN pending: user must create a NEW bot via @BotFather** (can't reuse Humdum token — getUpdates conflict with ccgram). Script exits silently until token filled.
- Meeting notes: master sync script also `git pull` `~/meeting-notes` + rsync `notes/`+`quotations/` → `40 Meeting Notes/`.
- Codex CLI: `~/.codex/AGENTS.md` now instructs writing "จำ/บันทึก" requests to `00 Inbox/`.
- Obsidian Sync Standard (yearly, renews 2027-06-11) purchased for Mac↔iPhone sync.

**Why:** User wants SynapTech-style "Memory Architecture" — one central brain readable by Claude Code + Claude Desktop + Codex + mobile (Obsidian iOS via Sync).

**How to apply:** When user mentions second brain / vault / Obsidian, work in `~/SecondBrain/`. Follow Operating Rules. Don't edit `30 Claude Memory/` directly.
