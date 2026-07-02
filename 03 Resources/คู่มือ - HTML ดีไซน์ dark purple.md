---
tags: [คู่มือ, playbook, html, design, dark-theme]
created: 2026-07-02
source: reve2-guide.html · cs-announcement-playbook (redesign รอบ 2)
---

# 🎨 คู่มือ — HTML ดีไซน์ dark purple (สไตล์ที่กูชอบ)

สไตล์ที่ใช้ประจำสำหรับ **คู่มือ / playbook / doc ภายในทีม** — dark theme + purple accent + Thai/Inter typography — ผู้ใช้เห็นแล้วรู้เลยว่า "ของทีมเรา"

> reference จริง: `~/reve2-guide.html` · `~/cs-announcement-playbook.html` · live: [cs-announcement-playbook.pages.dev](https://cs-announcement-playbook.pages.dev/)

---

## หัวใจ 1 — Palette ตายตัว

คัดลอกก้อนนี้ลง `:root` ห้ามเปลี่ยนถ้าไม่มีเหตุผลชัด (โทนนี้ทีมจำได้ = brand consistency ในเอกสารภายใน):

```css
:root {
  --bg: #0a0a0f;
  --surface: #12121a;
  --surface-2: #1a1a26;
  --surface-3: #222233;
  --border: #2a2a3d;
  --text: #e8e8f0;
  --text-dim: #8888a0;
  --accent: #6c5ce7;
  --accent-light: #a29bfe;
  --accent-glow: rgba(108, 92, 231, 0.15);
  --green: #00cec9;
  --orange: #fdcb6e;
  --red: #ff6b6b;
  --blue: #74b9ff;
  --pink: #fd79a8;
  --radius: 16px;
  --radius-sm: 10px;
}
```

**กติกา:**
- accent purple `#6c5ce7` = ปุ่ม / link / highlight สำคัญ · accent-light = text บน dark
- green = สถานะโอเค · red = อันตราย · orange = เตือน · blue = info · pink = variable/placeholder
- ห้ามใช้สีตัวอักษรบน bg โดยตรง (contrast ต่ำ) — ใช้ `--text` หรือ `--text-dim` เท่านั้น

## หัวใจ 2 — Typography

```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700;800;900&display=swap');

body { font-family: 'IBM Plex Sans Thai', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; line-height: 1.7; -webkit-font-smoothing: antialiased; }
```

- **body text** = IBM Plex Sans Thai (ไทยสวย ไม่ใช้ Sarabun/Kanit — เชยแล้ว)
- **heading + ตัวเลข + label uppercase** = Inter (บังคับ `font-family:'Inter',sans-serif` เพราะ IBM Plex Thai ไม่มี weight 800+)
- line-height 1.7 (อ่านสบายบนมือถือ)
- letter-spacing: h1 `-1.5px` ~ `-2px` (tight, feel premium) · uppercase label `+1.2px ~ 1.4px`

## หัวใจ 3 — Hero pattern

hero ทุกหน้าใช้โครงเดียวกัน — **badge + gradient title + subtitle + hero-meta**:

```html
<header class="hero">
  <span class="hero-badge"><span class="dot"></span>{{version หรือ status}}</span>
  <h1>{{ชื่อเอกสาร}}</h1>
  <p>{{subtitle}}</p>
  <div class="hero-meta">
    <div class="item"><div class="n">{{ตัวเลข}}</div><div class="l">{{label}}</div></div>
    ...
  </div>
</header>
```

CSS สำคัญ:
- bg = `linear-gradient(180deg, #1a1035 0%, var(--bg) 100%)` — ม่วงเข้ม fade ลง bg
- `::before` = radial gradient purple glow ตรงกลางบน — สร้างความลึก
- h1 = gradient text `linear-gradient(135deg, #fff 30%, var(--accent-light) 100%)` + `-webkit-background-clip: text`
- badge = pill `border-radius: 100px` + `.dot` pulse animation
- padding top ใช้ `env(safe-area-inset-top)` — รองรับ iPhone notch

## หัวใจ 4 — Component ประจำ

### Section header (icon + title)
```html
<div class="section-header">
  <div class="section-icon">🎯</div>
  <h2>ชื่อ section</h2>
</div>
```
`.section-icon` = 40x40 box, `background: accent-glow`, border `rgba(108,92,231,0.25)`, radius 10px, emoji ตรงกลาง

### Card
`background: --surface; border: 1px solid --border; border-radius: 16px; padding: 24px;` — hover เปลี่ยน `border-color: rgba(108,92,231,0.4)` + `translateY(-2px)`

### Flow (ขั้นตอนมีลำดับ)
```html
<div class="flow">
  <div class="flow-step" data-step="1">...</div>
  <div class="flow-step" data-step="2">...</div>
</div>
```
- `.flow::before` = เส้นแนวตั้ง 2px gradient purple → glow ต่อ dot
- `.flow-step::before` ใช้ `content: attr(data-step)` = วงกลม 24px accent purple พร้อมเลข Inter 700

### Table
```html
<div class="table-wrap">
  <table><thead>...</thead><tbody>...</tbody></table>
</div>
```
- `.table-wrap` wrap ให้ overflow-x + border-radius (ไม่งั้น table เกินขอบ)
- `thead th` = uppercase 11px, letter-spacing 1px, `color: --text-dim` (แม่ๆ ไม่แย่ง content)
- `tbody tr:hover td` = `background: rgba(108,92,231,0.04)` — subtle

### Tag pill
```css
.tag { padding: 3px 10px; border-radius: 100px; font-size: 11px; font-weight: 700; font-family: 'Inter'; }
.tag-t1 { background: rgba(255,107,107,0.12); color: var(--red); }
.tag-t2 { background: rgba(253,203,110,0.14); color: var(--orange); }
.tag-t3 { background: rgba(0,206,201,0.12); color: var(--green); }
```
สูตร: `background = สี rgba 0.12 · color = ตัวแปรสีเต็ม` — pastel bg + text เต็มสี

### Callout 3 แบบ (warn/info/ok)
โครง flex `<div class="ico">emoji</div><div>content</div>` · border 1px + bg แบบ 0.06 opacity ของสีนั้น

### Details (accordion)
- `<summary>` = `list-style: none` + custom `+/×` caret ทางขวา
- `details[open]` เปลี่ยน `border-color` = accent purple + caret หมุน 45°
- `.caret` มี `transition: transform 0.2s` — พลิกนุ่มๆ

## หัวใจ 5 — Mobile-first + a11y ที่บังคับเลย

**ทุกหน้าต้องมี ห้ามลืม:**
- `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">` — ต้อง `viewport-fit=cover` (notch)
- `env(safe-area-inset-*)` ที่ container padding + footer padding-bottom
- `html { -webkit-tap-highlight-color: transparent; }` — ลบสีฟ้าเด้ง iOS
- `body { overscroll-behavior-y: contain; }` — ปิด pull-to-refresh
- ปุ่มทุกปุ่ม `min-height: 44px` (iOS HIG)
- `:focus-visible { outline: 2px solid var(--accent-light); outline-offset: 3px; }` — Tab เห็นบน desktop
- `@media (prefers-reduced-motion: reduce)` ปิด animation
- `@media print` — override เป็น bg ขาว + text ดำ + ซ่อน copy button + `details > .body { display: block !important }`

## หัวใจ 6 — Head boilerplate

```html
<meta name="description" content="...">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='22' fill='%236c5ce7'/><text x='50' y='68' font-size='52' text-anchor='middle' fill='white' font-family='Inter,sans-serif' font-weight='800'>XX</text></svg>">
```

favicon inline SVG — ไม่ต้อง deploy ไฟล์แยก · เปลี่ยน `XX` เป็นตัวอักษร 2 ตัวของโปรเจ็กต์

## หัวใจ 7 — Copy button (ถ้ามี template ให้ก๊อป)

- ปุ่มมุมบนขวาของ `<pre>` — `position: absolute` + `min-height: 36px`
- `aria-label` แยกทุกปุ่ม (ห้ามซ้ำกัน) + live region `<div aria-live="polite" class="sr-only">` announce ตอนสำเร็จ
- ใช้ `navigator.clipboard.writeText` + fallback `document.execCommand('copy')` เผื่อ HTTP context
- ตอน copy สำเร็จ: เปลี่ยน text เป็น "คัดลอกแล้ว" + toggle class เปลี่ยนสีเขียว 1.6 วิ

## หัวใจ 8 — Deploy pattern

Cloudflare Pages ตัวเดียวจบ:
```bash
mkdir -p ~/PROJECT-deploy
cp ~/PROJECT.html ~/PROJECT-deploy/index.html
cd ~/PROJECT-deploy
wrangler pages project create PROJECT --production-branch=main   # ครั้งแรกเท่านั้น
wrangler pages deploy . --project-name=PROJECT --branch=main --commit-dirty=true
```
URL แบบสาธารณะ: `https://PROJECT.pages.dev/`

---

## เอกสารต้นแบบ (ก๊อปแล้วแก้)

- **cs-announcement-playbook** — เอกสาร SOP + template · โครงครบทุก component ที่พูดมา · เอาไปเป็น boilerplate ได้เลย
- **reve2-guide** — เอกสารคู่มือใช้งาน tool · โครงที่มาของสไตล์นี้

## เมื่อไหร่ห้ามใช้สไตล์นี้

- **สไลด์นำเสนอผู้บริหาร** — ใช้ [[คู่มือ - สไลด์ HTML ปิดบังตัวเลข]] (สไตล์ Apple, light theme)
- **เอกสารส่งลูกค้า/นอก** — แบรนด์ลูกค้าไปคนละทาง
- **หน้าเว็บ marketing/landing** — ต้องคิดใหม่ตาม positioning
