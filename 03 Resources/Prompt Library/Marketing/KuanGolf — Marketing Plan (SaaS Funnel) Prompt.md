---
title: KuanGolf — Marketing Plan (SaaS Funnel) Prompt
type: prompt
context: marketing
product: KuanGolf
use: สั่ง ChatGPT/Claude ให้เขียนแผนการตลาดฉบับทางการ จัดโครงรอบ SaaS funnel (AARRR) พร้อมอ้างอิง framework
model: ChatGPT (GPT-5+) / Claude Opus
created: 2026-07-01
last_verified: 2026-07-01
status: live
tags: [prompt, marketing, kuangolf, saas, gtm, funnel, aarrr, plg]
---

# KuanGolf — Marketing Plan (SaaS Funnel) Prompt

> พรอมป์สั่งให้ AI เขียน **แผนการตลาด GTM ฉบับทางการ** ให้ KuanGolf จัดโครงทั้งแผนรอบ **SaaS marketing funnel (AARRR เป็นแกน + Growth Loop co-primary)** พร้อมอ้างอิง framework จริงแบบ attribution ถูกต้อง
>
> **ที่มา:** สังเคราะห์จาก workflow research 5 สาย (funnel models / PLG-freemium / GTM structure / lifecycle-retention / positioning-content) → fact-check adversarial → blueprint 17 หมวด · 2026-07-01

## ใช้เมื่อไหร่
- ต้องการแผนการตลาด KuanGolf ที่ "ลงมือทำได้จริง" ไม่ใช่ทฤษฎีลอย
- ต้องการให้ทุกหัวข้อ map เข้า funnel + KPI + PostHog event
- อยากได้เอกสารระดับผู้บริหาร/บอร์ด ที่อ้างอิง framework ถูกต้อง audit ได้

## วิธีใช้
1. copy พรอมป์ในกล่องด้านล่างทั้งก้อน
2. แปะใน ChatGPT (แนะนำสร้างเป็น Project "KuanGolf" ก่อน) หรือ Claude
3. ถ้าข้อมูล product เปลี่ยน (ราคา/ช่องทาง/สถานะ) แก้ในส่วน CONTEXT + HARD CONSTRAINTS ก่อนส่ง
4. ได้แผนแล้ว → รอบสองสั่งต่อ "ขยายหมวด X เป็น execution checklist รายสัปดาห์"

---

## PROMPT (copy ทั้งก้อน)

```
บทบาท: คุณคือ SaaS CMO (Chief Marketing Officer) ที่เชี่ยวชาญ product-led growth
และ freemium go-to-market ในตลาดไทย

โจทย์: เขียน "แผนการตลาดฉบับทางการ" (Formal Go-to-Market / Marketing Plan)
ให้ผลิตภัณฑ์ KuanGolf โดยจัดโครงสร้างทั้งแผน "รอบ SaaS marketing funnel" อย่างชัดเจน
นี่คือเอกสารสำหรับ "ใช้จริง/ลงมือทำ" (execution document ~10-15 หน้า)
ไม่ใช่รายงานวิจัยหรือ pitch deck ระดมทุน

═══════════════════════════════════════════
ข้อมูลผลิตภัณฑ์ (CONTEXT)
═══════════════════════════════════════════
- KuanGolf = LINE-native PWA web app สำหรับก๊วนกอล์ฟไทย: บันทึกสกอร์ +
  คำนวณ side-bet + สร้าง PromptPay QR เคลียร์เงินอัตโนมัติ "แอปไม่ถือเงินเอง"
- Positioning: "Settlement specialist สำหรับก๊วนกอล์ฟไทย" ไม่ใช่แอปกอล์ฟครบวงจร
  (อย่าไปสู้ 18Birdies/GolfShot ตรงๆ) — คู่แข่งตัวจริงคือ "จดโพยมือ / Excel /
  คิดเงินในหัวในกลุ่ม LINE" (สถานะ do-nothing)
- Moat: ต่อแต้ม (Thai halve-on-tie handicap) + LINE-native + PromptPay +
  ไม่ถือเงิน (compliance-safe ไม่ต้องขอ gaming license)
- Side games 15+: Snake 3 แบบ, Nassau, Skins, ต่อแต้ม, Junk 8 แบบ, Birdie Pot,
  Stableford

═══════════════════════════════════════════
ข้อจำกัด (HARD CONSTRAINTS — ห้ามละเมิด)
═══════════════════════════════════════════
- Pricing (freemium): Free ฿0 (เล่นไม่จำกัด) / Pro ฿999/ปี / Group ฿1,290/ปี /
  Lifetime ฿2,490 ครั้งเดียว
- Payment: PromptPay QR อย่างเดียว ไม่มีบัตรเครดิต
- Platform: LINE-native (LIFF Mini App + OA @kuangolf), Next.js + Supabase
- Analytics: PostHog (ติดตั้งแล้ว)
- งบการตลาด: เพดาน ฿30,000/เดือน
- สถานะ: pre-traction, ผู้ใช้จ่ายเงิน 0 ราย, product live แล้ว
- Target/ICP: หัวก๊วน ("Captain") อายุ 40-65 ปี เจ้าของ SME/ผู้บริหาร กรุงเทพฯ+
  ปริมณฑล mobile-first ใช้ LINE หนัก ห่วง face/ภาพลักษณ์ในกลุ่มเพื่อน
- Channels: LINE OA + Facebook page + kuangolf.com พร้อมใช้ ·
  IG/TikTok/YouTube ยังไม่เริ่ม (ให้ roadmap ไว้ อย่าเปิดพร้อมกันหมด)

═══════════════════════════════════════════
สถาปัตยกรรม FUNNEL ที่ต้องใช้ (บังคับ)
═══════════════════════════════════════════
- SPINE (แกนหลัก) = AARRR / Pirate Metrics (Acquisition → Activation →
  Retention → Referral → Revenue) — ใช้เป็น operating model วัดใน PostHog
- CO-PRIMARY = Growth Loop "หัวก๊วนชวนก๊วน" (captain-invites-group) —
  reframe Acquisition+Referral เป็น loop เดียวที่ทบต้น เพื่อไม่ให้การเติบโต
  พึ่งงบ ฿30k/mo ตลอด
- OVERLAY 1 = See-Think-Do-Care → ใช้จัดสรรงบ ฿30k/mo ตาม intent
  (อย่ายิง "ซื้อเลย" ใส่คนที่ยังไม่มี intent)
- OVERLAY 2 = TOFU/MOFU/BOFU → ใช้จัด content calendar
- OVERLAY 3 = Awareness→Consideration→Conversion→Loyalty→Advocacy →
  ใช้เป็น narrative สำหรับบอร์ด/ผู้บริหารเท่านั้น
กติกา: ทุกหัวข้อในแผน ต้องติด "แท็ก funnel stage" ในวงเล็บที่หัวข้อ

═══════════════════════════════════════════
โครงสร้างแผน (ทำตามลำดับนี้เป๊ะ 17 หมวด ห้ามเปลี่ยนโครง)
═══════════════════════════════════════════
1. บทสรุปผู้บริหาร [All] — เขียนทีหลังสุดแต่วางไว้หน้าแรก · ประกาศ North-Star
   เดียวเป็นตัวเลข (แนะนำเป็น activation เช่น "ก๊วนที่ settle จริง X ก๊วน ใน 90 วัน"
   ไม่ใช่ "โต") · positioning หนึ่งบรรทัด · กรอบ funnel · งบ · เฟรมมิ่งตรงๆ ว่า
   ที่ 0 ผู้ใช้ อัตรา free→paid 2-5% ถือว่า on-benchmark, เลเวอเรจสูงสุดคือ
   ปริมาณ top-of-funnel + ความเร็ว activation ไม่ใช่บีบ paywall
2. Product Overview & Positioning [Foundation] — ใช้ April Dunford: คู่แข่งจริง
   คือ จดโพย/Excel/คิดในหัว · Big-Fish-Small-Pond ("แอป settle ของก๊วนไทย")
   ตอนนี้ → ค่อยขยับเป็น Create-New-Game ("ก๊วนจบในรอบ") · ย้ำว่าไม่ใช่แอป
   กอล์ฟครบวงจร
3. Market Sizing + ICP + Persona [Foundation] — TAM-SAM-SOM แบบ lean ·
   เขียน ICP + persona ก่อนพูดเรื่อง channel · ใช้ JTBD: งานจริงไม่ใช่ "จดสกอร์"
   แต่คือ "เลิกเป็นคนคิดเงินที่โดนเพ่งเล็ง → รอบที่ยุติธรรมและ settle เองโดยไม่มีใคร
   รู้สึกเป็นจำเลย" = "ไม่มีใครเป็นจำเลย" · ใส่ Job Story 1-2 อัน
4. Competitive Analysis [Foundation] — คู่แข่งพาดหัว = สถานะ do-nothing
   (กระดาษ + PromptPay มือ + ทะเลาะกัน) · อธิบายว่าทำไมห้ามสู้ฟีเจอร์กับแอป
   กอล์ฟระดับโลก
5. Positioning Statement + Messaging Hierarchy [Foundation→TOFU] —
   value prop เดียว → 3 pillars: FAIR (ยุติธรรม·ต่อแต้ม) / INSTANT (จบในรอบ·
   ส่งเข้า LINE) / TRUST (แอปไม่ถือเงิน) พร้อม proof แต่ละอัน · ใช้ JTBD
   Four Forces: ขยาย Push+Pull, ฆ่า Anxiety ("ไม่ถือเงิน โอนกันเอง ฟรีไม่ผูกบัตร")
   + Habit ("ลองรอบเดียวเลิกจดโพย") · เป็น single source of truth ของ copy ทั้งหมด
6. Pricing, Packaging & Value-Metric [Revenue] — value metric = "เลเยอร์ที่ทบต้น"
   ไม่ใช่ core job · เก็บ score+side-bet+QR settle "ฟรีตลอด" (นี่คือพื้นที่ viral) ·
   gate GPS + ประวัติเต็ม + season stats + handicap ไว้หลัง Pro
   ("gate power, not access") · เพิ่ม reverse trial (Pro เต็ม ~30 วัน/3 รอบแรก
   ไม่ผูกบัตร → ตัดกลับ → loss aversion) · social-status trigger (badge Pro
   ที่หัวก๊วนเห็นได้ ถ้วยเฉพาะ Pro) · เช็คราคาด้วย Van Westendorp เบาๆ · anchor
   ฿999 = ค่ากรีนฟีรอบเดียว · หมายเหตุ Lifetime กด NRR อนาคต = มองเป็น cash-now
7. GTM Motion + Channel Strategy (See-Think-Do-Care budget map) [Acquisition] —
   motion = PLG/self-serve · แบ่งงบ ฿30k ตาม intent: See=organic/earned
   อย่าฮาร์ดเซล / Think=remarketing+comparison / Do=ใส่งบ paid ที่หายากตรงนี้
   (search + LIFF signup) / Care=renewal+community · ลำดับ: LINE OA+FB+web+
   AI-search ก่อน, IG/TikTok/YouTube ทีหลัง
8. Acquisition Plan [Acquisition + See/Do] — แต่ละ channel ผูก CAC assumption:
   LINE OA add campaign + auto-tag · FB golf-ก๊วน community (ดึงหัวก๊วนตัวจริง
   เป็น advocate; FB=discovery, LINE=ใช้งาน) · product-led SEO คีย์เวิร์ด
   ("แอปคิดเงินก๊วนกอล์ฟ", "สรุปยอด PromptPay หลังออกรอบ", "คิดต่อแต้มอัตโนมัติ") ·
   AI-search land-grab: ship llms.txt (ไทย+อังกฤษ) + AEO FAQ/HowTo schema
   (คู่แข่งไทยยังไม่มีใครทำ)
9. Activation Plan (aha < 10 นาที ระดับก๊วน) [Activation] — นิยาม aha ชัด:
   PromptPay QR split ครั้งแรกต่อหน้าทั้งก๊วน · Setup→Aha→Habit: pre-fill สมาชิก
   จากกลุ่ม LINE, พิมพ์น้อยสุด (ผู้ใช้ 40-65) ให้ TTV<10 นาที · onboarding
   checklist ใน LIFF · วัด activation "ระดับก๊วน" (ทั้งก๊วน settle ไหม) ไม่ใช่ราย
   คน · นี่คือ north-star ต้อง instrument event นี้ก่อนจ่ายค่า acquisition
10. Retention & Lifecycle Plan [Retention] — retention คือฐาน สร้างก่อนสเกลงบ ·
    Hooked loop: trigger=LINE push ก่อน/หลังออกรอบ / action=แตะจดสกอร์ /
    variable reward=leaderboard+เผยใครติดใคร+ยอด settle / investment=roster
    ที่เซฟ+scorecard ย้อนหลัง+กติกาต่อแต้มเอง (moat+switching cost) · การ์ดสรุป
    หลังรอบยิงกลับเข้ากลุ่มอัตโนมัติ · D7/D30 cohort ใน PostHog · เฝ้า seasonal
    churn · PromptPay renewal reminder อัตโนมัติ
11. Referral & Growth-Loop Engine (แกนกลยุทธ์) [Referral + Growth Loop] —
    ออกแบบ loop ชัด: brand ทุก QR/สรุป ("สรุปโดย KuanGolf" + ลิงก์เข้าร่วม)
    ให้ทุกโพสต์ใน LINE = โฆษณาฟรีที่คน 3-15 คนในกลุ่มเป้าหมายเป๊ะเห็น · เพิ่ม hook
    "เริ่มก๊วนของคุณเอง / หัวก๊วนคนใหม่" · dual-sided referral (ได้ Pro ฟรีทั้งคู่
    จ่ายเมื่อเพื่อนซื้อ Pro; เป็นเครดิตไม่ใช่เงินสด; แชร์ผ่าน LINE แตะเดียว; กัน
    self-referral) · หลาย loop (collaboration/referral/content-SEO) · วัด
    share→click→signup · คำนวณ K = i × c (ตั้งเป้าจริง ~0.5 = ตัวคูณ 2 เท่า)
12. Revenue & Conversion Plan [Revenue] — free→paid คือ money metric (ไม่มี
    trial, free ไม่จำกัด) · ตัวขับ: reverse trial+loss aversion / status trigger /
    usage trigger (จำกัดประวัติ free เหลือ N รอบ; กำแพง "ดู season/handicap เต็ม"
    โผล่ตอนหัวก๊วนอยากย้อนดูพอดี) · Land→Adopt→Expand→Advocate: solo Pro →
    Group ฿1,290 ("ปลดล็อกทั้งก๊วน") → Lifetime เป็น anchor ของหายาก · เป้าจริง
    2-5% ช่วงแรก
13. Content Strategy (TOFU/MOFU/BOFU + Ahrefs Business-Potential) [Content] —
    calendar แบบ BOFU/product-led ก่อน (อย่าซื้อ TOFU กว้างด้วยงบ ฿30k) · ให้
    คะแนนหัวข้อ 0-3 ตาม product-fit เขียนคะแนน 2-3 ก่อน · TOFU: "วิธีคิดต่อแต้มให้
    ยุติธรรม", "รวมกติกาไซด์เกม 15 แบบ" (evergreen + เป็นอาหาร AI-search) ·
    MOFU: เครื่องคิดต่อแต้ม/side-bet บนเว็บ, เทียบ "จดมือ/Excel vs KuanGolf" ·
    BOFU: หน้า pricing คม, LIFF demo 1 นาที, testimonial ก๊วนจริง, FAQ ตอบ
    "ปลอดภัยไหม/ใช้ยากไหม" ล่วงหน้า · ตัดสินแต่ละชิ้นด้วย KPI ที่ถูก
14. Budget & Resource Allocation (฿30k/mo) [All] — ตาราง spend-by-channel
    ทุกบรรทัดผูก CAC · ให้น้ำหนัก organic/owned/loop (CAC ~0: LINE OA + FB
    community + referral + SEO/AEO) เป็นหลัก · paid = ตัวขยายไว้ "หว่านก๊วน active"
    ที่จะปั่น loop ไม่ใช่ซื้อ impression · math เพดาน: ที่ CAC ~฿250, ฿30k เลี้ยงได้
    ~120 paying/เดือนจาก paid ล้วน → loop ต้องแบกการเติบโต
15. Financial Model & Unit Economics [Revenue] — เขียนสูตรชัด (appendix):
    CAC (paid vs blended), LTV = (ARPU × gross margin)/churn, LTV:CAC ≥3:1,
    CAC payback · ARPU ~฿999/ปี (blended ต่ำลงเพราะมี free + Lifetime) · จุดแข็ง
    freemium: prepaid annual ผ่าน PromptPay = payback แทบทันที, annual churn
    ~1/3 ของ monthly · เพราะ LTV/user บาง โมเดลเวิร์กเมื่อ CAC ~0 + retention สูง
    เท่านั้น = ทำเป็น thesis ชัด
16. KPIs, Targets & Analytics Stack [All] — North-star = activation ไม่ใช่ MRR ·
    instrument OpenView 5 stage (Discover→Start→Activate→Convert→Scale) เป็น
    funnel เดียวใน PostHog รายงาน conversion ราย stage แล้วแก้ stage ที่อ่อนสุด ·
    ทุก AARRR stage มีเป้า + cadence · tripwire (LTV:CAC ≥3:1, payback <12mo,
    NRR, churn, free→paid 3-5% ดี/8-12% เยี่ยม) เป็นเส้นแดงใน risk · เลี่ยง vanity
    metric (ยอดดาวน์โหลด, กราฟสะสม)
17. 30-60-90 Day Roadmap + Risk Register [All] — เฟสพร้อมเจ้าของงาน:
    เฟส1=instrument activation+retention + native loop + LINE OA foundation
    (rich menu เป็นหน้า home ใน LINE: เริ่มรอบ/ก๊วนของฉัน/อัปเกรด Pro/ช่วยเหลือ) ·
    เฟส2=referral program + BOFU content + AEO · เฟส3=paid amplification เมื่อ
    LTV:CAC + Pro conversion พิสูจน์แล้ว + ค่อยลำดับ IG/TikTok/YouTube ·
    risk register + mitigation รายข้อ (โดยเฉพาะ free tier ใจดีเกิน → gate power +
    reverse trial, seasonal churn, LINE block rate <10%, ผู้ใช้สูงวัยกังวลตอนสมัคร,
    พึ่ง paid เกินในงบจำกัด)

═══════════════════════════════════════════
กรอบทฤษฎีที่ต้องอ้างอิง (อ้างชื่อ + attribution ให้ถูก ห้ามมั่ว)
═══════════════════════════════════════════
- AARRR / Pirate Metrics — Dave McClure, "Startup Metrics for Pirates" (2007)
  ⚠️ อย่าติดป้าย "500 Startups" (เขาตั้ง 500 Startups ปี 2010; ปี 2007 เป็น angel)
- Growth Loops — Reforge (Brian Balfour, Casey Winters, Kevin Kwok, Andrew Chen)
- See-Think-Do-Care — Avinash Kaushik (Google), ~2013
- TOFU/MOFU/BOFU — สาย inbound/HubSpot; นิยาม stage ใช้ Dave Chaffey
  (Smart Insights) แบบ vendor-neutral
- Classic funnel Awareness→Advocacy — โมเดลดั้งเดิม (ไม่มีผู้แต่งเดี่ยว)
- OpenView PLG funnel (Discover→Start→Activate→Convert→Scale) — OpenView
  Partners; benchmark โดย Kyle Poyar (นิวส์เลตเตอร์ปัจจุบัน growthunhinged.com)
- Activation: Setup→Aha→Habit — Reforge
- Hooked (Trigger→Action→Variable Reward→Investment) — Nir Eyal
- Viral loop / K = i×c — Andrew Chen (a16z)
- Reverse Trial + "Gate Power, Not Access" — Elena Verna ⚠️ ใช้ "popularized"
  ไม่ใช่ "coined"
- Value-Metric Pricing — Patrick Campbell / ProfitWell (Paddle); WTP ผ่าน
  Van Westendorp
- Positioning "Obviously Awesome" (5+1 components, 3 styles) — April Dunford
- JTBD + Four Forces (Push/Pull/Anxiety/Habit) — Clayton Christensen (ทฤษฎี
  1990s) + Bob Moesta ⚠️ อย่าเรียกว่า "mid-1990s milkshake study" (เคส milkshake
  เป็นยุค 2000s)
- SaaS unit economics (LTV:CAC ≥3:1, payback <12mo) — David Skok, forEntrepreneurs
- 16 Startup Metrics — a16z
- NRR/payback/magic number benchmarks — Bessemer (BVP Atlas) ⚠️ SaaS Magic
  Number = Scale Venture Partners (Lars Leckie) นิยมโดย Bessemer — อย่าไปยกให้ a16z
- Ahrefs Business Potential Score (0-3) — Ahrefs
- llms.txt / AEO — Jeremy Howard (Answer.AI), ก.ย. 2024 ⚠️ ใส่ caveat จริงว่า
  impact ยัง marginal/experimental (Google บอกไม่ใช้) → ของจริงที่ได้คือ AEO/schema,
  มอง llms.txt เป็นประกันราคาถูก
กติกา: อ้างอิง primary source เป็นหลัก อย่ายก vendor/SEO blog เป็น canonical authority

═══════════════════════════════════════════
น้ำเสียง & รูปแบบ OUTPUT
═══════════════════════════════════════════
- เขียนแผนเป็น "ภาษาไทยผู้บริหาร" ธรรมชาติ ตรงประเด็น ไม่ใช่ภาษาแปลหรือราชการ
  (audience = COO/บอร์ด) · คงอังกฤษเฉพาะศัพท์เทคนิค (AARRR, CAC, LTV, PostHog,
  LINE OA, PromptPay, ต่อแต้ม)
- ห้ามใช้ emoji ทุกที่
- ตัวเลขต้องซื่อสัตย์: ตัวเลขที่มาจากแหล่งเดียว (reverse-trial 10-40%, LINE open
  60-80%, "activated user convert 5x") ให้ label ว่าเป็นตัวอย่าง/directional
  ไม่ใช่ benchmark ตายตัว
- ทุก stage ต้องมี: KPI ที่ตั้งชื่อ + PostHog event + เป้าที่เป็นตัวเลข
- นิยาม aha moment ให้ชัด (PromptPay QR settle ครั้งแรกระดับก๊วน, TTV <10 นาที)
- ออกแบบ growth loop อย่างน้อย 1 อัน พร้อมคณิต K = i × c
- budget section ทุก channel ผูก CAC + ลำดับการใช้เงิน (LINE/FB/AEO ก่อน,
  IG/TikTok/YouTube ทีหลัง)
- หัวข้อใช้ header สะอาด + แท็ก funnel stage ในวงเล็บ · ย่อหน้าสั้นอ่านบนมือถือได้ ·
  มี appendix สูตรคำนวณ · บทสรุปผู้บริหารเขียนสุดท้ายวางหน้าแรก ·
  ปิดท้ายด้วยลิสต์ "Frameworks Cited" ให้ตรวจ attribution ได้

เริ่มเขียนแผนได้เลย ทำตามโครง 17 หมวดตามลำดับ
```

---

## ทำไมพรอมป์นี้ได้ผล (โน้ตออกแบบ)
- **แกน = AARRR** เป็น operating spine (map เข้า PostHog ที่มีอยู่แล้ว) เพราะ KuanGolf เป็น freemium/PLG หัวใจอยู่ที่ activation + retention ไม่ใช่ awareness
- **ยก Growth Loop เป็น co-primary** — งบ ฿30k/mo ถ้าใช้ funnel เชิงเส้นล้วนต้องเทเงินซื้อหัวก๊วนตลอด แต่กอล์ฟเป็นกิจกรรมกลุ่ม (1 หัวก๊วน = 3-15 คนเห็น QR) → loop "หัวก๊วนชวนก๊วน" ทำให้โตทบต้น (Dropbox-pattern)
- **บังคับโครง 17 หมวด verbatim** กัน AI มโนโครงสร้างทั่วๆ ไป
- **ฝัง 5 กับดัก attribution** ที่ fact-check เจอ: McClure≠500 Startups · Magic Number=Scale VP ไม่ใช่ a16z · Verna "popularized" ไม่ใช่ "coined" · JTBD milkshake ยุค 2000s · llms.txt มี caveat → อ้างอิงถูก ไม่หลอน

## Reference frameworks (attribution ตรวจแล้ว)
AARRR (McClure 2007) · Growth Loops (Reforge: Balfour/Winters/Kwok/Chen) · See-Think-Do-Care (Kaushik) · OpenView PLG funnel (Kyle Poyar / growthunhinged.com) · Hooked (Nir Eyal) · K=i×c (Andrew Chen) · Reverse Trial (Elena Verna) · Value-Metric Pricing (Patrick Campbell/ProfitWell) · Obviously Awesome (April Dunford) · JTBD Four Forces (Christensen + Moesta) · SaaS Metrics 2.0 (David Skok) · BVP Atlas (Bessemer) · Ahrefs BP Score · llms.txt (Jeremy Howard)

## Related
- [[UNIVERSAL MASTER PROMPT]]
- [[../../../01 Projects/KuanGolf/KuanGolf — Master Reference|KuanGolf — Master Reference]]
- [[../../../01 Projects/KuanGolf/Strategic Analysis|KuanGolf — Strategic Analysis]]
