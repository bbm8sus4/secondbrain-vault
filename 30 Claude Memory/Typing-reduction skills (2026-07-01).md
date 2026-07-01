---
name: reference-typing-reduction-skills
description: "5 skills installed 2026-07-01 to reduce typing overhead — auto-open, voice input, statusline enhancement, pathdrop hook, autonomous mode. Full docs in Obsidian."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 03af5f4c-146b-4dbf-9239-82adab903b56
---

Skills installed 2026-07-01 เพื่อลด typing repetition:

**1. Auto-open Stop hook** — `~/.claude/hooks/auto-open-recent.sh`
- Tracks Write/Edit paths → auto-opens HTML/PDF/etc after agent stops
- Cooldown 45s, max 3 files/turn
- Disable: `touch /tmp/claude-auto-open-disabled`

**2. voice2clip.sh** — `~/bin/voice2clip.sh` + Karabiner F5 hotkey
- sox record → whisper-cli transcribe → clipboard + auto-paste
- Models: `~/whisper-models/ggml-small.bin` (466MB) + `ggml-medium.bin` (1.5GB)
- Env: `WHISPER_MODEL`, `WHISPER_LANG` (default `th`)
- **User must:** start Karabiner-Elements.app + grant mic permission

**3. Statusline enhancement** — `~/.claude/statusline.sh` (row 5 added)
- Shows: `📁 project ⎇ branch* ✎ N files`
- Reads track-file-writes log for touched-file count

**4. Pathdrop hook** — `~/.claude/hooks/pathdrop-expand.sh` (UserPromptSubmit)
- URL-only or path-only prompt → auto-inject "read+summarize" context
- Skips if prompt > 500 chars OR has trailing instruction > 80 chars

**5. `/keep-going` autonomous** — already ON via `skipDangerousModePermissionPrompt: true`

**Settings.json changes:**
- Added `PostToolUse` matcher for Write|Edit|MultiEdit|NotebookEdit → track-file-writes.sh
- Added `UserPromptSubmit` → pathdrop-expand.sh
- Added Stop hook entry → auto-open-recent.sh
- Backup: `~/.claude/settings.json.backup-20260701-114047`

**Karabiner change:**
- Added F5 → voice2clip.sh rule
- Backup: `~/.config/karabiner/karabiner.json.backup-20260701-*`

**Full docs:** `~/SecondBrain/02 Areas/My Prompting Style/skills-built.md`

**If hooks misbehave:** revert with `cp <backup> <target>` + restart Claude Code.

related: [[My Prompting Style (Obsidian)|reference_my_prompting_style]] [[กติกา - โหมดแฮกเกอร์|feedback_vibe_hacker_mode]]
