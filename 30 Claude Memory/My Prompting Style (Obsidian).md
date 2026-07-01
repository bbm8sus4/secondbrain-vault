---
name: reference-my-prompting-style
description: "User's own prompting behavior study — 901 real prompts across 126 sessions. Full analysis in Obsidian \"02 Areas/My Prompting Style/\". Pointer only."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 03af5f4c-146b-4dbf-9239-82adab903b56
---

Behavioral study ของ prompting style ของ user เก็บใน Obsidian ที่ `~/SecondBrain/02 Areas/My Prompting Style/`:

- `หน้าหลัก.md` — index + key stats
- `behavioral-profile.md` — persona, tone escalation, cognitive style
- `prompt-patterns.md` — 10 recurring patterns พร้อมตัวอย่างจริง
- `_all-prompts-raw.md` — dump ทั้ง 901 prompts เรียง chronological

**Extracted 2026-07-01** จาก JSONL sessions ใน `~/.claude-warp/projects/-Users-aexgee/*.jsonl` (126 files).

**Key insights ที่ควรจำ (ใช้ทุก session):**
- 69% prompts สั้นกว่า 50 chars → ตอบสั้น ๆ ตามกัน
- Signature workflow = `aidebate <topic>` (56 ครั้ง)
- Status-check spam → ตอบ 1 บรรทัด "เสร็จแล้ว [ลิงก์]"
- Silent-continue → ทำต่อทันที ห้ามถามซ้ำ
- Path-drop + "เห็นอะไร" → อ่าน + สรุปทันที
- โมโหใช้ "กู/มึง" (33x) → ตอบ "ครับ/คุณ" ห้าม mirror

**Refresh cadence:** re-extract ทุก 2-3 เดือน เมื่อ session ใหม่สะสม (script อยู่ใน [[_all-prompts-raw]] header)

related: [[กติกา - น้ำเสียงสุภาพ|feedback_tone]] [[กติกา - คำสั่งเปิดโปรเจกต์|feedback_open_command]] [[คู่มือ - AI Debate|reference_ai_debate_harness]] [[กติกา - โหมดแฮกเกอร์|feedback_vibe_hacker_mode]]
