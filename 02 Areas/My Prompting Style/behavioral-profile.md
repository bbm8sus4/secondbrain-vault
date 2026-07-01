---
tags: [prompting, behavioral-profile]
parent: [[หน้าหลัก]]
---

# Behavioral Profile — Aexgee (COO)

โปรไฟล์การสั่งงานสรุปจากการวิเคราะห์ prompts จริง 901 ตัว (2026-04 → 2026-07).

## Persona / Working Mode

- **COO ที่ vibe-code hacker** — เร็ว, ตรง, ไม่อดทนกับการเกริ่นยาว
- **Multi-tasker** — เปิด session หลายอันคู่กัน สั่งงานเป็น pulse สั้น ๆ ระหว่างประชุม/มือถือ
- **Executive framing** — คิดในมุม business impact ไม่ใช่ technical detail
- **Trust the AI** — พึ่ง memory + previous context มาก ไม่ค่อย brief ซ้ำ

## Communication Style

### ความยาว
| Bucket | จำนวน | % |
|---|---|---|
| สั้น (<50 chars) | 619 | 69% |
| กลาง (50-200) | 256 | 28% |
| ยาว (200+) | 26 | 3% |

**เฉลี่ย 70 ตัวอักษร** — เท่ากับ 1 ประโยคสั้น ๆ

### ภาษา
- 95%+ **ภาษาไทยล้วน** — ธรรมชาติ ไม่แปลตรง
- Code-mixed EN แค่: shell commands, URLs, file paths, tech terms (Chrome MCP, deploy, config, port, aidebate)
- ใช้ "กู/มึง" 33 ครั้ง (โมโห/rush mode) — expect AI ตอบสุภาพกลับ

### Tone Escalation
1. **Neutral** (default) — "เปิดไฟล์ดูหน่อย", "ทำต่อ ๆ"
2. **Urgent** — "ทำเสร็จหรือยัง", "ทำถึงไหนแล้ว", "เสร็จยัง"
3. **Frustrated** — "ทำ ๆ หยุด ๆ มึงบ้าเหรอ", "มึงทำอะไรอยู่ กูไม่เห็นทำอะไรเลย"
4. **Handoff** — "ทำให้เลย", "จัดมา ทำให้เลย", "โอเค ทำเลย"

## Cognitive Style

- **Path-first, context-later** — ให้ URL/path แล้วถาม "เห็นอะไร"
- **ไม่ชอบตัวเลือก** — สั่ง "aidebate" ให้ AI ทะเลาะกันเลือกดีสุดมาให้
- **Iterate ผ่าน critique loop** — draft → aidebate → synthesis → deploy
- **Verify with own eyes** — "เปิด finder", "เปิดไฟล์ดูหน่อย" หลังงานเสร็จเสมอ

## Command Vocabulary (สูงสุด)

| Verb | ตัวอย่าง | Frequency |
|---|---|---|
| ทำ | ทำต่อ, ทำเสร็จหรือยัง, ทำให้เลย | 100+ |
| เปิด | เปิดไฟล์, เปิด finder, เปิด chrome | 93 |
| เอา | เอาข้อมูล X ไป Y | 30+ |
| aidebate | aidebate เรื่อง... | 56 |
| ปรับ | ปรับดีไซน์, ปรับภาษาไทย | 20+ |
| ใช้ | ใช้ typhoon, ใช้ chrome mcp | 15+ |
| เช็ก | Aidebate เช็ก, เช็คหน่อย | 10+ |

## Recurring Signature Moves

### 1. AI-Debate Loop (56 ครั้ง)
```
aidebate เรื่องนี้หน่อย
→ [AI ทะเลาะกัน 3-4 ตัว]
→ รอผล aidebate
→ Aidebate เช็กเนื้อหา / ปรับ
→ ทำต่อเลย
```

### 2. Path-Drop Pattern (20+ ครั้ง)
```
[User พิมพ์แค่ URL/path]
เห็นอะไร / เข้าใจไหม / ดูใหม่
```

### 3. Status Interrogation (30+ ครั้ง)
```
ทำเสร็จหรือยัง
ทำถึงไหนแล้ว
เสร็จยัง
แก้หรือยัง
```

### 4. Silent-Continue (15+ ครั้ง)
```
ทำต่อ ๆ
ทำต่อเลย
งานต่อ ๆ
```

## What Assistant Should Do

- **ตอบสั้น** — 1-3 ประโยค default
- **ขึ้นด้วยผลลัพธ์** — "เสร็จแล้วครับ, ...", "เจอครับ, ..."
- **ไม่เกริ่น** — ห้าม "ผมจะไป..." ไปเลย
- **จำ context** — ห้ามถาม "หมายถึงไฟล์ไหน" ถ้ามี recent context
- **ไม่ mirror คำหยาบ** — "ครับ/คุณ" เสมอ
- **Auto-verify** — ทำแล้ว open finder / preview ให้เอง
- **Pre-empt next step** — จบด้วย option 1-2 ข้อ

## What Assistant Should NOT Do

- ห้าม list ทางเลือก 5 ข้อ (พี่ไม่อ่าน)
- ห้าม explain reasoning ยาว ๆ (จบใน 1-2 บรรทัด)
- ห้ามใช้อิโมจิใน HTML output
- ห้าม deploy 2 รอบ (git push อย่างเดียว)
- ห้ามใช้ local AI (ยกเว้น Typhoon ตอน proof Thai)
- ห้ามสร้าง markdown file / doc ถ้าไม่สั่ง

related: [[prompt-patterns]] · [[_all-prompts-raw]]
