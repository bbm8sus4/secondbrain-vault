# Chrome MCP — capability roadmap (4-agent research 2026-07-18)

รอบที่ 3 ของงาน Chrome MCP. รอบ 1 = เสถียร (doctor/auto-heal), รอบ 2 = capability (chrome CLI + cookbook). รอบนี้ = **วิจัยลึกจาก 4 agent** เพื่อหาว่าจะเก่งกว่านี้ได้อีกยังไง แล้วลงมือ.

วิจัย 4 มุมขนานกัน: (1) เจาะโค้ด mcp-chrome จริง, (2) คู่แข่ง Playwright-MCP/browser-use/Stagehand/Skyvern/Chrome-DevTools-MCP, (3) use case จริง + reliability patterns, (4) งานจริงของ user เอง.

## ค้นพบใหญ่สุด: ของแรงมีอยู่แล้ว แค่ไม่ได้เปิด

**A. Hidden tools — implement เต็ม, callable, ไม่โผล่ใน tools/list** (verify แล้วเรียกได้จริง):
- `search_tabs_content` — semantic vector search ข้ามทุก tab (engine ready)
- `chrome_userscript` — userscript ถาวรแบบ Tampermonkey (ต้องเปิด toggle "Allow user scripts" ใน chrome://extensions ก่อน create)
- `record_replay_flow_run` / `_list_published` — RPA flow engine
- `chrome_inject_script` — persistent page hooks
- flow ที่ publish แล้วโผล่เป็น `flow.<slug>` tool อัตโนมัติ
- **in-browser cron**: flow ตั้งเวลา once/interval/daily ผ่าน chrome.alarms + trigger url/dom (รันเองไม่ต้องมี agent)
- embedded Claude/Codex agent API บนพอร์ต 12306

**B. Infrastructure ที่มีแล้วแต่ไม่ได้ surface** (คู่แข่งเพิ่งเจอ = mcp-chrome อยู่กลุ่มผู้นำแล้ว):
- accessibility-tree snapshot (`chrome_read_page` มี ref_N ids) — primitive เดียวกับ Playwright-MCP/browser-use
- self-healing multi-candidate selector engine (`selector-engine.ts`) — เกรด Stagehand
- record-replay flow engine (if/loop/http/extract/wait) — โมเดลเดียวกับ Skyvern workflow blocks
- CDP session manager, perf/CWV tools, network-capture-with-bodies

## ช่องว่างจริง vs ผู้นำ (= roadmap)

1. **ไม่มี actionability polling ก่อน action** — Playwright รอ visible+stable+enabled+receives-events (hit-test กัน overlay) ก่อนคลิกทุกครั้ง. tool ของเรายิงทันที = flaky. **นี่คือ #1 คุ้มสุด effort ต่ำสุด** — เขียน JS helper inject ISOLATED world poll ก่อน dispatch (ไม่ต้องแก้ server มาก)
2. **ไม่มี NL act/extract/observe** — Stagehand ให้พูด "คลิกปุ่ม sign-in" แล้ว tool resolve เอง. สร้างบน snapshot + selector-engine ที่มีอยู่
3. **extract ไม่มี schema** — ควร Zod/JSON-Schema → constrained output → validate → retry. anti-hallucination: ให้ model คืน ref แล้วอ่าน href จริงเอง
4. **ไม่มี observe→cache→replay self-heal** — cache การ resolve ไว้ replay แบบไม่เรียก LLM, heal เมื่อ DOM drift (Stagehand + Skyvern code-caching) = ประหยัด+deterministic สุด
5. **ไม่มี cron/webhook surface** — flow engine มี schedule แล้วแค่ยังไม่เปิดออกมา; เพิ่ม HMAC-signed webhook on completion

## หลักการ reliability (ทุก unattended job — ทุกแหล่ง converge ตรงกัน)

- **ห้าม sleep/networkidle** → รอ element/text/response เฉพาะ หรือ data-stasis (Set ไม่โต)
- **validate ผลลัพธ์ ไม่ใช่การคลิก** = silent failure #1
- **ดัก JSON/XHR ดีกว่า parse DOM** = เสถียร มี structure ถูกกว่า
- **session หมดอายุเงียบ** = re-auth on 401, keep-warm (live Chrome profile ของเราได้เปรียบ cookie อุ่นฟรี)
- **checkpoint + dedup by id** = snapshot ลง disk, scan already-done ก่อน resume
- **pacing สุ่ม + cap ต่อ domain** = fixed interval คือลายเซ็น bot

## สิ่งที่ build ไปแล้วรอบนี้ (ทำได้จริง verify แล้ว)

ขยาย `~/bin/chrome` — เปิด hidden tools + reliability verbs (ไม่แตะ extension = ไม่มีความเสี่ยง rebuild):
- `chrome search <q>` — semantic tab search
- `chrome userscript ...` — จัดการ userscript (บอกวิธีเปิด toggle เมื่อ API ปิด)
- `chrome flows` / `chrome flow <slug>` — RPA flows
- `chrome wait <id> <text> [--gone]` — รอ text แทน sleep
- `chrome snapshot <id>` — a11y tree + ref ids
- `chrome form <id> '<json>'` — เติมทั้งฟอร์มใน call เดียว
- `chrome console <id> --buffer` — persistent log buffer
- **`chrome kpi <id> '<js>' --state F --notify CMD`** — ตรวจการเปลี่ยนแปลง cron ได้ (baseline→unchanged→changed+notify, exit 10). ตัวนี้ตอบโจทย์ Master Dashboard/churn alert ตรงๆ

## จัดลำดับสำหรับงานจริงของ user (COO Thunder/EasySlip)

จาก agent ที่ขุดงานจริง — สิ่งที่ขาดไม่ใช่ capability แต่คือ **orchestration** (schedule/batch/alert/recover โดยไม่ต้องเปิด Claude session ค้าง). `chrome` CLI ปลดล็อกให้แล้ว. คุ้มสุดเรียงตามนี้:

1. **ดึง Master Dashboard revenue อัตโนมัติทุกวัน → CSV** (ตอนนี้ทำมือทุกเดือน) — cron + `chrome` CLI + `chrome kpi`/`chrome fetch`
2. **Alert churn EasySlip** (67K users, active 16%) → เตือนเข้า Telegram เมื่อ drop — `chrome kpi --notify`
3. **LINE OA broadcast แบบ queue** รันข้ามคืน 1000+ chats ปลอดภัย — ใส่ checkpoint+resume+pacing engine
4. **Facebook Ads snapshot รายเดือน** — `chrome capture` RE endpoint → `chrome fetch` loop

## Phase ถัดไป (ต้องแตะ extension = rebuild, ทำเมื่อพร้อม)

Phase 2 (surface ของที่มี): actionability wrapper (#1), เปิด flow_run เป็น MCP tool เต็ม, semantic search เข้า tools/list
Phase 3 (ของใหม่): NL act/extract/observe, schema extraction, observe→cache→replay self-heal, cron+webhook

## ไฟล์
- CLI: `~/bin/chrome` (28 verbs) · cookbook skill: `~/.claude/skills/chrome-mcp-cookbook/`
- รอบก่อน: `Chrome MCP — doctor autonomy stack + rollback`, `Chrome MCP — CLI + cookbook`
- Grounding: ทุก tool name verify กับ `~/mcp-chrome/packages/shared/src/tools.ts`
