---
name: reference-claude-code-multiagent
description: "Claude Code multi-agent guide — 5 วิธี (split pane, subagent, cmux, maw, workflow) + workflow script patterns + demo results"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 482646fd-28d4-44c5-b571-13e374d06885
---

Multi-agent workflow guide สำหรับ Claude Code อยู่ที่ `~/SecondBrain/03 Resources/AI Workshops/Claude Code Multi-Agent Workflow Guide.md`

ครอบคลุม 5 วิธี:
1. Warp Split Pane (`claude -p`)
2. Subagent (Agent tool ภายใน session)
3. cmux teams (user ไม่ใช้แล้ว)
4. maw (`maw --task "..."`)
5. Workflow (`"use a workflow"` / `"ultracode"`)

รวม workflow script ตัวอย่าง, hooks (agent/parallel/pipeline/phase/log), quality patterns (adversarial verify, judge panel, loop-until-dry), ผลจริงจาก demo review Friday Bot 2026-07-10.
