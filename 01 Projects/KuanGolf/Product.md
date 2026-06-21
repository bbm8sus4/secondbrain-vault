---
project: KuanGolf
type: product-spec
last_updated: 2026-06-21
tags: [kuangolf, product, features, pricing, side-games]
---

# Product — KuanGolf

## ปัญหาที่แก้
1. จดสกอร์ผิดจากสมุดเปียก / ลายมือคนละแบบ
2. นับแต้ม Side Game ไม่ทัน (Snake, Skins, Nassau, Press)
3. กว่าจะรู้ใครชนะก็ค่ำ (ไล่สกอร์ที่ 19th hole)
4. ไม่มีสถิติย้อนหลัง / handicap จริง

## ฟีเจอร์หลัก

### Scoring
- Stroke Play, Stableford (standard + modified)
- UI: ตัวเลขใหญ่ font 20px ปุ่ม 64px+ ใช้ได้กลางแดด ออกแบบให้พี่ๆ น้าๆ ใช้ได้
- ออฟไลน์ได้ (PWA standalone)

### Side Games (15+ ประเภท)
- **งู (Snake)** — 3 variants
  - งูธรรมดา (คนแย่สุดถืองู)
  - Triple Snake (3-Putt + Water + OB)
  - Snake-of-Snake (pot ทบไปเรื่อย)
- **Skins** — ดีสุดได้ skin · carry-over อัตโนมัติ
- **Nassau** — 3 matches (Front 9, Back 9, Total) · 2-2-2 + Press
- **Birdie Pot** — Eagle ×2, Albatross ×4
- **ต่อแต้ม (Tor Taem)** — handicap แบบไทย จับคู่ par-type, halve-on-tie (≠ ฝรั่ง spread). **มีเฉพาะ KuanGolf**
- **Stableford** — 4/3/2/1/0
- **Junk** — 8 types: Greenie · Sandy · Polly · Barkie · Fish · Arnie · Chip-in (×2) · Up & Down

### Settlement & Sharing
- **PromptPay QR Native** — generate QR + จำนวน + payee แล้วผู้เล่นโอนผ่านแอปธนาคารเอง · **แอปไม่ถือเงิน**
- **ระบบจับคู่หนี้-เจ้า** — เจ้าหนี้ใหญ่คู่กับลูกหนี้ใหญ่ ลดรายการโอน (6 → 2)
- **LINE Group share** — สรุปสกอร์ + ยอด + รายการโอน → ส่งเข้า LINE ก๊วน 1 คลิก

### History & Stats
- ประวัติเกมส่วนตัว
- สถิติ per-player
- **GPS ระยะถึงธงเรียลไทม์** (Pro เท่านั้น — ฟีเจอร์ใหม่)
- Group Leaderboard (Group package)

### Onboarding
- Wizard 4 ขั้นตอน · ข้ามได้ทุกอย่าง
- Default: Par 72, 18 หลุม
- LINE Login + LIFF Mini App

## Pricing (live ณ 2026-06-21)

| แพ็กเกจ | ราคา | สิทธิ์ |
|---|---|---|
| **Free** | ฿0 ตลอดไป | เล่นไม่จำกัด · Stableford + Side Game ครบ · แชร์ลง LINE ได้ |
| **Pro** | **฿999/ปี** (~฿83/เดือน) | Free + GPS ระยะถึงธง + ประวัติย้อนหลังเต็ม + สถิติส่วนตัว · 8 คน/ก๊วน · Nassau team 2/3 คู่ |
| **Group** | ฿1,290/ปี (หาร 6 ≈ ฿215/คน/ปี) | Pro + Group Leaderboard |
| **Lifetime** | ฿2,490 ครั้งเดียว | Pro ตลอดชีพ |

**ข้อสังเกต — pricing ไม่ตรงกัน:**
- llms.txt (updated 2026-05-06) ระบุ Pro = ฿790/ปี · Free = 1 เกม/เดือน
- หน้า /sale (FAQ live ตอนนี้) ระบุ Pro = ฿999/ปี · Free = เล่นไม่จำกัด
- → แปลว่า llms.txt **ล้าสมัย** ควร update ให้ตรงเว็บ (สำคัญ เพราะ AI bot อ่าน llms.txt ไปตอบลูกค้า)

### เงื่อนไขการชำระ
- **PromptPay QR เท่านั้น** (ไม่รับบัตรเครดิต)
- **ไม่ต่ออัตโนมัติ** — แจ้งผ่าน LINE/อีเมล 7 วันก่อนหมดอายุ
- คืนเงินภายใน 7 วัน

## Differentiator
1. **ต่อแต้ม halve-on-tie** — มีเฉพาะ KuanGolf (ฝรั่ง spread ไม่ใช่)
2. **Snake 3 variants** — รองรับทุกแบบที่ก๊วนไทยเล่นจริง
3. **LINE-native** — ตรงพฤติกรรมไทย ไม่ใช่ port มาจาก app ฝรั่ง
4. **PromptPay QR + ไม่ถือเงิน** — compliance-safe + ไม่ต้องลงข้อมูลบัตร
5. **โหมดตัวใหญ่กลางแดด** — ออกแบบให้นักกอล์ฟ 40-65 ปี ใช้ได้จริง
6. **AI-friendly** — มี llms.txt · robots.txt เปิดให้ GPTBot/ClaudeBot/PerplexityBot อ่าน /sale + /pricing

## Compliance
- **ไม่ใช่การพนัน** — บันทึกเฉพาะ ไม่ถือเงิน · PromptPay = peer-to-peer off-platform · subscription = SaaS billing
- ข้อตกลงห้ามใช้เพื่อการพนันผิดกฎหมายไทยทุกประเภท
- as-is service · ไม่รับผิดข้อพิพาทระหว่างผู้เล่นในก๊วน
- PDPA compliant · ไม่ขายข้อมูล · ไม่ใช้ cookie บุคคลที่สาม · เข้า/แก้/ลบ/โอน ได้ที่ hello@kuangolf.com
