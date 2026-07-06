---
name: feedback-secondbrain-vs-work-folder
description: User wants SecondBrain (Obsidian vault) to hold only notes (.md) and a separate ~/Work/<project>/ folder to hold real working files for every project
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 91c60f2b-347c-46e0-83e2-cf2529cbb471
---

For every project, keep SecondBrain (Obsidian vault) and the real working folder strictly separated:

- **SecondBrain** (`~/SecondBrain/01 Projects/<Project>/`) = notes only — `.md` files: brand strategy, research, decisions, FAQ, README. No images, no HTML deliverables, no binaries.
- **Work folder** (`~/Work/<Project>/`) = real files — assets, logos, mascots, content drops, HTML briefs, vendor files, docx, deliverables. Subfolders default: `brand/`, `assets/`, `marketing/`, `content/`, `vendors/`, `product/`, `archive/`.
- SecondBrain README links out to `~/Work/<Project>/` so the two stay connected. Use BOTH (a) markdown `file://` links for click-to-Finder, AND (b) a symlink `_files` inside the vault folder pointing at `~/Work/<Project>/` so Obsidian can browse/preview/embed real files via `[[_files/...]]` wikilinks. Confirmed pattern 2026-06-23 — user said "เอาหมด" when offered both options.

**Why:** User said "SecondBrain กับโฟลเดอร์งานจริงควรแยกกัน ไม่งั้น vault เต็ม" — Obsidian vault gets bloated and slow when binaries/HTML/large assets are stored inside. The vault is the "brain" (thinking), the Work folder is the "warehouse" (files). Confirmed 2026-06-23 when reorganizing KuanGolf.

**How to apply:**
- When starting a new project, create both `~/SecondBrain/01 Projects/<Project>/` and `~/Work/<Project>/` from day one.
- When user asks to "rวมไฟล์ของโปรเจ็ค X" or "organize files for X", default to this two-folder split — do NOT dump everything into SecondBrain.
- When discovering scattered project files across Desktop / Downloads / Documents, consolidate into `~/Work/<Project>/`, never into SecondBrain.
- If user wants assets visible inside Obsidian, suggest a symlink from vault → Work folder rather than copying files in.
