---
name: project_m_trainer_management
description: "m-trainer-management — independent clone of TrainerFlow, own repo + Vercel, evolved separately"
metadata: 
  node_type: memory
  type: project
  originSessionId: d02346a8-e0db-4158-82d0-70171f7ae46a
---

**m-trainer-management** — โคลนแยกจาก [[TrainerFlow (PT client mgmt)|project_trainerflow]] (2026-07-14) ให้เป็นโปรเจกต์อิสระ พัฒนาแยกกันทุกอย่าง. TrainerFlow ยังเป็นตัวหลัก; อันนี้แยกออกมาต่างหาก.

- **Folder**: `~/m-trainer-management` (git repo แยก own history)
- **GitHub**: `bbm8sus4/m-trainer-management` (private)
- **Vercel**: project แยก `m-trainer-management` · live **https://m-trainer-management.vercel.app** (DEMO_MODE=true, single clean deploy)
- **Identity เปลี่ยน**: package.json name + `supabase/config.toml` project_id → `m-trainer-management`. UI ยัง brand เป็น "TrainerFlow" (เปลี่ยน central ได้ทีหลังถ้าต้องการ).
- Codebase เหมือน TrainerFlow เป๊ะ (Next.js 16 + Supabase, demo/supabase adapters, session ledger, 3-layer authz). typecheck/lint/48 tests เขียวหลังโคลน.
- **สำคัญ**: 2 โปรเจกต์นี้แยกกันสนิท — แก้ที่ตัวไหนไม่กระทบอีกตัว. อย่าสับสนกับ office-seating (นั่นของ Codex/GPT คนละงาน user สั่งลืมไปแล้ว).
- **ต่อยอดเกิน trainerflow แล้ว** (2026-07-14/15, แรงบันดาลใจจาก `watcharin-kaewmoung/trainerhub` — repo ไม่มี license เลย reimplement เอง ไม่ก็อป): ธีม ดำ-เหลือง-ขาว (Jakarta+IBM Plex Thai), PWA ติดตั้งได้, เนื้อหาท่าฝึกเป็นอังกฤษ, เทรนเนอร์=โค้ชเอ็ม. + 7 ฟีเจอร์ใหม่: นัดวนซ้ำรายสัปดาห์, รหัสเชิญลูกค้า, /api/health, โภชนาการเต็ม (แผนมื้อ+บันทึกอาหาร+targets), เทียบพัฒนาการฝึก (progressive overload), LBM/BMR/TDEE, เช็คเอาต์หลังฝึก, LINE + daily digest (`/api/cron/daily-digest`, flag-gated, cron 08:00), SaaS owner console (`/owner/*`, role owner, demo login u-owner).
- **Caveats**: SaaS console + LINE = demo-only/flag-gated (Supabase methods throw/gated). 55 unit/integration tests. Demo login เพิ่ม owner@ (u-owner).
