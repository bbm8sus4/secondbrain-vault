---
title: Claude Code Multi-Agent Workflow Guide
type: reference
tags: [claude-code, multi-agent, workflow, parallel, tutorial]
saved: 2026-07-11
---

# Claude Code Multi-Agent — 5 วิธีทำงานคู่ขนาน

## 1. Warp Split Pane (ง่ายสุด)

เปิดหลาย pane ใน Warp แล้วสั่งแต่ละตัวทำคนละมุม:

```bash
# pane 1
claude -p "อ่าน ~/my-ai-bot/src/index.js หา 3 bugs"
# pane 2
claude -p "อ่าน ~/my-ai-bot/src/index.js หา 3 security issues"
# pane 3
claude -p "อ่าน ~/my-ai-bot/src/index.js หา 3 performance issues"
```

- `-p` = print mode (ไม่เข้า interactive, พิมพ์ผลแล้วจบ)
- agent แต่ละตัว context แยกกัน คุยกันไม่ได้
- ต้องรวมผลเอง
- เหมาะ: ลองเล่น, งานเบา, อยากดูผลแต่ละตัวแยก

## 2. Subagent ภายใน Claude Code

ไม่ต้องเปิดหลายหน้าต่าง — Claude Code spawn agent ภายในได้:

```
"ช่วย research เรื่อง X แล้วขณะเดียวกันก็แก้ไฟล์ Y ให้ด้วย"
```

Claude ใช้ **Agent tool** สร้าง subagent ทำงานคู่ขนานใน session เดียวกัน ผลรวมกลับมาที่ main context

- เหมาะ: fan-out + รวมผลในที่เดียว

## 3. cmux claude-teams

```bash
cmux claude-teams
```

หลาย tab = หลาย Claude Code instance แยก context กัน แต่ **teammate mode ส่ง message หากันได้** ผ่าน `SendMessage`

- เหมาะ: agent หลายตัวทำคนละส่วนแต่ประสานกัน

## 4. maw (Multi-Agent Orchestrator)

```bash
maw --task "Review ~/my-ai-bot/src/index.js — spawn 3 workers bugs/security/perf แล้วรวม report"
```

สร้าง **oracle** (ผู้สั่งงาน) + **worker agents** อัตโนมัติ ใน tmux sessions

- oracle แจกงาน → workers ทำคู่ขนาน → oracle รวมผล
- เหมาะ: งานใหญ่ decompose หลายส่วน

## 5. Workflow (ภายใน Claude Code — แนะนำ)

พิมพ์ **"use a workflow"** หรือ **"ultracode"** แล้ว Claude orchestrate multi-agent pipeline:

```
"ultracode — review ทุกไฟล์ที่เปลี่ยนใน branch นี้ หา bug + security issue"
```

### ตัวอย่าง Workflow Script

```javascript
export const meta = {
  name: 'demo-review',
  description: 'Multi-agent review across 3 dimensions',
  phases: [
    { title: 'Review', detail: '3 agents review bugs/security/perf in parallel' },
    { title: 'Summarize', detail: 'Synthesize into single report' },
  ],
}

const TARGET = '~/my-ai-bot/src/index.js'

const DIMENSIONS = [
  { key: 'bugs', prompt: `Read ${TARGET} and find top 3 BUGS...` },
  { key: 'security', prompt: `Read ${TARGET} and find top 3 SECURITY issues...` },
  { key: 'performance', prompt: `Read ${TARGET} and find top 3 PERFORMANCE issues...` },
]

phase('Review')
const results = await parallel(
  DIMENSIONS.map(d => () =>
    agent(d.prompt, { label: `review:${d.key}`, phase: 'Review' })
  )
)

phase('Summarize')
const summary = await agent(
  `Synthesize findings: Bugs: ${results[0]} Security: ${results[1]} Perf: ${results[2]}`,
  { label: 'synthesize', phase: 'Summarize' }
)

return summary
```

### Workflow Hooks ที่ใช้ได้

| Hook | หน้าที่ |
|------|--------|
| `agent(prompt, opts)` | spawn subagent |
| `parallel(thunks[])` | รันพร้อมกัน (barrier — รอทุกตัวเสร็จ) |
| `pipeline(items, ...stages)` | รันทีละ stage ต่อเนื่อง ไม่มี barrier |
| `phase(title)` | เริ่ม phase ใหม่ (แสดงใน progress) |
| `log(msg)` | แสดง progress message |

### agent opts

| Option | ค่า |
|--------|-----|
| `label` | ชื่อแสดงใน progress tree |
| `phase` | assign เข้า phase group |
| `schema` | JSON Schema → บังคับ structured output |
| `model` | override model (ปกติไม่ต้องใส่) |
| `effort` | 'low' / 'medium' / 'high' / 'xhigh' / 'max' |
| `isolation: 'worktree'` | แยก git worktree (ใช้เมื่อ agents แก้ไฟล์พร้อมกัน) |

### parallel vs pipeline

- **`parallel()`** = barrier → รอทุกตัวเสร็จก่อนไปต่อ (ใช้เมื่อต้อง merge/dedup ผลรวม)
- **`pipeline()`** = ไม่มี barrier → item A stage 3 ได้ขณะ item B ยัง stage 1 (default ที่ควรใช้)

### Quality Patterns

- **Adversarial verify**: spawn N skeptics ต่อ finding ให้ลอง refute
- **Judge panel**: N approaches → score → synthesize จาก winner
- **Loop-until-dry**: หา issues จนไม่เจอใหม่ K รอบติด
- **Multi-modal sweep**: หลาย agent ค้นคนละวิธี (by-container, by-content, by-entity)

---

## เปรียบเทียบ

| วิธี | Setup | Agent คุยกัน | รวมผลอัตโนมัติ | เหมาะกับ |
|------|-------|-------------|---------------|----------|
| Warp Split | ไม่ต้อง | ไม่ได้ | ต้องทำเอง | ลองเล่น |
| Subagent | ไม่ต้อง | ผ่าน main | ได้ | fan-out ใน session |
| cmux teams | `cmux claude-teams` | ได้ (SendMessage) | ต้องสั่ง | ประสานงาน |
| maw | `maw --task "..."` | ได้ (ผ่าน oracle) | oracle ทำให้ | งานใหญ่ซับซ้อน |
| Workflow | "use a workflow" | ผ่าน script | script จัดการ | review/audit/migration |

---

## ผลจริงจาก Demo (2026-07-10)

Review Friday Bot (`my-ai-bot/src/index.js` ~3,500 บรรทัด) ด้วย workflow 4 agents:
- 3 agents review พร้อมกัน (bugs/security/perf) + 1 agent synthesize
- ใช้เวลา ~3.5 นาที (ถ้าทำทีละตัว = 10+ นาที)
- เจอ 9 issues: 2 Critical, 4 High, 3 Medium
- Critical ที่สำคัญ: Prompt Injection ผ่าน AI Action Tags, Reply fallthrough ไป secretary AI
