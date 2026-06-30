---
name: project-ai-workshop-khonkaen
description: AI Workshop ที่บ.ขอนแก่นอิเล็คทริค ผู้เรียน 15 คนคละแผนก (บัญชี/การตลาด/วิศวกร/ช่าง) สอน Claude + deploy เว็บ + ฐานข้อมูล + GitHub
metadata: 
  node_type: memory
  type: project
  originSessionId: ee3243ee-719d-43e0-bff1-37e9a5221f48
---

**Workshop:** "Claude AI + ทำเว็บ deploy + ฐานข้อมูล + GitHub" ให้บ.ขอนแก่นอิเล็คทริค (ผู้ว่าจ้าง = คุณป๊อบ)
**ผู้เรียน:** 15 คน คละแผนกหนัก — บัญชี/การเงิน + การตลาด + วิศวกร + ช่าง ความต่างระดับสูงมาก
**ความท้าทายหลัก:** เจ้าของอยากให้ทุกคนทำเว็บ+DB ได้จริง แต่ครึ่งกลุ่มเป็น non-tech → ต้อง tiered outcome หรือลดเพดาน

**Why:** โปรเจกต์ใหม่ 2026-06-30 ใช้แบบสำรวจ Pre-training คัดระดับ + กำหนดความลึก ก่อนวันงาน

**How to apply:**
- Path: `~/Documents/Claude/Projects/AI Workshop Management/`
- ไฟล์: `1_แบบสอบถามเจ้าของธุรกิจ_NeedsAnalysis.md`, `2_แบบสำรวจผู้เรียน_AI_Workshop.md`, `3_สร้างGoogleForm_AppsScript.gs`, `BeforeAfter_Typhoon.md`, `4_Aidebate_Gaps_แบบสำรวจ.md`, `FORM_URLS.md`
- Apps Script project: `clasp-deploy/` (clasp standalone, deploy เป็น Web App, doGet สร้าง/อัปเดต 3 ฟอร์ม)
- 3 Form IDs (hard-coded ใน Code.gs):
  - Owner (Needs Analysis): `1oEUefpyYqe1MQPpbwyM_lrkzReq02ZaETM50rUf-bvw`
  - Learner (Pre-training): `1ekrJsyjnlVluHixcDwyJy0AcTnwO9vuYYfzfkw81G7o`
  - Manager (รายแผนก): เก็บใน `PropertiesService.getScriptProperties().MANAGER_FORM_ID`
- เนื้อหาฟอร์มผ่าน Typhoon polish แล้ว (61/121 strings เปลี่ยน) + เพิ่ม 3 insight จาก aidebate (tiered outcome / Excel-automation proxy + pre-task / ฟอร์มหัวหน้าแผนก)
- ใช้ bobbysomporn@gmail.com (ไม่ใช่ 9bomqu) ในการรันทุก script
- Workshop Company 7 ทีม (ของ marketing training อีกอันหนึ่ง) คนละโปรเจกต์ — ดู [[AI Workshop — 7 ทีมการตลาด|project-ai-workshop-7teams]]

**Reference workflows ที่ใช้:**
- [[clasp Apps Script + Web App workaround|reference-clasp-apps-script-webapp]] — วิธี deploy Apps Script ผ่าน clasp + Web App workaround
