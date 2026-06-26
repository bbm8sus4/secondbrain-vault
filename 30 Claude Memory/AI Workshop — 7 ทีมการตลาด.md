---
name: project-ai-workshop-7teams
description: "AI Workshop ทีมการตลาด 28 คน, 7 กลุ่ม × 4 บทบาท. โจทย์ = 7 บริษัทจำลอง. ใช้ ChatGPT Project + Project Instructions กลาง + AI Prompt Playbook. ส่ง Brand+GTM Proposal + ภาพคอนเทนต์"
metadata: 
  node_type: memory
  type: project
  originSessionId: f5e5c087-385d-450d-8885-2b6b9173d67e
---

# AI Workshop — ทีมการตลาด 7 กลุ่ม

Workshop สอนใช้ AI ทำงานเป็นทีม โดยใช้บริษัทจำลอง 7 บริษัทเป็นโจทย์

## โครงสร้าง
- **28 คน → 7 กลุ่ม × 4 บทบาท** (Strategist · Researcher · Content · Sales)
- แต่ละกลุ่ม = 1 บริษัทจำลอง ไม่ซ้ำ

## Workflow (4 Parts)
1. **SETUP** — สร้าง ChatGPT Project ของบริษัท · Add Sources (profile + asset) · วาง Project Instructions กลาง
2. **PART 1** — 8 สเตป แต่ละคนรันพรอมต์ของบทบาทตัวเอง
3. **PART 2** — รวม output 4 คน → ยิงพรอมต์ Merge → Tighten → Self-check
4. **PART 3-4** — สร้างภาพ Proposal (Code Interpreter เพราะ DALL-E ไทยเพี้ยน) + ภาพคอนเทนต์ (GPT-4o image)

## Asset/Tools
- **โจทย์ 7 บริษัท:** `~/Desktop/Workshop Company/<1-7>/` (profile.md + Logo + CI + Mood + 6 product images)
- **Workshop Guide (HTML):** `~/Desktop/Workshop Company/AI-Workshop-Guide.html` — คู่มือเต็มมีปุ่ม Copy ทุกพรอมต์
- **Part 1 Example (HTML):** `~/Desktop/Workshop Company/Part1-Example-GreenLeaf.html` — ตัวอย่าง output 4 บทบาทกลุ่ม 1
- **AI Prompt Playbook (Google Sheet):** https://docs.google.com/spreadsheets/d/15MKE8aXn2957ZTcBi9OGSGRE18n7MsaVoOm-vzTHZm4
- **Workshop Brief (Google Doc):** https://docs.google.com/document/d/1KJvxB-TvzZVdu7kf63dh7xt1HdbAlsQn5UG6-yoxl2U
- **Knowledge Base (Obsidian):** `~/SecondBrain/01 Projects/AI Workshop - Team 7 Groups/`
  - `index.md` (ภาพรวม) · `Project Instructions.md` (พรอมต์กลาง) · `Example Output - Group 1 GreenLeaf.md` · `Terminology.md` (Context Pack vs Brief)

## Deliverables (ส่ง 2 ชิ้น + นำเสนอ)
1. **Brand & GTM Proposal** (ทีมละ 1 ภาพ) — 3 บล็อก 15 หัวข้อย่อย
2. **ภาพคอนเทนต์ คนละ 1 ภาพ** (= 4 ภาพ/ทีม)

## 7 บริษัท
1. GreenLeaf Furniture (เฟอร์ไม้, เชียงใหม่) · 2. PureHarvest Foods (ออร์แกนิก, นครปฐม) · 3. Crystal Homeware (ครัว, สมุทรปราการ) · 4. Urban Cycle (จักรยาน, กทม.) · 5. Bloom & Co. (ดอกไม้, กทม.) · 6. Sunny Pet Nutrition (อาหารสัตว์, ชลบุรี) · 7. Aroma Mattress (ที่นอน, อยุธยา)

## สไตล์ HTML guide
- Dark mode + IBM Plex Sans Thai + accent purple/green
- Hero gradient + section labels UPPERCASE + cards
- ไม่ใส่ emoji · มี copy button ทุก prompt block
- ไฟล์อ้างอิงสไตล์: `~/reve2-guide.html`, `~/bni-thunder-5min.html`

## เคล็ดสำคัญ
- ห้ามใช้ DALL-E ทำภาพ Proposal (text-heavy ไทย → เพี้ยน) → ต้องใช้ Code Interpreter
- หลัง setup Project ต้องทดสอบด้วย "สรุปแบรนด์ 3 บรรทัด" ก่อนเข้า Part 1
- Iterate ในแชทเดียว อย่าสั่งใหม่ทั้งภาพ

## Open Items
ยังไม่มี: Template proposal รูปธรรม · Rubric · Run-sheet เวลา · Checklist ส่งงาน · Team Kit folder · ตัวอย่าง output กลุ่มอื่น
