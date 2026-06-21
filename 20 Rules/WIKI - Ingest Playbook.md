---
title: WIKI — Ingest Playbook
type: schema-playbook
status: live
date: 2026-06-21
tags: [schema, wiki, ingest, agent]
related:
  - "[[WIKI]]"
  - "[[WIKI - Page Templates]]"
---

# Ingest Playbook

> Source ใหม่ → Wiki ที่ดีขึ้น โดยไม่ทำลายของเดิม

## ลำดับ 7 ขั้น (ห้ามข้าม)

### 1) Identify source
- ไฟล์/URL/ข้อความอะไร · ใครเป็นเจ้าของ · วันที่
- ถ้าเป็น raw → ดรอปลง `00 Inbox/` หรือชี้ pointer ถ้าอยู่นอก vault
- ถ้าเป็น web → clip + download images ถ้ามี

### 2) Read fully ก่อน
- อ่านเต็ม ห้าม skim · จดประเด็นหลัก
- ถ้ายาว → สรุปย่อใน chat ให้ผู้ใช้รีวิวก่อน

### 3) Search wiki ที่เกี่ยวข้อง (สำคัญ — Karpathy ไม่ได้บอกแต่เราบังคับ)
- ค้นชื่อ entity / project / concept ที่ปรากฏใน source
- อ่านหน้าที่ match อย่างน้อย skim · ระบุ `last_verified:`
- **ถ้า claim ใน source ขัดกับหน้าเดิม** → ไป Step 6 (conflict resolution) ก่อน เขียนทับห้าม

### 4) Plan touch list
- บอกล่วงหน้า: หน้าไหนจะ **สร้างใหม่** · หน้าไหนจะ **อัพเดต** · หน้าไหนจะ **rename/move**
- โดยทั่วไป 1 source แตะ 5–15 หน้า
- ถ้า > 15 หน้า → พิจารณา `_pending/` staging (Step 7)

### 5) Write / update
- ใช้ template ใน `[[WIKI - Page Templates]]`
- frontmatter บังคับ: `source:`, `last_verified:`, `tags:`
- backlink ทุกหน้าที่อ้างอิงด้วย `[[...]]`
- หน้าใหม่ + update index entry ใน `/index.md`

### 6) Conflict resolution (ถ้ามี)
ลำดับการตัดสินใจ:
1. **ใหม่กว่า + น่าเชื่อกว่า** → อัพเดตหน้าเดิม + ใส่ note `> ** อัพเดต YYYY-MM-DD**: ค่าเดิม X เปลี่ยนเป็น Y เพราะ <source>`
2. **ขัดกันไม่ชัด** → เก็บทั้งคู่ + เพิ่ม section `## ⚠ Open questions / contradictions`
3. **Source ผิด** → ไม่เขียน + log `conflict | rejected <source> because <reason>`
4. ทุกกรณี — log บรรทัด `conflict` ใน `/log.md`

### 7) Atomic commit (optional แต่แนะนำสำหรับงานใหญ่)
- ถ้าจะแตะ > 15 ไฟล์ — เขียนลง `_pending/<batch-id>/` ก่อน
- รีวิวกับ user (`tree _pending/<batch-id>`) → ถ้า OK ค่อย `mv -i` เข้าตำแหน่งจริง
- ป้องกัน wiki พังครึ่งทางถ้า interrupt

---

## Frontmatter ของหน้าใหม่ (มาตรฐาน)

```yaml
---
title: <ชื่อ>
type: <project | area | resource | entity | concept | event>
source: <ไฟล์ใน 00 Inbox/ · URL · "Apple Notes #63" · "chat 2026-06-21">
source_date: YYYY-MM-DD            # วันที่ของ source ต้นทาง
imported: YYYY-MM-DDTHH:MM:SS      # วันที่นำเข้า wiki
last_verified: YYYY-MM-DD          # วันที่ตรวจล่าสุด (เริ่ม = imported date)
status: draft | live | archived
related:
  - "[[Page A]]"
  - "[[Page B]]"
tags: [domain, type, ...]
---
```

## Index update
หลังเขียนเสร็จ → เปิด `/index.md` → เพิ่ม/แก้บรรทัด:
```
- [[Page Title]] — one-line summary · last_verified: YYYY-MM-DD
```
จัดใต้ section ที่เหมาะสม (Project / Area / Resource / Brand)

## Log entry
หลัง commit → append `/log.md`:
```
## [YYYY-MM-DD HH:MM] ingest | <Source short name>
- created: [[New Page]], [[Another New Page]]
- updated: [[Existing Page]] (added X)
- touched: <N> pages
- source: <pointer to raw>
```

## Anti-patterns (ห้ามทำ)
- ❌ เขียนหน้าใหม่โดยไม่ search ของเก่าก่อน
- ❌ เขียนทับหน้าเดิมโดยไม่ flag conflict
- ❌ ลืม `source:` หรือ `last_verified:`
- ❌ ลืมอัพเดต `/index.md` + `/log.md`
- ❌ ingest > 15 ไฟล์รวดเดียวโดยไม่ staging
- ❌ แตะ `30 Claude Memory/` หรือ `40 Meeting Notes/` — read-only
