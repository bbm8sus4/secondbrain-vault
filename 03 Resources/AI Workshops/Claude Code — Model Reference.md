---
title: Claude Code — Model Reference
type: reference
tags: [claude-code, models, workshop, reference]
saved: 2026-07-11
---

# Claude Code — Model Reference

## วิธีเลือกโมเดลใน Claude Code

```bash
# เปิด Claude Code พร้อมเลือกโมเดล
claude --model <model-id>

# หรือเปลี่ยนระหว่างใช้งาน
/model
```

---

## โมเดลทั้งหมดที่ใช้ได้ (กลางปี 2026)

### Tier 1: Fable — แรงสุด แพงสุด

```bash
claude --model claude-fable-5
```

| รายละเอียด | ค่า |
|---|---|
| Context Window | 1M tokens |
| Max Output | 128K tokens |
| Input / Output | $10 / $50 ต่อ 1M tokens |
| จุดเด่น | Reasoning ยากสุด, Long-horizon agentic work |
| ข้อจำกัด | ปิด thinking ไม่ได้, ต้อง 30-day data retention |

---

### Tier 2: Opus — สมดุลที่สุด (แนะนำ)

```bash
claude --model claude-opus-4-8    # ใหม่สุด แนะนำ
claude --model claude-opus-4-7
claude --model claude-opus-4-6    # ตัวที่ใช้อยู่ปัจจุบัน
```

| รายละเอียด | ค่า |
|---|---|
| Context Window | 1M tokens |
| Max Output | 128K tokens |
| Input / Output | $5 / $25 ต่อ 1M tokens |
| จุดเด่น | Coding, Agentic, Knowledge work, Memory |

**ความแตกต่างระหว่าง version:**

| Feature | 4.6 | 4.7 | 4.8 |
|---|---|---|---|
| Adaptive Thinking | รองรับ | บังคับ (budget_tokens ใช้ไม่ได้) | บังคับ |
| Temperature/top_p | ใช้ได้ | ใช้ไม่ได้ (400 error) | ใช้ไม่ได้ |
| High-res Vision (2576px) | ไม่มี | มี | มี |
| Fast Mode | ไม่มี | มี | มี |
| Mid-session System Prompt | ไม่มี | ไม่มี | มี |
| Effort levels | low/medium/high/max | +xhigh | +xhigh |

---

### Tier 3: Sonnet — เร็ว คุ้มค่า

```bash
claude --model claude-sonnet-5     # ใหม่สุด ใกล้เคียง Opus
claude --model claude-sonnet-4-6
```

| รายละเอียด | Sonnet 5 | Sonnet 4.6 |
|---|---|---|
| Context Window | 1M | 1M |
| Max Output | 128K | 128K |
| Input / Output | $2/$10 (intro) | $3/$15 |
| Thinking default | เปิดอัตโนมัติ | ปิด |
| High-res Vision | มี (2576px) | ไม่มี |
| Effort levels | low-max +xhigh | low-max |

---

### Tier 4: Haiku — เร็วสุด ถูกสุด

```bash
claude --model claude-haiku-4-5
```

| รายละเอียด | ค่า |
|---|---|
| Context Window | 200K tokens |
| Max Output | 64K tokens |
| Input / Output | $1 / $5 ต่อ 1M tokens |
| จุดเด่น | งานง่าย เร็ว classify/extract/chat |

---

## เปรียบเทียบทุกโมเดล

| Model | Context | Output | $/1M In | $/1M Out | เหมาะกับ |
|---|---|---|---|---|---|
| `claude-fable-5` | 1M | 128K | $10 | $50 | Reasoning ยากสุด |
| `claude-opus-4-8` | 1M | 128K | $5 | $25 | งานทั่วไป ดีที่สุด |
| `claude-opus-4-7` | 1M | 128K | $5 | $25 | Coding/Agentic |
| `claude-opus-4-6` | 1M | 128K | $5 | $25 | Stable ใช้มานาน |
| `claude-sonnet-5` | 1M | 128K | $2 | $10 | เร็ว+ฉลาด คุ้มสุด |
| `claude-sonnet-4-6` | 1M | 128K | $3 | $15 | Balanced |
| `claude-haiku-4-5` | 200K | 64K | $1 | $5 | เร็ว ถูก งานเบา |

---

## แนะนำเลือกตามงาน

| งาน | โมเดลแนะนำ | เหตุผล |
|---|---|---|
| Coding / Debug | `claude-opus-4-8` | แม่นยำ ฉลาด |
| Code Review | `claude-opus-4-8` | หา bug เก่ง |
| Research / Analysis | `claude-fable-5` | Reasoning ลึก |
| Quick Chat / Q&A | `claude-haiku-4-5` | เร็ว ถูก |
| Content Writing | `claude-sonnet-5` | เขียนดี คุ้ม |
| Multi-agent Workers | `claude-sonnet-5` | เร็ว คุณภาพดี ต้นทุนต่ำ |
| Long-horizon Agent | `claude-fable-5` | ทำงานนานหลายนาทีได้ |

---

## คำสั่งเปลี่ยนโมเดลระหว่างใช้งาน

```
/model                    # เลือกจาก picker
/model opus               # เปลี่ยนเป็น Opus (ล่าสุด)
/model sonnet             # เปลี่ยนเป็น Sonnet
/model haiku              # เปลี่ยนเป็น Haiku
```

## คำสั่งปรับ Effort

```
/effort low               # เร็ว ประหยัด
/effort medium            # สมดุล
/effort high              # ค่าเริ่มต้น
/effort xhigh             # Coding/Agentic (Opus 4.7+ / Sonnet 5)
/effort max               # แม่นสุด แพงสุด
```

---

## หมายเหตุ

- ถ้าใช้ **Claude Max subscription** ราคาไม่กระทบ (จ่ายรายเดือนอยู่แล้ว)
- ราคาข้างบนเป็นราคา API สำหรับกรณีเรียกใช้ตรง
- `claude-opus-4-5` / `claude-sonnet-4-5` ยังใช้ได้แต่เป็น legacy
- `claude-opus-4-0` / `claude-sonnet-4-0` กำลังจะ retire
- **ห้ามต่อท้าย date suffix** เช่น `claude-opus-4-8-20251101` — ใช้ alias ตรงๆ เท่านั้น
