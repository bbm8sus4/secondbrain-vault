---
name: reference-claude-repos-ecosystem
description: "Curated dataset + dashboard of top 10,000 Claude Code GitHub repos, categorized, bilingual"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 13b494b3-94d0-42e7-8cdb-97fa23d26b24
---

**Claude Code Ecosystem — 10,000 Repos** (built 2026-07-03)

Pulled 10,543 unique GitHub repos related to Claude / Claude Code, kept top 10,000 by stars, categorized into 13 buckets via keyword heuristic.

- Knowledge base (Obsidian): `~/SecondBrain/03 Resources/Engineering/Claude Code Ecosystem — 10,000 Repos ยอดนิยม.md` — methodology + top 10 repos per category (Thai desc). Linked from [[คู่มือ - SecondBrain Resources|reference-secondbrain-resources-hub]] map note `แผนที่ - คู่มือ`.
- Files on disk: `~/Desktop/Claude Repos/` → `index.html` (bilingual TH/EN toggle dashboard, embedded Noto Sans Thai, search + category filter, client-side paginated), `repos_10k.csv`, `repos_10k_th.csv`, `raw_10543.json`.
- Regenerate scripts (in /tmp, may be cleared): `fetch_10k.py` (star-range partition to beat GitHub's 1000/query cap), `translate_desc.py` (Google Translate batch 25/req), `build_bilingual.py`.
- Key technique: single query `claude-code` + `sort=stars` + 27 `stars:X..Y` buckets → 10.5k unique. Pace 2.2s/request for the 30/min search rate limit.
- Top categories: Agents/Orchestration 2785, Skills/Commands/Prompts 1939, MCP 1782.

Related tool work this session: [[Model Shift × cmux patch|project-modelshift-cmux]] (also documented in Obsidian `คู่มือ - Model Shift`).
