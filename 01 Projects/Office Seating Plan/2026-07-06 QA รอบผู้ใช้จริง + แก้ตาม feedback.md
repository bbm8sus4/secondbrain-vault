---
tags: [seatmap, qa, feedback, session-log]
project: Office Seating Plan (SeatMap)
date: 2026-07-06
version-checkpoint: seatArh_v.1.0.0 (ก่อน QA) → v1.0.1 (8 bug fix) → v1.0.2 (i18n ครบ) · ~/Work/office-seating-deploy/versions/
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

## 🌐 Public GitHub repo (2026-07-06)
Bob สั่ง "อัปขึ้น GitHub + เปิด public" → **https://github.com/bbm8sus4/office-seating-plan** (public)
- **โฟลเดอร์ `~/Work/office-seating-deploy` เดิมไม่ใช่ repo ตัวเอง** — git root ชี้ home (`/Users/aexgee` = repo `ollama-api-chat`) → `git init` ใหม่แยกเฉพาะ SeatMap, remote ชื่อ `smorigin`
- **PII decision:** เตือน Bob ว่า source มีชื่อ/ตำแหน่งจริง 47 คน + git history ลบไม่ออก → Bob เลือก **"public ทั้งชื่อจริง"** (รับความเสี่ยงเอง). เงินเดือน/สุขภาพ = null หมด ไม่หลุด
- **กัน secret:** `.gitignore` = `_worker.js`, `*_worker.js`, `wrangler.toml`, `.wrangler/` (รหัส gate `thunder2026` อยู่ใน worker เท่านั้น) + scrub รหัสออกจาก `seatArh_v.1.0.0_MANIFEST.txt` → **verify remote: 0 จุดของ thunder2026, ไม่มี worker/wrangler บน GitHub**
- repo มี 10 ไฟล์: README + `dist/index.html` + `dist/robots.txt` + version snapshots (index.html + MANIFEST ของ v1.0.0/1.0.1/1.0.2)
- **deploy จริงยัง gate ด้วยรหัสเหมือนเดิม** (worker ไม่ได้ขึ้น public)

## ✅ UI fix — กล่อง "+ เพิ่ม" ในเลนโปรดักส์ (2026-07-06, หลัง v1.0.2)
Bob ทัก [Image]: กล่อง `+ เพิ่ม` กับการ์ดคนในเลนไม่เท่ากัน → สั่งยึดขนาดการ์ดคน
- **สาเหตุ:** การ์ดคนถูกล็อกกว้าง 210px จาก `.pbox{width:210px}` (บรรทัด ~518, rule เก่าสำหรับ layout flex) แต่กล่องเพิ่ม `.prow-add` กางเต็มช่อง grid (249px) + `min-height:56px` (การ์ดคนสูง 51px) → กว้าง+สูงไม่ตรง
- **แก้:** เพิ่ม rule `.prow-body .prow-add{width:210px;flex:0 0 auto;min-height:51px;padding:8px 10px;}` (scoped เฉพาะในเลนโปรดักส์)
- **verify Chrome MCP:** การ์ดคน = กล่องเพิ่ม = **210×51 เป๊ะ** ทั้งคู่ · 49 คนไม่แตะ · deploy แล้ว

## ✅ i18n เชิงลึก — ทำครบแล้ว (v1.0.2, deploy + verify)
สลับ TH/EN ได้ **ทุกจุดที่มองเห็น** แล้ว:
- **Form labels** person/room/org/linkOrg → `data-i18n` (18 label + 2 ตัวที่มี `*` ครอบ span คง `*` ไว้)
- **Modal titles** dynamic → `t()` (`mt.*`, 6 จุด: เพิ่ม/แก้พนักงาน·ห้อง·ผังองค์กร)
- **หน้า Prefs/ตั้งค่า** ทั้งหน้า → `pf.*` (~30 string) + `renderPrefs` ปุ่มล็อก/quota ผ่าน `t()`/`L()`; `applyLang` re-render Prefs ถ้าเปิดอยู่
- **Runtime messages** confirm(22)+alert(13)+toast(79) = **163 จุด (143 literal ไม่ซ้ำ)** → helper `L(th,en)` (ปลอดภัยกว่าเพิ่ม key ทีละตัว, รองรับ concatenation)
- I18N.en keys รวม **254**
- **verify (Chrome MCP, EN mode):** เหลือแค่ปุ่ม "ไทย" (สลับภาษา — ตั้งใจโชว์ชื่อภาษา) · 49 คน / 5 ห้อง / 2 owner ไม่แตะ
- Snapshot: `versions/seatArh_v.1.0.2_*`

**หมายเหตุ:** Blueprint rows (เบอร์/วันเกิด/กรุ๊ปเลือด...) เป็น label **สองภาษาในตัว** ("ที่อยู่ · Address") อยู่แล้ว — EN เห็นอังกฤษครบ เลยไม่แตะ (ตั้งใจ)

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
