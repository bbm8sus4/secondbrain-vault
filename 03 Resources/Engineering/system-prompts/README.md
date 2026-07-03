---
title: System Prompts (verbatim) — Claude Code
type: reference
tags: [engineering, prompt-engineering, system-prompt, claude-code, verbatim]
saved: 2026-07-03
source_repo: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
source_path: Anthropic/Claude Code*
---

# System Prompts (verbatim)

เก็บ system prompt จริงของเครื่องมือ AI ดัง ๆ แบบ **verbatim** (raw จาก repo) ไว้ศึกษา prompt engineering ระดับโปร

## Claude Code (Anthropic)

ดึงจาก [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) โฟลเดอร์ `Anthropic/` เมื่อ 2026-07-03

| ไฟล์ | ขนาด | คืออะไร |
|---|---|---|
| `Claude Code - Prompt (clean).txt` | 13 KB | **system prompt หลัก แบบสะอาด** — เริ่มที่นี่ อ่านง่ายสุด |
| `Claude Code - Tools.json` | 49 KB | **tool schemas** ทั้งหมด (Bash, Edit, Read, WebFetch ฯลฯ) เป็น JSON draft-07 valid |
| `Claude Code 2.0 - system prompt.txt` | 57 KB | ชุดเต็ม v2.0.0 (2025-09-29) — system-reminder + ตัวอย่าง convo + tools รวมในไฟล์เดียว |

### จุดน่าเรียนรู้ (จาก Prompt สะอาด)
- ขึ้นต้นบอก identity + จุดยืน security ("defensive security tasks only") ชัดเจนตั้งแต่บรรทัดแรก
- กติกาแข็ง ๆ ใช้ **IMPORTANT:** นำหน้า (NEVER guess URLs, refuse malicious)
- ให้ self-reference ผ่าน WebFetch เอกสารจริง แทนการเดา
- แยกกฎเป็นหมวด: tone, proactiveness, conventions, tool use, task management

---

*กติกา: ดึง verbatim ด้วย `curl` จาก raw.githubusercontent.com เท่านั้น (WebFetch สรุปทิ้ง). อยากได้ของเครื่องมืออื่น (Cursor, Windsurf, v0…) อยู่ folder อื่นใน repo เดียวกัน — บอกชื่อได้เลย.*
