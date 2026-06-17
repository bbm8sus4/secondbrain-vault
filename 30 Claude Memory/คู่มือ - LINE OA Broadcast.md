---
name: LINE OA broadcast skill (/lineoa-chat-mcp)
description: Per-chat bulk send on chat.line.biz via Chrome MCP. Trigger /lineoa-chat-mcp. Built from real EasyBot Affiliate broadcast 2026-05-06.
type: reference
originSessionId: a2b93822-ce43-4cac-833f-1424d5b6187d
---
`/lineoa-chat-mcp` — bulk broadcast text + image to LINE OA chats one-by-one via Chrome MCP at chat.line.biz.

**Skill location:** `~/.claude/skills/lineoa-chat-mcp/SKILL.md`

**When to use:** Want to send the SAME message to a SUBSET of OA chats (e.g. all `MS-` prefixed) that LINE OA's native broadcast can't filter. Each message lands in the individual chat thread (looks "personal"), not as a Broadcast tag.

**Built from incident:** EasyBot Affiliate broadcast on 2026-05-06 — sent 250/1245 chats before user said หยุด. Hard-won knowledge encoded in the skill:
- TEXTAREA-EX shadow DOM + Enter keydown is the only working text-send path
- `vm._events.selectFiles[0].fn.fns([file])` is the only working image-send entry (synthetic change/drop/paste all blocked)
- Manual chat mode (`canSendMessageFromCurrentChat`) gate must be opened per chat
- ~10s/chat is the safe pace — at 7.5s duplicates appeared
- Tab can die mid-loop → snapshot to disk every batch + scan chatlist preview on resume

**Broadcast logs persist at:** `~/.claude/projects/-Users-aexgee/broadcast/sent.log` (cumulative, append-only across sessions)
