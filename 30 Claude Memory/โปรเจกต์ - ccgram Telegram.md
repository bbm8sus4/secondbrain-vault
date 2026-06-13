---
name: project-ccgram-telegram
description: "ccgram — control Claude/Codex/Gemini + full terminal from Telegram, terminal mirrored as PNG. Installed 2026-06-10."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7e58d40f-663a-4676-8ff2-991f0fb82254
---

User wants Telegram as a "terminal wrapper" to drive AI agents + shell from phone, with images back. Chose **ccgram** (`alexei-led/ccgram`, v3.5.2) over building custom. Installed & configured 2026-06-10.

**What it is:** Bridges Telegram ↔ tmux. Renders tmux pane to PNG in Telegram (live view ~5s refresh via `pyte`+`pillow`), sends keystrokes to pane (= real terminal, not just chatbot), long-polling (no inbound port). Deps: libtmux, pyte, pillow, python-telegram-bot 22.7.

**Install:** `uv tool install ccgram` → bin at `~/.local/bin/ccgram`. Needs Python 3.14+ (have 3.14.4). CLI: `ccgram run|doctor|hook|status` (run = start the bot, NOT bare `ccgram`).

**Config:** `~/.ccgram/.env` (loads cwd `.env` > `~/.ccgram/.env`). Real keys: `TELEGRAM_BOT_TOKEN`, `ALLOWED_USERS` (csv user-id whitelist — the security gate), `CCGRAM_GROUP_ID` (-100…), `CCGRAM_PROVIDER` (claude|codex|gemini|pi|shell), `TMUX_SESSION_NAME`. Providers: claude/codex/gemini/pi/**shell** all supported.

**Hooks installed** (done): `~/.claude/settings.json` (9 events), `~/.codex/hooks.json` (2), `~/.gemini/settings.json` (4). NOTE: running inside claude-warp harness sets `CLAUDE_CONFIG_DIR=~/.claude-warp`, so first claude hook install landed there — had to reinstall with `CLAUDE_CONFIG_DIR=~/.claude` for real usage.

**YOLO / bypass-permission** = per-window toggle (🇾 button / `Ctrl-Y`), maps to real flags: claude `--dangerously-skip-permissions`, codex `--dangerously-bypass-approvals-and-sandbox`, gemini `--yolo`. No global default (per-session only). User explicitly wanted full-terminal + bypass.

**Keep-alive:** RUNNING via launchd `~/Library/LaunchAgents/com.user.ccgram.plist` (label `com.user.ccgram`, RunAtLoad+KeepAlive). Logs: `~/.ccgram/ccgram.out.log`. Manage: `launchctl kickstart -k gui/$(id -u)/com.user.ccgram` (restart), `launchctl bootout gui/$(id -u)/com.user.ccgram` (stop).

**STATUS 2026-06-10: FULLY CONFIGURED + LIVE.** Bot = **Humdum** @Humdum_dum_bot (privacy mode OFF — required). ALLOWED_USERS=6235317813 (Bob Sanchez @Bobsanchezz). CCGRAM_GROUP_ID=-1003766054316 (supergroup "humdum", Topics on, bot=admin). Token in `~/.ccgram/.env`. doctor all green. Got user-id + group-id automatically via Telegram API getUpdates (no @userinfobot needed once token exists).

**Phone usage:** in the group → `/sessions` (start session, pick provider) → type commands → `/live` (live terminal PNG) / `/screenshot` / `/toolbar` (🇾 YOLO = bypass). Plan file: `~/.claude-warp/plans/ai-telegram-serene-duckling.md`. Relates to [[reference_cmux]], [[project_thunder_solution]].

**UX TUNING 2026-06-11** (33-finding workflow review). Re-runnable patch scripts in `~/.ccgram/` (re-run after every `uv tool upgrade ccgram`, order: thai-ui-patch.py → ccgram-tune.py; restart `launchctl kickstart -k gui/$(id -u)/com.user.ccgram`):
- `thai-ui-patch.py` — Thai UI strings (121+ replacements: pickers, dashboard, status bubble, toasts, /start). `.bak-en` backups.
- `ccgram-tune.py` — 5 structural patches: (1) cc_commands.py trim menu 52→9 Thai cmds; (2) main.py fix CCGRAM_LOG_LEVEL bug (was always debug); (3) topic_lifecycle.py pin-resilient probe (no spam when can_pin off); (4) directory_callbacks.py CCGRAM_QUICK_START=1 → new topic launches Claude+YOLO immediately, skips provider/mode pickers; (5) sessions_dashboard.py "New Session" button rewired from no-op → createForumTopic. `.bak-tune` backups.
- `.env` adds: AUTOCLOSE_DONE_MINUTES=0 + AUTOCLOSE_DEAD_MINUTES=0 (was DELETING topics after 30min!), CCGRAM_QUICK_START=1.
- plist WorkingDirectory ~/.ccgram → /Users/aexgee (was opening picker in the secret dir).
- AI Thai instruction sharpened (natural mobile tone) in ~/.claude/CLAUDE.md + ~/.codex/AGENTS.md + ~/.gemini/GEMINI.md.
- `cmux-telegram` = `~/.local/bin/cmux-telegram` (alias for tmux attach -t ccgram). ~/.tmux.conf has `set -g mouse on`.
- VERIFIED LIVE via Chrome MCP (port 12306, Telegram Web): full loop works — Telegram msg → Claude → **Thai reply** confirmed; 9-cmd Thai menu; YOLO/Opus 4.6 active. can_pin still OFF but now harmless (probe resilient). Pending Thai: toolbar labels (Esc/Last/Get File) still EN — needs ~/.ccgram/toolbar.toml emoji style (not done, needs all 5 providers' default grids).

**SECURITY REVIEW + HARDENING 2026-06-10** (26 confirmed findings, multi-agent review). FIXED automatically: .env 644→600 + dir 700 + logs 600 + plist Umask 0077; group locked (setChatPermissions can_invite_users=false, invite link rotated); removed 9 stray ccgram hooks from ~/.claude-warp (bot uses ~/.claude — keep hooks ONLY there); .ccgram/ added to ~/.gitignore (home IS a git repo) + tmutil exclusion. STILL OWED BY USER (can't automate): (1) **rotate token** @BotFather /token (leaked in transcript + was 644 + visible via `ps eww` on tmux child) — then update .env + `launchctl kickstart -k gui/$(id -u)/com.user.ccgram`; (2) **demote bot's own group admin rights IN-APP** (bot can't self-demote — Telegram "can't promote self"; turn off invite/promote/restrict/change-info, **KEEP Manage Topics + Delete Messages + PIN MESSAGES**); ⚠️ CORRECTION 2026-06-11: ccgram REQUIRES can_pin_messages (pins per-topic status). Turning pin OFF caused "Not enough rights to manage pinned messages" errors + new sessions fail to bind. Pin must stay ON. (3) **enable 2FA on @Bobsanchezz Telegram acct + carrier port-out PIN** (that account == root shell). ACCEPTED-BY-DESIGN (user wants full terminal): YOLO bypass flags, group members see all output, /send bypassable via cat+screenshot — mitigated by single-user whitelist + 2FA. CLEAN: no telemetry (egress = Telegram only via lsof), no conflict w/ Friday/OCR/ai-news (diff tokens), screenshot is pyte→PNG (no TCC).
