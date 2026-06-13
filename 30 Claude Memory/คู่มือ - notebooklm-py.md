---
name: reference-notebooklm-py
description: "notebooklm-py CLI installed — unofficial Python API for Google NotebookLM. Login via Chrome cookies, skill available in Claude Code as /notebooklm."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 21f97610-2761-4edb-9949-1f428111f8fd
---

# notebooklm-py

Unofficial Python API + CLI + MCP server สำหรับ Google NotebookLM
GitHub: https://github.com/teng-lin/notebooklm-py

## Setup ที่เครื่องนี้ (2026-06-13)

- **Install:** `uv tool install --with rookiepy "notebooklm-py[browser]"` (ต้องใส่ rookiepy ไม่งั้น `--browser-cookies chrome` ไม่ทำงาน)
- **Version:** 0.7.1
- **CLI binary:** `notebooklm` (อยู่ใน `~/.local/bin/` ผ่าน uv tool)
- **Login method:** Chrome cookie reuse — `notebooklm login --browser-cookies chrome`
- **Storage state:** `~/.notebooklm/profiles/default/storage_state.json`
- **Skill installed:**
  - `~/.claude/skills/notebooklm/SKILL.md` (Claude Code)
  - `~/.agents/skills/notebooklm/SKILL.md` (Agent Skills / `npx skills`)

## Verify

```bash
notebooklm auth check --test --json   # expect "status": "ok"
notebooklm list                        # list user's notebooks
```

## เตือน

- **Unofficial** — ใช้ undocumented Google API พังเมื่อไหร่ก็ได้
- เหมาะกับ prototype / research / งานส่วนตัว ไม่เหมาะ production
- มี rate limit หนักไปโดน throttle
- ใช้กับ [[feedback-no-local-ai]] ได้ — เป็น cloud (Google) ไม่ใช่ local

## Useful commands

- `notebooklm create "Title"` + `notebooklm use <id>` + `notebooklm source add <url|file>`
- `notebooklm ask "question"`
- `notebooklm generate audio|video|cinematic-video|quiz|flashcards|slide-deck|infographic|mind-map|data-table --wait`
- `notebooklm download <type> ./out.ext` — รองรับ batch + format ที่ web UI ไม่ให้ (PPTX, CSV, JSON, Markdown, HTML)
- `notebooklm profile list|switch` — multi-account
- `notebooklm auth refresh --browser-cookies chrome` — repair routing เมื่อ Google account หลายตัว
- `notebooklm agent show claude|codex` — print skill template

## What it does that web UI can't

- Batch download artifacts
- Export quiz/flashcard เป็น JSON/Markdown/HTML
- Mind map JSON
- Slide deck → PPTX (UI มีแค่ PDF), แก้สไลด์ทีละแผ่นด้วย prompt
- Data table → CSV
- Programmatic sharing
- Multi-account switch
