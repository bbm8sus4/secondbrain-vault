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

**Persistent helper (2026-07-18):** reusable driver saved at `~/bin/mcp-chrome-curl.py` — handles initialize+initialized handshake + SSE parsing. Usage: `python3 ~/bin/mcp-chrome-curl.py --list` · `... get_windows_and_tabs '{}'` · `... chrome_javascript '{"tabId":N,"code":"..."}'` · `MCP_PORT=12307 ...` for 2nd profile. Use Python not raw bash — response is SSE (`data: {json}`) needing session-id header continuity.

**Root cause seen 2026-07-18 — tools not loaded despite correct config:** `chrome-mcp` was in `~/.claude-warp/settings.json` mcpServers, but the **session started (16:01) BEFORE settings.json was saved (16:14)** → server never registered. Diagnosis: `list_connected_browsers`=[] (that's the *other* extension, `claude-in-chrome`) + `ToolSearch chrome_navigate`=none. **Don't restart — use the curl fallback immediately** (service already up: `lsof -nP -iTCP:12306 -sTCP:LISTEN`). Note: `claude-in-chrome` (official Anthropic ext, needs claude.ai/chrome install) ≠ `mcp-chrome` (self-built, port 12306) — different products.

**Driving claude.ai (design/chat) gotchas (verified 2026-07-18, created HR doc in claude.ai/design):** input box is **contenteditable (ProseMirror), NOT textarea** → `chrome_fill_or_select` fails ("not a fillable element"). Fix: `chrome_javascript` → focus el, `document.execCommand('insertText',false,text)` (fires React/ProseMirror events); long/Thai text → base64 in Python, `atob`+`TextDecoder` in JS to dodge escaping. Don't type newlines via chrome_keyboard in a chat box (Enter submits). Get element refs via `chrome_read_page {filter:"interactive"}` (returns ref_N + coords); refs stay valid across curl calls (server-side ref map per tab). Confirm success via `location.href` (design done → URL `/design/p/<uuid>`). savePng screenshots often unfindable → prefer read_page refs over vision.

Full human-facing how-to in Obsidian: `03 Resources/Tools/Chrome MCP — curl fallback + ขับ claude.ai (วิธีแก้ tools ไม่โหลด).md`

Related: [[คู่มือ - Chrome MCP กับ Google Docs|reference_chrome_mcp_gdocs]]
