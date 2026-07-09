---
title: สรุป 2026-07-06 — Vault Overhaul ครบวงจร
type: synthesis
source: Claude Code session 2026-07-06 (Ghostty) — ทำจริงทั้งหมด verify แล้ว
source_date: 2026-07-06
imported: 2026-07-06T22:40:00
last_verified: 2026-07-09
status: live
project_status: ✅ เสร็จสมบูรณ์ 2026-07-09
tags: [synthesis, vault, maintenance, automation, milestone]
related:
  - "[[Automation Setup]]"
  - "[[WIKI]]"
---

# สรุป 2026-07-06 — Vault Overhaul ครบวงจร

> วันเดียวยกเครื่อง vault จาก "สะอาดแต่ต้องดูแลมือ" → "ดูแลตัวเอง + แจ้งเตือนเอง + ย่อยความรู้เอง"
> Health: 🟡 (96 dead links / 66 orphans) → **🟢 (0 / 0 / 0)** · ทุกอย่าง commit + push แล้ว
> **✅ ปิดโปรเจกต์ 2026-07-09** — blueprint ส่งถึงเพื่อนเรียบร้อย งานหลักจบครบ (เหลือเฉพาะงานค้างท้ายไฟล์ซึ่งเป็น backlog ต่อเนื่อง ไม่ใช่เงื่อนไขปิดงาน)

## รอบ 1 — Cleanup Sprint (ปิดหนี้เก่าทั้งหมด)

- **Dead links 96 → 0** — ครึ่งนึง (56) เป็น false positive ของ `vault-health.py` ที่เช็คเฉพาะ .md (รูป SRS 39 รูปอยู่ครบใน `_attachments/` ตลอด) → แก้ scanner ให้ resolve ไฟล์แนบทุกชนิด + escaped pipe + `file://` · ที่เสียจริงไล่ปิดหมด: KuanGolf folder links, Clippings author links ×11, memory slugs ×4, BoostSMS K13-15
- **Orphans 66 → 0** — สร้าง hub: [[04 Archive/README|Archive README]] · [[03 Resources/Clippings/README|Clippings README]] · [[03 Resources/COO/README|COO README]] · [[03 Resources/People/README|People README]] + โยงจาก Friday/AI Workshop/แผนที่/หน้าแบรนด์
- **Thunder + EasySlip KB เติมเต็ม** — แบรนด์ละ 3 หน้า (Overview / Products-Pricing / Revenue) จาก Claude Memory + เอกสารจริง
- **BoostSMS `_knowledge` ครบ K01-K15** — สร้าง K13-Deliverability-DLR, K14-Compliance-AntiSpam, K15-AB-Testing-SMS
- **Frontmatter retrofit 30+ ไฟล์** (EasyCRM/EasyBOT/BoostSMS ทุกหน้า + KuanGolf README) — additive, 0 deletions
- เอกสารพูดความจริง: 10 Daily = ยังไม่ใช้ · 40 Meeting Notes = pipeline พร้อมแต่ของน้อย
- rename ไฟล์ snippet ที่มี `^` ในชื่อ (ทำ wikilink พัง) · ลบ `_files/brand.md` (0 byte)

## รอบ 2 — ระบบดูแลตัวเอง (10 ข้อ)

1. **sync push fix** — เจอ push fail เงียบมาครึ่งวัน (origin นำหน้า → non-fast-forward ตลอด) → เพิ่ม `fetch + pull --rebase --autostash` ก่อน push ใน `sync-memory-to-vault.sh`
2. **auto-router sanitize clippings** — ถอด `[[wikilink]]` ใน frontmatter ตอน route → Web Clipper สร้าง dead link ใหม่ไม่ได้อีก
3. **Memory รวม 4 harness** — warp (หลัก) + `.claude` + cmux + ghostty → mirror เดียว 74→**81 ไฟล์** dedup ตาม mtime · ดัชนีความจำต่อ section "จาก harness อื่น" อัตโนมัติ
4. **vault-health v2** — เช็คเพิ่ม: frontmatter ขาด (backlog 143) · หน้าเก่า >90 วัน · **คิว `ต้อง verify`** (ทวงทุกวันจนเคลียร์) · launchd ครบ 5 ตัวไหม · commit ค้าง push
5. **Telegram alert** — มีปัญหา hard → เด้งผ่านบอท ccgram (send-only อ่าน token จาก `~/.ccgram/.env` — **ห้ามใส่ token ccgram ลง `.vault-capture.env`** เดี๋ยวแย่ง getUpdates กัน) · ทดสอบส่งจริง HTTP 200
6. **Ratchet loop** — `com.aexgee.ratchet-clippings` ทุกอาทิตย์ 19:00 รัน claude headless สรุป clippings ≤5 ชิ้น/รอบ → `Clippings/Synthesis/` · **รอบแรกรันจริงแล้ว ได้ 5 หน้า Takeaways** (1 หน้าตอบตรง ๆ ว่าไม่มีประเด็น COO)
7. **browse.base เป็น dashboard จริง** — 4 views: ทุกหน้าตาม last_verified · schema debt · Projects · draft
8. **Templates ใช้จริง** — 5 แบบใน `20 Rules/_templates/` + ตั้ง core plugin
9. **Graph colorGroups 12 กลุ่ม** แบบ `path:` + เปิด tags (ของเดิม query คำลอย ๆ จับไม่ติด)
10. **Inbox เกลี้ยง** — อบรมขอนแก่น → `01 Projects/AI Workshop - ขอนแก่นอิเล็คทริค/` · โครงคอร์ส Claude → `03 Resources/AI Workshops/`

## Blueprint ส่งเพื่อน

[[SecondBrain Blueprint Setup]] (เดิมชื่อ "Blueprint — สำหรับ vault เพื่อน" — พี่ rename ก่อนส่ง) — โครงสร้าง+กฎ+automation ทั้งระบบเป็น .md ให้ AI ฝั่งเพื่อน (mark-ai) ทำตาม · ออกแบบ **additive-only** เข้ากับ red-lines ฝั่งนั้น (map ไม่รื้อ, commit ทุก Phase, ไม่มีคำสั่งลบ) · ส่งไฟล์แล้ว 2026-07-06

## ของที่เจอระหว่างทาง (สำคัญ)

- ⚠️ **vault-capture bot ไม่เคยทำงานจริง** — `TELEGRAM_BOT_TOKEN` ใน `~/.vault-capture.env` ว่างมาตลอด ทั้งที่เอกสารเคลมว่ารัน · ต้องสร้างบอทใหม่ที่ @BotFather ถ้าจะใช้ (ดู [[Automation Setup]])
- Status line ของ Claude Code หายใน Ghostty เพราะ `~/.claude-ghostty/settings.json` ไม่มี `statusLine` (harness อื่นมีครบ) — เพิ่มแล้ว ชี้ `~/.claude/statusline.sh`

## งานค้าง (รอทำ/รอพี่ตัดสิน)

- [ ] **frontmatter backlog 143 ไฟล์** — health scan รายงานทุกวัน (ไม่กระทบสถานะเขียว) รอ sprint ถัดไป
- [ ] **คิว verify 8 รายการ** — ก้อนหลัก: สถานะ Gen QR เก็บเงินยัง · สัดส่วนรายได้ EasySlip (60% vs 54.3%) · ทวง KBank ~884K · สถานะ HUG COMPANY
- [ ] vault-capture: สร้างบอท + ใส่ token ถ้าอยากใช้ Telegram → Inbox
- [ ] เปิด-ปิด Graph view ใหม่เพื่อเห็นสีชุดใหม่ (ถ้า Obsidian ทับ `graph.json` ให้สั่งตั้งใหม่)
