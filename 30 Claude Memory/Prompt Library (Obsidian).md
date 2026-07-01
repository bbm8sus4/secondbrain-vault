---
name: reference_prompt_library
description: Where to save reusable AI prompts in Obsidian — 2-tier Prompt Library (by-type templates + by-context folders)
metadata: 
  node_type: memory
  type: reference
  originSessionId: bea2c19a-c41d-476d-9cd0-eeffb1abd1b3
---

Prompt Library อยู่ที่ `~/SecondBrain/03 Resources/Prompt Library/`. โครงสร้าง 2 ชั้น:

1. **root (flat files)** — เทมเพลตตามประเภทงาน 30+ อัน (Strategy, Summarize, HR, Finance…) import จาก Apple Notes 2026-02-18. `[[UNIVERSAL MASTER PROMPT]]` = pattern กลาง.
2. **โฟลเดอร์ย่อย = พรอมป์แยกตามบริบท** (Bob สร้างสะสม เพิ่มเรื่อยๆ) — `Marketing/`, `HR/` (ว่าง). แต่ละโฟลเดอร์มี `_index.md`.

**เมื่อผู้ใช้สั่งให้เก็บพรอมป์ใหม่:** วางในโฟลเดอร์บริบทที่ตรงสุด (สร้างใหม่ได้ เช่น Sales/Product/Ops/Finance/Legal) → frontmatter ต้องมี `type: prompt`, `context:`, `use:`, `created:` → เนื้อพรอมป์ใน ``` code fence ``` ให้ copy ทั้งก้อน → อัปเดตลิงก์ใน `_index.md` ของโฟลเดอร์ + บรรทัด "แยกตามบริบท" ใน README.md.

พรอมป์แรกในระบบนี้: `Marketing/KuanGolf — Marketing Plan (SaaS Funnel) Prompt.md` (2026-07-01). ดู [[โปรเจกต์ - Second Brain|project_second_brain]], [[คู่มือ - SecondBrain Resources|reference_secondbrain_resources_hub]], [[KuanGolf — Thunder Solution's golf scoring app|project_kuangolf]].
