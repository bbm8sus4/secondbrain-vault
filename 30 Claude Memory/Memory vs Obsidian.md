---
name: reference-memory-vs-obsidian
description: "Memory vs Obsidian — คนละชั้น คนละวัตถุประสงค์ memory=index/pointer สำหรับ Claude, Obsidian=data store สำหรับมนุษย์"
metadata: 
  node_type: memory
  type: reference
  originSessionId: c43a0a62-0da8-4cce-b114-43e25a68201f
---

# Memory vs Obsidian — ต่างกันยังไง

## คนละวัตถุประสงค์

| | Memory | Obsidian (SecondBrain) |
|---|---|---|
| ใครใช้ | Claude อ่านตอนเริ่ม session | ผู้ใช้อ่าน/เขียนเอง |
| เก็บอะไร | วิธีทำงาน, feedback, project pointer | ข้อมูลจริง: pricing, สัญญา, KB, docs |
| อายุ | ข้าม session ได้ ลบ/reset ได้ | ถาวร, git versioned |
| Format | frontmatter .md เฉพาะ Claude | PARA vault + Obsidian plugins |

## ทำงานร่วมกันยังไง

```
Memory (pointer/index) ──อ่าน──▶ Obsidian (ข้อมูลจริง)
Memory ──sync ทุก 30 นาที──▶ Obsidian (30 Claude Memory/) [read-only mirror]
```

- Memory เป็น **index** ชี้ว่าข้อมูลอยู่ไหนใน Obsidian
- Claude ไปอ่าน Obsidian ตอนต้องใช้จริง ไม่ได้ load ทั้ง vault
- ห้ามแก้ `30 Claude Memory/` ใน Obsidian → แก้ที่ต้นทาง memory dir

## ทำไมไม่รวมเป็นก้อนเดียว

1. Memory load ทุก session — vault ใหญ่เกินจะ inject ทั้งหมด
2. Memory = "วิธีทำงานกับผู้ใช้" ไม่ใช่ข้อมูลจริง
3. Obsidian = source of truth ที่ผู้ใช้ curate เอง
