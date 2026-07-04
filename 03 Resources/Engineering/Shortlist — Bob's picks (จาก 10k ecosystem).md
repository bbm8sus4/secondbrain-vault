---
title: Shortlist — Bob's picks (จาก Claude Code 10k ecosystem)
type: reference
tags: [engineering, shortlist, claude-code, mcp, skills, selected]
saved: 2026-07-04
note: ดาว (★) = ยืนยันสด GitHub API 2026-07-04 (ไม่ใช่ snapshot dataset) · ทุกตัว active push สัปดาห์นี้
source_dataset: ~/Desktop/Claude Repos/ (10,543 repos)
---

# Shortlist — ตัวที่พี่เลือก (Bob's picks)

5 repo ที่ Bob คัดจาก 10k Claude Code ecosystem (2026-07-04) — ดาวยืนยันสดจาก GitHub แล้ว ของจริงทุกตัว

| repo | ★ (จริง) | คืออะไร | เหมาะกับพี่เพราะ |
|---|---|---|---|
| **[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)** | 39.6k | สอน agent ใช้ Obsidian เป็น (คนทำ = ผู้สร้าง Obsidian) | ทั้งระบบรันบน SecondBrain — ให้ Claude อ่าน/เขียนวอลต์ฉลาดขึ้น ได้ประโยชน์ทบต้น |
| **[langbot-app/LangBot](https://github.com/langbot-app/LangBot)** | 16.6k | แพลตฟอร์มทำ IM bot (LINE/Telegram/Discord) เกรด production | ต่อยอด Friday bot / EasySlip LINE bot |
| **[oraios/serena](https://github.com/oraios/serena)** | 26k | MCP toolkit ค้น/แก้โค้ดเชิงความหมาย (ผ่าน LSP) | เสริม GitNexus/graphify — ทำงานโค้ดแม่นขึ้น |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | 25.6k | MCP index โค้ดทั้ง repo เป็น knowledge | ให้ agent เข้าใจ codebase (my-ai-bot ฯลฯ) เร็วขึ้น |
| **[mattpocock/skills](https://github.com/mattpocock/skills)** | 155.6k | ชุด skill จาก engineer จริง (Matt Pocock) | เอาไว้เป็นแบบเขียน skill เอง + หยิบใช้ได้เลย |

## หมายเหตุการเลือก
- **obsidian-skills + mattpocock/skills** = สาย skill/workflow · เสียบ `~/.claude/skills/` หรือเป็น plugin
- **serena + codebase-memory-mcp** = สาย MCP code intelligence · ทั้งคู่ทับกันบางส่วน (semantic code) — ถ้าจะลองเลือกตัวเดียวก่อน แนะนำ serena (โตกว่า, LSP-based)
- **LangBot** = ตัวใหญ่สุดที่ต้อง self-host — เป็น "อนาคต/reference" มากกว่าเสียบใช้ทันที (Friday เป็น Cloudflare Worker อยู่แล้ว)

## next
เจาะตัวไหนก่อน → เปิด README + เช็คว่าชนกับของที่มี (mcp-obsidian, GitNexus) ไหม + ลองติดตั้ง
