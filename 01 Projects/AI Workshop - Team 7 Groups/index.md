---
project: AI Workshop - Team 7 Groups
type: workshop
status: planning
created: 2026-06-27
tags: [project, workshop, ai, marketing, training]
---

# AI Workshop — ทีมการตลาด 7 กลุ่ม (28 คน)

Workshop สอนใช้ AI ทำงานเป็นทีม โดยใช้บริษัทจำลอง 7 บริษัทเป็นโจทย์ ผู้เรียนแบ่ง 7 กลุ่ม × 4 บทบาท เปิด AI Prompt Playbook แล้วทำงานตามบทบาท สุดท้ายส่ง 2 deliverable + นำเสนอ

## โครงสร้างผู้เรียน

```
28 คน → 7 กลุ่ม × 4 บทบาท
แต่ละกลุ่ม = 1 บริษัทจำลอง (ไม่ซ้ำ)
แต่ละคน = 1 บทบาท
```

### 4 บทบาทในทีม
| บทบาท | ใช้ข้อมูลจาก profile | รับผิดชอบ |
|---|---|---|
| **นักการตลาด (Strategist)** | Vision/Mission/USP/Goals | Brand Strategy |
| **นักวิจัยตลาด (Researcher)** | Target/Competitors/Channels | Target Customer |
| **นักเขียนคอนเทนต์ (Content)** | Product images + Mood + CI | Content + Communication |
| **ผู้ช่วยฝ่ายขาย (Sales)** | Portfolio + KPI | Sales & Pricing |

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
- `Company Profile/profile.md` — brief ครบ 12 หัวข้อ (Vision, Mission, USP, Target, Competitors 5 ราย, KPI, Goals)
- `Logo/` — โลโก้
- `CI Branding/` — รูปแบบ identity
- `Mood Board/` — อารมณ์แบรนด์
- `Product/` — 6 รูปสินค้า

> หมายเหตุ: เป็น synthetic dataset (AI-generated) ออกแบบให้เปรียบเทียบกันได้ — โครงสร้างเหมือนกันเป๊ะ, 7 อุตสาหกรรมไม่ทับซ้อน, ตัวเลขถูก calibrate ให้สมจริง (เป้าโต 18-25% ทุกตัว)

## เครื่องมือที่ใช้

### AI Prompt Playbook (Google Sheet)
URL: https://docs.google.com/spreadsheets/d/15MKE8aXn2957ZTcBi9OGSGRE18n7MsaVoOm-vzTHZm4

โครงสร้าง:
- 4 ชีตหลักตามบทบาท (Strategist / Researcher / Content / Sales)
- แต่ละพรอมต์มี: Use Case · Prompt พร้อมใช้ · ตัวแปร `{{}}` · ตัวอย่างผลลัพธ์ · Tips
- ชีตเสริม: 01 สารบัญ · 05 AI Tool Guide · 06 Variable Dictionary · 07 Master Index · 23 Version Control

**Flow ของผู้เรียน:** Copy พรอมต์ → แทน `{{ตัวแปร}}` ด้วยข้อมูลใน profile.md → รัน AI (ChatGPT/Claude/Gemini) → ได้ output

### Workshop Brief (Google Doc)
URL: https://docs.google.com/document/d/1KJvxB-TvzZVdu7kf63dh7xt1HdbAlsQn5UG6-yoxl2U

## Deliverables — ส่งงาน 2 ชิ้น + นำเสนอ

### ชิ้นที่ 1 — Brand & Go-to-Market Proposal (ทีมละ 1 ภาพ)

3 บล็อกใหญ่ ครอบคลุม 15 หัวข้อย่อย:

**Brand Strategy** (เพื่อ "แบรนด์ที่ชัดและต่าง")
- Positioning
- Brand Identity
- Brand Messaging
- Value Proposition

**Target Customer** (เพื่อ "รู้ว่าลูกค้าคือใคร")
- ICP / Persona
- Customer Journey
- Pain Point
- Buying Behavior

**Sales & Marketing Plan** (เพื่อ "สร้าง Awareness → Lead → ยอดขาย")
- Communication Strategy
- Channel Strategy
- Content Plan
- Campaign Plan
- Pricing Strategy
- Promotion Strategy
- Sales Forecast

### ชิ้นที่ 2 — ภาพสื่อสารคอนเทนต์ คนละ 1 ภาพ (= 4 ภาพ/ทีม)

## Mapping งาน → บทบาท

```
Strategist  →  Brand Strategy (Positioning · Identity · Messaging · Value Prop)
Researcher  →  Target Customer (ICP · Journey · Pain Point · Behavior)
Sales       →  Sales & Marketing Plan (Pricing · Promotion · Forecast · Channel)
Content     →  Communication + Content Plan + Campaign + คุมภาพคอนเทนต์ทีม
```

ทุกคนใน 4 บทบาทยังต้องส่ง **ภาพคอนเทนต์คนละ 1 ภาพ** เพิ่ม (ชิ้นที่ 2)

## Open Items (สิ่งที่ trainer ต้องเตรียมเพิ่ม)

ของที่ workshop brief ยังไม่ครอบ — ควรเติมก่อนวันจริง:

- [ ] **Template ภาพนำเสนอเป็นรูปธรรม** (Doc บอกแค่ "ตัวอย่างภาพใช้นำเสนอ" ไม่มีรูปจริง) → ผู้เรียนจะออกแบบไม่ตรงกัน เทียบยาก
- [ ] **Rubric เกณฑ์ให้คะแนน** (ครบ/ชัด/ตรงข้อมูล/สร้างสรรค์)
- [ ] **Run-sheet เวลา** — ยังไม่รู้ workshop กี่ชม. (ครึ่งวัน/เต็มวัน/2 วัน)
- [ ] **Checklist ส่งงาน 15 หัวข้อ** ป้องกันกลุ่มส่งไม่ครบ
- [ ] **Team Kit Folder** — โฟลเดอร์พร้อมส่งให้แต่ละกลุ่ม (profile + asset + worksheet + Quick Start)

## ขั้นต่อไป

1. ขอข้อมูลเวลา workshop จาก trainer
2. ออกแบบ Proposal Template (HTML 1 หน้า ที่ผู้เรียนแค่กรอกข้อความ → ออกมาเป็น "ทีมละ 1 ภาพ")
3. ทำ Worksheet 4 หน้าสำหรับ 4 บทบาท
4. ทำ Trainer Run-Sheet + Rubric

## ไฟล์/Asset ที่เกี่ยวข้อง

- Asset 7 บริษัท: `~/Desktop/Workshop Company/`
- Prompt Playbook: [Google Sheet](https://docs.google.com/spreadsheets/d/15MKE8aXn2957ZTcBi9OGSGRE18n7MsaVoOm-vzTHZm4)
- Workshop Brief: [Google Doc](https://docs.google.com/document/d/1KJvxB-TvzZVdu7kf63dh7xt1HdbAlsQn5UG6-yoxl2U)
