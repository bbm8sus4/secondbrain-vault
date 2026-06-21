---
title: WIKI — Page Templates
type: schema-playbook
status: live
date: 2026-06-21
tags: [schema, wiki, template, frontmatter]
related:
  - "[[WIKI]]"
  - "[[WIKI - Ingest Playbook]]"
---

# Page Templates

> Frontmatter + structure มาตรฐานทุกประเภทหน้า · copy แล้วแก้ค่า

## ฟิลด์บังคับ (ทุกหน้า wiki)

```yaml
title:           # ชื่อแสดง (ไทยหรืออังกฤษก็ได้ ตรงกับโดเมน)
type:            # ดู taxonomy ข้างล่าง
source:          # ต้นทาง (file path / URL / Apple Notes #N / chat YYYY-MM-DD)
source_date:     # วันที่ของ source
imported:        # YYYY-MM-DDTHH:MM:SS
last_verified:   # YYYY-MM-DD (เริ่มเท่า imported, อัพเดตทุกครั้งที่แตะ)
status:          # draft | live | archived
tags:            # [domain, type, ...]
```

## ฟิลด์เลือก (เพิ่มเมื่อเข้ากับหน้า)

```yaml
related:         # [[backlinks]]
memory_pointer:  # slug ใน ~/.claude-warp/memory/ ถ้ามี memory ชี้มา
deprecates:      # [[Page]] ถ้าหน้านี้แทนหน้าเก่า
deprecated_by:   # [[Page]] ถ้าหน้านี้ถูกแทน
review_after:    # YYYY-MM-DD วันที่ต้องกลับมาดูแน่ ๆ
owner:           # ใคร own ความถูกต้อง
```

---

## Taxonomy — type

| type | ใช้กับ | อยู่ที่ไหน |
|---|---|---|
| `project` | งานมี deadline | `01 Projects/` |
| `area` | งานต่อเนื่อง | `02 Areas/` |
| `resource` | reference · playbook | `03 Resources/` |
| `entity` | คน · บริษัท · product | brand folder · `01 Projects/<X>/` |
| `concept` | idea · framework | `03 Resources/` |
| `event` | meeting · launch · incident | `01 Projects/<X>/` |
| `decision` | go/no-go ที่ commit แล้ว | brand folder |
| `synthesis` | คำตอบที่ file back จาก query | ใกล้หน้าที่ refer |
| `vendor-quote` | ใบเสนอราคา | brand folder |
| `schema` / `schema-playbook` | กฎ wiki | `20 Rules/` |
| `archived` | จบ + เก็บ | `04 Archive/` |

---

## Template 1 — Project (root README)

```markdown
---
title: <Project name>
type: project
source: <pointer>
source_date: YYYY-MM-DD
imported: ...
last_verified: ...
status: live
owner: Bob (COO)
tags: [project, <domain>, <brand>]
---

# <Project name>

> 1-line tagline

## ทำไมต้องสน
- ...

## ดัชนีไฟล์ (sub-pages)
- [[Strategic Analysis]] — ...
- [[Product]] — ...

## สถานะปัจจุบัน (YYYY-MM-DD)
- ...

## Quick wins ที่ยังไม่ทำ
1. ...

## Assets นอก Obsidian
- `~/Desktop/...`
```

## Template 2 — Entity (คน / บริษัท / product)

```markdown
---
title: <Entity>
type: entity
source: ...
source_date: ...
last_verified: ...
status: live
related:
  - "[[Project X]]"
tags: [entity, <domain>]
---

# <Entity>

## ใครคือใคร
- ...

## บทบาทใน projects ของเรา
- ...

## ติดต่อ
- ...

## ประวัติย่อ (timeline)
- YYYY-MM-DD: ...
```

## Template 3 — Concept / Framework

```markdown
---
title: <Concept>
type: concept
source: ...
last_verified: ...
status: live
tags: [concept, <domain>]
---

# <Concept>

## คืออะไร (1 ย่อหน้า)

## ทำไมสำคัญ

## ใช้กับ projects ไหน
- [[Project A]]
- [[Project B]]

## ตัวอย่าง

## เกี่ยวข้องกับ
- [[Concept ใกล้เคียง]]
```

## Template 4 — Synthesis (file back จาก query)

```markdown
---
title: <Topic> — Synthesis
type: synthesis
source: chat YYYY-MM-DD
source_date: YYYY-MM-DD
imported: ...
last_verified: ...
status: draft
related:
  - "[[Pages ที่ใช้สังเคราะห์]]"
tags: [synthesis, <domain>]
---

# <Topic> — Synthesis

> สังเคราะห์จาก [[Page A]] + [[Page B]] + [[Page C]] เพื่อตอบคำถาม: <question>

## TL;DR

## รายละเอียด

## Open questions
- ...
```

## Template 5 — Decision

```markdown
---
title: Decision — <subject>
type: decision
source: chat YYYY-MM-DD / meeting ...
source_date: YYYY-MM-DD
last_verified: ...
status: live
owner: Bob (COO)
tags: [decision, <domain>]
---

# Decision — <subject>

## เลือกอะไร
> 1 ประโยค

## ทางเลือกที่พิจารณา
1. ...
2. ...

## เหตุผล

## ผลกระทบ / next steps
- ...

## Revisit
- เงื่อนไขที่จะรื้อ decision นี้ใหม่
```

---

## Naming convention (file)

- ไทย/อังกฤษ: ใช้ภาษาที่ entity เป็น (KuanGolf = อังกฤษ, บ๊อบ = ไทย)
- ห้าม: `:`, `/`, ตัวอักษรพิเศษ filesystem (script Apple Notes export จัดการให้ละ)
- ตัวคั่น: ` — ` (em-dash space) สำหรับ sub-topic เช่น `KuanGolf — Brand Strategy Brain.md`
- Sync mirror (`30 Claude Memory/`) จะแปลง slug → ไทย อัตโนมัติ — อย่าตั้งเอง

## Synonyms / aliases
ถ้า entity มีหลายชื่อ ใช้ Obsidian aliases ใน frontmatter:
```yaml
aliases:
  - "ก๊วนกอล์ฟ"
  - "Kuan Golf"
```
ทำให้ `[[ก๊วนกอล์ฟ]]` resolve ไป `KuanGolf — ...md` ได้
