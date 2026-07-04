---
name: reference_model_config_fix
description: "Fable 5 IS available (trust the /model picker, not the stale disabled flag in ~/.claude.json cache). All 4 config dirs pinned to claude-fable-5[1m]."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1f995c76-07d7-4e94-8d25-4e118177716b
---

**2026-07-04:** แก้ปัญหา model pin. อาการ: `/model` เลือก Fable 5 แต่ restart แล้วเด้งกลับ + คนละเทอร์มินัลได้คนละโมเดล.

**ต้นตอ 2 ชั้น:**
1. **⚠️ แก้ 2026-07-04: Fable 5 ใช้ได้จริง** — picker `/model` โชว์ Fable (ข้อ 3) เลือกได้ปกติ. **`~/.claude.json` → `additionalModelOptionsCache` `disabled:True` เป็น cache เก่า/stale — อย่าเชื่อ! ให้ดู live picker เป็นหลัก.** (ก่อนหน้าผมวินิจฉัยพลาดว่า Fable ปิด เพราะเชื่อ cache นี้ → ตั้ง opus ผิด → user โมโห). id ของ Fable = `claude-fable-5[1m]`.
2. **model pin ไม่ตรงกัน 4 dir**: `.claude`=sonnet · `.claude-warp`=claude-fable-5[1m] · `.claude-ghostty`=none · `.claude-cmux`=**claude-opus-4-6 (id ผิด ไม่มีจริง)**.

**ที่ทำ (สุดท้าย):** set `"model": "claude-fable-5[1m]"` (= Fable 5 ตามที่ user ต้องการ) ครบทั้ง 4 dir. Backup ค่าเดิม: `settings.json.bak-modelfix`. มีผลตอน session ใหม่ · session ปัจจุบันสลับได้เลยด้วย `/model` → กด 3.

**บทเรียน:** อย่าเชื่อ `disabled` flag ใน `additionalModelOptionsCache` — ให้เชื่อ live `/model` picker. อยากคุมด้วย `/model` ล้วน ๆ ไม่ให้ settings ทับ → ลบ key `model` ออกทุก dir. ดู [[Model Shift × cmux patch|project_modelshift_cmux]].
