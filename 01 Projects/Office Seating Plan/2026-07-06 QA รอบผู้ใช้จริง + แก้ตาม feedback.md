---
tags: [seatmap, qa, feedback, session-log]
project: Office Seating Plan (SeatMap)
date: 2026-07-06
version-checkpoint: seatArh_v.1.0.0 (snapshot ก่อน QA อยู่ที่ ~/Work/office-seating-deploy/versions/)
---

# SeatMap — QA รอบ "ผู้ใช้จริง" + แก้ตาม feedback (2026-07-06)

> Bob สั่ง: เซฟเวอร์ชัน `seatArh_v.1.0.0` ก่อน → เล่นเป็นผู้ใช้จริง ฟีดแบ็กตรง ๆ ห้ามเข้าข้างตัวเอง → แก้ตาม feedback (autonomous)
> ทำโดยแยก **2 sub-agent** (UX reviewer + senior engineer/QA) วิจารณ์แบบไม่ปั้นแต่ง + ผมเทสต์ runtime เอง

## ✅ แก้แล้ว (deploy + verify ครบ, 0 error)
1. **Blueprint badge สถานะผิดสำหรับ hybrid/owner** — เดิม fallback เป็น "Active". เปิดโปรไฟล์ WOOT (owner) เคยขึ้น "ทำงานปกติ" → แก้ให้ครบ 5 สถานะ (verify: WOOT = "เจ้าของ")
2. **Owner ถูกดึงเข้า WFH แล้วเสียสถานะ owner เงียบ ๆ** — performDrop wfh / setWfhFromPicker / _wfhAdd / openWfhAssign candidates กัน owner ทั้งหมด (verify: ลาก WOOT เข้า WFH → ยังเป็น owner)
3. **companyShort คืน "Other" เสมอ** — Thai UI เห็น "Other" ไม่ใช่ "อื่นๆ" → ใช้ t("stat.other")
4. **ที่นั่ง "จอง" hardcode** → t("seat.reserved") (EN = HOLD). ("EMPTY" คงไว้ตามที่ Bob สั่งให้ใช้คำเดียว)
5. **ปุ่ม Lock ป้ายหาย + ไม่สลับภาษา** — render() เขียนทับ innerHTML เหลือแต่ไอคอน (ไม่เข้าชุดกับ Save/Present) → ใส่ label กลับ + สลับ TH/EN (ล็อก/Lock)
6. **migrateOrg ไม่ clamp `col`** — node ที่ col ผิดช่วง (import/legacy) จะล่องหนแก้ไม่ได้ → clamp 1–5
7. **Sync race — poll ทับ local edit ที่ยังไม่ push** — pullShared bail เพิ่มเงื่อนไข `_sharedPushT` (มี push ค้าง) + _applyShared เคลียร์ timer ก่อน adopt server state (กัน edit หาย + กัน stale push ตีกลับ)
8. **Empty states + Present/Lock + ปุ่ม modal + prod/org buttons + stats + WFH zone + roster hint** — ผูก i18n (t()/data-i18n) สลับ TH/EN ได้ · ปุ่ม modal มาตรฐาน (common.save/cancel/delete/close) 13 ปุ่ม

## ⏳ ยังเหลือ (i18n เชิงลึก — งานใหญ่ ~150+ strings)
สลับ EN แล้ว **modal/ฟอร์มเชิงลึกยังเป็นไทย** — ยังไม่ได้ทำ:
- **ทุก field label ในฟอร์มพนักงาน** (บริษัท/ทีม/สถานะ/วันเริ่มงาน/เบอร์/อีเมล/ฉุกเฉิน/สุขภาพ/เงินเดือน...) — บาง label bilingual "ไทย · English" อยู่แล้ว
- **Blueprint rows** (เบอร์โทร/วันเกิด/กรุ๊ปเลือด/อายุงาน...) — bilingual บางส่วน
- **หน้า Prefs/ตั้งค่า** ทั้งหน้า
- **confirm() 26 จุด + alert() 14 จุด + toast ส่วนใหญ่** hardcode ไทย
- Roster CSV modal, Quick-assign "จองที่นั่ง (Reserve)" ปนภาษาในปุ่มเดียว
→ ควรทำเป็น i18n pass รอบใหญ่แยกต่างหาก (route ทุกอย่างผ่าน t())

## 🟡 feedback ที่ "ไม่แก้" เพราะ Bob สั่งไว้เอง (ไม่ใช่ bug)
- **HR Dashboard ซ่อน** (agent flag P0) — Bob สั่งซ่อน 2026-07-03 (code ยังครบ)
- **Manage table ไม่มีคอลัมน์สถานะ** — Bob สั่งเปลี่ยนเป็น "สัญญาจ้าง" เอง (image #92) · stBadge เลย dead code
- **ตารางไม่มีปุ่มลบ/unseat** — Bob สั่งลบปุ่ม unseat เอง (image #117)
- **owner หายจาก filter** — เป็น spec ที่ Bob สั่ง ("ไม่นับเป็นพนักงาน")

## 🔵 feedback ค้างที่ควรพิจารณา (ยังไม่แก้ — คุ้มค่าแต่ risk/design)
- **status field รวม onboarding+work-mode+role** — hybrid ไม่มี placement wfh, toggleNewHire ทับ mode. โครงสร้าง ควรแยก workMode ออกจาก status (agent2 #10)
- **409 conflict ทิ้ง local edit เงียบ** — ตอนนี้ apply server + toast เตือน แต่ไม่ merge/undo local (ควรมี Undo ใน toast)
- **importJSON: Cancel = merge** (ไม่มี abort จริง) → ควรเป็น 3 ปุ่ม replace/merge/cancel
- **company donut นับพลาด** ถ้า company เป็น string อื่น (dashboard ซ่อนอยู่ เลย impact ต่ำ)
- ของที่ HR อยากได้แต่ไม่มี: **Export CSV แบบกรองจาก Manage, แจ้งเตือน probation/startDate, utilization รวมทุกห้อง, audit log**

เชื่อมโยง: [[2026-07-05 Session — สั่งงาน + วิธีทำงาน]] · [[HANDOFF]] · [[DEPLOY]]
