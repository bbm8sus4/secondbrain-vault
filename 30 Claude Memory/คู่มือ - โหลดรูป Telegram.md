---
name: reference-telegram-download-pic-block
description: Skill for downloading photos from content-protected Telegram channels via Chrome MCP. Uses blob-fetch + canvas re-encode + anchor-click pipeline.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 5eb2b5d2-234c-4060-ad10-9dc3a02ec7d2
---

Skill `/telegram-download-pic-block` at `~/.claude/skills/telegram-download-pic-block/SKILL.md`.

Trigger: `/telegram-download-pic-block` then provide Telegram Web URL + folder name.

**Pipeline:** Telegram viewer → fetch blob → open in new tab → canvas drawImage → toBlob JPEG 95% → anchor.click download → close tab → ArrowRight → repeat.

**Key lessons from 2026-05-31 build:**
- `chrome_handle_download` times out on blob URLs — don't use
- Chrome MCP redacts base64 AND hex in JS responses — never try to extract binary data
- Tab-confusion bug: close other tabs or always `chrome_navigate` before `chrome_javascript`
- Chrome temp files (`.com.google.Chrome.*`) = stalled downloads, just `cp` them
- ~9 seconds per photo when scripted

Related: [[กติกา - Chrome MCP transport|feedback_chrome_mcp_transport]]
