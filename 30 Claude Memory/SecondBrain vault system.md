---
name: project-secondbrain-vault-system
description: "ระบบ automation ของ ~/SecondBrain หลัง overhaul 2026-07-06 — health 🟢, launchd 5 ตัว, กติกาที่ต้องรู้ก่อนแตะ"
metadata: 
  node_type: memory
  type: project
  originSessionId: d5d67d52-7263-445a-a4dd-7c1102c89665
---

Vault `~/SecondBrain` ยกเครื่องเสร็จ 2026-07-06: dead links 96→0, orphans 66→0, สถานะ 🟢

**Launchd 5 ตัว** (สคริปต์ `~/bin/` + สำเนา version ใน `20 Rules/_automation/`):
sync ทุก 30 นาที (รวม memory 4 harness: warp หลัก + claude/cmux/ghostty, dedup ตาม mtime, commit + rebase + push) · inbox-auto-ingest ทุก 3 นาที (ถอด `[[wikilink]]` ใน frontmatter clippings) · vault-health ทุกเช้า 9:00 (v2: frontmatter/stale/verify-queue/jobs/push-lag + Telegram alert ผ่านบอท ccgram send-only) · vault-capture (ยังไม่ทำงาน — token ว่าง) · ratchet-clippings อาทิตย์ 19:00 (claude headless สรุป clippings ≤5 ชิ้น → Clippings/Synthesis/)

**กติกาต้องรู้:** แตะหน้า wiki → อัพเดต last_verified + ลง log.md (entry ใหม่บนสุด, ops: ingest/query/lint/rename/delete/conflict/decision) · 30 Claude Memory + 40 Meeting Notes + 00 Inbox = read-only mirror แก้ที่ต้นทาง · ห้ามใส่ token ccgram ลง ~/.vault-capture.env (แย่ง getUpdates) · ชื่อไฟล์ห้ามมี ^ | [ ]

รายละเอียดเต็ม: `~/SecondBrain/03 Resources/สรุป 2026-07-06 — Vault Overhaul ครบวงจร.md` + `20 Rules/Automation Setup.md` · Blueprint: `03 Resources/SecondBrain Blueprint Setup.md` — **โปรเจกต์ปิดแล้ว 2026-07-09** (ส่งเพื่อนเรียบร้อย) · งานค้าง backlog: frontmatter 143 ไฟล์, คิว verify (Gen QR / รายได้ EasySlip / KBank 884K), token vault-capture, [[SeatMap app|project-seatmap]]
