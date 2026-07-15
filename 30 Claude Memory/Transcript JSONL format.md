---
name: reference-transcript-jsonl-format
description: "Claude Code transcript JSONL format — type='user' (ไม่ใช่ 'human'), ai-title มี session title, ใช้สำหรับ backfill/analysis"
metadata: 
  node_type: memory
  type: reference
  originSessionId: c43a0a62-0da8-4cce-b114-43e25a68201f
---

# Transcript JSONL Format

Session transcripts อยู่ที่ `~/.claude[-*]/projects/-Users-aexgee/<session-uuid>.jsonl`

## Types ที่พบ

| type | เนื้อหา |
|---|---|
| `user` | ข้อความผู้ใช้ — `message.content` (string หรือ array) |
| `assistant` | ตอบกลับ — `message.content[]` มี `tool_use` items |
| `ai-title` | ชื่อ session — `title` field |
| `system` | system prompt |
| `attachment` | ไฟล์แนบ |
| `last-prompt` | pointer ไป leaf node |
| `mode` | permission mode changes |
| `bridge-session` | MCP session info |

## ข้อควรระวัง

- type คือ `user` **ไม่ใช่** `human` (เคยพลาดทำให้ extract ไม่ออก)
- user message content อาจเป็น string หรือ array of `{type: "text", text: "..."}` objects
- subagent transcripts อยู่ใน `<session-uuid>/subagents/agent-*.jsonl`
- ไฟล์ใหญ่ได้มาก (5,000+ lines) — อย่าอ่านทั้งไฟล์ใน context ให้ extract เฉพาะที่ต้องการ
