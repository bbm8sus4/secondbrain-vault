---
project: KuanGolf
type: tech-spec
last_updated: 2026-06-21
tags: [kuangolf, tech-stack, sitemap, compliance]
---

# Website & Tech — KuanGolf

## Sitemap

| Path | Status | Notes |
|---|---|---|
| `/` | OK | Landing — "จดสกอร์ทั้งก๊วน" + screenshot |
| `/sale` | OK | หน้าขาย — pain points + features + FAQ + Side Game cards |
| `/pricing` | OK | Free + Pro + ปุ่มเริ่มฟรี |
| `/onboarding` | OK (auth) | Wizard 4 ขั้นตอน |
| `/history` | OK (auth) | ประวัติเกมส่วนตัว |
| `/terms` | OK | Terms of Service |
| `/privacy` | OK | Privacy Policy (PDPA) |
| `/llms.txt` | OK | สำหรับ AI bots |
| `/docs/KNOWLEDGE_BASE` | 404 | อ้างใน llms.txt แต่ยังไม่มีจริง — TODO |
| `/marketing` | 404 | ไม่มี |
| `/about` | 404 | ไม่มี |
| `/account` | 404 | ไม่มี |

## Hidden paths (จาก robots.txt)
- `/api/` — API endpoints (disallowed)
- `/liff/` — LINE LIFF integration
- `/(standalone)/` — PWA standalone mode

## robots.txt
- **AI Bots** (GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, Google-Extended): Allow `/sale`, `/pricing`, `/llms.txt`
- **ทั่วไป**: Allow `/`, Disallow `/api/`, `/liff/`, `/(standalone)/`

## Tech Stack (จาก llms.txt + meta)
- **Frontend**: Next.js 16 · React 19 · TypeScript · Tailwind v4
- **State**: Zustand
- **Backend/DB**: Supabase (Postgres + Auth + Storage)
- **Auth**: LINE Login + LIFF Mini App
- **Analytics**: PostHog
- **Messaging**: LINE Messaging API
- **Payment**: PromptPay QR (generate-only, ไม่ถือเงิน)
- **Locale**: th_TH (Thai-first, English secondary)
- **App version**: 0.1.0 (commit `fa754d2782883abe63a8046d7d708538ae889ce5`)

## Compliance / PDPA สรุป

### ข้อมูลที่เก็บ
- LINE profile (ชื่อแสดง + รูปสาธารณะ)
- สกอร์กอล์ฟ
- ข้อมูล PromptPay (เพื่อ generate QR)
- สถิติการใช้งาน

### การใช้
- ให้บริการจดสกอร์
- ซิงค์ข้อมูลภายในก๊วน
- แสดงสถิติส่วนตัว
- ปรับปรุงระบบ

### การแชร์
- **ไม่ขาย ไม่ให้เช่า ไม่แลก** กับบุคคลที่สามเพื่อการตลาด
- แชร์เฉพาะ: ผู้เล่นในก๊วนเดียวกัน · ผู้ให้บริการ infra · หน่วยงานราชการตามคำสั่งศาล

### สิทธิ์ผู้ใช้ (PDPA)
- ขอเข้าถึง / แก้ไข / ลบ / โอนข้อมูล / เพิกถอนความยินยอม → hello@kuangolf.com ภายใน 30 วัน

### Cookies
- Session cookies + localStorage เพื่อจดจำ login + ตั้งค่า
- **ไม่ใช้ third-party cookies**

## Anti-gambling stance
- ห้ามใช้เพื่อการพนันผิดกฎหมายไทยทุกประเภท (ระบุใน ToS)
- แอป "บันทึกเฉพาะ" — ไม่เคยถือ / ประมวลผล / escrow เงินเดิมพัน
- PromptPay QR = ความสะดวกสำหรับการโอน peer-to-peer ที่ผู้เล่นทำเอง
- Subscription billing = SaaS revenue ไม่ใช่ gambling revenue
- **Implication**: เปิดได้ทั่วไทยตามกฎหมาย ไม่ต้องขอใบอนุญาตการพนัน
