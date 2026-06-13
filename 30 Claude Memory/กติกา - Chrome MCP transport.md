---
name: feedback-chrome-mcp-transport
description: "Chrome MCP transport: type:http is correct config, mcp-remote also works but may fail to connect. Direct HTTP curl fallback available."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5c47d6f1-f223-4181-9434-93678a86a05b
---

Chrome MCP config in `~/.claude/settings.json` — **use `type: "http"`** (switched back 2026-05-24).

**History:** mcp-remote proxy was used 2026-05-20 → 2026-05-24 but also failed to connect (server listed in config but Claude Code didn't register it at startup). Switched back to `type: "http"` per Chrome MCP extension's own recommended config.

**Why:** Both transports can silently fail if Claude Code doesn't connect at startup. The real fix is the **direct HTTP curl fallback** — call Chrome MCP tools via raw HTTP from Bash, bypassing Claude Code's MCP client entirely.

**Current config (2026-05-24):**
```json
"chrome-mcp": {
  "type": "http",
  "url": "http://127.0.0.1:12306/mcp"
}
```

**How to apply — direct HTTP fallback when MCP tools don't load:**
```bash
# 1. Initialize session
SESSION=$(curl -s -i -X POST http://127.0.0.1:12306/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"claude-direct","version":"1.0"}}}' | grep mcp-session-id | cut -d' ' -f2 | tr -d '\r')

# 2. Send initialized notification
curl -s -X POST http://127.0.0.1:12306/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}'

# 3. Call any tool (e.g. screenshot)
curl -s -X POST http://127.0.0.1:12306/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"chrome_screenshot","arguments":{"tabId":TAB_ID}}}'
```

**Key tools:** get_windows_and_tabs, chrome_navigate, chrome_screenshot, chrome_read_page, chrome_javascript, chrome_click_element, chrome_fill_or_select, chrome_keyboard

**Checklist if broken:** (1) Chrome open with MCP extension, (2) native server running on port 12306 (`lsof -i :12306`), (3) screenshots save to ~/Downloads/

**Multi-profile — run SEVERAL Chrome accounts at once (verified 2026-06-04):** Each Chrome profile loads its own copy of the extension and runs its own native-host node process. They fight over a single port by default → only one shows "Service Running". Fix: in each profile's extension popup set a DIFFERENT **Connection Port** (12306, 12307, …), then add one `mcpServers` entry per port in `~/.claude.json` (`chrome-mcp`→12306, `chrome-mcp-kuan`→12307, …). Restart Claude Code to load new entries, or just use the direct-HTTP curl flow above (works immediately, no restart). Proven: bobbysomporn @12306 + KUAN GOLF (hello.kuangolf) @12307 driven simultaneously & independently (opened YouTube on both, neither disturbed the other).

**Installing the extension in a new profile:** manifest has NO `key` → extension ID = hash of the unpacked folder PATH. So load-unpacked the SAME folder in each profile to reuse one ID, OR load from a new folder and add that folder's computed ID to `~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.chromemcp.nativehost.json` `allowed_origins`. Working source: `~/mcp-chrome/app/chrome-extension/.output/chrome-mv3` (ID `nckehcmgbblnmibclnnongjamneibjjj`); visible Desktop copy `~/Desktop/ChromeMCP-Extension` (ID `eofkmabjglagcipljdminponlcfmldjk`, already registered). `.output` is hidden → in Load-unpacked dialog use Cmd+Shift+G + paste path. After editing the host manifest, fully quit Chrome (Cmd+Q) and reopen. Compute an unpacked ID: `sha256(path)` first 32 hex nibbles mapped 0→a…f→p.

Related: [[reference_chrome_mcp_gdocs]]
