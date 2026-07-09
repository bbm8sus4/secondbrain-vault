---
name: project-github-team-access
description: สิทธิ์ GitHub ที่แจกให้ AI agents ภายนอก (mark-ai/Thunder/Athena) — ใช้ตอน audit/revoke
metadata: 
  node_type: memory
  type: project
  originSessionId: 4614a27b-d57d-4c7d-bb20-23f74d18f3c6
---

Team Setup ปิดโปรเจกต์ 2026-07-09. สิทธิ์ที่ยัง active บน repo ของ bbm8sus4:
- `nextainextgen-prog` (mark-ai, เครื่อง A) = collaborator **write** ทั้ง `secondbrain-vault` และ `easyslip-pricing-calculator` (private, Cloudflare Pages)
- Thunder Solution Management = deploy key SSH read-only ชื่อ `thunder-solution-management (read-only)` บน `secondbrain-vault`
- Athena secretary = fine-grained PAT `athena-vault-readonly` (Contents: Read, repo เดียว) — Bob สร้างบนเว็บเอง

ตารางเต็ม + คำสั่ง revoke: `~/SecondBrain/03 Resources/สรุป 2026-07-06 — Team Setup (เชื่อมทีม AI เข้า GitHub).md`
เกี่ยวข้อง: [[SecondBrain vault system|project-secondbrain-vault-system]]
