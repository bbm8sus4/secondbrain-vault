---
name: project-office-layout
description: "Office seating plan (Thunder Solution + EasySlip) — knowledge base in Obsidian, memory holds pointer only"
metadata: 
  node_type: memory
  type: project
  originSessionId: 863e50ae-74a6-4a27-b32e-7745a27340ea
---

ออฟฟิศมี 5 ห้อง (Marketing, Development, Jetder, Thunder, Marketing EasySlip ห้องใหม่) รวม 49 ที่นั่ง

**Single source of truth (เนื้อหา):** `~/SecondBrain/02 Areas/Office Layout/Office Seating Plan.md`
**Interactive tool:** `~/Desktop/office-seating-planner.html` — single-file HTML v2.0.0, drag-drop seating planner (Pointer Events), onboarding tray (7 new hires pre-loaded), localStorage+IndexedDB durability, undo/redo, search/filter, PNG/PDF/CSV export, lock + presentation mode. Built via multi-agent workflow + adversarial review (25 bugs fixed), passes headless smoke test. Validate edits with the extract-script + `node -c` + /tmp/osp-smoke.js harness. Next step (not done): deploy to Cloudflare Pages.

ทุก update เรื่องที่นั่ง / พนักงานเข้า-ออก / ย้ายห้อง → แก้ที่ Obsidian อย่างเดียว memory ไม่ต้องเก็บรายชื่อ

**Why:** ผู้ใช้ (Bob/COO) ต้องการ track layout + HR planning ระยะยาว เก็บใน Obsidian PARA เพื่อเปิดดูจาก Obsidian ได้ และมี change log
**How to apply:** ถามเรื่องที่นั่ง/ห้อง/พนักงานใหม่เมื่อไหร่ → อ่าน + แก้ไฟล์ใน Obsidian ก่อน อย่าตอบจาก memory

**Pending (2026-06-30):** Bob กำลังจะย้ายตำแหน่ง, มีพนักงานใหม่ 5-7 คน (PM/COO ใหม่/Sales/Marketing Exec/PO/CFO/Manager CS) — ยังไม่ allocate

ดู [[โปรเจกต์ - Thunder Solution|project_thunder_solution]], [[โปรเจกต์ - Second Brain|project_second_brain]]
