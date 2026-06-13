---
tags: [friday, ai-bot, memory, knowledge-base]
type: index
project: Friday AI Bot
created: 2026-06-12
updated: 2026-06-12
---

# 🧠 Friday — Knowledge Base / Bot Memory

โฟลเดอร์นี้คือ **"สมอง" ของ Friday AI bot** — เก็บข้อมูลทุกอย่างที่ Friday ควรรู้/จดจำเกี่ยวกับงานบริหารของ COO (Bob/Watcharin) ทีม Thunder Solution / EasySlip / EasyBOT / EasyCRM / BoostSMS / SHIFT

> **ขอบเขต**: เฉพาะข้อมูลที่เกี่ยวกับ Friday bot's operations เท่านั้น — ไม่ใช่ memory ส่วนตัวของ user หรือเรื่องอื่นๆ
>
> **แหล่งข้อมูลหลัก**: D1 database `my-ai-bot-db` (Cloudflare) — table `summaries` (weekly + daily), `commitments`, `alerts`, `tasks`, `memories`, `group_registry`

---

## 📂 โครงสร้าง

### Monthly Recaps/
สรุปเดือนรวมจากทุกกลุ่มแชท — ใช้ AI สังเคราะห์จาก weekly + daily summaries
- [[Monthly Recaps/2026-05 พฤษภาคม|May 2026]] — เดือนแรกที่บันทึก (151 weekly + 426 daily)

### Themes/
รายงานละเอียดแยกตามหมวด business — ใช้เป็น context สำหรับงานเฉพาะหัวข้อ
- [[Themes/2026-05 Thunder Operations]]
- [[Themes/2026-05 EasySlip + Finance]]
- [[Themes/2026-05 EasyBOT + Marketing]]
- [[Themes/2026-05 Product + Dev]]
- [[Themes/2026-05 EasyCRM + Sales + HR]]
- [[Themes/2026-05 SHIFT + Talk to Bob]]

### _assets/
ไฟล์ HTML render-ed สำหรับ print/share

---

## 🤖 Friday Bot — Technical Reference

**Type**: Cloudflare Worker, single-file `src/index.js` (~3500 lines)
**Repo**: `~/my-ai-bot`
**DB**: D1 SQLite `my-ai-bot-db` (id: cecf8fa2-a44c-4605-ab9e-e726f3c1e0b4)
**Migrations**: `migrations/0001-0029` (KV store added 0029)
**Cron**: ทุก 3 ชั่วโมง → `proactiveAlert`, `proactiveInsightAlert`, `summarizeAndCleanup`
**AI**: Gemini 2.5 Flash (via `askGemini` helper)
**Telegram**: Bot API + callback queries (inline keyboards) via `sendTelegramWithKeyboard`

### Tables
- `messages` — ข้อความดิบ
- `commitments` — promises ที่ตรวจจับได้
- `memories` — long-term memories
- `summaries` — weekly + daily summaries (โดย AI)
- `alerts` — proactive alerts (urgency: critical/high/medium/low)
- `group_registry` — รายการกลุ่มที่ bot อยู่ (44 กลุ่ม ตอนนี้)
- `allowed_users` — role-based access (boss/member/null)
- `tasks`, `task_blockers`, `task_comments` — task tracking
- `calendar_reminders`, `calendar_tokens` — Google Calendar
- `workspace_members`, `companies` — org structure
- `kv_store` — key-value cache

### Multi-instance (Wrangler envs)
- **Friday** (default) — บอท COO (boss = Bob/Watcharin)
- **Daisy** — DISABLED 2026-04-30 (cron empty, code preserved)
- **Sigma** — TBD

### Key behaviors
- Role-based commands: `boss` = full, `member` = limited (`MEMBER_COMMANDS`, `MEMBER_CALLBACKS`)
- Proactive Alert v2: JSON output, dedup via `topic_fingerprint`, real-time urgent via regex
- Callback format: `pa:<mode>:<chatId>:<alertId>` (mode = s/d/h/x)
- Multi-user: `getUserRole()`, `/allow`, `/revoke`, `/users` commands
- `handleMemberChat` = simplified AI (no action tools)

---

## 📊 Source — D1 query patterns

```bash
# List all tables
cd ~/my-ai-bot && npx wrangler d1 execute my-ai-bot-db --remote \
  --command "SELECT name FROM sqlite_master WHERE type='table';" --json

# Pull weekly summaries for a date range
cd ~/my-ai-bot && npx wrangler d1 execute my-ai-bot-db --remote \
  --command "SELECT summary_date, chat_title, week_start, week_end, summary_text \
             FROM summaries WHERE summary_type='weekly' \
             AND summary_date BETWEEN '2026-05-01' AND '2026-05-31' \
             ORDER BY summary_date, chat_title;" --json

# Daily summaries
cd ~/my-ai-bot && npx wrangler d1 execute my-ai-bot-db --remote \
  --command "SELECT summary_date, chat_title, summary_text, message_count \
             FROM summaries WHERE summary_type='daily' \
             AND summary_date BETWEEN '2026-05-01' AND '2026-05-31';" --json
```

---

## 🏢 Business Context (สำหรับ Friday เข้าใจบริบท)

### Companies / Brands
- **บจ. ธันเดอร์ โซลูชั่น** (Thunder Solution) — Slip verification API
- **บจ. บี.วี.** (B.V.) — EasySlip business
- **บจ. อีซี่สลีพ / Easy Sleep** — separate entity (รับหนังสือเชิญสรรพากร 29/5)
- **EasyBOT / Gen Picture** — user's own product
- **EasyCRM** — loyalty/CRM platform
- **BoostSMS** — SMS marketing (boost-sms.com)
- **SHIFT Cafe** — coffee shop side project

### Key people
- **Bob (Bobsanchezz)** — boss (COO)
- **Watcharin / watcharin1004 / พี่วุทธ** — boss/CEO
- **Pop / ป๊อบ** — finance ops
- **Beer** — accounting
- **Mind / Mint** — billing
- **Bank Chanvit** — dev lead
- **bomquza / บอม** — dev (billing webapp)
- **Khunjadi** — marketing
- **Mizteen** — sales
- **Olivesterr** — sales
- **Folk** — graphic (EasyBOT)
- **Ann** — marketing/QA
- **G / Golf** — auto-reply
- **Guitar** — HR ทดลองงาน
- **น้องมิว** — ออกแบบ UI (เดือนสุดท้าย พ.ค. 2026)
- **น้องนพ / Nop** — รับส่งเอกสาร

### Active products + URLs
- `app.boost-sms.com/login` — BoostSMS หน้าบ้าน
- `backoffice.boost-sms.com` — BoostSMS หลังบ้าน
- `master-dashboard-eight-nu.vercel.app` — Smart Dashboard (master)
- `easycrm-two.vercel.app` — EasyCRM portal
- `dinarr-animal-hospital.vercel.app` — demo

---

## 🔗 Related
- Main user memory: `~/.claude-warp/projects/-Users-aexgee/memory/`
- Source code: `~/my-ai-bot/`
- Dashboard: `~/my-ai-bot/dashboard/`
- Architecture: `~/my-ai-bot/ARCHITECTURE.md`

---

## 📝 Update protocol

- เพิ่ม Monthly Recap ใหม่: สร้างไฟล์ใน `Monthly Recaps/YYYY-MM.md` + link จาก README
- เพิ่ม Theme deep-dive: ไฟล์ใน `Themes/YYYY-MM <topic>.md`
- อย่าลบไฟล์เก่า — ใช้ archive ถ้าจำเป็น
- ทุกครั้งที่บันทึกใหม่ ให้ Friday อ่านไฟล์นี้ก่อนเป็น index

---

## 🤖 Auto-recap (launchd schedule)

**ตั้งแต่ 2026-06-12 มี automation รัน Mac ทุกวัน 23:55:**
- **ทุกพฤหัสบดี 23:55** → Weekly Recap → `Weekly Recaps/YYYY-Www.md`
- **วันสุดท้ายของเดือน 23:55** → Monthly Recap → `Monthly Recaps/YYYY-MM <ภาษาไทย>.md`

ใช้:
- `_scripts/friday_recap.sh` — main dispatcher
- `_scripts/pull_summaries.py` — pull D1 → source markdown
- Claude CLI headless (`-p --permission-mode acceptEdits`) — synthesize
- launchd job `com.friday.recap` (~/Library/LaunchAgents/com.friday.recap.plist)
- Log → `_logs/recap.log`

### Manual triggers
```bash
# This week (Fri prev → today)
~/SecondBrain/Friday/_scripts/friday_recap.sh weekly

# Specific week ending date
~/SecondBrain/Friday/_scripts/friday_recap.sh weekly 2026-06-12

# Current month
~/SecondBrain/Friday/_scripts/friday_recap.sh monthly

# Specific month
~/SecondBrain/Friday/_scripts/friday_recap.sh monthly 2026-05

# Auto mode (decides based on today)
~/SecondBrain/Friday/_scripts/friday_recap.sh auto
```

### Manage schedule
```bash
# Check status
launchctl print gui/$(id -u)/com.friday.recap

# Force run now
launchctl kickstart -k gui/$(id -u)/com.friday.recap

# Disable
launchctl bootout gui/$(id -u)/com.friday.recap

# Re-enable
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.friday.recap.plist

# View logs
tail -f ~/SecondBrain/Friday/_logs/recap.log
```

### หมาย Mac sleep
ถ้า Mac หลับตอน 23:55 launchd จะ catch up ตอน Mac ตื่น (default behavior ของ StartCalendarInterval). แต่ถ้าผ่านไปนานเช่นข้ามวัน อาจ skip — แนะนำให้ Mac ตื่นตอนเที่ยงคืน (Energy Saver → schedule wake) ถ้าอยากให้แม่นยำ 100%.
