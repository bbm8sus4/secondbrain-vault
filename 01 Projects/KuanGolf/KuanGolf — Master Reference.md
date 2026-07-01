# KuanGolf — Master Reference

> เอกสารสรุปทุกอย่างของ KuanGolf จากทุกที่ในเครื่อง (SecondBrain + Work + Memory + specs + assets)
> อัปเดต: 2026-07-01

---

## 1. Product Overview

**คืออะไร:** LINE-native PWA สำหรับก๊วนกอล์ฟไทย — บันทึกสกอร์ + คำนวณ side-bet + เคลียร์เงินด้วย PromptPay QR อัตโนมัติ

**กลุ่มเป้าหมาย:** นักกอล์ฟไทยอายุ 40-65 ปี ส่วนใหญ่เป็นเจ้าของ SME / ผู้บริหาร กรุงเทพฯ + ปริมณฑล
**Core user:** "หัวก๊วน" (Captain) — คนจัดก๊วน คุมสกอร์ เคลียร์เงิน

**Positioning:** "Settlement specialist สำหรับก๊วนกอล์ฟไทย" — ไม่ใช่แอปกอล์ฟครบวงจรแบบ Hole19/18Birdies แต่โฟกัสเฉพาะการปลดภาระเหรัญญิกออกจากหัวก๊วน — Unique ในตลาดไทย

---

## 2. Business Model & Pricing

**Live ณ 2026-06-21:**

| Package | ราคา | Features |
|---------|------|----------|
| **Free** | ฿0 ตลอดชีพ | เล่นไม่จำกัด, ทุก side game, แชร์เข้า LINE |
| **Pro** | **฿999/ปี** (~฿83/เดือน) | Free + GPS ระยะถึงกรีน real-time + ประวัติเต็ม + สถิติส่วนตัว · 8 คน/ก๊วน · Nassau team 2/3 คู่ |
| **Group** | ฿1,290/ปี (~฿215/คน หาร 6) | Pro + Group Leaderboard |
| **Lifetime** | ฿2,490 ครั้งเดียว | Pro ตลอดชีพ (tier ซ่อน ไม่โชว์ในหน้า /pricing) |

**การจ่ายเงิน:** PromptPay QR อย่างเดียว (ไม่มีบัตรเครดิต) · คืนเงินภายใน 7 วัน · ไม่มี auto-renewal — LINE/email แจ้งก่อนหมด 7 วัน

**⚠️ ปัญหา:** `llms.txt` (อัปเดต 2026-05-06) ยังลิสต์ Pro = ฿790 และ Free = 1 game/month — **outdated ต้องอัปเดต** ทำให้ AI bot ตอบลูกค้าราคาผิด

---

## 3. Features

### Core Scoring
- Stroke Play + Stableford (standard + modified)
- UI ออกแบบสำหรับมือถือ · touch target 64px+ · อ่านชัดกลางแดด · เหมาะกลุ่ม 40-65
- Offline-capable (PWA standalone)

### Side Games — 15+ แบบ

| หมวด | เกม | หมายเหตุ |
|------|-----|----------|
| **Snake** | 3 variants | Standard (คนสกอร์ต่ำสุดเก็บ) · Triple Snake (3-putt + water + OB) · Snake-of-snake (pot สะสม) |
| **Skins** | 1 | คนสกอร์ต่ำสุดต่อหลุมได้ · carry-over อัตโนมัติ |
| **Nassau** | 1 | 3 match (Front 9, Back 9, Total) · 2-2-2 + Press |
| **Birdie Pot** | 1 | Eagle ×2 คะแนน, Albatross ×4 |
| **ต่อแต้ม** | 1 | ระบบแฮนดิแคปไทย (halve-on-tie ไม่ใช่ spread) — **Unique ของ KuanGolf** |
| **Stableford** | 1 | 4/3/2/1/0 |
| **Junk** | 8 แบบ | Greenie, Sandy, Polly, Barkie, Fish, Arnie, Chip-in (×2), Up & Down |

### Settlement
- **จับคู่หนี้อัตโนมัติ** — จับคนหนี้มากสุดกับคนได้มากสุด → ลดจำนวน transaction (เช่น 6 → 2)
- **สร้าง PromptPay QR** พร้อมยอดเงิน + ผู้รับ · โอนผ่านแอปธนาคารเอง · **แอปไม่ถือเงินเลย**
- **สรุปเข้ากลุ่ม LINE** — สกอร์ + settlement + list การโอน ทีเดียวจบ

### History & Stats
- ประวัติเกมส่วนตัว
- สถิตินักกอล์ฟ
- **GPS ระยะถึงกรีน real-time** (Pro) — ฟีเจอร์ใหม่ 2026
- Group Leaderboard (Group package)

### Onboarding
- Wizard 4 ขั้น (ข้ามได้ทุกขั้น)
- Default: Par 72, 18 หลุม
- แก้ทีหลังได้

---

## 4. Technical Stack

| Layer | Tech |
|-------|------|
| Frontend | Next.js 16 · React 19 · TypeScript · Tailwind v4 |
| State | Zustand |
| Backend/DB | Supabase (Postgres + Auth + Storage) |
| Auth | LINE Login + LIFF Mini App |
| Payment | PromptPay QR (generate-only, ไม่มี escrow) |
| Integration | LINE Messaging API |
| Analytics | PostHog |
| Localization | Thai-first, English secondary (th_TH) |
| Version | 0.1.0 (`fa754d2782883abe63a8046d7d708538ae889ce5`) |

**Infrastructure:** ฝังใน Thunder Solution ecosystem — ใช้ learning ร่วมจาก EasySlip / BoostSMS / EasyCRM + PromptPay flow

### Sitemap
- `/` — Landing
- `/sale` — Sales page
- `/pricing` — Pricing
- `/onboarding` — Wizard (auth required)
- `/history` — Game history (auth required)
- `/terms` — ToS
- `/privacy` — Privacy (PDPA)
- `/llms.txt` — สำหรับ AI bots (⚠️ ราคา outdated)
- `/docs/KNOWLEDGE_BASE` — **404 ยังไม่ได้ทำ** (อ้างใน llms.txt)

---

## 5. Marketing Status

### สภาพปัจจุบัน (2026-06-21)
- **Website:** Live (kuangolf.com)
- **LINE OA (@kuangolf):** Live แต่ minimal content
- **Facebook Page:** "KuanGolf - ก๊วนกอล์ฟ" — **2 posts, 0 engagement, ใหม่มาก**
- **Instagram / TikTok / YouTube:** ยังไม่เริ่ม
- **Blog/SEO:** ไม่มี content marketing

### งบ & ทีม
- งบเพดาน: **฿30,000/เดือน**
- Content brief พร้อม: 30-day post plan (8 themes) + 60-day overview
- Assets พร้อม 100% แต่ **ยังไม่โพสต์** (ทำเสร็จ 2026-05-26 นอนอยู่)
- มี Marketing Manager Roadmap (DOCX)

### Quick Wins (ยังไม่ทำ)
1. โพสต์ 30-day Facebook brief (assets + captions พร้อม)
2. ตั้ง custom Facebook URL (ตอนนี้เป็น profile ID ยาว)
3. เปิด Instagram + sync content จาก FB
4. เปิด LINE OA เต็ม + Rich Menu
5. รัน "Page Like" ads
6. **อัปเดต llms.txt** ให้ราคาถูก (Pro ฿999, Free unlimited)
7. สร้าง `/docs/KNOWLEDGE_BASE` (ตอนนี้ 404)

### Content Themes (30-day brief)
Hook | Pain Point | Educate | Use Case | Promo | Niche | Engage | Recap

---

## 6. Team & Stakeholders

| Role | Name | Email |
|------|------|-------|
| Company | Thunder Solution | — |
| Admin/Tech Lead | Watcharin Kaewmoung | watcharin.k@thunder.in.th |
| COO/Strategy | Bob (ผู้ใช้) | — |
| Customer Support | — | hello@kuangolf.com |

---

## 7. URLs & Digital Assets

### Live URLs
| Channel | URL/Handle |
|---------|-----------|
| Website | https://kuangolf.com |
| Sales | https://kuangolf.com/sale |
| Pricing | https://kuangolf.com/pricing |
| llms.txt | https://kuangolf.com/llms.txt |
| LINE OA | @kuangolf |
| Facebook | facebook.com/profile.php?id=61589538174943 |
| Email | hello@kuangolf.com |

### Asset Locations

**Knowledge Base:** `/Users/aexgee/SecondBrain/01 Projects/KuanGolf/` (11 markdown files)
- README.md
- Product.md
- Brand Strategy Brain.md (1,037 lines)
- Website & Tech.md
- Marketing.md
- FAQ — Live.md
- Strategic Analysis.md
- Research Demand — Report.md
- Research Demand — Prompt.md
- Vendor Quote
- llms.txt mirror

**Working Assets:** `/Users/aexgee/Work/KuanGolf/` (จัดระเบียบ 2026-06-23)
```
├── marketing/
│   ├── specs/ (01-overview → 07-analysis)
│   ├── briefs-html/ (9 HTML: 60-day master, phases, calendars)
│   ├── briefs-md/ (content-30-brief.md)
│   ├── captions.md (copy พร้อมโพสต์)
│   ├── promo-master-plan.md (v3 final, 35 assets)
│   ├── promo-master-plan.v1.md / v2.md
│   ├── asset-recipes.md (designer handoff)
│   ├── ai-image-prompts.md
│   ├── README.md
│   └── Marketing Manager Roadmap.docx
├── brand/
│   ├── Logo/ (Kuan-golft-logo-01 → 07, kuangolf.png)
│   ├── Mascot 3D/ (12 poses)
│   ├── covers/ (Rich Menu, LINE OA, Facebook)
├── assets/
│   ├── qr/ (2D barcodes — BW และ GW: S/M/L)
│   ├── misc/
│   ├── ai-generated/ (kg-*.png, _test-explorations/)
├── content/ (50 posts, IG carousels, FB content)
├── archive/ (old brand — logo-lockups, mascot-poses, app-icons, patterns)
```

**Memory Cache:** `/Users/aexgee/.claude-warp/projects/-Users-aexgee/memory/project_kuangolf.md`

**Smart-Env Index:** `/Users/aexgee/SecondBrain/.smart-env/multi/` (30+ .ajson files)

---

## 8. Legal & Compliance

### จุดยืนเรื่องพนัน
- **ไม่ใช่พนัน:** แอปบันทึกสกอร์อย่างเดียว ไม่ถือเงิน · PromptPay QR = โอนตัวต่อตัวที่ user เริ่มเอง (off-platform)
- Subscription = รายได้ SaaS ไม่ใช่ gaming revenue
- Terms ห้าม "การพนันที่ผิดกฎหมายไทย" ทุกประเภทชัดเจน
- **Implication:** ดำเนินการเปิดในไทยได้ ไม่ต้องมีใบอนุญาต gaming

### Data Privacy (PDPA compliant)
- **เก็บ:** LINE profile (display name + รูปสาธารณะ), สกอร์กอล์ฟ, PromptPay info, usage stats
- **ใช้:** service ให้คะแนน, sync group, สถิติส่วนตัว, ปรับปรุงระบบ
- **แชร์:** เฉพาะเพื่อนในก๊วน / infrastructure providers / รัฐเมื่อมีคำสั่งศาล · **ไม่ขายให้ third party**
- **Cookies:** Session + localStorage · ไม่มี third-party cookies
- **User rights:** access/edit/delete/transfer/revoke ผ่าน hello@kuangolf.com ภายใน 30 วัน

### Terms of Service
- As-is service ไม่รับผิดข้อพิพาทระหว่างผู้เล่น
- ห้าม: พนันผิดกฎหมาย, hacking, harassment
- User ครอบครองข้อมูลตัวเอง

---

## 9. Roadmap & Current Status

### Phase: Pre-traction (2026-06-21)
- **Product:** Live v0.1.0
- **Users:** 0 paying (product live แต่ยังไม่ push marketing)
- **Validation:** USP claims ทั้งหมด **[hypothesis]** ยังไม่ได้ interview captain 10-15 คน
- **Recommended strategy:** **Path B (Park แต่ไม่ทิ้ง)**

### Strategic Analysis
> "Product ดี · Brand ดี · Tech ดี — แต่ zero go-to-market motion"

**Path B (Recommended): Maintenance mode**
- ไม่ปิด ไม่ลงทุนเพิ่ม (priority ต่ำเทียบ EasySlip/BoostSMS)
- Quick fixes (1 สัปดาห์): อัปเดต llms.txt, สร้าง /docs/KNOWLEDGE_BASE, เปิด LINE OA auto-reply
- รอ Thunder core products stable ก่อนกลับมาโฟกัสเต็ม

**ทำไมไม่เลือก Path A / C:**
- Path A (commit) ต้อง owner full-time + ฿30-50K/mo ad → กินโฟกัส product ที่ทำเงิน
- Path C (spin-off) ต้อง internal buyer หรือ equity deal
- TAM = 50-100K หัวก๊วนไทย (เล็กแต่ ARPU ฿999 = ฿50-100M ถ้ายึดได้) — คุ้ม park ไม่คุ้มฆ่า

### Next Validation (ถ้ากลับมา)
1. Interview 10-15 หัวก๊วน confirm "identity tension" เป็น pain จริง
2. Test Facebook ads (Phase 2 รอ approve)
3. วัด activation: 1-click signup → บันทึกเกมแรก → referral
4. Hit 1,000 paid users ใน 6 เดือน = ฿1M ARR threshold justify กลับมาเต็มตัว

---

## 10. Competitive Landscape

### Direct Competitors

| คู่แข่ง | Positioning | จุดแข็ง | จุดอ่อนเทียบ KuanGolf |
|--------|-------------|--------|----------------------|
| **Paper + LINE chat** | Status quo ฟรี | Inertia, ฟรี | ช้า ผิดพลาด ไม่มี settlement |
| **DogFight Golf** | Thai scoring app | 4,500 users, ฟรี | ไม่ LINE native, ไม่ PromptPay, ไม่มีต่อแต้ม |
| **Beezer Golf** | Side-bet calc + bank | 28+ games, ledger | ไม่มี halve-on-tie ไทย, wallet custody = compliance risk |
| **18Birdies/Hole19/GolfShot** | Global scoring | Premium, features | Eng-only, แพง (฿2,800-3,500/yr), ไม่มีต่อแต้ม, ไม่ LINE |
| **Golfdigg** | Booking + social | 100K+ installs | Booking-first ไม่ scoring |
| **โลกัณฑ์กอล์ฟ** | Thai calc + score | Thai UI | Basic, ไม่ LINE, ไม่ PromptPay |

### Unique Moat
1. **ต่อแต้ม halve-on-tie** — game format ไทยเท่านั้น คู่แข่ง copy ไม่ได้ถ้าไม่รู้กอล์ฟไทย
2. **Snake 3 variants** — ครอบคลุมทุก format ก๊วนไทย
3. **LINE-native** — match พฤติกรรม target (ชายไทย 45-65 อยู่บน LINE 56M MAU)
4. **PromptPay QR** — Thunder infra · Beezer ทำได้ยากไม่มี e-wallet license
5. **Compliance-safe** — records-only = ไม่ต้องขอ gaming license, ไม่มี escrow liability

---

## 11. Market Research

### Market Size (TAM)
- **นักกอล์ฟไทย:** ~2M (1.2M in-country + 800K tourist/expat)
- **SAM:** ~50-100K หัวก๊วนไทย 40-65 (10-20% ของนักกอล์ฟในประเทศที่จัดก๊วน)
- **Pricing power:** greenfee เฉลี่ย ฿1,500-7,500/รอบ · เดือนละ 2-4 รอบ → ฿999/ปี KuanGolf = <1 รอบ

### Pain Points (Ranked)

| Rank | Pain | Evidence | ความถี่ |
|------|------|----------|--------|
| 🔴🔴🔴 | **"Identity tension"** — Captain = exec ที่ได้รับความเคารพในงาน กลายเป็น "เหรัญญิก" ในก๊วน | Interview | ทุกรอบ |
| 🔴🔴🔴 | **Score card สลับ** → คนผิดได้รางวัล | "เอาสกอร์การ์ดผมไปใส่ในของเพื่อน" | บ่อย |
| 🔴🔴🔴 | **30+ นาทีคิดเงินหลังรอบ** — Pantip ถามค้าง 5+ ปี | "เสียเวลาคิด" | ทุกรอบ |
| 🔴🔴 | **จ่ายช้า** — "อีกไม่นาน" กลายเป็น 3 วัน | วัฒนธรรมเลี่ยงพูดตรง | หลังรอบ |
| 🔴🔴 | **เสียเพื่อน** — ทะเลาะเพราะ ฿500-1,000 | "เลิกคบเพื่อนเพราะเงิน" | รายปี |
| 🔴 | **กฎ side game งง** — Skins/Nassau/ต่อแต้มไม่ชัด | Pantip Q&A ซ้ำๆ | ตามรอบ |

### Channel Effectiveness (acquisition)
1. **LINE OA + forward 1:1** (open rate 80-90%, conversion สูงสุด)
2. **Facebook ads** (45+ = 23% ของ Thai FB · ฿10-20/click)
3. **Clubhouse word-of-mouth** (trust สูงสุด · CAC ต่ำสุด)
4. **Pantip** (intent สูง · volume ต่ำ)
5. **YouTube** (awareness ไม่ conversion)
6. **TikTok** (45+ = 22.6% · entertainment-focused ไม่ utility)

---

## 12. Brand Strategy

### Core Values (3 pillars)
1. **"ไม่มีใครเป็นจำเลย"** — หัวก๊วนไม่โดนโทษ · เป็นตัวกลางเป็นกลาง — ไม่มีคู่แข่งใครถือ messaging นี้
2. **"จบในรอบ ส่งเข้า LINE"** — Speed + workflow match (30 วิ vs 30 นาที)
3. **"ของก๊วนไทย ไม่ใช่ตำราฝรั่ง"** — Cultural moat (ต่อแต้ม, halve-on-tie, LINE, PromptPay)

### Brand Tone
- เพื่อนหัวก๊วนอาวุโสกว่า 5 ปี — ตรงๆ ใช้ได้จริง เคารพกัน
- ไทย 100% · ภาษาปาก · ไม่โอเวอร์ · ไม่ถ่อมตัว
- Copy สั้น กระชับ ชัดเจน ไม่ abstract

### Words to Use
- **identity:** หัวก๊วน, ก๊วน, เพื่อนซี้
- **pain:** เหรัญญิก, จำเลย, ดราม่าหลังรอบ
- **value:** จบในรอบ, 30 วินาที, เป็นกลาง, โปร่งใส, ส่งเข้า LINE, QR PromptPay
- **game:** ต่อแต้ม, halve-on-tie, System 36, รอบนี้

### Words to Avoid
- **Competitor-like:** "Score tracking app", "GPS", "Handicap tracker", "All-in-one", "Social golf"
- **Legal risk:** "Wallet", "Betting", "Gambling", "Bank", "Ledger"
- **Tech jargon:** "Subscription" → "ปีนึงเลย" · "Onboard" → "เริ่มใช้"

### Hero Positioning

**External:**
> "KuanGolf — หัวก๊วนไทยที่ฉลาด ไม่ต้องเป็นเหรัญญิกอีกต่อไป จบในรอบ ส่ง QR + สรุปเข้า LINE ก๊วน"

**Internal:**
> ปลดบทบาท "เหรัญญิก" จากหัวก๊วน โดยคำนวณ + ส่ง PromptPay QR + สรุปเข้า LINE ใน 30 วินาที — เพราะแอปสร้าง **สำหรับ** หัวก๊วน ไม่ใช่ **ดัดแปลง** มาจากแอปกอล์ฟระดับโลก

**Color scheme:** Primary green `#00C853` · Dark `#1d1d1f` · PWA theme `#0F3B2E`

---

## 13. Critical Gaps & Next Steps

1. **llms.txt ราคาผิด** — Pro ยังเขียน ฿790, Free = 1 game/month (ผิดหมด) → AI bot ตอบลูกค้าผิด → **แก้ด่วน**
2. **/docs/KNOWLEDGE_BASE หาย** — อ้างใน llms.txt แต่ 404 → **ต้องสร้าง**
3. **Marketing ยังไม่ยิง** — 30-day brief พร้อม 100% (captions, 35 assets) แต่ **โพสต์ 0 ตั้งแต่ 2026-05-26** → **push publish**
4. **User validation ค้าง** — pain/persona/emotional insights เป็น [hypothesis] จนกว่าจะ interview 10-15 หัวก๊วน → **ยังไม่ได้ทำ**
5. **Facebook URL** — ยังเป็น `profile.php?id=61589538174943` → เปลี่ยนเป็น `/KuanGolfApp`
6. **Free tier เกินไป** — Free = unlimited + ทุก side game ทำให้ไม่มี urgency upgrade Pro (GPS + history) เป็น "nice-to-have" ไม่ใช่ "must-have"

---

## Appendix: File Locations by Topic

| Topic | Primary Files | Location |
|-------|---------------|----------|
| Product specs | Product.md · FAQ — Live.md | `/Users/aexgee/SecondBrain/01 Projects/KuanGolf/` |
| Website & tech | Website & Tech.md · specs/01-07 | KB + `/Users/aexgee/Work/KuanGolf/marketing/specs/` |
| Pricing | Product.md · specs/03-pricing.md | ทั้งสองที่ |
| Brand | Brand Strategy Brain.md (v2.0, 1,037 บรรทัด) | KB |
| Strategy | Strategic Analysis.md | KB |
| Marketing status | Marketing.md | KB |
| Marketing plan (60-day) | promo-master-plan.md (v3) · briefs-html/ · briefs-md/ | `/Users/aexgee/Work/KuanGolf/marketing/` |
| Market research | Research Demand — Report.md (36KB, 60+ sources) | KB |
| Legal | specs/05-terms-privacy.md · Product.md | Work + KB |
| Design assets | Logo/, Mascot 3D/, covers/ | `/Users/aexgee/Work/KuanGolf/brand/` |
| Content | captions.md · content-30-brief.md · ai-image-prompts.md | `/Users/aexgee/Work/KuanGolf/marketing/` |
| Quick memory | project_kuangolf.md | `/Users/aexgee/.claude-warp/projects/-Users-aexgee/memory/` |
| Smart-Env index | 30+ .ajson | `/Users/aexgee/SecondBrain/.smart-env/multi/` |
