# 📦 คู่มือ — Claude Skills สำหรับ COO

> คัดจาก 3 แหล่ง: bundle 501 สกิลในเครื่อง · สกิลทางการ Anthropic · ตัวฮิตในชุมชน
> อัปเดต: 2026-06-12

## กฎเหล็กก่อนติดตั้ง

- **อย่าติดตั้งเกิน ~8–12 สกิล** — ทุกสกิลที่ติดตั้งกินโทเคน context ทุก session แม้ไม่ได้ใช้ (community เรียกว่า "context tax")
- ติดตั้ง = คัดลอกโฟลเดอร์สกิล (ที่มี `SKILL.md`) ไป `~/.claude/skills/` แล้วเปิด session ใหม่
- สกิลที่ใช้นานๆ ครั้ง **ไม่ต้องติดตั้ง** — ชี้ path ให้ Claude อ่านตรงๆ ได้เลย เช่น
  `อ่าน ~/Claude Skills Ultimate Bundle/Operations & Systems/decision-matrix/SKILL.md แล้วทำตาม`

---

## 1) ของที่มีในเครื่องอยู่แล้ว — Claude Skills Ultimate Bundle (501 สกิล)

Path: `~/Claude Skills Ultimate Bundle/` · 20 หมวด · ทุกตัวเป็น SKILL.md มาตรฐาน คัดลอกใช้ได้ทันที

### ตัวเด็ดสำหรับงาน COO (คัดแล้ว)

**บริหาร / Operations** (`Operations & Systems/`)
- `decision-matrix` — ตารางถ่วงน้ำหนักตัดสินใจ เลือก vendor / เครื่องมือ / กลยุทธ์ แบบไม่ใช้อารมณ์
- `weekly-report` + `status-update-template` — รายงานประจำสัปดาห์ให้ทีม/บอร์ด
- `meeting-agenda` + `meeting-notes` — คู่กับระบบ [[40 Meeting Notes]] ที่มีอยู่
- `sop-builder` — เขียน SOP ให้ทีม (เหมาะกับ EasySlip/Thunder ที่ทีมโต)
- `risk-assessment` — ประเมินความเสี่ยงก่อนตัดสินใจใหญ่
- `vendor-evaluation` + `vendor-onboarding` — คัดเลือก/รับ vendor ใหม่
- `delegation-framework` — กรอบมอบหมายงาน
- `annual-planning` — วางแผนประจำปี

**การเงิน** (`Finance & Pricing/`)
- `cash-flow-forecast` — สำคัญมากกับธุรกิจ pre-paid cycle แบบ Thunder
- `unit-economics` — ต่อยอดจากงาน EasyBOT ที่ขาดทุน ฿3.1M
- `revenue-forecast` — คู่กับเป้า ฿125M/ปี
- `financial-dashboard` + `quarterly-review` — รีวิวรายไตรมาส
- `pricing-strategy` + `pricing-analysis` — ปรับ package EasyCRM/BoostSMS
- `investor-update` — รายงานผู้ถือหุ้น/บอร์ด

**HR / ทีม** (`HR & Team/`)
- `okr-builder` — ตั้ง OKR ทั้งบริษัท
- `hiring-scorecard` + `interview-question-bank` — จ้างคนแบบมีเกณฑ์
- `one-on-one-template` + `performance-review` — ดูแลทีม
- `onboarding-checklist` — รับพนักงานใหม่

**ข้อมูล / Analytics** (`Analytics & Data/`)
- `kpi-dashboard` + `saas-metrics-dashboard` — metrics ธุรกิจ SaaS (ตรงกับ EasySlip)
- `cohort-analysis` + `customer-lifetime-value` — วิเคราะห์ลูกค้า
- `survey-analysis` + `feedback-analysis` — อ่านผล survey ลูกค้า/พนักงาน

### วิธีติดตั้งจาก bundle

```bash
cp -R ~/Claude\ Skills\ Ultimate\ Bundle/"Operations & Systems"/decision-matrix ~/.claude/skills/
```

---

## 2) สกิลทางการจาก Anthropic — เอกสาร Office จริง

Repo: [github.com/anthropics/skills](https://github.com/anthropics/skills) · ฟรี Apache 2.0 · 17 สกิล

ตัวที่คุ้มสุดสำหรับผู้บริหาร (ชุมชนยกให้เป็น skill ที่คนใช้เยอะสุด):

| สกิล | ได้อะไร |
|---|---|
| `xlsx` | สร้าง/แก้ Excel จริง พร้อมสูตร + format + pivot |
| `pptx` | สร้างสไลด์ PowerPoint จริง (ส่งต่อให้คนอื่นแก้ได้ ต่างจาก HTML slides) |
| `docx` | เอกสาร Word พร้อม styles + tracked changes |
| `pdf` | สร้าง/กรอกฟอร์ม/ดึงข้อมูลจาก PDF |
| `doc-coauthoring` | เขียนเอกสารแบบมีโครง: context → outline → draft |

```bash
git clone https://github.com/anthropics/skills.git /tmp/anthropic-skills
cp -R /tmp/anthropic-skills/skills/xlsx ~/.claude/skills/
cp -R /tmp/anthropic-skills/skills/pptx ~/.claude/skills/
```

หมายเหตุ: งานสไลด์ปัจจุบันใช้ HTML (ดู [[คู่มือ - สไลด์ HTML ปิดบังตัวเลข]]) — `pptx` เหมาะตอนต้องส่งไฟล์ให้ทีมแก้เองต่อ

---

## 3) ตัวฮิตในชุมชน (สาย dev เป็นหลัก — รู้ไว้พอ)

- **superpowers** ([github.com/obra/superpowers](https://github.com/obra/superpowers)) — ฮิตสุดในตลาด (90k+ stars) บังคับ workflow clarify → spec → plan → execute เหมาะงานเขียนโค้ดจริงจัง ไม่ใช่งานบริหาร
- **web-design-guidelines** ([vercel-labs](https://github.com/vercel-labs/web-interface-guidelines)) — มาตรฐาน UI ของ Vercel ติดตั้งแล้ว dashboard/HTML ที่ให้ Claude ทำจะสวยขึ้นแบบมีหลักการ — **อันนี้เกี่ยวกับเราตรงๆ** เพราะทำ HTML dashboard บ่อย
- **frontend-design** (Anthropic official) — คล้ายกัน เน้นให้ UI ไม่ติด default ai-look

---

## ชุดแนะนำให้เริ่ม (ติดตั้งจริง 5 ตัว)

1. `xlsx` (Anthropic) — รายงานการเงิน/DB ส่งทีมได้เลย
2. `pptx` (Anthropic) — เด็คประชุมที่ทีมแก้ต่อได้
3. `decision-matrix` (bundle) — ใช้ทุกครั้งที่เลือก vendor/เครื่องมือ
4. `kpi-dashboard` (bundle) — metrics Thunder/EasySlip/BoostSMS
5. `okr-builder` (bundle) — รอบวางแผนรายไตรมาส

ที่เหลือเรียกใช้แบบชี้ path เอาตามจังหวะงาน ไม่ต้องติดตั้งถาวร

## สกิลที่ติดตั้งอยู่แล้วในเครื่อง (อย่าซ้ำ)

graphify · CRUD-basic · spaghetti-fix · lineoa-chat-mcp · Chrome-MCP-Owly · marketing-plan · telegram-download-pic-block · ai-loop · neomake-cycle · gitnexus (7 ตัว)

---

แหล่งอ้างอิง:
- [Anthropic official skills](https://github.com/anthropics/skills)
- [Claude Skills Hub — Best of 2026](https://claudeskills.info/best/)
- [Top 10 Claude Code Skills — Composio](https://composio.dev/content/top-claude-skills)
- [The 10 Claude Code Skills I Actually Use at Work](https://www.welcomedeveloper.com/posts/the-10-claude-code-skills/)
- [Firecrawl — Best Claude Code Skills](https://www.firecrawl.dev/blog/best-claude-code-skills)
