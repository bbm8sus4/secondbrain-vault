---
title: project-bob — Team & Obsidian Setup
type: note
status: live
created: 2026-07-06
tags: [project-bob, team, tmx, obsidian, setup]
---

# project-bob — Team & Obsidian Setup

บันทึกการตั้งค่าที่ทำในห้อง tmx `project-bob` (2026-07-06).

## 1. เชื่อม Obsidian vault เข้ากับ project-bob
- vault "SecondBrainSync" (Obsidian Sync ของ Bob) ถูก mirror ขึ้น GitHub **private repo**: `bbm8sus4/secondbrain-vault` (auto-push ทุก ~30 นาที ด้วย obsidian-git จากเครื่อง Bob)
- เครื่อง agent (Mac mini ของ watcharin) clone repo มาไว้ที่ `project-bob/vault` ผ่านบัญชี `nextainextgen-prog` (collaborator)
- skill `obsidian-bob` ให้ agent อ่าน/ค้นโน้ตได้ · refresh ด้วย `git -C project-bob/vault pull`
- **สิทธิ์ปัจจุบัน: READ-ONLY** (pull เท่านั้น) — เขียนกลับ/ push ขึ้น repo ยังไม่ได้จนกว่าจะเปลี่ยน permission เป็น write

## 2. ทีมพัฒนา project-bob (tmx multi-room)
ห้องนี้ (`project-bob`) = **CEO** — Bob สั่งงานที่นี่ที่เดียว แล้ว CEO กระจายงานต่อ

| ห้อง | บทบาท | engine |
|---|---|---|
| project-bob | CEO | claude |
| bob-po | Product Owner | claude |
| bob-pm | Project Manager | claude |
| bob-dev | Dev 1 | claude |
| bob-dev-2 | Dev 2 | claude |
| bob-reviewer | Reviewer | codex |

- กฎ: Claude เขียนโค้ด, Codex ตรวจ diff อย่างเดียว, ทุก change ผ่าน review ก่อน merge, dev แยก worktree/branch
- เอกสารกลาง: `project-bob/TEAM_WORKFLOW.md`
- role skills: `bob-ceo`, `bob-po`, `bob-pm`, `bob-coder`, `bob-reviewer` (ใน `~/.claude/skills/`)

## สถานะ
- โปรเจกต์ยังไม่มีโค้ด — รอ Bob กำหนดว่าจะสร้างอะไร
