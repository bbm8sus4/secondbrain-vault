---
title: Caveman Prompting — ตอบห้วนแบบมนุษย์ถ้ำ ประหยัด token
type: reference
context: prompt-technique
tags: [prompt-library, prompt-engineering, technique, token-saving, claude-code]
use: ลด output token 60-75% โดยสั่งให้ AI ตอบสั้น ห้วน ตัด fluff — เหมาะงาน coding/technical
created: 2026-07-03
source_reddit: https://www.reddit.com/r/ClaudeAI/comments/1sble09/
source_repo: https://github.com/JuliusBrussee/caveman
source_gist: https://gist.github.com/chkp-roniz/79518f458cd9c8399e05a4bcb732c1c7
---

# Caveman Prompting

เทคนิค viral (จาก Reddit r/ClaudeAI, 10k votes) — สั่งให้ AI ตอบแบบ "มนุษย์ถ้ำ": สั้น ห้วน ตัดคำเชื่อม/คำสุภาพ/คำเกริ่น เหลือแต่เนื้อ **ลด output token ~60-75%** โดยคุณภาพงาน coding/technical ไม่ตก

## ทำไมเวิร์ก
- LLM คิดค่าเงินเป็น **token** — ทุกคำ filler = เงินจริง + เวลา
- caveman ไม่ได้ทำโมเดลโง่ลง — สมองเท่าเดิม แค่ **บีบวิธีพูด** (ตัด article/pronoun/คำเชื่อม เก็บ noun/verb/ตัวเลข/technical term)
- ได้ผลดีกับงานมี structure (code review, debug, สรุป) · งานเขียนเชิงบรรยายอาจไม่เหมาะ

## ตัวอย่าง
- ปกติ: "The reason your React component is re-rendering is likely because you're creating a new object reference on each render…"
- caveman: **"New object ref each render. Inline object prop = new ref = re-render. Fix: useMemo."**

## ข้อควรรู้
- ลดแค่ **output token** — ไม่ได้ลด input (ไฟล์/ประวัติแชทที่โมเดลอ่าน ซึ่งมักแพงกว่า)
- อยากได้รายละเอียดเมื่อไหร่ สั่ง "อธิบายเต็ม" ได้ตลอด

---

## วิธีใช้กับ Claude Code (ติดตั้งแล้ว)

ติดตั้ง output-style ไว้ที่ `~/.claude/output-styles/caveman.md` (+ warp/ghostty/cmux) แล้ว
เปิดใช้: พิมพ์ `/output-style Caveman` · ปิด: `/output-style default`

### output-style เต็ม (verbatim)

```markdown
---
name: Caveman
description: Few words, do trick
keep-coding-instructions: true
---

Respond with the minimum text needed.

Rules:
- Prefer action over explanation
- Use short sentences
- No motivational filler
- No step-by-step reasoning unless asked
- No long summaries
- When possible, return only:
  1. finding
  2. fix
  3. next step
- For code tasks, keep prose under 5 lines unless I ask for detail
- If a command output is noisy, summarize it in 1-3 bullets
- If confidence is high, state the answer directly
- Do not restate my request
```

## พรอมป์แบบแปะเอง (ChatGPT/Claude/Gemini ทั่วไป)

```
Respond terse like smart caveman. All technical substance stay. Only fluff die.
Drop: articles (a/an/the), filler (just/really/basically/actually), pleasantries, hedging.
Keep: fragments OK, short synonyms, technical terms + code blocks + errors quoted exactly.
```

---

## Repo/แหล่งที่เกี่ยว
- [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) ★~560 — Claude Code skill ตัวเต็ม (รองรับ Cursor/Windsurf/Copilot 40+ agents)
- [chkp-roniz gist](https://gist.github.com/chkp-roniz/79518f458cd9c8399e05a4bcb732c1c7) — output-style ที่ติดตั้งไว้นี้
