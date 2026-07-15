---
name: feedback-hook-budget-unlimited
description: SessionEnd summarize hook ใช้ $10 budget — ไม่เสียเงินเพิ่ม (Max sub) อย่าประหยัด อย่าตั้งต่ำ
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c43a0a62-0da8-4cce-b114-43e25a68201f
---

`--max-budget-usd` ใน SessionEnd hook ไม่ใช่เงินจริง แค่ cap token usage (คิดเป็น list price) ภายใน Max sub ที่จ่ายอยู่แล้ว

**Why:** เคยตั้ง $0.50 → session ยาวๆ transcript เป็นแสนบรรทัด แค่อ่าน input ก็เกิน budget → `Exceeded USD budget` สรุปไม่จบ → session log หายไป 5 สัปดาห์ เคยเพิ่มเป็น $1.50 ผู้ใช้บอก "ไม่ได้เสียเงินอยู่แล้ว ดันให้เต็มเลย" → เปลี่ยนเป็น $10.00

**How to apply:** ห้ามตั้ง budget hook ต่ำเพื่อประหยัด — Max sub ไม่มี per-token billing เพิ่ม ตั้งสูงไว้ให้สรุปจบทุกกรณี ถ้าแก้ hook อย่าลดกลับ
