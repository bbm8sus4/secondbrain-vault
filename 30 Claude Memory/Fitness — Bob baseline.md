---
name: project-fitness-bob
description: "Bob fitness baseline + deployed HTML report for trainer. Knowledge base in Obsidian, working files in Documents, live URL on CF Pages."
metadata: 
  node_type: memory
  type: project
  originSessionId: b021af49-0884-4c0b-bf02-afb7be709027
---

Personal fitness tracking for Bob (user). Baseline 29 มิ.ย. 2026 = 105 kg / BMI 35.5 / BF 35.4% (obese class 2) but skeletal muscle excellent (38.8 kg). Target 77.7 kg / waist ≤100 cm / BF <20%. Program: 3 วัน/สัปดาห์ Full Body A/B · 2,000 kcal · P 180g.

**Why:** ผู้ใช้เริ่มโปรแกรมลดไขมัน 29 มิ.ย. ส่งโปรไฟล์ให้เทรนเนอร์รีวิวผ่าน HTML deployed.

**How to apply:**
- ทุกข้อมูล fitness → `~/SecondBrain/02 Areas/Fitness/` (Obsidian, ongoing area not project)
- Working HTML/photos → `~/Documents/Claude/Projects/Fitness Coach/`
- Deploy folder → `~/Desktop/Fitness/bob-profile-deploy/`
- **Live URL (stable):** https://bob-fit-baseline.pages.dev (CF Pages project `bob-fit-baseline`)
- Redeploy: `wrangler pages deploy . --project-name=bob-fit-baseline --commit-dirty=true --branch=main`
- URL ไม่เปลี่ยน — แก้แล้ว deploy ทับได้เลย
- Design rules (ดู [[No emoji in HTML outputs|feedback_no_emoji]]): ไม่ใช้อิโมจิ, light default, vanilla JS, Inter + Noto Sans Thai

ดู `Bob - Baseline 2026-06-29.md` ใน Obsidian สำหรับข้อมูลครบ (body comp, รอบตัว, BMI/BMR/TDEE table, nutrition, training program, health flags).
