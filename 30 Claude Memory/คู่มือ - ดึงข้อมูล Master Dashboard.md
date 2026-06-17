---
name: reference-master-dashboard-chrome-mcp
description: "How to extract monthly revenue data from the Thunder Master Dashboard via Chrome MCP (date picker, per-product, gotchas)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: dd2aa127-e1a7-4dc3-bb0f-dd764571bcc8
---

Extracting data from **master-dashboard-eight-nu.vercel.app** (Thunder Group CEO Dashboard) via Chrome MCP. Related: [[โปรเจกต์ - Thunder Solution|project_thunder_solution]], [[กติกา - Chrome MCP transport|feedback_chrome_mcp_transport]].

**Access:** Login session persists in the user's Chrome (no need to type password). Next.js App Router, Base UI components, live data ("อัปเดต just now" → numbers drift by hundreds between reads).

**Pages:**
- `/` = "ภาพรวมวันนี้" (Today/this-month). **IGNORES the date picker AND URL query params** — always current month. Has Bot/Flex/Thunder API/EasyBot/EasySlip API but NO BoostSMS.
- `/thunder`, `/easyslip` = brand drill-downs. **Respect the global date-range picker.** Per-product revenue is in the "เปรียบเทียบสินค้า → รายได้เดือนนี้" block (cleanest source; matches root MoM badges exactly).
- BoostSMS revenue: only under the **"Boost SMS" tab** on `/easyslip`.
- `/reports` = "Action Center" (todo list), NOT raw data.

**Date picker (the hard part):** header button shows "dd/mm - dd/mm/yyyy" with a *dynamic* id (e.g. `#base-ui-_R_pidb_`) — find it by `[...document.querySelectorAll('header button')].find(x=>/\d{2}\/\d{2}/.test(x.textContent))`. A JS `.click()` does NOT open it (Base UI ignores untrusted clicks). **Tag the element with an id then real-click via `chrome_click_element` on `#thatid`.** The popover has presets: วันนี้/เมื่อวาน/สัปดาห์นี้/สัปดาห์ที่แล้ว/เดือนนี้/**เดือนที่แล้ว**/ไตรมาสนี้/ไตรมาสที่แล้ว/ปีนี้/ปีที่แล้ว. Click **"เดือนที่แล้ว"** (one click) to get previous month — far more reliable than prev-arrow+day1+day30+apply (that sequence's Thai buttons "ก่อนหน้า"/"ใช้ช่วงเวลานี้" kept failing). Verify by re-reading the picker button text (should become "01/04 - 30/04/2026"). Navigating via location.href RESETS picker to current month, so set the picker AFTER landing on each page.

**chrome_javascript gotcha:** the tool wraps code in a function → bare expressions return `"undefined"`. **Must use `return ...`** to get a value (e.g. `return document.body.innerText`). Statements like `location.href=url` work fine (side effect). Most reliable text extraction: `return document.body.innerText`, then parse offline.

**Chrome MCP transport:** tools often DON'T load as MCP tools in Claude Code. Fallback = curl/python to `http://127.0.0.1:12306/mcp` with full MCP handshake (initialize → capture `mcp-session-id` header → notifications/initialized → tools/call). Reusable helper written at `/tmp/mcpc.py` (call/text/js). chrome_get_web_content textContent uses Readability and is unreliable on this SPA (returns footer only) — prefer innerText via chrome_javascript.

**Products → user's taxonomy:** Thunder = Bot (BOT) + Thunder API + Flex(small). EasySlip = Easy Bot (BOT) + EasySlip API + Boost SMS. EasySlip API ≈ 96.9% of EasySlip (dashboard flags concentration risk). BoostSMS data is placeholder-like (0 sent, "ยังไม่มี log").

**WARNING — anti-hallucination:** harness tool results were delivered a turn late / batched during this session; it's easy to invent numbers when output looks empty. ONLY report figures literally present in real tool output. Cross-check brand product-sums vs the root overview totals + the MoM % badges before trusting.
