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

**2 ลิงก์ stable** (ลิงก์ไม่เปลี่ยนแม้ deploy ทับ):

| ลิงก์ | เนื้อหา | Project |
|---|---|---|
| https://khonkaen-ai-workshop.pages.dev | **ครบ 3 แท็บ** — เจ้าของ / ผู้เรียน / ความสอดคล้อง | `khonkaen-ai-workshop` |
| https://khonkaen-workshop-learner.pages.dev | **2 แท็บ** — ผู้เรียน (default) + ความสอดคล้อง (ตัดหน้าเจ้าของออก) | `khonkaen-workshop-learner` |

- **Source ตัวเต็ม 3 แท็บ:** `AI-Workshop-รวม.html` → `index.html`
- **Source ตัว 2 แท็บ:** สร้างจากตัวเต็มด้วย Python patch — ตัด `#tab-owner` DOM + สลับ default active → learner + ปรับ subtitle · เก็บที่ `/tmp/kk-learner-deploy/index.html` (ใน /tmp = หายเมื่อ reboot; regen จาก 3-tab source ได้)

**ขั้นตอน redeploy 3-tab:**
1. แก้ข้อมูล → รัน `/tmp/gen_combined.py` (regen `AI-Workshop-รวม.html`) — ถ้า /tmp หาย ดู [[#บทเรียนทำ dashboard (technical)]]
2. `mkdir -p /tmp/kk-deploy && cp "AI-Workshop-รวม.html" /tmp/kk-deploy/index.html`
3. `wrangler pages deploy /tmp/kk-deploy --project-name=khonkaen-ai-workshop --branch=main --commit-dirty=true`
4. ลิงก์เดิมอัปเองภายในไม่กี่วินาที (ไม่ต้องแชร์ใหม่)

**ขั้นตอน redeploy 2-tab (learner-only):**
1. Regen จาก 3-tab: `cp AI-Workshop-รวม.html /tmp/kk-learner-deploy/index.html` แล้วรัน Python patch ตัด owner tab (ดู [[#Python patch สร้าง 2-tab variant]])
2. `wrangler pages deploy /tmp/kk-learner-deploy --project-name=khonkaen-workshop-learner --branch=main --commit-dirty=true`

## Mobile balance + typography (2-tab variant, 2026-07-01)

ปรับเฉพาะตัว 2-tab (`khonkaen-workshop-learner`) หลัง user feedback บนมือถือ:

- **Font stack** — `IBM Plex Sans Thai` มาก่อน `IBM Plex Sans` · เพิ่ม `text-rendering:optimizeLegibility` + `font-feature-settings:"kern","liga","calt"` · `line-height:1.55`
- **H1 mobile 2 บรรทัด** — split เป็น `<span class="hb-main">` + `<span class="hb-tail">` · desktop มี em-dash · mobile ซ่อน em-dash + tail เป็น block สีอ่อนลง
- **KPI mobile** — 3-col → **2-col** (ตัวเลข 22px, ไม่ล้น)
- **Alignment table mobile** — ใช้ card layout stacked (thead หาย, td เป็น block · reset `width:22%` ที่ตกค้าง = สาเหตุที่ Thai แตกเป็นตัวๆ)
- **Global reset** — `word-break:normal; overflow-wrap:normal; line-break:strict` ที่ body · `overflow-x:hidden; max-width:100%` ที่ html/body (safety)
- **Section tools mobile** — ปุ่ม "เปิดทั้งหมด/ย่อทั้งหมด" ยก order:99 + width:100% เป็นแถวเต็ม (เดิม margin-left:auto ทำให้ลอยขวา)
- **Radar chart** — เพิ่ม `layout.padding` 24px + `pointLabels` 10.5px บนมือถือ (labels ไม่ถูก clip)

Verified ที่ 320/360/390/414/480/640/700 ผ่าน puppeteer — `scrollWidth === viewport` ทุก breakpoint

### Python patch สร้าง 2-tab variant

```python
# ตัด owner tab + สลับ default active → learner
h = h.replace('<button class="tabbtn active" ... data-tab="owner">...</button>\n    <button class="tabbtn" ... data-tab="learner">...</button>',
              '<button class="tabbtn active" ... data-tab="learner">สรุปผู้เข้าอบรม</button>')
# ลบ section id="tab-owner" ทั้งก้อน
pattern = re.compile(r'<div class="tab active" id="tab-owner">.*?</div>\s*(?=<div class="tab" id="tab-learner">)', re.DOTALL)
h = pattern.sub('', h)
# ทำ learner active default
h = h.replace('<div class="tab" id="tab-learner">', '<div class="tab active" id="tab-learner">')
# แก้ subtitle ให้ตรงกับ 2-tab context
# แก้ JS default: showTab('learner') แทน showTab('owner')
```

Full patch script + mobile-balance CSS อยู่ใน git history conversation 2026-07-01 (Claude Code session)

> ⚠️ `/tmp/gen_combined.py` + `/tmp/kk-deploy` + `/tmp/kk-learner-deploy` อยู่ใน /tmp = หายเมื่อ reboot — แต่ source HTML จริงอยู่ใน RECOVERY ถาวร ใช้ deploy ตรงได้เลยถ้าไม่ต้อง regen

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
