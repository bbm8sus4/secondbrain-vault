# 06 — Dashboard สรุปผลสำรวจ + ความสอดคล้อง

> สร้าง 2026-06-30 → 2026-07-01 · หลังกู้ข้อมูลจาก [[05-INCIDENT-ข้อมูลหาย-กู้คืน]] สำเร็จ

## ส่งมอบ: ไฟล์เดียวจบ 3 แท็บ

**`AI-Workshop-รวม.html`** (ที่ `~/Documents/Claude/Projects/AI Workshop Management/RECOVERY/`)
ธีมน้ำเงินเข้ม (indigo) · IBM Plex Sans + Thai · Chart.js 4.4.1 + datalabels · ไม่มี emoji

| แท็บ | เนื้อหา |
|---|---|
| **1. ความคาดหวังเจ้าของธุรกิจ** (default) | meta เจ้าของ + 7 ส่วน (ระดับผลลัพธ์/ทำไมตอนนี้/เป้าหมาย/ตัวชี้วัด/หัวข้อ/ผลงาน/งบ) — ไม่ปนข้อมูลผู้เรียน |
| **2. สรุปผู้เข้าอบรม** | KPI 6 ตัว + อันดับความพร้อม 11 คน (คลิก→modal วิเคราะห์รายคน) + เรดาร์ + accordion ข้อค้นพบ/กราฟทุกคำถาม |
| **3. ความสอดคล้อง** | เทียบความคาดหวังเจ้าของ ↔ ข้อมูลจริง: เรดาร์ 2 เส้น + ตารางช่องว่าง 9 หัวข้อ + ข้อเสนอ |

**ไฟล์ย่อย (backup/แยกมุม):** `สรุปแบบสำรวจ-เต็ม.html` (ผู้เรียน) · `ความคาดหวังเจ้าของธุรกิจ.html` (เจ้าของ)

## 🌐 Deploy (Cloudflare Pages)

- **ลิงก์ stable (ส่งวิทยากร):** https://khonkaen-ai-workshop.pages.dev
- **Project:** `khonkaen-ai-workshop` (production branch `main`) · ลิงก์ไม่เปลี่ยนแม้ deploy ทับ
- **Source:** `AI-Workshop-รวม.html` → copy เป็น `index.html` ใน deploy dir

**ขั้นตอน redeploy เมื่อมีข้อมูลเพิ่ม:**
1. แก้ข้อมูล → รัน `/tmp/gen_combined.py` (regen `AI-Workshop-รวม.html`) — ถ้า /tmp หาย ดู [[#บทเรียนทำ dashboard (technical)]]
2. `mkdir -p /tmp/kk-deploy && cp "AI-Workshop-รวม.html" /tmp/kk-deploy/index.html`
3. `wrangler pages deploy /tmp/kk-deploy --project-name=khonkaen-ai-workshop --branch=main --commit-dirty=true`
4. ลิงก์เดิมอัปเองภายในไม่กี่วินาที (ไม่ต้องแชร์ใหม่)

> ⚠️ `/tmp/gen_combined.py` + `/tmp/kk-deploy` อยู่ใน /tmp = หายเมื่อ reboot — แต่ source HTML จริงอยู่ใน RECOVERY ถาวร ใช้ deploy ตรงได้เลยถ้าไม่ต้อง regen

## ข้อมูลจริง: ผู้เรียน 11 คน (8 เดิม + 3 เพิ่ม)

3 คนที่เพิ่มจากชีต (2026-07-01): **เบนซ์** (ช่าง/เทคนิค หัวหน้างาน — ใช้ Claude ประจำ เขียนโค้ดได้) · **เจ** (กราฟิก) · **โดนัท** (การตลาด)

**KPI:**
- 11 ผู้เข้าอบรม · 9/11 สายการตลาด
- ความมั่นใจเฉลี่ย **2.7/5**
- 6/11 ไม่เคยเขียนโค้ด
- 7/11 กังวลเรียนไม่ทัน
- มี **1 คน** ใช้ Claude เป็นประจำ (เบนซ์)

**อันดับความพร้อม (มาก→น้อย):** เบนซ์ 95 · ต่อ 88 · นัท 80 · ฟ้า 60 · อาย 55 · แบ๊ก 48 · เจ 52 · หมี 40 · โดนัท 35 · ยิม 30 · มอส 15
(สเกล composite จากความมั่นใจ + ประสบการณ์โค้ด + การใช้ AI)

## ความสอดคล้อง (แท็บ 3) — ผลวิเคราะห์

**Verdict:** สอดคล้องบางส่วน — เป้าหมายตรงกัน แต่ความพร้อมยังห่างจากที่คาดหวัง

เรดาร์ความพร้อมจริงผู้เรียน (0–3): Claude 1.6 · ทำเว็บ deploy 1.5 · ฐานข้อมูล 0.9 · GitHub 0.8 · ใช้ AI ทั่วไป 2.1
เทียบเจ้าของคาดหวัง = 3 ทุกหัวข้อ ("ทำเองได้จริง")

| สี | หัวข้อ |
|---|---|
| 🟢 สอดคล้องสูง | ใช้ AI ในงาน · โฟกัสการตลาด (9/11 สายการตลาด) |
| 🟡 ต้องปรับ/เตรียม | ทำเว็บ (ใช้ no-code) · Claude (ต้อง onboard) · ติดตั้งโปรแกรม (4/11 ติดเองได้) |
| 🔴 ต้องตัดสินใจขอบเขต | "ทำเองได้จริงทุกหัวข้อใน 1 วัน" · ฐานข้อมูล (0.9) · GitHub (0.8) · เวลา 1 วัน |

**ข้อเสนอปิดช่องว่าง:** tiered (Core ทุกคน + Advanced คนพร้อม) · เน้น use case การตลาด · ลด DB/GitHub เป็น "ภาพรวม + ดู demo" · เตรียมเครื่อง/บัญชีก่อนวันงาน · เพิ่ม clinic ครึ่งวัน follow-up

## บทเรียนทำ dashboard (technical)

- **gen script:** `/tmp/gen_combined.py` (ต่อยอดจาก `gen_dash.py`) — ฝัง ANALYSIS รายคน + RANK + INSIGHT_GROUPS + CSS/JS
- **Chart.js lazy render** — วาดกราฟตอนเปิดแท็บ/กด accordion เท่านั้น (กัน sizing bug จาก `display:none`); canvas ใช้ `position:absolute` ใน wrapper สูงคงที่
- **เรดาร์ lazy** — `renderRadar()` (แท็บผู้เรียน) + `renderRadar2()` (แท็บความสอดคล้อง) ยิงตอน showTab
- **multi-select " / " bug** — ค่า option มี " / " ในตัว → parse ผิด แก้ด้วย substring-match กับ option list (longest-first)
- **CSS Grid auto-placement** เคยฉีกข้อความเป็นรายตัวอักษร → เลี่ยง grid ใน list item, ใช้ marker `position:absolute`
- **verify ทุกครั้งก่อนส่ง** — headless Chrome `--screenshot` แล้ว Read ดูจริง

## คำที่ห้ามใช้ (ลบหมดแล้ว)
คนไทยอ่อนไหวง่าย — ห้ามคำด้อยค่า/ล้อเลียนคนที่ระบุชื่อ
น่าห่วง→ต้องการการสนับสนุน · ต่ำสุดทุกด้าน→ผู้เริ่มต้นในทุกด้าน · มั่นใจพอตัว→มีความมั่นใจในการใช้งาน · เสียของ→ใช้ศักยภาพได้เต็มที่
