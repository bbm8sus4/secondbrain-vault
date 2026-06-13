---
name: reference-gitnexus
description: "GitNexus codebase knowledge-graph MCP — installed 2026-05-15, 16 tools (impact/blast-radius/rename/diff-risk), 7 Claude Code skills, indexed my-ai-bot first"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 84acdf92-6890-4c36-9ed8-179b2ddfdb58
---

GitNexus v1.6.4 installed globally via npm. MCP server configured for Claude Code + Codex. 7 skills in `~/.claude/skills/` (gitnexus-refactoring, -debugging, -exploring, -impact-analysis, -pr-review, -guide, -cli). PreToolUse + PostToolUse hooks for auto-enrichment + stale-index detection.

Repo: `~/GitNexus/` (cloned from github.com/abhigyanpatwari/GitNexus).

First indexed repo: `my-ai-bot` (Friday AI) — 1,886 nodes.

Complements [[คู่มือ - Graphify|reference_graphify]] — GitNexus has MCP integration (16 tools), web UI, multi-repo registry; graphify is lighter-weight CLI-only.

**How to apply:** Use GitNexus skills (`/gitnexus-*`) for impact analysis before refactoring, debugging traces, and PR reviews on indexed repos. Run `gitnexus analyze` in a repo before deep work.
