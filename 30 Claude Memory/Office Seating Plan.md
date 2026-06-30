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
**Interactive tool (LIVE FILE):** `~/Desktop/office-seating-overview.html` — single-file HTML, ไฟล์จริงที่ใช้งาน/แก้อยู่ (ไม่ใช่ `office-seating-planner.html` ที่เป็นของเก่า). **3 แท็บ:** ผังที่นั่ง (Seating) · ผังองค์กร (Org Chart: Thunder+EasySlip toggle, ความเสี่ยง handover) · แดชบอร์ด (Dashboard — stat chips + บาร์ใช้พื้นที่รายห้อง + แยกบริษัท + legend, ย้ายมาจากหน้า Seating 2026-07-01). Drag-drop (Pointer Events), onboarding tray, localStorage+IndexedDB durability, undo/redo, search/filter, PNG/CSV export, lock + presentation mode, templates (เซฟผังแบบ A/B). Room modal แก้ได้ละเอียด: ชื่อ+เลขห้อง(num)+แถว(top/bottom)+layout พร้อม live seat-count preview + safe-shrink eviction (ลดที่นั่งแล้วคนเด้งไปรอจัดที่ + confirm). Seating sizing = proportional flex-grow (ห้อง 9 ที่เท่ากัน, Thunder island ใหญ่สุด ไม่แตะ). 25 bugs fixed, verified headless.
**สำคัญ:** ผู้ใช้ลอง redesign v2.1 (poster/SVG) แล้ว **ไม่ชอบ → revert กลับ v2.0**. อย่าเสนอ redesign ใหญ่ซ้ำเว้นแต่ผู้ใช้ขอ. **เก็บ backup ก่อนแก้ใหญ่ทุกครั้งที่ `~/Desktop/.seating-backups/`** (overwrite Write ทับเวอร์ชันเก่าโดยไม่มี git = เคยทำเกือบหายมาแล้ว). Validate ด้วย extract-script + `node -c` + smoke harness. Next (ยังไม่ทำ): deploy Cloudflare Pages.

ทุก update เรื่องที่นั่ง / พนักงานเข้า-ออก / ย้ายห้อง → แก้ที่ Obsidian อย่างเดียว memory ไม่ต้องเก็บรายชื่อ

**Why:** ผู้ใช้ (Bob/COO) ต้องการ track layout + HR planning ระยะยาว เก็บใน Obsidian PARA เพื่อเปิดดูจาก Obsidian ได้ และมี change log
**How to apply:** ถามเรื่องที่นั่ง/ห้อง/พนักงานใหม่เมื่อไหร่ → อ่าน + แก้ไฟล์ใน Obsidian ก่อน อย่าตอบจาก memory

**Pending (2026-06-30):** Bob กำลังจะย้ายตำแหน่ง, มีพนักงานใหม่ 5-7 คน (PM/COO ใหม่/Sales/Marketing Exec/PO/CFO/Manager CS) — ยังไม่ allocate

ดู [[โปรเจกต์ - Thunder Solution|project_thunder_solution]], [[โปรเจกต์ - Second Brain|project_second_brain]]
