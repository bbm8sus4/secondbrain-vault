---
title: Claude Code — Model × Effort อธิบายแบบเปรียบเทียบ
type: reference
tags: [claude-code, models, effort, workshop, analogy, teaching]
saved: 2026-07-11
---

# Claude Code — Model × Effort อธิบายแบบเปรียบเทียบ

> **Model = เครื่องยนต์** (กำหนดพลังสูงสุดที่มี)
> **Effort = คันเร่ง** (กำหนดว่าจะใช้พลังนั้นแค่ไหน)

---

## Model = เครื่องยนต์

### Fable 5 — เครื่อง F1

```
claude --model claude-fable-5
```

- แรงที่สุดในโลก ไม่มีใครเทียบ
- กินน้ำมัน (token) มากที่สุด — $10/$50 ต่อ 1M tokens
- ปิดเครื่องไม่ได้ (thinking เปิดตลอด)
- ใช้กับสนามแข่งจริงๆ เท่านั้น: reasoning ซับซ้อนสุด, งานที่ต้องทำหลายชั่วโมงต่อเนื่อง
- เหมือน F1 ที่ใช้บนถนนปกติ = เปลืองเปล่า

### Opus 4.8 — เครื่อง V8 Supercar

```
claude --model claude-opus-4-8
```

- แรง ทนทาน ขับได้ทุกสถานการณ์
- ราคาสมเหตุสมผล — $5/$25 ต่อ 1M tokens
- ตัวเลือกหลักสำหรับทุกงาน
- เหมือน V8 ที่ขับได้ทั้งในเมืองและสนามแข่ง

### Sonnet 5 — เครื่อง Turbo 4 สูบ

```
claude --model claude-sonnet-5
```

- เร็ว ประหยัด แต่แรงใกล้เคียง V8
- ถูกกว่าครึ่ง — $2/$10 ต่อ 1M tokens (ราคา intro)
- เหยียบเต็มที (effort high) แข่งกับ V8 ขับชิลล์ (effort medium) ได้
- คุ้มค่าที่สุดในทุกโมเดล

### Haiku 4.5 — เครื่องมอเตอร์ไซค์

```
claude --model claude-haiku-4-5
```

- เบา เร็ว ถูก
- ถูกสุด — $1/$5 ต่อ 1M tokens
- Context เล็กกว่า (200K แทน 1M)
- เหมาะวิ่งสั้นๆ: classify, extract, ถาม-ตอบง่าย
- ไม่เหมาะบรรทุกหนัก (coding ซับซ้อน, research ลึก)

---

## Effort = คันเร่ง

เครื่องยนต์เดียวกัน คันเร่งต่างกัน ผลต่างกัน:

### low — เหยียบนิดเดียว ขับในเมือง

```
/effort low
```

- เร็วสุด ประหยัด token สุด
- คิดไม่ลึก ตอบสั้น
- เหมาะ: chat ง่ายๆ, classify, lookup
- ระวัง: งานซับซ้อนจะคิดไม่พอ

### medium — ขับปกติบนถนนหลวง

```
/effort medium
```

- สมดุลดี ระหว่างเร็วกับฉลาด
- เหมาะ: งานทั่วไปที่ไม่ต้องคิดหนักมาก
- Sonnet 5 ที่ medium ≈ Sonnet 4.6 ที่ high

### high — เหยียบเต็มบนทางด่วน (ค่าเริ่มต้น)

```
/effort high
```

- ค่าเริ่มต้นของทุกโมเดล
- คิดละเอียด ตอบดี ครอบคลุม
- เหมาะ: งานส่วนใหญ่ 80% ของเวลา
- แนะนำเริ่มที่นี่แล้วปรับขึ้น/ลงตามงาน

### xhigh — โหมด Sport บนสนาม

```
/effort xhigh
```

- สำหรับ coding และ agentic ยากๆ
- ใช้ได้กับ Opus 4.7+ และ Sonnet 5 เท่านั้น
- Claude Code ใช้ level นี้เป็น default ของตัวเอง
- เหมาะ: debug ยากๆ, refactor ซับซ้อน, multi-step agent

### max — เหยียบจนสุด red line

```
/effort max
```

- แม่นที่สุดเท่าที่เป็นไปได้
- กิน token มากที่สุด
- บางทีคิดมากเกินไป (overthinking)
- เหมาะ: งานที่ถูกต้องสำคัญกว่าเร็ว (audit, compliance)

---

## ภาพรวม: Model × Effort

```
     ┌─────────────────────────────────────────────────┐
     │              ฉลาด / แม่นยำ                        │
     │                   ▲                              │
     │                   │                              │
     │  Fable+max ──────●                               │
     │                   │                              │
     │  Opus+xhigh ─────●                               │
     │                   │                              │
     │  Opus+high ───────●── Sonnet+xhigh               │
     │                   │                              │
     │  Opus+medium ─────●── Sonnet+high                 │
     │                   │                              │
     │  Sonnet+medium ───●── Opus+low                    │
     │                   │                              │
     │  Haiku+high ──────●                               │
     │                   │                              │
     │  Haiku+low ───────●                               │
     │                   │                              │
     │──────────────────►                               │
     │   เร็ว / ถูก                                      │
     └─────────────────────────────────────────────────┘
```

จุดสำคัญ: **Sonnet 5 + high ≈ Opus 4.8 + medium** — Turbo เหยียบเต็มแข่งกับ V8 ขับชิลล์ ผลใกล้กัน

---

## สูตรเลือกใช้จริง

```
ผลลัพธ์ = เครื่องยนต์ (Model) × คันเร่ง (Effort)
```

### ตามประเภทงาน

| งาน | Model | Effort | เปรียบเหมือน |
|---|---|---|---|
| ถามสั้นๆ / classify | Haiku 4.5 | low | มอไซค์วิ่งซอย |
| Chat / Q&A ทั่วไป | Sonnet 5 | low | Turbo ขับในเมือง |
| เขียน content / สรุป | Sonnet 5 | medium | Turbo ขับทางหลวง |
| Coding ทั่วไป | Opus 4.8 | high | V8 ทางด่วน |
| Debug / Refactor ยากๆ | Opus 4.8 | xhigh | V8 โหมด Sport |
| Code Review ละเอียด | Opus 4.8 | xhigh | V8 สนามแข่ง |
| Multi-agent workers | Sonnet 5 | high | Turbo 10 คันวิ่งพร้อมกัน |
| Research ลึก | Opus 4.8 | max | V8 เหยียบสุด |
| Audit ทั้ง repo | Fable 5 | high | F1 เต็มสนาม |
| งานที่โมเดลอื่นทำไม่ได้ | Fable 5 | max | F1 red line |

### ตามงบ (สำหรับ API — Max sub ไม่กระทบ)

| งบ | แนะนำ | เหตุผล |
|---|---|---|
| ประหยัดสุด | Haiku + low | $1/$5 + คิดน้อย = ถูกมาก |
| คุ้มค่าสุด | Sonnet 5 + high | $2/$10 + คุณภาพใกล้ Opus |
| สมดุล | Opus 4.8 + high | $5/$25 + ทำได้ทุกอย่าง |
| ไม่สนราคา | Fable 5 + max | $10/$50 + ดีที่สุดเท่าที่เป็นไปได้ |

---

## เทคนิคขั้นสูง: ผสมใช้ในงานเดียวกัน

เหมือนทีมแข่งที่ใช้รถต่างกันตามสถานการณ์:

### ตัวอย่าง: Review โค้ดแบบ Multi-Agent

```
Orchestrator (สั่งงาน)     = Opus 4.8 + high      ← V8 เป็นหัวหน้า
Workers 3 ตัว (หา bugs)    = Sonnet 5 + high       ← Turbo 3 คันค้นหา
Synthesizer (รวมผล)        = Opus 4.8 + xhigh      ← V8 Sport สรุป
```

ประหยัดกว่าใช้ Opus ทุกตัว แต่ผลดีเท่ากัน

### ตัวอย่าง: พัฒนา Feature ใหม่

```
1. /plan          → Opus + high       วางแผน (ต้องคิดดี)
2. coding         → Opus + xhigh      เขียนโค้ด (ต้องแม่น)
3. /recheck       → Sonnet + high     ตรวจหลังแก้ (เร็วพอ)
4. /code-review   → Opus + xhigh      review สุดท้าย
5. /deploy        → Haiku + low       deploy (ไม่ต้องคิดมาก)
```

---

## คำสั่งที่เกี่ยวข้อง

```bash
# เลือกโมเดลตอนเปิด
claude --model claude-opus-4-8

# เปลี่ยนระหว่างใช้งาน
/model opus
/model sonnet
/model haiku

# ปรับ effort
/effort low
/effort high
/effort xhigh

# เปิด Fast Mode (Opus 4.8/4.7 เท่านั้น)
/fast
```

---

## สรุป 1 บรรทัด

> **เลือกเครื่องยนต์ตามงาน เหยียบคันเร่งตามความยาก**
> Opus + high คือค่าเริ่มต้นที่ดีสำหรับ 80% ของงาน ปรับจากตรงนี้

---

*ดูเพิ่ม: [[Claude Code — Model Reference]] | [[Claude Code — Skills & Commands Reference]] | [[Claude Code Multi-Agent Workflow Guide]]*
