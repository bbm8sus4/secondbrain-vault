---
name: reference-chrome-mcp-cli
description: "`~/bin/chrome` CLI + chrome-mcp-cookbook skill — drive Chrome from any shell, 27-tool capability map, API-sniff/replay playbook (2026-07-18)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: acc70acc-cdbe-4a6b-b204-65ea0e2b3526
---

Capability layer on top of Chrome MCP (built 2026-07-18, รอบ "ทำให้กว้าง+ฉลาดกว่านี้"). ต่อยอดจาก [[Chrome MCP doctor + autonomy stack|reference-chrome-mcp-doctor]].

## `~/bin/chrome` — ergonomic CLI
ขับ Chrome จาก **shell ไหนก็ได้** (cron/script/ccgram/terminal) ไม่ต้องมี Claude session. verbs บนชั้น JSON-RPC เดิม, auto-heal พอร์ตก่อนเรียก.
- verbs: `tabs js text html read shot fill click key console capture fetch history download perf gif dialog tabs tools raw`
- `chrome help` = verb list เต็ม, `chrome tools` = raw tool signatures
- 2nd profile: `chrome --port 12307` หรือ `CHROME_MCP_PORT=12307`
- **ไม่แตะ `mcp-chrome-curl.py`** (skills พึ่งพา) — เพิ่มชั้นบน ไม่ทับของเดิม
- ตัวแรงที่เพิ่งปลดล็อก (มี 27 tools แต่เคยใช้ไม่ถึงครึ่ง):
  - `chrome capture <id> --secs N` = ดัก XHR/fetch + response body → RE เว็บ
  - `chrome fetch <url> --method POST --body '{}'` = ยิง HTTP **ผ่าน browser → ใช้ cookie ที่ login ค้าง** (ทดสอบแล้ว status 200). ไม่ต้อง juggle token.
  - `chrome perf` = Core Web Vitals, `chrome console --errors` = debug web app, `chrome history/download/gif`

## Playbook: RE เว็บ private API (ethical scope)
1. `chrome tabs` → tab id, login ปกติ
2. `chrome capture <id> --secs 15` → กดฟีเจอร์ที่อยากเข้าใจ
3. อ่าน request ที่ดักได้: endpoint, headers, payload, response
4. `chrome fetch <endpoint> --method POST --body '<json>'` replay ด้วย session cookies → loop จาก shell ได้เลย

## Skill: `/chrome-mcp-cookbook`
`~/.claude/skills/chrome-mcp-cookbook/SKILL.md` — capability map 27 tools + dialog trap (arm ก่อน trigger) + สูตรเว็บที่พิสูจน์แล้ว (Sheets pbcopy+Cmd+V, Docs, claude.ai ProseMirror, LINE OA, Telegram) ลิงก์ไป memory ที่เกี่ยว. ลงทะเบียน trigger ใน CLAUDE.md ทั้ง 2 (warp + .claude). **ให้ consult ทุกครั้งที่ทำ browser automation ที่ไม่ trivial.**

## Permissions
allow `chrome:*` + curl helper + doctor ครบ 4 harness → zero prompt.

## Upstream
`git remote add upstream hangwin/mcp-chrome` แล้ว fetch: **0 commit behind** — fork itorz7 ไม่ตกรุ่น (2026-07-18).
