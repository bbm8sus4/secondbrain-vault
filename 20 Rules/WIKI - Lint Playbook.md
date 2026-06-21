---
title: WIKI — Lint Playbook
type: schema-playbook
status: live
date: 2026-06-21
schedule: weekly
tags: [schema, wiki, lint, agent, health]
related:
  - "[[WIKI]]"
---

# Lint Playbook

> ตรวจสุขภาพ wiki ทุกสัปดาห์ — Karpathy แนะนำ เราใส่ checklist + scoring + commands

## เมื่อไหร่ลิ้นต์
- **Weekly** — Sunday night (เร็ว, ~10 นาที)
- **Monthly** — ต้นเดือน (เต็ม, ~30 นาที)
- **On-demand** — หลัง ingest ใหญ่ (10+ source ในช่วง 1 สัปดาห์)

---

## Weekly checklist (10 นาที)

### A. Stale pages
```bash
# หาหน้าที่ last_verified เก่า > 60 วัน
grep -lrE "^last_verified: " "/Users/aexgee/SecondBrain" \
  | xargs -I {} sh -c 'date=$(grep "^last_verified:" {} | cut -d" " -f2); echo "$date {}"' \
  | sort | head -20
```
- รายชื่อมาแล้ว → จัดลำดับโดย impact (project ใช้งานจริง > archive)
- ไป re-verify หรือ archive

### B. Orphans (หน้าที่ไม่มีใคร link มา)
```bash
# หาหน้าที่ไม่ถูก [[link]] จากใครเลย (manual check ผ่าน Obsidian graph)
```
- Obsidian → กราฟวิว → unlinked nodes
- ลบ / merge / link เพิ่ม

### C. Conflicts ที่ค้างจาก ingest
```bash
grep -rE "^## ⚠ Open questions|^> \*\*อัพเดต" "/Users/aexgee/SecondBrain"
```
- ปิด conflict ที่ตอบได้แล้ว
- ที่ค้าง > 30 วัน → ตัดสินใจ หรือ flag escalate

### D. Index drift
```bash
# นับไฟล์ใน vault vs entries ใน /index.md
find "/Users/aexgee/SecondBrain" -name "*.md" -not -path "*/.*" | wc -l
grep -c "^- \[\[" "/Users/aexgee/SecondBrain/index.md"
```
- ต่างกันมาก = index ขาด

### E. Log entries วันนี้ vs commit ใน git
```bash
cd "/Users/aexgee/SecondBrain" && git log --since="1 week ago" --oneline | wc -l
grep -c "^## \[" log.md
```
- ถ้า git commits >> log entries = ลืม log

---

## Monthly checklist (30 นาที)

ทำทุกอย่างใน weekly + ต่อด้วย:

### F. Contradiction sweep (cross-page)
- เลือก 3 brand/project · อ่าน README ของแต่ละ · เทียบ claim สำคัญ
- ตัวอย่าง: pricing ใน Product.md vs llms.txt mirror.md
- พบขัด → resolve + อัพเดต

### G. Missing pages
- ค้น claim ที่ปรากฏซ้ำ 3+ หน้าแต่ไม่มีหน้าของตัวเอง
- → สร้างหน้า canonical

### H. Tag hygiene
```bash
grep -hrE "^tags: " "/Users/aexgee/SecondBrain/01 Projects" | sort | uniq -c | sort -rn | head -20
```
- รวม tag ใกล้เคียง · ลบ tag ไร้ค่า

### I. Dead pointer
- หน้าที่ frontmatter `source:` ชี้ไปไฟล์/URL ที่ไม่มีอยู่แล้ว
- → re-source หรือ archive

### J. Memory ↔ Wiki sync
- เปิด `30 Claude Memory/MEMORY.md` (auto-mirror) → check ทุก pointer ยังชี้ไปหน้าจริง
- หน้าที่ memory ชี้แต่ wiki ไม่มี = ต้อง ingest

---

## Lint Score (เก็บแบบ)

ทุกครั้งที่ลิ้นต์ append `/log.md`:
```
## [YYYY-MM-DD HH:MM] lint | weekly | score: 8/10
- stale: 3 → fixed 2
- orphans: 5 → linked 3, archived 2
- conflicts: 1 open
- index_drift: 0
- log_drift: 4 missing entries (backfilled)
```

Score = 10 - (stale_unfixed + orphans_unfixed + conflicts_open + drift)

ถ้า score < 6 — สัปดาห์หน้าทำ monthly แทน

## Anti-patterns
- ❌ ลิ้นต์แล้วไม่ append log
- ❌ พบ stale แล้วไม่ตัดสินใจ (re-verify หรือ archive)
- ❌ orphan ทั้งหมดไป archive โดยไม่ดู (บางอันอาจเพิ่งสร้าง)
- ❌ ปิด conflict โดยไม่ note resolution ลงหน้านั้น
