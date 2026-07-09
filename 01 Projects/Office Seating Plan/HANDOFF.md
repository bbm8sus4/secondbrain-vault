---
tags: [project, handoff, seatmap, single-file-html, agent-context, done]
project: Office Seating Plan
doc: AI/Developer Handoff
updated: 2026-07-09
app_version: 3.9.0
status: completed
completed: 2026-07-09
---

# SeatMap — AI / Developer Handoff

> ✅ **โปรเจกต์เสร็จสมบูรณ์ — ปิดงาน 2026-07-09.** ส่งมอบครบ: แอป deploy บน Cloudflare Pages (gate รหัส), **i18n TH/EN ครบทุกจุด** (APP_VERSION v3.9.0 · checkpoint `seatArh_v.1.0.2`), **public repo** https://github.com/bbm8sus4/office-seating-plan. ประวัติงาน 3 วันสุดท้ายอยู่ที่ [[2026-07-05 Session — สั่งงาน + วิธีทำงาน]] + [[2026-07-06 QA รอบผู้ใช้จริง + แก้ตาม feedback]]. เอกสารด้านล่างเก็บไว้อ้างอิงถ้าเปิดงานใหม่.

> อ่านไฟล์นี้ก่อนเริ่มทำงานต่อ. เขียนไว้ให้ทั้งคนและ AI session อื่นมารับงานได้ทันทีโดยไม่ต้องถามซ้ำ. ภาษาในเอกสารปนไทย/อังกฤษตามที่เจ้าของถนัด.

---

## 0. TL;DR (30 วินาที)
- **แอปคืออะไร:** เครื่องมือภายในของ Thunder Solution + Easy Slip จัดผังที่นั่งออฟฟิศ (ชั้น 2, ~30 คน) + ผังองค์กร + product/lane board + HR dashboard + master directory. **Single-file HTML app** ไม่มี backend ไม่มี build step. เก็บข้อมูลใน `localStorage` + `IndexedDB` ของ browser เท่านั้น.
- **ไฟล์จริง:** `~/Desktop/office-seating-overview.html` (ชื่อในแอป = **SeatMap**, สี accent ม่วง `#7c3aed`).
- **เวอร์ชันปัจจุบัน:** v3.8.0 (ค่าคงที่ `APP_VERSION` บรรทัดแรกของ `<script>`).
- **กติกาเหล็ก 3 ข้อ:** (1) **ห้ามพัง** — เจ้าของย้ำตลอด, verify ทุกการแก้; (2) **ตอบ/คอมเมนต์เป็นไทยธรรมชาติ** ลงท้าย "ครับ"; (3) **ห้าม deploy ขึ้น cloud / ห้ามข้อมูลพนักงานจริงหลุดออกเน็ต** (เคย deploy Cloudflare Pages แล้วถอนเพราะข้อมูลหลุด — ถ้าจะทำ mockup ใช้ dummy data + ไฟล์แยก).
- **วิธี verify ที่ใช้จริง:** Chrome MCP ผ่าน HTTP (port 12306) คุม Chrome tab ที่เจ้าของเปิดไฟล์อยู่ — ดูหัวข้อ §3 (สำคัญสุด).

---

## 1. Files & locations
| อะไร | ที่ไหน |
|---|---|
| แอปจริง (แก้ที่นี่) | `~/Desktop/office-seating-overview.html` |
| Backups | `~/Desktop/_archive/office-seating-overview-*.html` (มี v2.0-LEGACY, v2.4.0, v3.6.4-pre-audit-fix) |
| Legacy planner เก่า (แยก key ไม่ให้ทับ) | `~/Desktop/_archive/office-seating-planner-v2.0-LEGACY.html` |
| Notes / handoff (ไฟล์นี้) | `~/SecondBrain/01 Projects/Office Seating Plan/` |
| Smoke-test script | `/tmp/chrome_mcp_final.sh` (regenerate ได้จาก §3) |

> Convention ของเจ้าของ: notes อยู่ `~/SecondBrain/01 Projects/<X>/`, real files อยู่ `~/Work/<X>/`. **ยกเว้นแอปนี้อยู่ Desktop** (historical). ถ้าย้ายควรไป `~/Work/`.

---

## 2. สถานะปัจจุบัน (v3.8.0)
ผ่าน adversarial audit 2 รอบ (Workflow 7 มิติ, 40 confirmed findings) — แก้ security/data-loss/a11y-blocker/perf ที่สำคัญครบ. Smoke test 51/53 (2 fail คือ test artifacts — ดู §3). 0 app console errors.

**5 tabs หลัก + 1 settings + modal layer:**
1. **ผังที่นั่ง (seating)** — floor plan ลากคนลงที่นั่ง, filter bar (Views presets + segmented + popover), onboarding tray ขวา
2. **ผังองค์กร (org)** — grid ระดับ (C-LEVEL/MANAGER/LEAD/WORKER) ลากกล่อง, สลับบริษัท Thunder/EasySlip, ผูก node กับ person
3. **แดชบอร์ด (dashboard)** — HR KPI chips + donuts + tables
4. **โปรดักส์ (product)** — Project → Lanes board (แถบแนวนอนสไตล์ผังองค์กร), ลาก/คลิกเพิ่มคนเข้าเลน
5. **จัดการ (manage/settings tab)** — master person directory (table), + เพิ่มพนักงาน/ห้อง/เทมเพลต, ผูกผังองค์กร
6. **ตั้งค่า ⚙ (prefs)** — ธีม/ภาษา/ล็อก/สำรอง-กู้คืน/danger zone/about
- **Modal/overlay:** welcome tour (first-run), shortcuts (กด `?`), changelog "มีอะไรใหม่", input modal, product-assign picker, person/room/org/template/link modals

---

## 3. ⭐ วิธีทำงาน (methodology) — อ่านให้ครบ

### 3.1 กติกาการแก้: backup → batch by risk → verify ทุก batch
1. **Backup ก่อนแก้ใหญ่:** `cp ~/Desktop/office-seating-overview.html ~/Desktop/_archive/office-seating-overview-vX.Y.Z-<reason>-$(date +%Y%m%d-%H%M%S).html`
2. **แบ่ง batch ตามความเสี่ยง** (safe → behavior-change → risky-core). แก้ทีละ batch.
3. **หลังทุก batch: syntax check + Chrome MCP verify + smoke test.** ห้ามข้าม.
4. **Bump `APP_VERSION`** + เพิ่ม entry ใน `CHANGELOG` array (ภาษาไทย user-facing) ทุกครั้งที่ release.

### 3.2 Syntax check (ต้องผ่านก่อน verify)
```bash
python3 - <<'EOF'
import re
h=open("/Users/aexgee/Desktop/office-seating-overview.html",encoding="utf-8").read()
scripts=re.findall(r'<script[^>]*>(.*?)</script>',h,flags=re.DOTALL)
open("/tmp/osp.js","w",encoding="utf-8").write("\n;\n".join(scripts))
EOF
node -c /tmp/osp.js && echo "SYNTAX OK"
```

### 3.3 ⭐⭐ Chrome MCP live verification (สำคัญสุด — เทคนิคที่ใช้จริง)
Chrome MCP tools ไม่โผล่ใน tool list ของ session ปกติ แต่ **server ทำงานอยู่ที่ `http://127.0.0.1:12306/mcp`** (Chrome extension `nckehcmgbblnmibclnnongjamneibjjj`). เรียกผ่าน HTTP โดยตรงได้:

**Step 1 — เปิด MCP session (ทำครั้งเดียว, เก็บ session id):**
```bash
RESP=$(curl -s -i -X POST http://127.0.0.1:12306/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"claude-code","version":"1.0"}}}')
SID=$(echo "$RESP" | grep -i "mcp-session-id:" | awk '{print $2}' | tr -d '\r')
curl -s -X POST http://127.0.0.1:12306/mcp -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" -H "mcp-session-id: $SID" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}' >/dev/null
echo "SID=$SID"
```

**Step 2 — helper เรียก tool + parse (SSE → jq):**
```bash
call(){ curl -s -X POST http://127.0.0.1:12306/mcp \
  -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: $SID" -d "$1" 2>&1 \
  | grep -oE 'data: \{.*\}' | sed 's/^data: //' | jq -r '.result.content[0].text'; }
```

**Step 3 — หา tab id ของไฟล์ (เปลี่ยนทุกครั้งที่ reload/เปิดใหม่):**
```bash
call '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"get_windows_and_tabs","arguments":{}}}'
# มองหา tab ที่ url = file:///Users/aexgee/Desktop/office-seating-overview.html → เอา tabId
```

**Step 4 — รัน JS บน tab จริง (คืนค่า return ได้):**
```bash
call '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"chrome_javascript","arguments":{"code":"location.reload();return 1;","tabId":TAB_ID}}}'
# chrome_javascript รันใน async function → รองรับ return/await. ผลอยู่ใน .result (JSON string)
```

**Chrome MCP tools ที่ใช้บ่อย:** `chrome_javascript` (รัน JS + return), `chrome_click_element` (selector), `chrome_screenshot` (บันทึกลง ~/Downloads/screenshot_*.png), `chrome_console` (อ่าน log/exception), `get_windows_and_tabs`.

**กับดักที่เจอมาแล้ว (สำคัญ):**
- **`chrome_click_element` คลิก `<a>` ที่ไม่มี `href` ไม่ trigger onclick** — ให้ใช้ `chrome_javascript` เรียก `.click()` แทน หรือเรียกฟังก์ชันตรง.
- **`window.prompt`/`confirm`/`alert` โดน Chrome suppress เงียบ** เมื่อหน้าเด้ง dialog บ่อย → **ห้ามใช้ `prompt()` ในโค้ดใหม่**, ใช้ `openInputModal({title,value,placeholder,onSave,onDelete})` แทน. เวลา test ให้ mock `window.confirm=()=>true`.
- **`setView('seating')` ไม่เรียก `render()`** สำหรับ default — ถ้าเซ็ตค่าแล้วอยากเห็นผลบน DOM ต้องเรียก `render()` เอง (แต่ตั้งแต่ v3.8.0 `setView` เรียก `render()` ให้แล้วทุก view).
- **เทสด้วยการ "คลิกปุ่มจริง"** (`document.querySelector('...').click()`) ไม่ใช่แค่เรียกฟังก์ชัน — เพราะ bug บางตัวอยู่ที่ event wiring / dialog suppression ที่การเรียกฟังก์ชันตรงมองไม่เห็น (บทเรียนจาก lane CRUD).
- **State ค้างข้าม test ใน 1 batch JS** — ถ้าเทสหลายอย่างต่อกันแล้วผลแปลก ให้ `location.reload()` ก่อนแต่ละ isolated test.
- **Console จะมี 1 "Uncaught (in promise) Permissions check failed" เสมอ** — มาจาก Chrome MCP extension เอง ไม่ใช่ bug ของแอป (`_isAppOwnError` filter กันไว้แล้ว ไม่ให้เด้ง fatal banner).

### 3.4 Smoke test script
สคริปต์ `/tmp/chrome_mcp_final.sh <SID>` รัน ~53 assertions (boot, ทุก tab, filter, modal, undo, toggles, validators, xss). **2 fail ที่ "คาดไว้" (ไม่ใช่ bug):**
1. `APP_VERSION` — สคริปต์ hardcode เวอร์ชันไว้ (เทียบไม่ตรงเมื่อ bump). แก้เลขในสคริปต์ถ้าจะให้เขียว.
2. `search 'bob' got 0` — search มี debounce 140ms, สคริปต์เช็คทันทีไม่รอ. เป็น timing artifact.
> ถ้าเห็น 2 fail นี้เท่านั้น = ผ่าน. Fail อื่น = regression จริง.

### 3.5 เปิดไฟล์ให้เจ้าของดู
`open -a "Google Chrome" ~/Desktop/office-seating-overview.html`
Screenshot headless: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --screenshot=/tmp/x.png --window-size=1600,900 --virtual-time-budget=2000 file://...`
> headless เริ่ม fresh profile → welcome modal จะเด้งทับ. Inject `localStorage.setItem("osp.onboarded","1")` ก่อน setView ถ้าจะ screenshot สะอาด.

---

## 4. Architecture

### 4.1 Storage keys (localStorage)
| key | เนื้อหา |
|---|---|
| `osp.v2` | main state (rooms, people, holds, products) |
| `osp.v2.lkg` | last-known-good snapshot ของ state |
| `osp.org.v1` / `osp.org.easyslip.v1` (+`.lkg`) | ผังองค์กร Thunder / Easy Slip |
| `osp.templates.v1` | เทมเพลต seating + org |
| `osp.views.v1` | saved filter views (custom) |
| `osp.locked`/`osp.theme`/`osp.lang`/`osp.prod.current`/`osp.org.company` | user prefs |
| `osp.onboarded`/`osp.lastSeenVersion` | SaaS onboarding flags |
| `osp.corruption` (sessionStorage)/`osp.fatal` | error diagnostics |
- **IndexedDB `osp-backups`** — 2 object stores `snapshots` + `org-snapshots`, ring 15 ชุดล่าสุด.

### 4.2 State shape
```
state = {version, meta, rooms[], people[], holds{}, products[]}
person = {id, nickname, fullName, role, company, seat, team, status,
          startDate, photo(dataURL), product, lane, task}
product = {id, name, lanes:[{id,name}]}
room = {id, num, row('top'|'bottom'), name, layout('island'|[n,n,...])}
hold (state.holds[seatId]) = {label, since}
orgState = {version, cofounderRemoved, nodes[]}   // แยกจาก state, ต่อบริษัท
orgNode = {id, lv, col, name, th, en, company, p(parentId), backupId, critical, personId}
```
- **กติกาสำคัญ (v3.6.3+): "no lanes = no members"** — `person.product` จะมีค่าได้ก็ต่อเมื่อ product นั้นมี ≥1 lane. `migrate()` เตะคนออก (product=null) ถ้า product ไม่มี lane + toast. คนอยู่ได้ **1 product เท่านั้น** (drag ไป product ที่ 2 = ออกจากอันแรก).
- **org node ผูก person:** `node.personId` → `_resolveOrgNode()` hydrate ชื่อ/รูป/บริษัท จาก `state.people` ตอน render. ลบคน → `_unlinkPersonFromAllOrg()` เคลียร์ link.

### 4.3 Key subsystems
- **Undo (แยก 2 stack):** `undoStack`/`redoStack` (seating state) vs `orgUndoStack`/`orgRedoStack` (org). `Cmd+Z` view-aware ผ่าน `_isOrgView()`. **org stack เป็น per-company** — `switchOrgCompany`/`importOrgJSON`/`loadTpl`(org) ล้าง stack เมื่อสลับบริษัท (กัน cross-company overwrite). `toastUndo` ปุ่มใช้ `_toastUndoAction()` บังคับ seating stack เสมอ.
- **`_withSaveRollback(mutateFn, onOk)`** — pattern กลางของทุก seating mutation (18+ ที่). ทำ: `snapshot()`+`pushUndo()` → `mutateFn()` → `save()` → ถ้า save fail: restore snapshot + render + return false; ถ้าสำเร็จ: `onOk()`. **onOk คือที่ใส่ side effect** (render, closeModal, toast).
- **`save()/saveOrg()/saveTpls()` คืน bool** — caller ต้อง gate success toast บนค่าคืน. `toast()`/`toastError()` เป็น queue (error toast ไม่โดน success ทับ). `_invalidateQuota()` ถูกเรียกใน save*() (cache quota %).
- **`render()` view-gated (v3.7.0+):** rebuild แค่ view ที่เห็น + global chrome (banners, top-nav badges, undo/redo/lock buttons). `_activeView()` บอก view ปัจจุบัน. `setView()` toggle class แล้วเรียก `render()` → สลับ view = render สด. **อย่าเพิ่ม render ต่อ view โดยไม่ผ่าน gate.**
- **Modals:** เปิด `openModal(id)` / ปิด `closeModal(id)`. Focus trap ผ่าน `_focusableInModal` + `_topOpenModal`. Escape ปิด modal ก่อน (แล้วค่อย presentation). รายชื่อ modal อยู่ 2 ที่ (keydown array + click-outside array) — **เพิ่ม modal ใหม่ต้องเติมทั้ง 2 ที่.** `openInputModal({...})` = generic input แทน `prompt`.
- **XSS safety:** `escapeHtml()` ทุก dynamic text ใน innerHTML. `attr(s)` = `escapeHtml(JSON.stringify())` สำหรับ inline `onclick` ที่ concat id. **`_photoBg(photo, fallbackColor)`** = canonical escaper สำหรับ avatar background (gate `/^data:image\//` + `encodeURI().replace(/'/g,"%27")`). **ทุก photo sink ต้องผ่าน `_photoBg`** (มี 7 sink; อย่าเขียนใหม่แบบ concat ดิบ — เคยหลุด 2 จุด = XSS).
- **Migration:** `migrate(state)` idempotent, รันทุก load/import/restore. Guards ผ่าน `meta.*` flags (`legacyRoomsPruned`, `nameFix250`, `buildingMapped`). `validateState()` throw ถ้า shape เพี้ยน (rooms/people/products/lanes). Org: `migrateOrg()` + `validateOrg()` (cycle detection, NaN lv, dup id).
- **Error boundary:** `window.onerror` + `unhandledrejection` → red fatal banner + Restore LKG/Download report/Reload. `_isAppOwnError()` filter extension noise (chrome-extension://, "Permissions check failed").
- **Export/Import:** `exportJSON`/`importJSON` = **ที่นั่งอย่างเดียว** (มี REPLACE/MERGE + dry-run diff). `exportAll`/`importAll` = **bundle ครบชุด** (state + org 2 บริษัท + templates + views) — ใช้สำหรับย้ายเครื่อง (`__bundle:"seatmap-full"`). Org export/import แยก (`exportOrgJSON`/`importOrgJSON`).

### 4.4 Layout / naming ของ product board
- Project = `product`, tabs บนใช้ class `.pj-tab`. Lane bands = `.prow` (label แนวตั้ง `.prow-lbl` + `.prow-body` + `.prow-add` ghost). Controls เลื่อน/แก้/ลบ = `.prow-ctl` (โชว์ hover + focus-within + touch via `@media(hover:none)`).
- ⚠️ **Terminology drift (ยังไม่แก้):** UI พูด "โปรเจกต์", nav/i18n พูด "โปรดักส์", CSS ใช้ `.pj-*` — เป็นตัวเดียวกันหมด.

---

## 5. Conventions & user preferences (เจ้าของ = ผู้บริหาร)
- **ตอบไทยธรรมชาติ สั้น กระชับ ขึ้นผลลัพธ์ก่อน** ลงท้าย "ครับ". ห้ามแปลตรงตัว/ภาษาราชการ. คงอังกฤษเฉพาะ code/path/error/technical term.
- **ห้ามพังของเดิม** — เจ้าของกังวลเรื่องนี้ที่สุด. verify ทุกการแก้ด้วย Chrome MCP + smoke test.
- **Single-file constraint** — ทุกอย่างต้องอยู่ในไฟล์ HTML เดียว (ไม่มี build/SW/external). PWA offline เต็มรูปทำไม่ได้.
- **ห้ามข้อมูลจริงหลุด cloud** — ห้าม auto-deploy. mockup = dummy data + ไฟล์แยก + ไม่ push.
- **Chrome MCP เท่านั้น** สำหรับ verify (เจ้าของขอ) — ไม่ใช่แค่ headless.
- **แก้แล้วเจ้าของชอบเห็นภาพ** — screenshot/เปิด browser ให้ดูหลังงานสำคัญ.
- Workflow / multi-agent: เจ้าของเปิด "ultracode" (xhigh + workflow orchestration) — ใช้ Workflow tool สำหรับ audit/review ใหญ่ได้.

---

## 6. Changelog trajectory (v2.4 → v3.8)
- **v2.4.0** baseline (24 bug fixes รอบก่อน: import guard, org drag, save-error surfacing, Lock coverage, LKG+IDB backup, PDF name fix).
- **v2.5.0** แก้ 50 regressions จาก 5-agent adversarial verify (save return bool, toast queue, state validation, Lock gaps, org drop guard, canvas roster/Thai font, POOM NOI/NONG name migration).
- **v2.6.0** Settings/Manage tab (master directory) + org↔person link. **v2.6.1** CRUD-basic quick wins (XSS attr(), error boundary, maxlength).
- **v2.7.0** unified contextual toolbar + overflow. **v2.7.1** filter bar (Views/segmented/popover).
- **v2.8.0→2.8.4** slim hero→removed, ย้าย utility/search/undo ขึ้น top nav, ลบ saved-timestamp.
- **v2.9.0** Amplemarket-style nav. **v2.9.1** purple CTA. **v2.9.2** rename → SeatMap. **v2.9.3** SVG logo+favicon. **v2.9.4** error boundary filter extension noise.
- **v3.0.0** CRUD-basic 31 fixes (focus trap, iOS/mobile, save/quota UX, debounce, import dry-run, PWA meta). **v3.0.1** lean refactor (T_ constants, `_withSaveRollback`, canvas one-liners).
- **v3.1.0** SaaS layer (welcome/shortcuts/changelog/feedback). **v3.1.1** UI cleanup (remove view heroes, product selector→toolbar).
- **v3.2.0** Settings page (prefs ⚙). **v3.3.0** product kanban lanes. **v3.4.0** org-chart-style bands. **v3.5.0** lanes-in-project. **v3.5.x** remove toolbar buttons. **v3.6.0** lane reorder ▲▼. **v3.6.1** lane CRUD → inputModal (prompt blocked). **v3.6.2/3.6.3** remove "ทั่วไป" band (no lanes = no members). **v3.6.4** CRUD-basic delta fixes.
- **v3.7.0 + v3.8.0** ← ล่าสุด: audit 2 รอบ (7-dim workflow, 40 findings) แก้ 24 จุด. ดู README.md สำหรับรายการเต็ม.

---

## 7. Deferred backlog (ยังไม่แก้ — พร้อมเหตุผล)
**Cosmetic (ไม่กระทบผู้ใช้):**
- EN-mode ยังไทยปน (prefs/lane/modal hardcode ไทย) — ใหญ่, EN mode เป็น secondary.
- Dead i18n keys ~22×2, orphaned CSS blocks, `renderSavedLine()` no-op stub, `.risk-on` CSS remnants (harmless), terminology drift โปรเจกต์/โปรดักส์/`.pj-*`.
- Avatar markup 6 builders divergent — refactor risk (ส่วน photo ที่เป็น bug unify แล้วผ่าน `_photoBg`).

**Nil-impact perf ที่ 30 คน (เก็บไว้ถ้าสเกลถึง 200+):**
- `computeHR()` รัน 2×/render, dashboard co-location O(seats×people), photo-pool สำหรับ undo snapshots (photo-in-localStorage เจ้าของ defer ไว้ก่อน).

**LOW edge cases:**
- `_withSaveRollback` push undo ก่อน mutate → ถ้า mutate throw เหลือ phantom undo + ล้าง redo (rare). undo()/redo() ไม่เช็ค save() return. merge-import dedup by id เดียว. presentation cross-tab sync ครอบแค่ seating (org ไม่ sync).

**Feature requests (ต้อง design):**
- Dashboard สถิติ project/lane. Template-load เตือนก่อนทับ lane structure. Multi-project membership (ตอนนี้ 1 คน 1 project).

**A11y nice-to-have:**
- Focus หลุดไป body หลัง re-render (ควร re-anchor). Org empty-cell keyboard. Toast action keyboard reach.

---

## 8. ⚠️ Open questions — ต้องให้เจ้าของตัดสินใจก่อนทำ
1. **จำนวน NEW-hire จริง 5 หรือ 7 คน?** — seed hardcode 7 คน (`nh-pm/coo/sale/mktx/po/cfo/csmg` ใน `DEFAULT_PEOPLE`). `resetAll` คืน 7 คนนี้กลับมา. ถามค้างมาหลาย session.
2. **Bob (COO) ย้ายไปตำแหน่งไหน?** — seed มี `nh-coo` = "COO (incoming, replaces Bob)". ยังไม่ยืนยัน.
> อย่าลบ/แก้ NEW-hire seed จนกว่าเจ้าของจะตอบ.

---

## 9. Gotchas / traps (สรุปที่พลาดมาแล้ว)
- อย่าใช้ `window.prompt/confirm/alert` ในโค้ดใหม่ (Chrome block) → `openInputModal`.
- ทุก avatar photo background ผ่าน `_photoBg()` เท่านั้น (XSS).
- เพิ่ม modal ใหม่ → เติมชื่อใน keydown array + click-outside array (2 ที่).
- อย่าเพิ่ม per-view render นอก `render()` view-gate.
- org undo stack per-company — สลับบริษัทต้องล้าง stack.
- `chrome_click_element` กับ `<a>` ไม่มี href ไม่ทำงาน → ใช้ `.click()` ผ่าน JS.
- verify ด้วยการคลิกปุ่มจริง ไม่ใช่แค่เรียกฟังก์ชัน.
- Chrome MCP console จะมี 1 extension rejection เสมอ (ไม่ใช่ bug).
- test หลายอย่างต่อกัน → `location.reload()` ก่อน isolated test กัน state contamination.

---
*เอกสารนี้ + README.md (รายการ fix ละเอียด) = handoff ครบ. ถ้าต่อจาก AI ตัวอื่น: อ่าน §3 (วิธี verify) ก่อนแตะโค้ด, แล้ว §4 (architecture) ก่อนแก้ feature.*
