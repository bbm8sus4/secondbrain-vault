---
name: project_expense_dashboard
description: "Thunder/EasySlip expense dashboard — single HTML file, iterated via AI debates, design system + principles"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4c412e2e-06f8-4f1b-826f-72e3e4cae1d3
---

แดชบอร์ดสรุปค่าใช้จ่าย Thunder & EasySlip (ม.ค.-พ.ค. 2569) — ไฟล์เดียวจบ.

**ไฟล์:** `~/Desktop/รายจ่าย Thunder&Easyslip.html` (CSS+JS inline, vanilla JS) + ข้อมูลแยก `~/Desktop/expense-data.js` (shape `D[brand][month].categories[].items[]`; brand = `thunder`/`easy`). Backups: `.bak`, `.bak2`, `.bak3`.

**ข้อมูลจริง:** `it.category` มี 4 ค่า (ต้นทุนบริการ / ค่าใช้จ่ายในบริหาร / ค่าใช้จ่ายในขาย / ว่าง) → ใช้ทำ COGS·Admin·Sales split. `it.company` 168 ราย. 41 หมวด (`cat.name`).

**Workflow การพัฒนา:** ผู้ใช้สั่ง "Aidebate <หัวข้อ>" → รัน `~/ai-debate/debate.py` (Codex+Gemini+Claude+Typhoon) → review → "เอามาปรับ/ทำเลย" → implement. รอบหลังใช้ Workflow (8-lens verified review) ควบคู่ debate. ทำมาแล้ว 7 รอบ: UX/proportions, filters, theme/menu, Thai language, SaaS refs (Ramp/Mercury/Stripe), responsive, human+AI UXUI.

**ข้อจำกัดตายตัว (ผู้ใช้ย้ำ):** ห้าม emoji, ธีมสว่างเป็นค่าเริ่มต้น, single HTML + vanilla JS, ภาษาไทย.

**Design system:** Ramp/Mercury/Stripe-inspired · light/dark theme (CSS custom props; localStorage key `expense-theme-2`, default light) · **`fs()` = เลขจริงเต็มมีคอมมา ปัดเป็นบาท ไม่ย่อ ลบ./แสน (ผู้ใช้สั่ง 2026-06-07 "ใส่ตัวเลขจริงไปเลย")** + `fmt()` 2 ทศนิยม (ตาราง/drill-down) · tabular-nums ทั้งระบบ · clamp() typography · 3 breakpoints (600/1024/1440)+cap 1600 · pointer:coarse touch · print styles · Lead Insight (alert รวมเข้า hero eyebrow) · ปุ่ม "ดูที่มา" (provenance `<dialog>`) ทุก anomaly · ไม่มี Donut (ตัดแล้ว).

**หลักการ human+AI (จาก debate):** "AI เลือกว่าควรมองอะไร · มนุษย์กำหนดว่ามองแล้วรู้สึกอย่างไร" — AI เติมช่องในเทมเพลตที่มนุษย์วาง, จัดลำดับเนื้อหาได้แต่ห้ามรีโฟลว์ layout, ห้ามแต่งสาเหตุที่ไม่มีในข้อมูล (hallucination), พยากรณ์ต้องบอกความไม่แน่นอน. AI features ที่ทำแล้ว: variance attribution, z-score/materiality anomaly, linear forecast, COGS/Admin/Sales structure, recurring-vs-one-off, vendor concentration, direction-aware narrative.

**ทำครบหมดแล้ว** (รวม 3 ข้อปิดท้าย: ตัด Donut, Lead Insight, provenance dialog + เลขเต็มไม่ย่อ). Backups: `.bak3` = ก่อน human+AI rewrite, `.bak4` = ก่อนต่อ Google Sheets loader.

**Google Sheets backend (2026-06-08, จาก Aidebate):** ตัดสินสถาปัตยกรรม = **Apps Script doGet/doPost (private sheet) + token + Cloudflare Access** (ทุกวิธีที่ต้อง publish ชีต = ข้อมูลการเงินรั่ว ตัดทิ้ง). สร้างชีต back office ไทยในบัญชี thunder.in.th แล้ว (id `1PaCBBWlpGPpAspCtKaocIptFDP4NAoZ3ZFLKDebWFvs`, แท็บเดียว 10 คอลัมน์: แบรนด์/ปี/เดือน/หมวด/ประเภท/รายละเอียด/บริษัท/จำนวนเงิน/วันที่/หมายเหตุ + 3 ตัวอย่าง — ผู้ใช้กรอกเอง). Apps Script พร้อม deploy ที่ `~/Desktop/EasyBot-Sheets-Backend.gs` (reshape เป็น D[brand][month] เป๊ะ). แดชบอร์ดเพิ่มชั้น `loadData()` async + cache 15 นาที + fallback static + ปุ่มรีเฟรช + รองรับ 12 เดือน (MONTHS derive จากข้อมูล) — ตั้ง `SHEET_API`/`SHEET_TOKEN` ในไฟล์ = ใช้ live, ว่าง = static เดิม. **เหลือฝั่งผู้ใช้:** deploy Apps Script (Execute as Me, Anyone) → เอา /exec URL + token ใส่ใน config + เปิด CF Access. Sheets เทคนิค: [[reference_chrome_mcp_sheets]].

**พอร์ตจาก EasyBOT Finance (2026-06-08):** section ใหม่ `#sec-plan` "วางแผน" — (1) **Scenario simulator** สไลเดอร์ปรับรายจ่าย ±50% → run-rate ทั้งปี + ประหยัด/เพิ่ม (planAvg/planFnext stash ตอน render, slider เสถียรด้วย scnOut), (2) **Budgets รายหมวด** ตั้งงบ/เดือน top 8 หมวด เก็บ localStorage `expense-budgets-2` (delegated change listener + data-bcat), (3) **budget-overrun alert** เด้งใน Lead Insight eyebrow (`notif-tag budget`). Variance = relabel Waterfall (มีอยู่แล้ว). หมายเหตุ: cash-runway ตรงๆ ทำไม่ได้เพราะไม่มีข้อมูลรายได้ → พอร์ตแก่น expense run-rate+scenario แทน.

เกี่ยวข้อง: [[reference_ai_debate_harness]] · [[project_thunder_solution]]
