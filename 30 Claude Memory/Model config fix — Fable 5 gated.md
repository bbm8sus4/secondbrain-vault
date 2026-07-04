---
name: reference_model_config_fix
description: "Fable 5 is gated/unavailable on this account (silent fallback). All 4 Claude config dirs unified to `opus` alias to stop inconsistent pins overriding model choice."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1f995c76-07d7-4e94-8d25-4e118177716b
---

**2026-07-04:** แก้ปัญหา model pin. อาการ: `/model` เลือก Fable 5 แต่ restart แล้วเด้งกลับ + คนละเทอร์มินัลได้คนละโมเดล.

**ต้นตอ 2 ชั้น:**
1. **Fable 5 gated** — `~/.claude.json` → `additionalModelOptionsCache` มี `claude-fable-5[1m]` `disabled:True` "Claude Fable 5 is currently unavailable" (ลิงก์ anthropic.com/news/fable-mythos-access). เลือก Fable → fallback เงียบ ๆ เป็น Opus 4.8. **แก้ที่ config ไม่ได้ — เป็น account-level access gate.**
2. **model pin ไม่ตรงกัน 4 dir**: `.claude`=sonnet · `.claude-warp`=claude-fable-5[1m] · `.claude-ghostty`=none · `.claude-cmux`=**claude-opus-4-6 (id ผิด ไม่มีจริง)**.

**ที่ทำ:** set `"model": "opus"` (alias → Opus 4.8 ล่าสุด, auto-upgrade) ให้ครบทั้ง 4 dir. Backup: `settings.json.bak-modelfix` ในแต่ละ dir. มีผลตอน session ใหม่.

**How to apply:** ถ้า Fable 5 เปิดให้ใช้เมื่อไหร่ → เปลี่ยน `model` เป็น `claude-fable-5[1m]` ทั้ง 4 dir (หรือใช้ Model Shift). อยากคุมด้วย `/model` ล้วน ๆ ไม่ให้ settings ทับ → ลบ key `model` ออกทุก dir. ดู [[Model Shift × cmux patch|project_modelshift_cmux]].
