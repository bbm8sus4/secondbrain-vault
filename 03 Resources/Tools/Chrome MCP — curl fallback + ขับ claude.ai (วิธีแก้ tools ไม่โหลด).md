---
title: "Chrome MCP — curl fallback + ขับ claude.ai"
type: reference
tags: [tool, chrome-mcp, troubleshooting, automation]
created: 2026-07-18
status: live
---

# Chrome MCP — curl fallback (วิธีแก้ตอน tools ไม่โหลด)

> ปัญหาที่เจอบ่อย: อยากให้ Claude ขับ Chrome ผ่าน mcp-chrome (port 12306) แต่ **tool `mcp__chrome-mcp__*` ไม่โผล่** ในเซสชัน → ขับไม่ได้
> **วิธีแก้ที่ใช้ได้เสมอ:** ยิง **curl/HTTP ตรงเข้า MCP endpoint** `http://127.0.0.1:12306/mcp` ผ่าน Bash — bypass ตัว MCP client ของ Claude Code ไปเลย **ไม่ต้อง restart**

## ทำไม tool ถึงไม่โหลด (root cause ที่เจอ 2026-07-18)
- `chrome-mcp` อยู่ใน config ถูกต้องแล้ว (`~/.claude-warp/settings.json` → `mcpServers.chrome-mcp` type http url 12306)
- แต่ **เซสชันเปิดก่อนที่ config จะถูกเซฟ** (เซสชันเปิด 16:01, settings.json แก้ 16:14) → เซสชันนั้นไม่เคยโหลด server
- เช็ค: `list_connected_browsers` ของ `claude-in-chrome` = ว่าง (คนละ extension), `ToolSearch chrome_navigate` = ไม่เจอ → ยืนยันว่าไม่ได้โหลด
- **อย่าเสียเวลา restart** — ใช้ curl fallback ได้เลย (service รันอยู่แล้ว เช็คด้วย `lsof -nP -iTCP:12306 -sTCP:LISTEN`)

> หมายเหตุ: `claude-in-chrome` (extension ทางการ Anthropic) กับ `mcp-chrome` (self-built port 12306) เป็น **คนละตัว** — tool `mcp__claude-in-chrome__*` ต่อกับตัวทางการที่ต้องติดตั้งจาก claude.ai/chrome, ส่วนตัว 12306 ต้องยิง HTTP ตรง

## เครื่องมือถาวร: `~/bin/mcp-chrome-curl.py`
Helper จัดการ handshake (initialize + notifications/initialized) + parse SSE ให้ครบ:
```bash
python3 ~/bin/mcp-chrome-curl.py --list                          # ดู tool ทั้งหมด
python3 ~/bin/mcp-chrome-curl.py get_windows_and_tabs '{}'       # หา tab
python3 ~/bin/mcp-chrome-curl.py chrome_switch_tab '{"tabId":123}'
python3 ~/bin/mcp-chrome-curl.py chrome_javascript '{"tabId":123,"code":"return document.title"}'
MCP_PORT=12307 python3 ~/bin/mcp-chrome-curl.py --list           # โปรไฟล์ Chrome ที่ 2
```
> ทำไมใช้ Python ไม่ใช่ bash curl ล้วน: response เป็น **SSE** (`data: {json}`) + ต้องส่ง `Mcp-Session-Id` header ต่อเนื่อง — bash parse ยุ่ง, Python จบใน script เดียว

## Flow ขับหน้าเว็บ (ที่ใช้จริงกับ claude.ai/design)
1. `get_windows_and_tabs` → หา tabId ของ tab เป้าหมาย
2. `chrome_switch_tab {tabId}` → โฟกัส
3. `chrome_read_page {tabId, filter:"interactive"}` → ได้ ref ของ element (เช่น `ref_5` ช่องพิมพ์, `ref_11` ปุ่ม)
4. ใส่ข้อความ + กดปุ่ม → ดู gotcha ด้านล่าง

## Gotchas สำคัญ
- **ช่องพิมพ์ของ claude.ai เป็น contenteditable (ProseMirror) ไม่ใช่ textarea** → `chrome_fill_or_select` **ใช้ไม่ได้** ("not a fillable element")
  - วิธีที่ได้ผล: `chrome_javascript` → focus element แล้ว `document.execCommand('insertText', false, text)` (trigger event ให้ React/ProseMirror รับรู้). ข้อความยาว/ไทย: base64-encode ใน Python แล้ว `atob`+`TextDecoder` ใน JS กัน escape พัง
- **อย่าพิมพ์ newline ด้วย chrome_keyboard ในช่อง chat** — Enter = ส่งฟอร์ม (ควรใช้ insertText ทีเดียวจบ)
- กดปุ่มส่ง: `chrome_click_element {ref:"ref_11", tabId}` (ref จาก read_page ล่าสุด — ยัง valid ข้าม MCP session เพราะ ref map เก็บ server-side ต่อ tab)
- ยืนยันผล: `chrome_javascript` อ่าน `location.href` / `document.title` (design สำเร็จ = URL เปลี่ยนเป็น `/design/p/<uuid>`)
- screenshot `savePng` หาไฟล์ไม่เจอบ่อย → ใช้ `chrome_read_page filter:interactive` หา ref แทนการดูภาพ เชื่อถือกว่า

## เช็คลิสต์ถ้าพัง
1. Chrome เปิด + extension mcp-chrome ทำงาน (popup ขึ้น "Service Running")
2. port ฟังอยู่: `lsof -nP -iTCP:12306 -sTCP:LISTEN`
3. curl init ตอบ (400 กับ payload มั่ว = service เป็น, แค่ต้อง handshake ให้ถูก)

Related: memory `feedback_chrome_mcp_transport` · [[reference_chrome_mcp_gdocs]] · skill `Chrome-MCP-Owly`
