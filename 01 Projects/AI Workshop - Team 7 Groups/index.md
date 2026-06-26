---
project: AI Workshop - Team 7 Groups
type: workshop
status: planning
created: 2026-06-27
updated: 2026-06-27
tags: [project, workshop, ai, marketing, training]
---

# AI Workshop — ทีมการตลาด 7 กลุ่ม (28 คน)

Workshop สอนใช้ AI ทำงานเป็นทีม โดยใช้บริษัทจำลอง 7 บริษัทเป็นโจทย์ ผู้เรียนแบ่ง 7 กลุ่ม × 4 บทบาท ใช้ ChatGPT Project + AI Prompt Playbook ทำงานตามบทบาท ส่ง 2 deliverable + นำเสนอ

## ไฟล์ใน folder นี้

| ไฟล์ | หน้าที่ |
|---|---|
| [[index]] (ไฟล์นี้) | ภาพรวม project ทั้งหมด |
| `workshop-guide.html` | คู่มือผู้เรียน+ผู้สอน เปิดบนมือถือ/จอใหญ่ได้ มีปุ่ม Copy พรอมต์ |
| `Part1-Example-GreenLeaf.html` | ตัวอย่าง output 4 บทบาทกลุ่ม 1 (HTML สวย ๆ พร้อม Context Paste) |
| [[Project Instructions]] | พรอมต์กลางสำหรับ ChatGPT Project — ใช้ได้ทุกธุรกิจ |
| [[Example Output - Group 1 GreenLeaf]] | ตัวอย่างเดียวกัน เวอร์ชั่น markdown (อ่านใน Obsidian) |
| [[Terminology]] | คำที่ใช้ในวงการ (Context Pack, Project Instructions, Sources, ฯลฯ) |

## โครงสร้างผู้เรียน

```
28 คน → 7 กลุ่ม × 4 บทบาท
แต่ละกลุ่ม = 1 บริษัทจำลอง (ไม่ซ้ำ)
แต่ละคน = 1 บทบาท
```

### 4 บทบาทในทีม
| บทบาท | ใช้ข้อมูลจาก profile | รับผิดชอบ |
|---|---|---|
| **นักการตลาด (Strategist)** | Vision/Mission/USP/Goals | Brand Strategy (Positioning · Identity · Messaging · Value Prop) |
| **นักวิจัยตลาด (Researcher)** | Target/Competitors/Channels | Target Customer (ICP · Journey · Pain Point · Behavior) |
| **นักเขียนคอนเทนต์ (Content)** | Product images + Mood + CI | Communication + Content Plan + Campaign + ภาพคอนเทนต์ |
| **ผู้ช่วยฝ่ายขาย (Sales)** | Portfolio + KPI | Sales & Pricing (Pricing · Promotion · Forecast · Channel) |

## 7 บริษัทจำลอง (โจทย์ของแต่ละกลุ่ม)

| # | บริษัท | หมวด | ตั้งที่ | รายได้/ปี | พนง. |
|---|---|---|---|---|---|
| 1 | GreenLeaf Furniture | เฟอร์นิเจอร์ไม้ | เชียงใหม่ | 320 ลบ. | 85 |
| 2 | PureHarvest Foods | อาหารออร์แกนิก | นครปฐม | 210 ลบ. | 60 |
| 3 | Crystal Homeware | เครื่องครัว/โฮมแวร์ | สมุทรปราการ | 450 ลบ. | 95 |
| 4 | Urban Cycle | จักรยาน/EV bike | กทม. | 280 ลบ. | 70 |
| 5 | Bloom & Co. | ดอกไม้/ของขวัญ | กทม. | 95 ลบ. | 40 |
| 6 | Sunny Pet Nutrition | อาหารสัตว์เลี้ยง | ชลบุรี | 560 ลบ. | 120 |
| 7 | Aroma Mattress | ที่นอน/เครื่องนอน | อยุธยา | 780 ลบ. | 150 |

### Asset ที่แต่ละกลุ่มได้
`~/Desktop/Workshop Company/<1-7>/` ประกอบด้วย:
- `Company Profile/profile.md` — brief ครบ 12 หัวข้อ
- `Logo/` · `CI Branding/` · `Mood Board/` · `Product/` (6 รูปสินค้า)

> Synthetic dataset (AI-generated) — โครงสร้างเหมือนกันเป๊ะ 7 อุตสาหกรรมไม่ทับซ้อน เป้าโต 18-25% ทุกตัว เปรียบเทียบกันได้

## เครื่องมือที่ใช้

### 1. ChatGPT Projects + Project Instructions
ผู้เรียนแต่ละทีมสร้าง ChatGPT Project ตามชื่อบริษัทตัวเอง → Add Sources (profile + asset) → ใส่ Project Instructions (พรอมต์กลางที่ [[Project Instructions]]) → ทุกแชทใน project นั้นรู้บริบทอัตโนมัติ

### 2. AI Prompt Playbook (Google Sheet)
URL: https://docs.google.com/spreadsheets/d/15MKE8aXn2957ZTcBi9OGSGRE18n7MsaVoOm-vzTHZm4
- 4 ชีตหลักตามบทบาท + ชีตเสริม (สารบัญ, Tool Guide, Variable Dictionary, Master Index)
- พรอมต์มี: Use Case · Prompt พร้อมใช้ · ตัวแปร `{{}}` · ตัวอย่าง output · Tips

### 3. Workshop Brief (Google Doc)
URL: https://docs.google.com/document/d/1KJvxB-TvzZVdu7kf63dh7xt1HdbAlsQn5UG6-yoxl2U

## Workflow ของผู้เรียน (4 Parts)

### SETUP — ทำครั้งเดียวก่อนเริ่ม
1. สร้าง ChatGPT Project ตามชื่อบริษัท
2. Add Sources — อัปโหลด profile + Logo + CI + Mood + Product
3. วาง [[Project Instructions]] ใน Project settings
4. ทดสอบ: พิมพ์ "สรุปแบรนด์นี้ 3 บรรทัด" → ถ้าตรง profile = ผ่าน

### PART 1 — แต่ละคนทำงานตามบทบาท (8 สเตป)
- รู้ตัวเอง → เปิด 2 ของ (profile + ชีต Playbook ของบทบาท) → หาพรอมต์ → paste ChatGPT → แทน `{{ตัวแปร}}` → รัน → เก็บลง Doc ส่วนตัว → วนทำจนครบหัวข้อ

### PART 2 — รวมงาน 4 คน เป็นไฟล์สรุปทีม
- เปิดแชทใหม่ใน Project ของทีม
- วาง Context Pack (profile + ผลงาน 4 คน) → ยิง 3 พรอมต์: **Merge & Structure** → **Tighten** → **Self-check**
- ได้ output 3 บล็อก 15 หัวข้อ พร้อมเอาไปทำภาพ

### PART 3 — สร้างภาพ Brand & GTM Proposal (ทีมละ 1 ภาพ)
- ใช้ **Code Interpreter** (Python + matplotlib) เพราะ DALL-E เขียนภาษาไทยยาว ๆ ไม่เป๊ะ
- Layout 3 คอลัมน์ตาม 3 บล็อก → ออกเป็น PNG → iterate ในแชทเดียว

### PART 4 — สร้างภาพคอนเทนต์ (คนละ 1 ภาพ)
- ใช้ **GPT-4o image / DALL-E** + อ้างอิงรูปสินค้า/Mood Board
- 3 พรอมต์: A) สรุปตัวตนแบรนด์ → B) สร้างภาพ → C) ใส่ caption ไทยด้วย Code Interpreter

## Deliverables — ส่งงาน 2 ชิ้น + นำเสนอ

### ชิ้นที่ 1 — Brand & Go-to-Market Proposal (ทีมละ 1 ภาพ)
3 บล็อก ครอบคลุม 15 หัวข้อย่อย:

**Brand Strategy** (เพื่อ "แบรนด์ที่ชัดและต่าง")
- Positioning · Brand Identity · Brand Messaging · Value Proposition

**Target Customer** (เพื่อ "รู้ว่าลูกค้าคือใคร")
- ICP / Persona · Customer Journey · Pain Point · Buying Behavior

**Sales & Marketing Plan** (เพื่อ "สร้าง Awareness → Lead → ยอดขาย")
- Communication · Channel · Content Plan · Campaign · Pricing · Promotion · Sales Forecast

### ชิ้นที่ 2 — ภาพสื่อสารคอนเทนต์ คนละ 1 ภาพ (= 4 ภาพ/ทีม)

## เคล็ดสำคัญ (ที่ trainer ต้องเน้นย้ำ)

- **อย่าใช้ DALL-E ทำภาพ Proposal** — ตัวอักษรไทยเพี้ยน อ่านไม่ออก → ใช้ Code Interpreter
- **อย่ารัน ChatGPT แบบไม่อ่าน profile ก่อน** — output จะลอย
- **หลัง setup Project แล้ว ให้ทดสอบด้วย "สรุปแบรนด์ 3 บรรทัด"** — กันเริ่มงานแล้วผิดบริษัท
- **Iterate ในแชทเดียว** — อย่าสั่งใหม่ทั้งภาพ บอกแค่จุดที่จะแก้

## Open Items (สิ่งที่ trainer ต้องเตรียมเพิ่ม)

- [ ] **Template ภาพนำเสนอเป็นรูปธรรม** (Doc บอกแค่ "ตัวอย่างภาพใช้นำเสนอ" ไม่มีรูปจริง)
- [ ] **Rubric เกณฑ์ให้คะแนน** (ครบ/ชัด/ตรงข้อมูล/สร้างสรรค์)
- [ ] **Run-sheet เวลา** — ยังไม่รู้ workshop กี่ชม.
- [ ] **Checklist ส่งงาน 15 หัวข้อ** ป้องกันกลุ่มส่งไม่ครบ
- [ ] **Team Kit Folder** — โฟลเดอร์พร้อมส่งให้แต่ละกลุ่ม
- [ ] **ตัวอย่าง output ของกลุ่มอื่น** (มีแล้วแค่ GreenLeaf — อาจทำเพิ่ม 1-2 ตัวให้เห็นความต่าง)

## ไฟล์/Asset ที่เกี่ยวข้องนอกโฟลเดอร์

- Asset 7 บริษัท: `~/Desktop/Workshop Company/`
- Workshop Guide (ของจริง): `~/Desktop/Workshop Company/AI-Workshop-Guide.html`
- Part 1 Example (ของจริง): `~/Desktop/Workshop Company/Part1-Example-GreenLeaf.html`
- Prompt Playbook: [Google Sheet](https://docs.google.com/spreadsheets/d/15MKE8aXn2957ZTcBi9OGSGRE18n7MsaVoOm-vzTHZm4)
- Workshop Brief: [Google Doc](https://docs.google.com/document/d/1KJvxB-TvzZVdu7kf63dh7xt1HdbAlsQn5UG6-yoxl2U)
