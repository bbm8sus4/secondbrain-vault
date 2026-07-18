---
name: reference-chrome-mcp-doctor
description: "chrome-mcp-doctor — auto-heal + statusline + PreToolUse hook + perms, ครบทุก harness (2026-07-18)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: acc70acc-cdbe-4a6b-b204-65ea0e2b3526
---

Chrome MCP autonomy stack (built 2026-07-18), goal = เต็มสปีด ไม่ต้อง babysit:

- **`~/bin/chrome-mcp-doctor`** — health check + auto-heal. `--status` (check only), no args (heal: เปิด Chrome โปรไฟล์ที่ map ไว้ แล้วรอพอร์ตขึ้น ≤30s), `--hook` (PreToolUse mode, exit 0 เสมอ ไม่ block).
- **Port→profile map**: `~/.config/chrome-mcp/doctor.conf` → `12306=Profile 1` (โปรไฟล์ "A"). 12307 (kuan) ยัง comment ไว้ — **ไม่มีโปรไฟล์ไหนลง extension จริง** ณ วันสร้าง; ติดตั้งเมื่อไหร่ค่อยเปิดบรรทัดใน conf.
- **Statusline row 6**: `⚙ Chrome MCP 12306 ✓/✗` ใน `~/.claude/statusline.sh` (ทุก harness ใช้ไฟล์เดียวกัน) — อ่านพอร์ตจาก doctor.conf.
- **PreToolUse hook** (ทั้ง 4 harness): matcher `mcp__chrome-mcp.*` → doctor --hook → พอร์ตตาย = เปิด Chrome ให้เองก่อน tool call วิ่ง.
- **Permissions allow** (ทั้ง 4 harness): `mcp__chrome-mcp`, `mcp__chrome-mcp-kuan`, curl helper, doctor — ไม่มี prompt.
- **MCP registration synced**: chrome-mcp + chrome-mcp-kuan อยู่ครบใน `~/.claude.json`, `.claude-warp/.claude.json`, `.claude-ghostty/.claude.json`, `.claude-cmux/.claude.json` → ปัญหา "tools not loaded" หมดไปสำหรับ session ใหม่ (session เก่ายังใช้ curl fallback ตาม [[กติกา - Chrome MCP transport|feedback-chrome-mcp-transport]]).
- Fork `itorz7/mcp-chrome` มี auto-connect on browser startup + keepalive + reconnect ในตัวแล้ว — extension ต่อเองเสมอ ไม่ต้องกด Connect.
- Backups ทุกไฟล์: `*.bak-chromemcp` (รวม `statusline.sh.bak-chromemcp`). **เวอร์ชั่นเก่า + คำสั่ง rollback ทั้งชุด** อยู่ใน Obsidian: `03 Resources/Tools/Chrome MCP — doctor autonomy stack + rollback (2026-07-18).md` (cmux `.claude.json` เป็นไฟล์สร้างใหม่ — rollback = ลบ).
- **ตั้งใจไม่ทำ** (คำสั่งผู้ใช้ 2026-07-18: เต็มที่/เร็ว/อิสระ ห้ามแย่ลง): ไม่เพิ่ม auth token บน native server (เพิ่ม friction), ไม่มี watchdog เปิด Chrome เองแบบ background (น่ารำคาญ) — ใช้ lazy heal ผ่าน hook แทน.
