---
tags: [คู่มือ, playbook, html, presentation, dataviz]
created: 2026-06-12
source: งานทำสไลด์ Thunder Group revenue (thunder-revenue-report.pages.dev/slides)
---

# 🗺️ คู่มือ — สไลด์ HTML นำเสนอผู้บริหาร (ปิดบังตัวเลขได้)

วิธีทำสไลด์ HTML ไฟล์เดียว ธีม Apple พร้อมปุ่ม "ตา" ซ่อนตัวเลขเงิน + กราฟที่เล่าเรื่องได้แม้ตัวเลขถูกซ่อน — เคยทำเวิร์กแล้ว ไม่ต้องเดาใหม่

> ตัวอย่างจริง: `~/thunder-monthly-slides.html` · live ที่ [thunder-revenue-report.pages.dev/slides](https://thunder-revenue-report.pages.dev/slides)

---

## หัวใจ 1 — ปิดบังตัวเลขด้วย CSS ล้วน (ไม่แตะ DOM)

ใช้ตอนนำเสนอต่อพนักงานต่างระดับ — ซ่อนยอดเงิน ฿ เป็นดอกจัน แต่ **% การเติบโต/สัดส่วนยังโชว์**

**Markup:** ห่อเลขเงินทุกตัวด้วย span เดียว ตัวเลขอยู่ใน attribute:
```html
<span class="m" data-v="฿11,523,721"></span>
```

**CSS:** สลับด้วย class บน body — ไม่ใช้ JS ยุ่งกับ DOM:
```css
.m::after{content:attr(data-v);}
body.masked .m::after{content:"฿******";letter-spacing:.06em;}
```

**กติกาที่เรียนรู้:**
- เปิดหน้ามา `<body class="masked">` **เสมอ** → reload กลางห้องประชุมก็ปลอดภัย (กลับมาปิดเอง)
- ดอกจัน **ยาวคงที่ 6 ตัว** ทุกจำนวน — ไม่ให้เดา magnitude จากจำนวนหลัก
- ปิด **ทุก** ยอดเงินรวมถึงเป้า/projection/ตัวเลขบนกราฟ — ไม่งั้นคำนวณย้อนจาก % ได้
- ปุ่มตา: คลิก toggle `body.masked` + คีย์ลัด `H` + `aria-pressed` · ตอนเปิดเผยให้ปุ่มเปลี่ยนเป็นสีแดงเตือน
- **กราฟ SVG:** ป้ายตัวเลข ฿ บนแกนใส่ `class="m"` ด้วย เพื่อโดนซ่อนพร้อมกัน — แต่ดีไซน์ให้กราฟใช้ % ล้วน จะไม่ต้องซ่อนอะไรเลย

## หัวใจ 2 — เลือกกราฟให้รอดโหมดซ่อนตัวเลข

หลักเดียวที่ตัดสินทุกอย่าง: **กราฟต้องเล่าเรื่องด้วยรูปทรงสัมพัทธ์ + % เพียงลำพัง** ห้ามพึ่งแกนตัวเลขเงินเป็นตัวเล่าเรื่อง (ได้จาก aidebate Gemini+Claude+Typhoon)

| ข้อมูล | ใช้ | เหตุผล |
|---|---|---|
| รายได้รายเดือน (5 จุด) | แท่งตั้ง + ไฮไลต์เดือนล่าสุด (สีเต็ม+เงา, แท่งอื่น opacity .4) | 5 จุดแท่งอ่านง่ายกว่าเส้น · ความสูงสัมพัทธ์เล่าเอง |
| KPI การ์ด | **sparkline เส้น + area gradient + จุดปลาย** (ไม่ใช่ mini-bar) | เส้นโชว์ "ทรงการเดินทาง" · ติด badge "ผันผวน" กันอ่าน +326% เป็นเทรนด์นิ่ง |
| ตารางรายสินค้า | **sparkline ต่อแถว** (normalize min–max ของแถวตัวเอง) | ตารางเลขล้วน "ตายสนิท" พอซ่อนเงิน · sparkline เห็น hockey-stick/ความนิ่งได้ |
| โครงสร้าง/สัดส่วน + ความเสี่ยงกระจุก | **nested treemap** (div absolute, พื้นที่=สัดส่วน) | ก้อนยักษ์ข้างเศษเล็ก = เห็น "ไข่ในตะกร้าใบเดียว" ใน 1 วิ · เล่าได้ 2 ชั้น |
| Progress เทียบเป้า | progress bar + เส้น marker เวลา = **bullet chart** | จริง vs เป้า vs เวลา ในรูปเดียว · แกน % รอดซ่อนเงินเอง |
| Projection หลาย scenario | **range bars แนวนอน** เทียบเส้นตั้ง 100% | เห็นทันที Bear ไม่ถึง / Base เลยนิด / Bull ทะลุ · ช่วงค่าเป็นแท่ง range |
| สะสมทั้งปี + คาดการณ์ | **cumulative YTD line + fan chart** (เส้นประ 3 ทาง) | เส้นทึบไต่ตามเส้นเป้า แล้วแตกพัด |

**⚠️ กับดัก fan chart:** ต้องวาดบน **สเกลสะสม YTD** (9.56→19.42→…→51.0) แล้วแตกเส้นประจากจุดล่าสุดไปสิ้นปี — **ห้าม** ลากจากกราฟรายเดือน (จุดรายเดือน ~11M ต่อเข้า projection รายปี ~125M ไม่ได้ สเกลคนละเรื่อง)

**โดนัท:** หลีกเลี่ยง — สัดส่วนใกล้ 50/50 คนเทียบมุม/ส่วนโค้งแม่นน้อยกว่าเทียบความยาวแท่ง · ใช้ split bar หรือ treemap แทน

**สี fan/scenario** ใช้สีตามความหมาย (Bear เทา / Base น้ำเงิน / Bull เขียว) **ไม่ใช่สีแบรนด์** — กันปนความหมาย

## หัวใจ 3 — projector-friendly

- เส้นหลัก `stroke-width:5–6` `stroke-linecap:round` · จุดข้อมูล `<circle r=7>` ขอบหนา ชี้จากหลังห้องได้
- gridline ≤3 เส้นจางๆ · direct labeling ปลายเส้น (ไม่มี legend) · font ป้าย ≥18px
- เงาใช้ CSS `filter:drop-shadow()` ระดับการ์ด ไม่วาดใน SVG
- เด็คเต็ม viewport ไม่ scroll ในสไลด์ · nav: ←/→ Space, swipe, dots, คีย์ `F` เต็มจอ

## Deploy (Cloudflare Pages)

```bash
mkdir -p ~/<proj>-deploy && cp report.html ~/<proj>-deploy/index.html && cp slides.html ~/<proj>-deploy/slides.html
cd ~/<proj>-deploy && npx wrangler pages deploy . --project-name=<proj> --branch=main --commit-dirty=true
```

**⚠️ กับดักใหญ่:** ต้องใส่ `--branch=main` ไม่งั้นขึ้นเป็น **preview** ไม่ใช่ production — URL stable (`<proj>.pages.dev`) จะไม่อัปเดต · แชร์ URL stable เดียว ไม่แชร์ per-commit hash (ดู [[กติกา - Deploy ใช้ stable URL]])

## เช็คงานเร็ว (headless screenshot ไม่ง้อ Chrome MCP)

```bash
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CH" --headless --disable-gpu --window-size=1440,810 --screenshot=/tmp/s.png "file://$PWD/slides.html#4"
```
test ทั้งสถานะ masked (default) และ unmasked (sed แทน `<body class="masked">` เป็น `<body>` ชั่วคราว)

---

เกี่ยวข้อง: [[คู่มือ - AI Debate]] · [[คู่มือ - ดึงข้อมูล Master Dashboard]] · [[แผนที่ - คู่มือ]]
