---
name: Graphify skill installed
description: Knowledge-graph skill for Claude Code — turns any folder into queryable graph. Reduces token-per-query in large repos. Installed 2026-05-03.
type: reference
originSessionId: 7be13753-0760-437b-8848-7dfe6cb9ca55
---
**Installed:** 2026-05-03 via `pipx install graphifyy && graphify install` (PyPI package `graphifyy`, CLI/skill name `graphify`, v0.6.8). Skill file at `~/.claude/skills/graphify/SKILL.md`. Registered in `~/.claude/CLAUDE.md` (which was created fresh — did not overwrite anything; user's main memory remains at `~/.claude/projects/-Users-aexgee/memory/MEMORY.md`).

**Trigger:** `/graphify .` (or path). Useful subcommands: `update`, `watch`, `query "<question>"`, `path "A" "B"`, `explain "X"`, `cluster-only`, `add <url>`. Output → `graphify-out/` (graph.html, graph.json, GRAPH_REPORT.md, cache/, optional obsidian/wiki/).

**Why:** Graphify builds a knowledge graph of a codebase so coding agents don't re-grep from scratch each query. The viral "71.5x" figure = token reduction per query in their benchmark, not "smarter Claude." Real win = structured context > longer prompts.

**How to apply:**
- Suggest `/graphify .` for large/unfamiliar repos before deep work (especially `my-ai-bot/src/index.js` ~3500 lines, or merging across cost-intelligence-platform / invoice-control-hub / ai-orchestrator).
- For incremental work use `graphify update <path>` (no LLM, fast) or `graphify watch <path>`.
- **Privacy caveat:** code is parsed locally, but images/PDFs/diagrams go through Claude's vision API. Do NOT run on folders containing customer data, OAuth secrets, or `.env` files without `.graphifyignore`. Friday AI / easyslip / OCR-bot repos contain sensitive data — gate carefully.
- Aligns with user's "no local AI" rule (cloud Claude, not Ollama). ✓
