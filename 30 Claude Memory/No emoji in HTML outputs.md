---
name: feedback-no-emoji
description: "User dislikes emojis in HTML reports / dashboards — keep purely typographic (text, color, shape). Applies broadly, not just one project."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b021af49-0884-4c0b-bf02-afb7be709027
---

ห้ามใส่อิโมจิใน HTML output ทุกประเภท (dashboards, reports, profiles, slides). ใช้สี + typography + ขอบ/พื้นหลังสื่อสารแทน.

**Why:** ผู้ใช้บอกซ้ำๆ ในหลายงาน — 2026-04 เรื่อง Expense Dashboard ("No emoji, light default, vanilla JS"); 2026-06-29 ใน Fitness Profile HTML ("ไม่เอาอิโมจิ เอาออกเลย"). อิโมจิทำให้รายงานดูไม่เป็น exec-grade · ขัดกับโทน clean dashboard ที่ user ชอบ.

**How to apply:**
- เริ่มต้นโดยไม่ใส่อิโมจิเลย แม้ user จะใส่ในข้อความเดิม (เช่น 🏋️ ใน markdown)
- ใช้สี (แดง=danger, เขียว=good, ส้ม=warn) + tag badge (`<span class="tag danger">HIGH</span>`) สื่อสารแทน ⚠ / ✓
- ใช้สัญลักษณ์ typographic ที่ไม่ใช่อิโมจิได้ (→ ↑ ↓ ★ × ⊕) แต่หลีกเลี่ยงถ้าไม่จำเป็น
- ยกเว้น: ถ้า user สั่งให้ใส่เอง (เช่น "ใส่ 🏋️ ให้หน่อย") ถึงจะใส่
- ครอบคลุม: meta titles, section headers, nav buttons, badges, table cells, footer notes — ทุกที่ในหน้าเว็บ

ดู [[โปรเจกต์ - Dashboard รายจ่าย|project_expense_dashboard]] สำหรับสไตล์ที่ user ชอบ (light default, vanilla JS, no emoji).
