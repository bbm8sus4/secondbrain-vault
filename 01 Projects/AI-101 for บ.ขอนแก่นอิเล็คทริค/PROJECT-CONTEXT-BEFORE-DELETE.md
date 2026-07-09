# Project Context Before Delete — Seatmap / KKAi AI Workshop

อัปเดตล่าสุด: 2026-07-07  
Workspace เดิม: `/home/thunder-management/workspaces/seatmap`  
สถานะรวม: งานเตรียมคอร์ส AI Workshop ปิดแล้ว, PM = `10/10 FINAL + QA PASS`, ใบเสนอราคา PDF ทำแล้ว

> หมายเหตุความปลอดภัย: ในแชตเคยมีการส่ง private key / password / credential บางส่วนมาแล้ว แต่ไฟล์สรุปนี้ไม่บันทึกค่าลับจริง ให้ถือว่า credential ทั้งหมดที่เคยส่งผ่านแชตต้อง rotate/revoke หากเคยใช้งานจริง

## สรุปสั้น

- โปรเจกต์นี้เริ่มจากตรวจ Seatmap/Obsidian แต่ภายหลังโฟกัสหลักเปลี่ยนเป็น AI Workshop สำหรับบริษัทขอนแก่นอีเลคทริค
- สร้างระบบ agent หลายบทบาทเพื่อเตรียมคอร์สครบทุกมิติ
- ผลลัพธ์หลักคือคอร์ส 1 วันแบบ Core / Advanced / Demo-only
- Core ใช้ browser-only เป็นแกนหลัก เพื่อให้ผู้เรียนทั่วไปตามทัน
- Advanced / GitHub / deploy / database / CLI / Cowork ให้ทำเฉพาะคนพร้อม หรือใช้เป็น demo บนจอ
- Dashboard learner 2-tab เป็นลิงก์หลักสำหรับหน้างาน
- Google Forms ที่มี response แล้วห้าม rebuild / clear / delete
- ใบเสนอราคา PDF ล่าสุดปรับราคาเป็น 2,499 บาทต่อคนแล้ว

## ข้อมูลลูกค้า / งาน

- ลูกค้า: บริษัท ขอนแก่น อีเลคทริค เทคโนโลยี เอนจิเนียริ่ง จำกัด
- ชื่ออังกฤษ: KHONKAEN ELECTRIC TECHNOLOGY ENGINEERING CO., LTD.
- ผู้ติดต่อ: คุณป๊อบ
- ที่อยู่ที่ใส่ในใบเสนอราคา:
  - 888/216 หมู่บ้าน ศุภาลัย การ์เด้นวิลล์ หมู่ที่ 14
  - ตำบลบ้านเป็ด อำเภอเมืองขอนแก่น จังหวัดขอนแก่น 40000
- ผู้เรียนอ้างอิง: 15 คน
- แบบสอบถามมีผู้ตอบ 11 คน
- ผู้ตอบ 9/11 เป็นสายการตลาด
- ความมั่นใจใช้ AI เฉลี่ยประมาณ 2.7/5

## Scope ที่ตัดสินแล้ว

### Core Track

- สำหรับทุกคน
- ใช้ browser-only เป็นแกน
- ใช้ Claude กับงานจริง
- สร้าง prompt ที่ใช้ซ้ำได้
- ทำคอนเทนต์ / สรุป / แปล / วิเคราะห์เบื้องต้น
- ทำ landing page จาก template
- ไม่บังคับติดตั้งโปรแกรม
- ไม่บังคับ GitHub / deploy / database / terminal

### Advanced Track

- สำหรับคนพร้อมจริง
- ทำคู่ buddy ได้
- GitHub / deploy / database ทำจริงได้ถ้าเครื่องและบัญชีพร้อม
- Cowork / Claude CLI ทำ hands-on เฉพาะกลุ่มพร้อม
- เบนซ์ / ต่อ / นัท ถูกจัดเป็นกลุ่มพร้อมตาม research

### Demo-only Track

- หัวข้อที่เสี่ยงหรือเกินเวลาทำเป็น demo บนจอ
- ใช้บัญชี demo ของวิทยากร
- Deploy / GitHub / Database / Claude Code / Warp เป็น overview/demo ได้
- Core ดูภาพรวม ไม่ต้องทำตาม

## Agenda FINAL โดยย่อ

- 09:00-09:30: Setup / เปิดภาพรวม / เข้า Claude
- 09:30-10:45: Claude Basics + prompt foundation
- 10:45-12:00: ใช้ AI กับงานการตลาด / content / งานจริง
- 13:10-13:35: Cowork Basic
- 13:35-14:00: Claude CLI Basic
- 14:15-14:35: Claude Code / Warp overview demo
- 14:35-14:50: Deploy / GitHub / Database demo
- 14:50-15:05: Core catch-up / Advanced stretch
- 15:05-15:45: Capstone
- 15:45-16:30: Showcase / post-evaluation / wrap-up

## Part4 FINAL

- Part4 ถูก reopen เพื่อเพิ่ม Cowork Basic และ Claude CLI Basic
- Master guardrail: ห้ามทับ QA-PASS baseline, scope บ่ายเท่านั้น, Core ดู demo, hands-on เฉพาะ Advanced
- ทำ fallback snapshot ไว้ที่ `part4-vfinal-fallback/`
- v-next ผ่าน QA แล้วและ master เคาะ SHIP IT
- Part4 FINAL = Cowork-first + Claude CLI Basic + overview demo

## การตัดสินใจสำคัญ

- ใช้ Plan B เป็น baseline เพราะไม่ต้องรอ owner ตอบ
- ไม่ต้อง login บัญชี Claude สำรอง 2 บัญชี
- ไม่ต้องส่ง pre-task ให้ผู้เรียนหรือเก็บคำตอบ
- ไม่ต้อง login Cloudflare / GitHub เพื่อโชว์ deploy สด
- ไม่ต้องพิมพ์ handout เป็นชุดกระดาษ
- ไม่ต้องรอคุณป๊อบตอบ 5 เรื่องเพื่ออัปเกรด Plan A
- ใช้ soft copy / PDF / live learner link แทนการพิมพ์
- เน็ตล่มให้ใช้ demo + prompt PDF + buddy
- ห้าม rebuild/clear Google Forms ที่มี response แล้ว

## Link สำคัญ

- Learner dashboard หลัก: https://khonkaen-workshop-learner.pages.dev
- PM / owner / trainer dashboard 3-tab: https://khonkaen-ai-workshop.pages.dev
- Pricing calculator: https://khonkaen-pricing.pages.dev
- Google Forms: ใช้ published URL เท่านั้น, ห้ามใช้ edit/debug/webapp links กับผู้เรียน

## Agent Rooms / บทบาท

ห้องอยู่ใต้ category `Seatmap` ใน Discord/tmx:

- `seatmap-talk-with-me`: ห้องคุยหลักกับผู้ใช้
- `kkai-master`: ตัดสินใจระดับ master / final approval
- `kkai-pm`: รวมสถานะ, checklist, ประสานงาน
- `kkai-research`: วิเคราะห์ผู้เรียนจากแบบสอบถาม
- `kkai-po`: ตัด scope Core / Advanced / Demo-only
- `kkai-curriculum`: agenda นาทีต่อนาที
- `kkai-slides`: ตรวจและปรับ slide flow
- `kkai-lab`: แบบฝึกหัด, prompt, fallback pack
- `kkai-tech-setup`: readiness ด้านเครื่องมือ/บัญชี/tech fallback
- `kkai-logistics`: ห้อง, อาหาร, handout, offline pack
- `kkai-dashboard`: dashboard/forms/readiness/mobile
- `kkai-qa`: QA alignment และ risk
- `kkai-dayof`: runbook หน้างาน

หมายเหตุ:

- ห้ามสร้างห้องผิดไปไว้ใต้ `master`
- ถ้าจะไม่ให้ sidebar ยาว ให้ใช้ Discord `Mute Category` + `Hide Muted Channels` หรือย้ายห้องไป `Seatmap Archive`
- ไม่แนะนำให้ลบทันทีถ้ายังต้องการประวัติงาน/หลักฐาน

## ไฟล์สำคัญใน root

- `pm-status.md`: สถานะรวม, checklist, master decision
- `part4-vnext-status.md`: สถานะ Part4 v-next และ master guardrails
- `research-learner-profile.md`: วิเคราะห์ผู้เรียน
- `scope-core-advanced-demo.md`: scope FINAL
- `agenda-minute-by-minute.md`: agenda นาทีต่อนาที
- `slides-review-and-fixes.md`: notes ตรวจสไลด์
- `lab-exercises-and-prompts.md`: lab + prompt + fallback
- `tech-readiness-checklist.md`: readiness ด้านเทคนิค
- `logistics-readiness.md`: readiness ด้านสถานที่/อาหาร/สำรอง
- `dashboard-forms-readiness.md`: dashboard + forms readiness
- `qa-findings.md`: QA PASS
- `dayof-runbook.md`: runbook หน้างาน
- `pre-task-message-to-learners.md`: pre-task draft แต่ owner override แล้วว่าไม่ต้องส่ง
- `cowork-basic-module.md`: module Cowork Basic
- `claude-cli-basic-module.md`: module Claude CLI Basic
- `kkai-agent-system.md`: โครงระบบ agent
- `AI-Workshop-Quotation.html`: ใบเสนอราคา HTML
- `AI-Workshop-Quotation.pdf`: ใบเสนอราคา PDF ล่าสุด
- `AI-Workshop-Quotation-preview.png`: preview ของ PDF ล่าสุด
- `PROJECT-CONTEXT-BEFORE-DELETE.md`: ไฟล์นี้

## ไฟล์ ZIP / Pack

- `AI-Workshop-Presentation-Pack.zip`
  - ขนาดประมาณ 895K
  - เน้นไฟล์สำหรับนำเสนอ
- `AI-Workshop-Complete-Pack.zip`
  - ขนาดประมาณ 3.8M
  - รวมไฟล์งานจำนวนมากประมาณ 171 ไฟล์
  - ใช้เป็น backup หลักถ้าจะย้ายออกก่อนลบ workspace
- `ai-workshop-complete-pack/`
  - โฟลเดอร์ staging ของ complete pack
- `ai-workshop-presentation-pack/`
  - โฟลเดอร์ staging ของ presentation pack

## Handouts / PDF ที่มีแล้ว

- `handouts/kkai-lab-handout-full.html`
- `handouts/kkai-lab-handout-full.pdf`
- `handouts/kkai-prompt-template-pack.html`
- `handouts/kkai-prompt-template-pack.pdf`
- `lab-offline-pack.html`
- `lab-offline-pack.pdf`

## Dashboard / Forms

- Dashboard 2-tab สำหรับผู้เรียนผ่าน mobile แล้ว
- Dashboard 2-tab source ถูกย้ายออกจาก `/tmp` แล้ว
- Source สำคัญใน vault/project:
  - `Files/Dashboard/build-learner-dashboard.js`
  - `Files/Dashboard/AI-Workshop-learner.html`
  - `Files/Dashboard/AI-Workshop-รวม.html`
- Apps Script ถูกล็อกจุด clear/delete แล้ว
- `clearAllItems()` block ถ้าฟอร์มมี response
- `createBothForms()` disabled
- `action=removemenu` disabled
- Google Forms ที่มี response แล้วห้าม rebuild/clear/delete

## ใบเสนอราคา

ไฟล์ล่าสุด:

- `AI-Workshop-Quotation.pdf`
- `AI-Workshop-Quotation.html`
- script สร้าง PDF:
  - `scripts/generate-quotation-image-pdf.js`
  - `scripts/generate-quotation-pdf.js`

ตัวเลขล่าสุด:

- ราคา/คน: 2,499.00 บาท
- จำนวน: 15 คน
- รวมก่อน VAT: 37,485.00 บาท
- VAT 7%: 2,623.95 บาท
- รวมทั้งสิ้น: 40,108.95 บาท

หมายเหตุ:

- PDF ล่าสุดทำเป็นภาพ A4 ฝังใน PDF เพื่อแก้ปัญหาฟอนต์/สระไทยใน environment นี้
- Preview ล่าสุดตรวจแล้วตัวเลขถูกต้อง
- ถ้าต้องการใบเสนอราคาฉบับเป็นข้อความ selectable เต็ม ควร export จาก browser/Canva/LibreOffice ในเครื่องที่มี renderer พร้อม

## Repo / External Source

- Obsidian vault: `https://github.com/bbm8sus4/secondbrain-vault`
- Seatmap repo ที่เคยให้มา: `https://github.com/bbm8sus4/office-seating-plan`
- ภายหลังผู้ใช้บอกให้ลืม Seatmap เรื่องนั้นไป โฟกัสหลักจึงเป็น AI Workshop

ตำแหน่ง local ที่เคยมี:

- `secondbrain-vault/`
- `office-seating-plan/`
- `.tmp-ai-workshop/AI-101 for บ.ขอนแก่นอิเล็คทริค/`

## Uploaded Inputs ที่ใช้

- `.uploads/mraaia72-AI-Workshop-.zip`: zip ต้นฉบับ AI Workshop
- ภาพ pricing calculator:
  - 15 learners
  - 2,500/head เดิม
  - revenue 37,500
  - total cost 22,479
  - profit 15,022
  - margin 40.1%
  - break-even 9
- ภาพที่อยู่ลูกค้า:
  - ชื่อบริษัท
  - ที่อยู่ 888/216...
- ภาพ Discord channel list ใช้อธิบายการซ่อน/ยุบห้อง agent

## สิ่งที่เสร็จแล้ว

- วิเคราะห์แบบสอบถามผู้เรียน
- ตัด scope 3 ชั้น
- ทำ agenda นาทีต่อนาที
- ปรับ Part4 ให้เน้น Cowork Basic และ Claude CLI Basic
- ทำ lab / prompt / offline pack
- ทำ runbook หน้างาน
- ตรวจ QA แล้ว PASS
- ทำ dashboard readiness และ mobile check
- ทำ zip pack สำหรับดาวน์โหลด
- ทำใบเสนอราคา HTML/PDF
- ส่ง PDF ใบเสนอราคาเข้า Discord แล้ว

## สิ่งที่ไม่ใช่ blocker แล้ว

- Claude account สำรอง
- pre-task
- Cloudflare/GitHub login เพื่อ deploy สด
- handout hard copy
- owner ตอบ Plan A
- บัญชี GitHub/Cloud ของผู้เรียนทุกคน
- สิทธิ์ติดตั้งเครื่องของทุกคน

## สิ่งที่ควรระวังถ้ารันคลาสจริง

- ถ้าผู้เรียน login Claude พร้อมกันแล้วติด ให้จับ buddy ทันที อย่าปล่อยค้างเกิน 3 นาที
- ถ้าเน็ตล่ม ใช้ demo + prompt PDF + buddy
- ห้ามใส่ข้อมูลลูกค้าจริง/รหัสผ่าน/เงินเดือน/ข้อมูลส่วนบุคคลเข้า AI
- Cowork/CLI ให้ใช้เฉพาะโฟลเดอร์สำเนา เช่น `cowork-demo-copy/` และ `claude-cli-demo/`
- ห้ามให้ Core เปิด terminal/แอปตามในช่วง demo
- Advanced เท่านั้นที่ทำ hands-on กับเครื่องมือเทคนิค
- ห้าม clear/rebuild Forms ที่มี response
- 3-tab dashboard ใช้เฉพาะ PM/owner/trainer

## ข้อความรายงานที่ต้องใช้ต่อ

ผู้ใช้ประกาศกฎให้ตอบใน Discord ด้วย `incident-report-format` โดยเฉพาะงาน report/status/problem:

- สรุปสั้น
- สาเหตุ
- หลักฐานที่เช็กแล้ว
- วิธีแก้
- สถานะตอนนี้

ข้อกำหนด:

- ห้ามส่งเป็นย่อหน้ายาวก้อนเดียว
- ใช้ bullet สั้น
- เลี่ยงศัพท์เทคนิคดิบ
- ถ้ายาว ให้สรุปสั้นก่อน

Skill path:

- Codex: `/home/thunder-management/.codex/skills/incident-report-format/SKILL.md`
- Claude: `/home/thunder-management/.claude/skills/incident-report-format/SKILL.md`

## ถ้าจะกู้โปรเจกต์หลังลบ

ลำดับแนะนำ:

1. เก็บไฟล์ `PROJECT-CONTEXT-BEFORE-DELETE.md`
2. เก็บ `AI-Workshop-Complete-Pack.zip`
3. เก็บ `AI-Workshop-Quotation.pdf`
4. เก็บ `AI-Workshop-Quotation.html` ถ้าต้องแก้ราคา/ข้อมูลต่อ
5. เก็บ `AI-Workshop-Presentation-Pack.zip` ถ้าต้องนำเสนอ
6. ถ้าจะกู้ทั้ง workspace ให้ unzip complete pack ก่อน แล้วเปิด `pm-status.md`
7. ใช้ `scope-core-advanced-demo.md`, `agenda-minute-by-minute.md`, `dayof-runbook.md` เป็นเอกสารหลักในการรันต่อ

## คำสั่งที่ใช้ซ้ำได้

สร้าง PDF ใบเสนอราคาใหม่จาก script ภาพ A4:

```bash
node scripts/generate-quotation-image-pdf.js
```

เช็กเลขราคาในไฟล์ใบเสนอราคา:

```bash
rg -n "2,499|37,485|2,623\\.95|40,108\\.95|2,500|37,500|40,125" AI-Workshop-Quotation.html scripts/generate-quotation-image-pdf.js
```

แนบไฟล์ PDF เข้า Discord:

```bash
tmx discord-send "แนบไฟล์ใบเสนอราคา PDF" -f /home/thunder-management/workspaces/seatmap/AI-Workshop-Quotation.pdf
```

## Known Caveats

- Workspace นี้ไม่ใช่ git repo ที่ root (`git status` แจ้งว่าไม่ใช่ repository)
- ไม่มี browser PDF renderer พร้อมใช้งานใน environment ตอนทำใบเสนอราคา
- เคยลองติดตั้ง Puppeteer แต่ดาวน์โหลด browser นานผิดปกติ จึงหยุด
- PDF ล่าสุดจึงใช้วิธี render เป็นภาพ A4 แล้วฝังใน PDF
- `node_modules/` อาจมีแพ็กเกจชั่วคราวจากการสร้าง PDF (`sharp`, `pdf-lib`) ไม่จำเป็นต้องเก็บถ้าเก็บ PDF แล้ว
- มี credential/secret ในประวัติแชตที่ไม่ควรเก็บซ้ำในเอกสารนี้

## ไฟล์ที่ควรดาวน์โหลดก่อนลบ

- `PROJECT-CONTEXT-BEFORE-DELETE.md`
- `AI-Workshop-Complete-Pack.zip`
- `AI-Workshop-Presentation-Pack.zip`
- `AI-Workshop-Quotation.pdf`
- `AI-Workshop-Quotation.html`

