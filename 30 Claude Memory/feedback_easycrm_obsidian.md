---
name: feedback-easycrm-obsidian
description: EasyCRM info ทุกอย่างต้อง save/lookup ใน ~/SecondBrain/EasyCRM/ ใน Obsidian — ไม่ใช่ memory เปล่าๆ
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d3a23350-d19b-4945-be43-ce0af6d1f290
---

ข้อมูลเกี่ยวกับ **EasyCRM** ทุกประเภท (specs, pricing, workflow, team, ลิงก์, ปัญหา, decisions, meeting notes) ต้องไปลงที่ Obsidian folder `~/SecondBrain/EasyCRM/`

**Why:** ผู้ใช้สั่งวันที่ 2026-06-11 ว่า "เอาทุกอย่างเกี่ยวกับ EasyCRM ไปจำในนี้ [Obsidian EasyCRM folder] และต่อๆ ไปด้วย" — Obsidian = single source of truth สำหรับ EasyCRM (ค้นได้ง่าย, link ภายในได้, ใช้ผ่านมือถือ/ทุก device)

**How to apply:**
- มีข้อมูล EasyCRM ใหม่เข้ามา → append/create note ใน `~/SecondBrain/EasyCRM/` (kebab-case ชื่อไฟล์ + อัปเดต `หน้าหลัก.md` ถ้าเพิ่มไฟล์ใหม่)
- มีคำถามเรื่อง EasyCRM → ค้น `~/SecondBrain/EasyCRM/` ก่อนเสมอ
- ต้นทาง (PDF/HTML/source) → เก็บไว้ที่ `_assets/`
- โครงไฟล์ปัจจุบัน: 01-Overview, 02-Packages-Pricing, 03-Features-Comparison, 04-LINE-OA-Setup, 05-Workflow-Onboarding, 06-Team-Roles-SOP, 07-Admin-Portal, 08-Message-Templates, 09-Team-Channels-Links
- แชท EasyCRM (future) → `_chats/YYYY-MM.md` — SessionEnd hook ที่ `~/.claude/hooks/summarize-session.sh` auto-append เข้าให้ตามเดือนเมื่อ detect คำว่า EasyCRM/easycrm-two.vercel.app/easy-crm.co/@easycrm (กฎเดียวกับ EasyBOT)
- Memory เก็บแค่ pointer (ดู [[project_easycrm]]) — เนื้อหาจริงอยู่ใน Obsidian
- ระวัง: vault sync mirror memory → Obsidian แต่ EasyCRM folder = native Obsidian (แก้ที่นี่ตรงๆ ได้เลย ไม่ต้องผ่าน memory)
- **อย่าสับสน:** EasyCRM ≠ EasySlip (API ตรวจสลิป) ≠ EasyBOT — ทั้ง 3 คนละ product
