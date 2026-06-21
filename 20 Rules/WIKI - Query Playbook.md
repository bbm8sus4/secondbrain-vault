---
title: WIKI — Query Playbook
type: schema-playbook
status: live
date: 2026-06-21
tags: [schema, wiki, query, agent]
related:
  - "[[WIKI]]"
  - "[[WIKI - Ingest Playbook]]"
---

# Query Playbook

> ตอบคำถามแล้ว **เซฟกลับเป็นหน้า wiki** ถ้าควรค่า — pattern นี้ทำให้ knowledge compound

## ลำดับ 5 ขั้น

### 1) Read index ก่อน
- เปิด `/index.md` หา section ที่เกี่ยวข้อง
- ถ้า query ครอบหลาย brand → อ่าน หน้าหลัก.md ด้วย

### 2) Drill into pages
- เปิดหน้าที่ดูเกี่ยวข้อง 3–8 หน้า · อ่าน frontmatter + content
- เช็ก `last_verified:` — ถ้าเก่ากว่า 60 วัน → flag ในคำตอบว่า "อาจ stale"

### 3) Synthesize + cite
- ตอบ **พร้อม backlink** `[[Page]]` ทุก claim
- ถ้าข้อมูลไม่พอ → บอกชัด ๆ ว่า "ไม่มีใน wiki, ต้อง ingest source ใหม่"
- ถ้าเจอ contradiction ระหว่างหน้า → flag ให้ผู้ใช้รู้ (จะกลายเป็น lint item)

### 4) Ratchet rubric (สำคัญ — Karpathy บอกแค่ "ควร" เราใส่กฎ)

ถามตัวเอง 5 ข้อ ก่อนปล่อย answer ทิ้ง:

| คำถาม | ถ้า "ใช่" → file back |
|---|---|
| 1. คำตอบนี้รวมข้อมูลจาก 2+ หน้าเข้าด้วยกันไหม | ใช่ → สร้างหน้า synthesis |
| 2. มี framework / table / matrix ที่จัดเอง ไหม | ใช่ → เซฟเป็น resource |
| 3. ผู้ใช้น่าจะถามอีก > 1 ครั้งใน 30 วันไหม | ใช่ → เซฟเป็น FAQ/หน้าเฉพาะ |
| 4. คำตอบนี้ contradict หน้าเก่าไหม | ใช่ → อัพเดตหน้าเก่า + flag |
| 5. มี decision ที่ผู้ใช้ commit ไหม | ใช่ → เซฟเป็น decision log |

**ถ้า ≥ 2 ข้อ "ใช่"** → file กลับเป็นหน้า + อัพเดต `/index.md` + log

### 5) Log entry
```
## [YYYY-MM-DD HH:MM] query | <topic>
- read: [[Page A]], [[Page B]]
- result: <answer summary 1 line>
- filed_back: [[New Page]] (ถ้ามี) / none
```

---

## รูปแบบคำตอบที่ดี (output formats)

| รูปแบบ | เมื่อไหร่ |
|---|---|
| Plain text + backlink | คำถามตรง ๆ |
| Table | เปรียบเทียบ 2+ ทาง |
| Matrix | trade-off หลายแกน |
| Markdown page (file back) | ผ่าน rubric ≥ 2 ข้อ |
| HTML deck (Marp) | ต้องนำเสนอ |
| Chart (matplotlib/HTML) | มีตัวเลข trend |

## เมื่อ wiki ไม่มีข้อมูล
1. บอกผู้ใช้ตรง ๆ "ไม่มีใน wiki"
2. ถามว่าจะ ingest source อะไรเพิ่ม หรือใช้ web search
3. **ห้าม hallucinate** เติมเอง — ผิดกฎ Karpathy หลัก

## Anti-patterns
- ❌ ตอบโดยไม่ cite `[[Page]]`
- ❌ ตอบจากความจำตัวเอง ไม่ได้อ่านหน้าจริง
- ❌ ไม่ flag stale (`last_verified:` > 60 วัน)
- ❌ มี ratchet ≥ 2 ข้อ "ใช่" แต่ไม่ file back → ความรู้ตกหล่น
- ❌ ไม่ log query เลย → ไม่เห็น pattern คำถามซ้ำ
