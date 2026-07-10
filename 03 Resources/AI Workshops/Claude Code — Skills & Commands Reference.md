---
title: Claude Code — Skills & Commands Reference
type: reference
tags: [claude-code, skills, commands, workshop, reference]
saved: 2026-07-11
---

# Claude Code — Skills & Commands ที่ควรรู้

## วิธีเรียกใช้

พิมพ์ `/` ตามด้วยชื่อ skill ใน Claude Code prompt:

```
/deploy
/code-review ultra
/deep-research "หัวข้อที่ต้องการ"
```

---

## 1. Review & Quality

### /code-review — ตรวจโค้ด

```
/code-review              # review ปกติ (diff ปัจจุบัน)
/code-review high         # ละเอียดขึ้น
/code-review ultra        # Multi-agent cloud review (แรงสุด)
/code-review --fix        # review แล้วแก้ให้เลย
/code-review --comment    # review แล้ว post comment บน PR
```

| Level | ความละเอียด | วิธีทำงาน |
|---|---|---|
| low/medium | เร็ว high-confidence เท่านั้น | Agent เดียว |
| high | ครอบคลุมกว่า อาจมี uncertain | Agent เดียว |
| ultra | ลึกสุด ครบทุกมุม | Multi-agent บน cloud |

### /review-security — ตรวจความปลอดภัย

```
/review-security
```

ตรวจ: secrets leak, injection, auth bypass, SSRF, OWASP Top 10

### /qa-pitbull — หาบั๊กแบบกัดไม่ปล่อย

```
/qa-pitbull
```

QA แบบเข้มข้น ห้ามปล่อยผ่าน ตำหนิเอาตาย หาบั๊กทุกตัว

### /logic-audit — ตรวจ Logic ครบทุกมุม

```
/logic-audit
```

ตรวจ BA + SA + Domain + Data + Risk แบบห้ามมั่ว ห้ามข้าม

### /full-check — รัน 5 checks พร้อมกัน

```
/full-check
```

รันทุกอย่างพร้อมกัน:
- Code Review
- Security Audit
- Silent-failure Audit
- Health Check
- Cost Analysis

ได้ report รวมครั้งเดียว

---

## 2. Code Improvement

### /simplify — ลดความซับซ้อน

```
/simplify
```

หา dead code, duplication, over-engineering แล้วแก้ให้เลย (ไม่หา bug — ใช้ /code-review สำหรับ bug)

### /lean — หาส่วนเกิน

```
/lean
```

หา dead code, duplication, over-engineering (รายงานอย่างเดียว ไม่แก้)

### /lean-pro — Refactor แบบรอบคอบ

```
/lean-pro
```

Lean-code master — refactor ที่เก่งที่สุด ไม่ทำพัง รอบคอบยิบ ป้องกันทุกทาง

### /spaghetti-fix — แก้ Spaghetti Code

```
/spaghetti-fix
```

8 มิติวิเคราะห์ + 3 ระดับความเสี่ยง (GREEN/YELLOW/RED) + auto-rollback ถ้าพัง

---

## 3. Planning & Debugging

### /plan — วางแผนก่อนทำ

```
/plan
```

วางแผน feature ใหม่: files ที่เกี่ยว, risks, test plan — ให้ approve ก่อนลงมือ

### /debug — หาสาเหตุ bug

```
/debug
```

Trace code, query logs/DB, identify root cause

### /recheck — ตรวจหลังแก้

```
/recheck
```

Syntax check, หา broken callers, check regressions หลังแก้โค้ด

---

## 4. Deploy & Operations

### /deploy — Deploy อัตโนมัติ

```
/deploy
```

Auto-detect: Wrangler (Cloudflare), Fly.io, Vercel, Netlify, npm scripts แล้ว deploy ให้

### /health — เช็คสุขภาพ Project

```
/health
```

ดู deploy state, errors, data flow, uptime signals

### /tail — ดู Live Logs

```
/tail
```

Tail logs สั้นๆ แล้วสรุปให้ — auto-detect wrangler/fly/vercel/docker

### /ghpush — Push to GitHub (safe)

```
/ghpush
```

Stage → commit → push (ไม่ force, ไม่ -A, ปลอดภัย)

---

## 5. Research & Analysis

### /deep-research — วิจัยแบบลึก

```
/deep-research "หัวข้อ"
```

Fan-out web search หลายแหล่ง → fetch sources → adversarially verify → cited report

ถ้าหัวข้อกว้างเกินจะถามคำถามกลับ 2-3 ข้อก่อนเริ่ม

### /graphify — สร้าง Knowledge Graph

```
/graphify .
```

แปลง code/docs/papers/images เป็น knowledge graph — เหมาะก่อนเริ่มงานกับ repo ใหม่

---

## 6. Automation & Scheduling

### /schedule — ตั้ง Agent อัตโนมัติบน Cloud

```
/schedule
```

สร้าง scheduled agent ที่รันบน cloud ตาม cron:

ตัวอย่าง:
- "ทุกเช้า 9:00 สรุป PR ที่เปิดค้าง"
- "ทุกวันศุกร์ run /full-check"
- "ทุก 3 ชม. เช็ค deploy status"

ไม่ต้องเปิดเครื่อง ทำงานบน cloud

### /loop — รันซ้ำ

```
/loop 5m /health          # เช็ค health ทุก 5 นาที
/loop 10m /tail           # ดู logs ทุก 10 นาที
/loop                     # ให้ Claude กำหนดจังหวะเอง
```

---

## 7. Performance & Mode

### /fast — Fast Mode

```
/fast
```

เปิด/ปิด Fast Mode: Opus เร็วขึ้น 2.5x (ไม่ลดโมเดล เป็น Opus เหมือนเดิม)

ใช้ได้กับ Opus 4.8 / 4.7 เท่านั้น

### /model — เปลี่ยนโมเดล

```
/model                    # เลือกจาก picker
/model opus               # เปลี่ยนเป็น Opus ล่าสุด
/model sonnet             # Sonnet
/model haiku              # Haiku
```

### /effort — ปรับความลึกในการคิด

```
/effort low               # เร็ว ประหยัด token
/effort medium            # สมดุล
/effort high              # ค่าเริ่มต้น (แนะนำ)
/effort xhigh             # Coding/Agentic (Opus 4.7+, Sonnet 5)
/effort max               # แม่นสุด ใช้ token มากสุด
```

---

## 8. Project Setup

### /init — สร้าง CLAUDE.md

```
/init
```

สร้าง CLAUDE.md ใหม่พร้อมข้อมูล codebase — ไฟล์นี้คือ "คู่มือ" ที่ Claude อ่านทุกครั้งที่เปิด session

### /schema — ดู Database Schema

```
/schema
```

แสดง schema + row counts — D1, Postgres, MySQL, SQLite

---

## 9. Multi-Agent

### Workflow (ภายใน Claude Code)

```
"use a workflow" หรือ "ultracode" ตามด้วยคำสั่ง
```

Fan-out หลาย agents ทำงานพร้อมกัน เช่น:
- 3 agents review bugs/security/perf พร้อมกัน
- 1 agent สรุปผลรวม

### Warp Split Pane

```bash
# เปิดหลาย pane แล้วสั่งแต่ละตัว
claude -p "หา bugs ใน index.js"        # pane 1
claude -p "หา security issues"          # pane 2
claude -p "หา performance issues"       # pane 3
```

`-p` = print mode (one-shot ไม่เข้า interactive)

### maw (Multi-Agent Orchestrator)

```bash
maw --task "Review src/index.js — bugs + security + perf → report"
```

สร้าง oracle + workers อัตโนมัติใน tmux

---

## 10. Utility

### /verify — ทดสอบว่า code ทำงานจริง

```
/verify
```

รัน app แล้วดูว่า change ทำงานจริงไหม (ไม่ใช่แค่ test pass)

### /run — เปิด App

```
/run
```

Launch project's app — auto-detect ประเภท (CLI/server/TUI/browser)

### /webhook — เช็ค Telegram Bot Webhook

```
/webhook
```

เรียก getWebhookInfo ดูสถานะ — multi-env aware

### /user — ค้นหา User ใน DB

```
/user
```

Look up user's activity ใน project database

---

## แนะนำ Workflow ประจำวัน

### เริ่มงาน
```
/health                   # เช็คสถานะ project
/tail                     # ดู logs ล่าสุด
```

### ก่อน Push
```
/recheck                  # ตรวจหลังแก้โค้ด
/code-review              # review ตัวเอง
/ghpush                   # push safe
```

### ก่อน Deploy
```
/full-check               # ตรวจครบทุกมุมพร้อมกัน
/deploy                   # deploy
/tail                     # ดู logs หลัง deploy
```

### Review คนอื่น
```
/review PR#123            # review PR บน GitHub
/code-review ultra        # ultra review (ลึกสุด)
```

---

## หมายเหตุ

- Skills บางตัวเป็น built-in (มากับ Claude Code) บางตัวเป็น custom (ติดตั้งเพิ่ม)
- ดูรายการทั้งหมดที่ใช้ได้: พิมพ์ `/` แล้วดู autocomplete
- Skills ที่มี `(custom)` หมายถึงต้องติดตั้งเพิ่ม
- ดู workshop guide เพิ่มเติมที่ `Claude Code — full teaching guide` (Obsidian เดียวกัน)
- ดูโมเดลทั้งหมดที่ `Claude Code — Model Reference` (Obsidian เดียวกัน)
