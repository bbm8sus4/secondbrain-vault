---
title: WIKI — Master Schema
type: schema
status: live
version: 1.0
date: 2026-06-21
based_on: "Karpathy LLM Wiki pattern (gist 442a6bf)"
tags: [schema, wiki, rules, agent]
---

# WIKI — Master Schema

> กฎ Wiki ของ SecondBrain นี้ — อ่านก่อนทำงานทุกครั้งที่จะแตะหน้าใน vault
> ปรับปรุงจาก **Karpathy LLM Wiki** ให้แข็งแรงขึ้น 10 จุด (ดูท้ายไฟล์)

## TL;DR สำหรับ Agent

1. Source ต้นทาง = ห้ามแตะ · Wiki = LLM เป็นคนเขียน · Schema = ไฟล์นี้ + 4 Playbook
2. ก่อนเขียนหน้าใหม่ — **search ก่อนเสมอ** ว่ามีหน้าที่เกี่ยวข้องไหม → ป้องกัน contradictions
3. ทุกหน้า wiki ต้องมี `source:` (ต้นทาง) + `last_verified:` (วันที่ตรวจครั้งล่าสุด)
4. แตะหน้าไหน → อัพเดต `last_verified:` + เพิ่มบรรทัดใน `/log.md`
5. ทุก query ที่ตอบดี → ถามตัวเองว่า "เก็บเป็นหน้าได้ไหม" (ดู Query Playbook)

---

## 1) สถาปัตยกรรม 3 ชั้น

### Layer A — Raw Sources (immutable)
- `00 Inbox/` — sources ที่ยังไม่แปลง (Apple Notes, Telegram captures, web clips, screenshots)
- `40 Meeting Notes/` — auto-sync จาก `meeting-notes` repo (read-only)
- `30 Claude Memory/` — auto-mirror จาก `~/.claude-warp/memory/` (read-only, ห้ามแก้ที่นี่ — แก้ที่ต้นทาง)
- assets นอก vault: `~/Desktop/Work+/...`, `~/Desktop/Business/...`

**กฎ**: ห้ามลบ ห้ามแก้ ห้าม restructure อ่านได้อย่างเดียว

### Layer B — Wiki (LLM-owned)
- `01 Projects/` — project ที่มี deadline
- `02 Areas/` — งานต่อเนื่อง
- `03 Resources/` — ความรู้อ้างอิง
- `04 Archive/` — จบแล้วเก็บค้น
- `<Brand>/` ที่ root — BoostSMS, EasyBOT, EasyCRM, EasySlip, Friday, Thunder Solution (knowledge base ต่อแบรนด์)

**กฎ**: LLM เป็นคนเขียน คนอ่านอย่างเดียว ถ้ามีหน้าที่ขัดกัน — ต้อง flag ก่อน เขียนทับห้าม

### Layer C — Schema (กฎ)
- `20 Rules/WIKI.md` — ไฟล์นี้ (กฎกลาง)
- `20 Rules/WIKI - Ingest Playbook.md` — วิธีรับ source เข้า wiki
- `20 Rules/WIKI - Query Playbook.md` — วิธีตอบคำถาม + ratchet กลับเป็นหน้า
- `20 Rules/WIKI - Lint Playbook.md` — checklist health check
- `20 Rules/WIKI - Page Templates.md` — frontmatter + naming
- `20 Rules/กติกาการทำงาน.md` — กติกาเก่า (ยังใช้ได้)
- `20 Rules/คู่มือ vault.md` — คู่มือ vault เก่า (ยังใช้ได้)

---

## 2) ไฟล์พิเศษ 2 ตัว (ระดับ vault)

### `/index.md` — Catalog
- Content-oriented · จัดตาม PARA + Brand
- Agent อ่านก่อนตอบคำถามใหญ่
- อัพเดตทุกครั้งที่สร้าง/ลบ/ย้ายหน้าใหญ่
- รูปแบบ: `- [[Page]] — one-line · `last_verified: YYYY-MM-DD``

### `/log.md` — Timeline (append-only)
- Chronological · grep-friendly prefix
- รูปแบบบรรทัด: `## [YYYY-MM-DD HH:MM] <op> | <subject>`
- `op` มี: `ingest` · `query` · `lint` · `rename` · `delete` · `conflict` · `decision`
- ตัวอย่าง grep: `grep "^## \[" log.md | tail -10`

---

## 3) Operations 3 อย่าง

### Ingest
ดู `[[WIKI - Ingest Playbook]]`
- รับ source ใหม่ → search หน้า related → diff vs ของเดิม → เขียน/อัพเดต 10–15 หน้า → log

### Query
ดู `[[WIKI - Query Playbook]]`
- ค้น index → อ่านหน้า → สังเคราะห์ + cite → ถามตัวเอง "filed back ได้ไหม?" → log

### Lint
ดู `[[WIKI - Lint Playbook]]`
- รัน weekly/monthly: contradictions · stale · orphans · missing pages · gaps

## 3.5) Auto-router (rule-based)

`~/bin/inbox-auto-ingest.py` ทำงานเงียบ ๆ ทุก 3 นาทีผ่าน launchd (`com.aexgee.inbox-auto-ingest`)

**กฎปัจจุบัน**
| frontmatter tag | ปลายทาง |
|---|---|
| `clippings` (Web Clipper) | `03 Resources/Clippings/` |

**กฎความปลอดภัย**
- Skip `_vault-health.md` (auto-regen)
- Skip ไฟล์ที่ mtime ใหม่กว่า 30 วินาที (อาจกำลังเขียน)
- ถ้าชื่อชนกัน → suffix `(auto-HHMMSS).md` ไม่ทับ
- หลัง route → update `last_verified:` + insert log entry `auto-ingest | inbox sweep`

**เพิ่มกฎใหม่**
แก้ list `ROUTES` ใน script — ตัวอย่าง:
```python
ROUTES = [
    (re.compile(r"\bclippings\b"), "03 Resources/Clippings", "clippings"),
    # (re.compile(r"\bmeeting\b"), "40 Meeting Notes", "meeting"),  # ถ้าเปิด
]
```

**ตรวจสุขภาพ**
```bash
launchctl list | grep inbox-auto-ingest      # ต้องเห็น PID
tail ~/Library/Logs/inbox-auto-ingest.log    # ดู route ล่าสุด
grep "auto-ingest" ~/SecondBrain/log.md | head   # ดู audit
```

---

## 4) Memory ↔ Wiki Bridge

| | Memory (`~/.claude-warp/memory/`) | Wiki (vault) |
|---|---|---|
| เก็บอะไร | สถานะปัจจุบัน · preference · pointer | ความรู้เต็ม · ประวัติ · synthesis |
| ขนาด | สั้น (1 ย่อหน้า/ไฟล์) | ยาวได้ |
| Source | LLM เขียน ผู้ใช้สั่งจำ | LLM เขียนจาก raw |
| TTL | คงทน แต่ลบได้ | คงทน + version ใน git |

**กฎเชื่อม**:
- Memory ที่ชี้ไปหน้า wiki — ใช้ pointer ตรง: `KB: ~/SecondBrain/01 Projects/X/README.md`
- หน้า wiki ที่อยากให้ memory จำ — ระบุใน frontmatter: `memory_pointer: <slug>`
- `30 Claude Memory/` mirror อัตโนมัติ — ดู ไม่ใช่แก้

---

## 5) ความแตกต่างจาก Karpathy (ดีขึ้นตรงไหน)

| Karpathy v1 | SecondBrain v1 (ของเรา) |
|---|---|
| `index.md` flat | **PARA + Brand tiered** index — เข้ากับโครงเดิม |
| Source attribution = ตัวเลือก | **`source:` frontmatter บังคับ** ทุกหน้า |
| Stale = ตรวจตอน lint | **`last_verified:` frontmatter** + lint flag อัตโนมัติ |
| Conflict = "note where" | **Conflict-detect on ingest** (search ก่อนเขียน) |
| Schema = 1 ไฟล์ | **Master + 4 playbooks + per-brand sub-schema** |
| Query ratchet = แนะนำเฉย ๆ | **Ratchet rubric ใน Query Playbook** (decide go/no-go) |
| ไม่มี memory layer | **Memory ↔ Wiki bridge** ชัดเจน |
| log = chronological แค่นั้น | **Structured ops vocabulary** (ingest/query/lint/...) grep-friendly |
| Lint = "periodically" | **Lint checklist** + schedule + scoring |
| ไม่มี atomic | **`_pending/` staging pattern** สำหรับ multi-file ingest (optional) |

หลักการเดียวกัน: human curate + ask, LLM ทำ bookkeeping
