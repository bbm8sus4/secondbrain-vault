---
name: reference_chrome_mcp_sheets
description: Chrome MCP × Google Sheets — how to create/populate a Sheet reliably (and the traps)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4c412e2e-06f8-4f1b-826f-72e3e4cae1d3
---

ขับ Google Sheets ผ่าน Chrome MCP (port 12306, curl fallback ตาม [[กติกา - Chrome MCP transport|feedback_chrome_mcp_transport]]) ได้ แต่มีกับดักเยอะ — สรุปสิ่งที่**เวิร์ก/ไม่เวิร์ก** (เรียนรู้ 2026-06-08):

**สร้างชีตใหม่:** `chrome_navigate` → `https://sheets.new` (สร้างในบัญชีที่ login ใน Chrome นั้น = ของผู้ใช้เอง private ตั้งแต่ต้น). ได้ tabId กลับมา. URL จริงดูได้จาก `chrome_javascript` return `location.href` (harness อาจ redact base64 id ใน output แต่เห็นใน screenshot ได้).

**วางข้อมูลลง grid — วิธีที่เวิร์กจริง (สำคัญสุด):**
1. `pbcopy` ตั้ง clipboard ระบบโดยตรงจาก Bash (เชื่อถือได้ 100% ไม่ต้องพึ่ง browser focus) — ใส่ TSV (tab=คอลัมน์, \n=แถว)
2. `chrome_switch_tab` เอาแท็บชีตขึ้นหน้า + `osascript activate Chrome` (ต้อง foreground จริง)
3. `chrome_click_element` ด้วย **coordinates** (เช่น A1 ~ x40,y150) เพื่อ focus cell จริง
4. `osascript -e 'tell application "System Events" to keystroke "v" using command down'` = **Cmd+V จริงระดับ OS** → paste ลง grid สำเร็จ

**สิ่งที่ไม่เวิร์ก (อย่าทำ):**
- `document.execCommand('copy')` ใน CDP → คืน false (ถูกบล็อก)
- `navigator.clipboard.writeText` → ได้เฉพาะตอน document focused จริง (flaky)
- CDP `chrome_keyboard` ส่ง "Meta+v"/"Ctrl+v" → **ไม่ trigger native paste** (แค่ simulate key event เฉยๆ)
- `chrome_keyboard` พิมพ์ข้อความบางตัว → "Some keyboard events failed" (text input ไม่เสถียร)
- **rename ไฟล์/แท็บ ด้วย click element + osascript Cmd+A/Cmd+V = อันตราย!** Google Sheets ดักจับ Cmd+A (เลือกทั้งชีต) + Cmd+V (วางทับ) ไปที่ **grid** แม้คลิกที่ title/tab → **ทับข้อมูล A1**. กู้ด้วย `osascript Cmd+Z` ทีละครั้งจนค่ากลับมา (เช็ก A1 ผ่าน formula bar `#t-formula-bar-input`).

**หา coords แม่นยำ:** `chrome_javascript` คืน `getBoundingClientRect()` center ของ element (coords เดียวกับ CDP click) — แต่จำไว้ว่า rename ยังเสี่ยงเพราะ Sheets ดัก key. ชื่อไฟล์/แท็บเป็นแค่ความสวยงาม (Apps Script ผูกชีตด้วย ID/อ่าน sheet แรกได้) — ไม่ต้องฝืน rename ผ่าน automation ให้ผู้ใช้ทำเอง 5 วิ.

**อ่านค่า cell:** Sheets เป็น canvas อ่าน cell ผ่าน DOM ไม่ได้ตรงๆ — เลือก cell แล้วอ่าน formula bar `#t-formula-bar-input`. Name box = `#t-name-box`.

เกี่ยวข้อง: [[คู่มือ - Chrome MCP กับ Google Docs|reference_chrome_mcp_gdocs]] · [[โปรเจกต์ - Dashboard รายจ่าย|project_expense_dashboard]] · [[กติกา - Chrome MCP transport|feedback_chrome_mcp_transport]]
