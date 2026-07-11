---
name: reference_claude_code_commands_teaching
description: "Full Claude Code teaching guide (.md) — built-in slash commands + permission modes + how to pin a model (Opus 4.6) + how to set up the multi-row status line. For COO's workshops."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 523d3065-5a4e-4bfa-b668-afb1db462f4b
---

Single all-in-one **Claude Code teaching guide** built for COO's AI workshops. Covers 4 things:
1. ~45 built-in slash commands (multi-dimensional tables: ทำอะไร/ใช้เมื่อไร/บริบท)
2. 5 permission modes (shift+tab: Plan/Default/accept-edits/auto/bypass) + matrix
3. **Pin a model permanently** (e.g. Opus 4.6) — Prompt version + one-liner + caveats (settings.json wins over /model picker on restart; picker list is app-baked so can't add previous models). See [[Model config — pin in settings.json|reference_model_config_fix]].
4. **Set up multi-row status line** (model+context bar / Current 5h / Weekly 7d / 📁 folder ⎇ branch) — installer + Prompt + manual.

**Files (all in `~/SecondBrain/03 Resources/AI Workshops/`):**
- `Reference — Claude Code คำสั่ง built-in (ฉบับสอน).md` — the master .md (recall surface)
- `claude-code-commands-guide.html` — printable one-page cheat sheet (also at `~/claude-code-commands-guide.html`)
- `คู่มือ Claude Code (ฉบับสอน).pdf` — 9-page PDF handout (Chrome headless from the HTML; also on ~/Desktop)
- `claude-statusline-installer.sh` — self-contained status line installer (also at `~/claude-statusline-installer.sh`)
- `claude-code-setup-pack.html` — install+config pack, both OSes, **tabs + per-block คัดลอก (copy) buttons** (also at `~/claude-code-setup-pack.html`). Native installers: mac `curl .../install.sh|bash`, Win PowerShell `irm .../install.ps1|iex` (Windows native, no WSL). Verified 2026-07-11. (`.md` version also exists.)
- `Prompt สอน — Use Case ง่ายๆ (ผู้เริ่มต้น).md` — beginner copy-paste prompt library, see [[Teaching prompts — easy use cases|reference_teaching_prompts_usecases]]. **TODO: HTML-with-copy-buttons version not built yet.**

**FORMAT PREFERENCE (important):** teaching/workshop deliverables should be **HTML** (unified light design, no emoji, per-block copy buttons for command/prompt packs) — NOT raw .md. User expects HTML for these. Convert .md packs to HTML.

Key teaching point: distinguish built-in commands from custom skills/plugins (`/Chrome-MCP-Owly`, `/CRUD-basic`, `/codex:*` are NOT built-in). Complements [[Anthropic Claude 101 curriculum|reference_anthropic_claude_101]]. Vault not auto-pushed — `git push` secondbrain-vault manually if sharing.
