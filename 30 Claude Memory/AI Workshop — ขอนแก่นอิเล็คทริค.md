---
name: project-ai-workshop-khonkaen
description: AI Workshop ที่บ.ขอนแก่นอิเล็คทริค ผู้เรียน 15 คนคละแผนก (บัญชี/การตลาด/วิศวกร/ช่าง) สอน Claude + deploy เว็บ + ฐานข้อมูล + GitHub
metadata: 
  node_type: memory
  type: project
  originSessionId: ee3243ee-719d-43e0-bff1-37e9a5221f48
---

**Workshop:** "Claude AI + ทำเว็บ deploy + ฐานข้อมูล + GitHub" ให้บ.ขอนแก่นอิเล็คทริค (ผู้ว่าจ้าง = คุณป๊อบ)
**ผู้เรียน:** เชิญ 15 คน · ตอบแบบสำรวจจริง **11 คน** (9/11 สายการตลาด · มั่นใจเฉลี่ย 2.7/5 · 1 คนใช้ Claude ประจำ = เบนซ์) คละแผนกหนัก ความต่างระดับสูงมาก
**ความท้าทายหลัก:** เจ้าของอยากให้ทุกคนทำเว็บ+DB ได้จริง แต่ครึ่งกลุ่มเป็น non-tech → ต้อง tiered outcome หรือลดเพดาน
**ส่งมอบแล้ว:** dashboard รวมไฟล์เดียว 3 แท็บ `AI-Workshop-รวม.html` (เจ้าของ / ผู้เรียน 11 คน + กราฟ / ความสอดคล้องเจ้าของ↔ผู้เรียน) — รายละเอียด+ผลวิเคราะห์ใน Obsidian `06-Dashboard-Summary.md`
**Live (Cloudflare Pages) — 2 ลิงก์ stable:**
- **3 แท็บ (ครบ):** https://khonkaen-ai-workshop.pages.dev · project `khonkaen-ai-workshop`
- **2 แท็บ (ผู้เรียน + ความสอดคล้อง, ตัดหน้าเจ้าของ):** https://khonkaen-workshop-learner.pages.dev · project `khonkaen-workshop-learner` · mobile-tuned + typography ปรับใหม่ 2026-07-01 · สร้างจากตัวเต็มด้วย Python patch (ตัด `#tab-owner` DOM + สลับ default active)
**Generators (ถาวร):** `RECOVERY/_generators/gen_combined.py` (+ `gen_dash.py`) — เผื่อ /tmp หาย · มีข้อมูลเพิ่ม → แก้ generator แล้ว regen + redeploy (วิธีเต็มใน Obsidian `06-Dashboard-Summary.md` § Deploy)

**Why:** โปรเจกต์ใหม่ 2026-06-30 ใช้แบบสำรวจ Pre-training คัดระดับ + กำหนดความลึก ก่อนวันงาน

**How to apply:**
- **KB ใน Obsidian:** `~/SecondBrain/01 Projects/AI Workshop - ขอนแก่นอิเล็คทริค/` — ดูรายละเอียดทั้งหมด (forms setup, content, gaps, menu) ที่นั่น
- **Working dir:** `~/Documents/Claude/Projects/AI Workshop Management/` (markdown + Apps Script + outputs)
- **Apps Script:** `clasp-deploy/Code.gs` — clasp standalone, deploy เป็น Web App, doGet rebuild 2 ฟอร์ม
- **Form IDs:**
  - Owner: `1oEUefpyYqe1MQPpbwyM_lrkzReq02ZaETM50rUf-bvw` (29 items)
  - Learner: `1ekrJsyjnlVluHixcDwyJy0AcTnwO9vuYYfzfkw81G7o` (35 items, รวม section 7 เมนูอาหาร/เครื่องดื่ม/ขนม)
  - ~~Manager~~: trashed 2026-06-30 (user ไม่เอา)
- ใช้ **bobbysomporn@gmail.com** (ไม่ใช่ 9bomqu) ในการรันทุก script
- Workshop Company 7 ทีม (ของ marketing training) คนละโปรเจกต์ — ดู [[AI Workshop — 7 ทีมการตลาด|project_ai_workshop_7teams]]

**Reference workflows ที่ใช้:**
- [[clasp Apps Script + Web App|reference_clasp_apps_script_webapp]] — วิธี deploy Apps Script ผ่าน clasp + Web App workaround
