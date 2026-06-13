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

**Memory mirror:** `~/bin/sync-memory-to-vault.sh` → `sync-memory-to-vault.py` copies `~/.claude-warp/projects/-Users-aexgee/memory/` → `30 Claude Memory/` every 30 min via launchd `com.aexgee.memory-vault-sync` (RunAtLoad + StartInterval 1800). One-way: edit memories at source, never in vault. **Vault filenames are THAI, resolved self-healing** (rewritten 2026-06-13): name = `.display-names.json` (sidecar in the memory dir, DATA not code — curate Thai names here) → else the MEMORY.md index title → else English stem + log warning. So a NEW memory is never broken — no more hand-editing the .py dict. The sync also rewrites inline `[[english_slug]]` in memory bodies → `[[Thai|slug]]` so the graph connects. Vault-native notes are Thai-named too: `หน้าหลัก.md` (Home), `20 Rules/กติกาการทำงาน.md` + `20 Rules/คู่มือ vault.md` (operating manual), `03 Resources/แผนที่ - *.md` (4 MOC hubs).

**MCP:** `mcp-obsidian` (npx, vault-path flavor, read/search) registered in:
- Claude Code user scope (`claude mcp add --scope user obsidian`)
- Claude Desktop `claude_desktop_config.json`

**Rules for agents:** `20 Rules/Operating Rules.md` in vault — no duplicate notes, Title Case filenames, new notes to `00 Inbox/`, log completed work to daily/project notes. [[กติกา - Deploy ใช้ stable URL|feedback-deploy-link]] [[กติกา - ส่งข้อความหมู่ต้องช้า|feedback-broadcast-pacing]] rules are duplicated there.

**Capture pipelines (added 2026-06-11):**
- Telegram quick-capture: `~/bin/telegram-vault-capture.py` via launchd `com.aexgee.vault-capture` (60s poll) → appends to `00 Inbox/Telegram YYYY-MM-DD.md`, photos to `00 Inbox/แนบ/`. Config `~/.vault-capture.env` — ALLOWED_USERS prefilled from ccgram; **TELEGRAM_BOT_TOKEN pending: user must create a NEW bot via @BotFather** (can't reuse Humdum token — getUpdates conflict with ccgram). Script exits silently until token filled.
- Meeting notes: master sync script also `git pull` `~/meeting-notes` + rsync `notes/`+`quotations/` → `40 Meeting Notes/`.
- Codex CLI: `~/.codex/AGENTS.md` now instructs writing "จำ/บันทึก" requests to `00 Inbox/`.
- Obsidian Sync Standard (yearly, renews 2027-06-11) purchased for Mac↔iPhone sync.

**Why:** User wants SynapTech-style "Memory Architecture" — one central brain readable by Claude Code + Claude Desktop + Codex + mobile (Obsidian iOS via Sync).

**Hardening (2026-06-13):** Vault is now its OWN git repo (`~/SecondBrain/.git`, was untracked under home repo = no real backup). `sync-memory-to-vault.sh` auto-commits every run → rollback via git. **Off-machine backup (2026-06-14):** auto-pushes to PRIVATE GitHub `bbm8sus4/secondbrain-vault` after each commit (offline-tolerant — flushes backlog next sync). Recover a fresh machine with `git clone https://github.com/bbm8sus4/secondbrain-vault.git ~/SecondBrain`. **MUST stay private** (contracts/financials/security audit inside). Push uses gh credential helper (`gh auth setup-git`, account bbm8sus4). `.smart-env/` (50MB embedding cache) gitignored. rsync of meeting-notes now guarded (won't `--delete` if source empty). All sync scripts log to `~/Library/Logs/secondbrain-sync.log` + launchd plists have StandardOut/ErrorPath. New watchdog `~/bin/vault-health.py` (launchd `com.aexgee.vault-health`, daily 9am) → writes `00 Inbox/_vault-health.md`: dead-links, orphans, empty files, source↔mirror drift, sync age, recap freshness. friday_recap.sh `/tmp` issue was already self-fixed (uses `Friday/_source/`).

**How to apply:** When user mentions second brain / vault / Obsidian, work in `~/SecondBrain/`. Read `20 Rules/คู่มือ vault.md` first. Don't edit `30 Claude Memory/` or `40 Meeting Notes/` (mirrors). Curate Thai names in `.display-names.json`, never in the .py. Run `python3 ~/bin/vault-health.py` to check vault health.
