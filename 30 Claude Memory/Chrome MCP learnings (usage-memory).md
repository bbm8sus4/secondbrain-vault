---
name: reference-chrome-mcp-learnings
description: Chrome MCP usage-memory — known gotchas + open gaps captured by the self-improvement loop (chrome-learn). Read before non-trivial browser automation. (2026-07-19)
metadata: 
  node_type: memory
  type: reference
  originSessionId: acc70acc-cdbe-4a6b-b204-65ea0e2b3526
---

Usage-memory for Chrome MCP, fed by the `/chrome-mcp-learn` loop + `~/bin/chrome-learn`.
Full log: `~/chrome-mcp-jobs/LEARNINGS.jsonl` · Obsidian mirror: `03 Resources/Tools/Chrome MCP — Learning Log.md`.
Related: [[Chrome MCP CLI + cookbook|reference_chrome_mcp_cli]], [[Chrome MCP doctor + autonomy stack|reference_chrome_mcp_doctor]].

## Known gotchas (แก้แล้ว รู้ทางหนีทีไล่)
- **`chrome_javascript` ตัด output ~10KB** → ส่ง `maxOutputBytes` (observe ตั้ง 200000). อาการ: JSON ขาด "Unterminated string".
- **extension รับเฉพาะ http/https** ไม่รับ `file://` / `data:` URL (navigate = "Invalid url pattern"). เทสต์หน้า controlled ใช้ https จริง (เช่น httpbin.org/forms/post).
- **`chrome_userscript` create/enable ต้องเปิด toggle "Allow user scripts"** ที่ chrome://extensions → Details ก่อน ไม่งั้น error "Cannot read properties of undefined (reading 'indexOf')". list/get/rm ใช้ได้เสมอ.
- **`chrome_javascript` await Promise + async/await ได้** → actionability polling ทำใน 1 call.
- **skill ที่เพิ่งสร้าง mid-session เรียกผ่าน Skill tool ไม่ได้จน session ใหม่** (registration ตอนเปิด session) → รัน protocol manual + `chrome-learn` ได้เลยไม่ต้องรอ.
- **`chrome extract --schema` ดึง meta/og/SEO tags ได้** (อ่าน `content` attr) → verified: title/og:title/description/og:image. เป็น recipe C8 ใน [[/chrome-usecases]].

## Open gaps
(ว่าง — 2 gap เดิมแก้แล้ว 2026-07-19 ↓)

## Gaps ที่แก้แล้ว (RESOLVED)
- **~~12307 (โปรไฟล์ 2) ไม่มี extension~~** → RESOLVED โดยเลี่ยง: authz/BFLA test ไม่ต้องใช้ 2 profile จริง. เพิ่ม `chrome fetch --headers '{"Authorization":".."}'` → replay endpoint ด้วย token/cookie คนละตัวใน profile เดียว (recipe A9 เขียนใหม่). *Dual live-UI session จริงยังต้อง load extension + ตั้งพอร์ต 12307 ในป๊อปอัพ (ขั้นตอน GUI manual, ทำเมื่อจำเป็นจริง) — แต่ API-authz ครบแล้วไม่ต้อง setup.*
- **~~Master Dashboard ย้าย URL~~** → RESOLVED: `master_dashboard_pull.py` มี `detect_origin()` auto-detect จาก tab ที่เปิด (env `MD_DASHBOARD_URL` > tab title "Thunder Group"/"master-dashboard" > fallback jetder.com). URL เปลี่ยนอีกก็หาเจอเอง ไม่ hardcode. ปัจจุบัน `master-dashboard-1188573204505198593.cluster-1.jetder.com` (ไม่ใช่ vercel แล้ว).

## How the loop works
`/chrome-mcp-learn` skill = protocol: หลังงาน browser ที่ไม่ trivial → `chrome-learn win|recipe|gotcha|gap`. recipe ที่ reusable → เขียนเข้า `/chrome-usecases` (skill โตเอง). gap → บันทึกที่นี่ + Obsidian ก่อนปล่อย (ห้าม silently ยอมแพ้). อัปเดตไฟล์นี้เมื่อมี gotcha/gap ใหม่หรือ gap ถูกแก้.
