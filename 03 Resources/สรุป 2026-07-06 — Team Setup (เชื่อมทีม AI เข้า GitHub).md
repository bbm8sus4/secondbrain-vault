---
title: สรุป 2026-07-06 — Team Setup (เชื่อมทีม AI เข้า GitHub)
type: synthesis
source: Claude Code session 2026-07-06 (Ghostty) — ทำจริงทั้งหมด verify ผ่าน gh CLI
source_date: 2026-07-06
imported: 2026-07-09T00:00:00
last_verified: 2026-07-09
status: live
project_status: ✅ เสร็จสมบูรณ์ 2026-07-09
tags: [synthesis, github, team, access-control, milestone]
related:
  - "[[สรุป 2026-07-06 — Vault Overhaul ครบวงจร]]"
  - "[[SecondBrain Blueprint Setup]]"
---

# สรุป 2026-07-06 — Team Setup (เชื่อมทีม AI เข้า GitHub)

> เชื่อม AI agents 3 ตัว (คนละเครื่อง/คนละ environment) เข้า repo ของ Bob ด้วยสิทธิ์ที่เหมาะกับงานแต่ละตัว
> หลักที่ใช้: **least privilege** — ให้สิทธิ์ต่ำสุดที่งานเดิน, ทุกช่องทาง revoke ได้คำสั่งเดียว, ไม่ทำ repo public
> **✅ ปิดโปรเจกต์ 2026-07-09** (ยืนยันโดย Bob)

## สิทธิ์ที่แจกไป (ตารางหลัก — ใช้ audit/revoke)

| Agent | ช่องทาง | Repo | สิทธิ์ | วิธี revoke |
|---|---|---|---|---|
| mark-ai (เครื่อง A, GitHub: `nextainextgen-prog`) | collaborator | `secondbrain-vault` | **write** (เริ่ม read แล้วอัปเป็น write เพื่อ push โน้ต) | `gh api repos/bbm8sus4/secondbrain-vault/collaborators/nextainextgen-prog -X DELETE` |
| mark-ai | collaborator | `easyslip-pricing-calculator` | **write** | เหมือนบน เปลี่ยนชื่อ repo |
| Thunder Solution Management | deploy key (SSH) `thunder-solution-management (read-only)` | `secondbrain-vault` | **read-only** | GitHub → repo Settings → Deploy keys → ลบ (หรือ `gh api repos/bbm8sus4/secondbrain-vault/keys` หา id แล้ว DELETE) |
| Athena · secretary | fine-grained PAT `athena-vault-readonly` (Bob สร้างบนเว็บ) | `secondbrain-vault` | **read-only** (Contents: Read) | github.com → Settings → Developer settings → Fine-grained tokens → revoke |

## Repo ที่เกี่ยวข้อง

- **`bbm8sus4/secondbrain-vault`** (private) — vault นี้ทั้งก้อน · auto-sync commit+push ทุก 30 นาที (ดู [[Automation Setup]])
- **`bbm8sus4/easyslip-pricing-calculator`** (private) — แอปคำนวณราคา EasySlip · mark-ai เขียนโค้ด+push · deploy ผ่าน Cloudflare Pages (Connect to Git, build `npm run build`, output `dist`)

## บทเรียน / กติกาที่ตกผลึก

1. **ไม่ทำ vault เป็น public เด็ดขาด** — ทางเลือกเวลา AI ภายนอกเข้าไม่ถึง: collaborator (ถ้ามี account) → deploy key (SSH, read-only) → fine-grained PAT (HTTPS, repo เดียว)
2. PAT สร้างผ่าน CLI ไม่ได้ — ต้องกดบนเว็บ GitHub เท่านั้น (Settings → Developer settings → Fine-grained tokens)
3. ให้สิทธิ์ write กับ agent ภายนอก = เขาแก้ vault ได้จริง → auto-sync ฝั่งเราจะดึงมาเห็นใน Obsidian เอง ถ้าไม่ไว้ใจให้ลดกลับเป็น pull
4. ทุก key/token ตั้งชื่อระบุเจ้าของ+ระดับสิทธิ์ (`thunder-solution-management (read-only)`, `athena-vault-readonly`) จะได้ audit ง่าย
