# AI Workshop — บ.ขอนแก่นอิเล็คทริค

**ผู้ว่าจ้าง:** คุณป๊อบ (เจ้าของบริษัท)
**ผู้เรียน:** 15 คน คละแผนก — บัญชี/การเงิน · การตลาด · วิศวกร · ช่าง/เทคนิค
**หลักสูตร:** Claude AI + ทำเว็บ deploy + ฐานข้อมูล + GitHub
**ผู้เรียนจริงที่ตอบแบบสำรวจ:** 11 คน (9/11 สายการตลาด · มั่นใจเฉลี่ย 2.7/5 · มี 1 คนใช้ Claude ประจำ)
**สถานะ:** กู้ข้อมูลสำรวจสำเร็จ → ส่งมอบ dashboard รวม 3 แท็บแล้ว (`AI-Workshop-รวม.html`)
**Working dir:** `~/Documents/Claude/Projects/AI Workshop Management/` (Apps Script clasp deploy ใช้ที่นี่)
**ไฟล์โปรเจกต์ทั้งหมด (รวมแล้ว):** `Files/` ในโฟลเดอร์นี้ — ดู [[#โฟลเดอร์ Files (รวมไฟล์ทั้งหมด)]]
**Live dashboard:** https://khonkaen-ai-workshop.pages.dev

## ความท้าทายหลัก

**ความต่างระดับสูงมาก** — บางคนไม่เคยเขียนโค้ดเลย บางคนทำเว็บได้
เจ้าของอยากให้ทุกคนทำเว็บ + DB ได้จริง → ต้อง tiered outcome หรือลดเพดาน

## โครงสร้างไฟล์

- [[05-INCIDENT-ข้อมูลหาย-กู้คืน]] — ⚠️ บทเรียน clearAllItems ทับฟอร์มมี response + วิธีกู้ผ่าน Forms REST API (สำคัญ อ่านก่อนแก้ฟอร์ม)
- [[01-Forms-Setup]] — Apps Script + Form IDs + Web App deployment
- [[02-Survey-Content]] — เนื้อหาฟอร์มทั้ง 2 (เจ้าของ + ผู้เรียน)
- [[03-Gaps-Analysis]] — จาก aidebate: 3 insight สำคัญที่ใส่เพิ่มแล้ว
- [[04-Menu-Catering]] — เมนูอาหาร/เครื่องดื่ม/ขนมเบรค (SHIFT 2026-06-30)
- [[06-Dashboard-Summary]] — 📊 ส่งมอบ dashboard รวม 3 แท็บ (เจ้าของ/ผู้เรียน 11 คน/ความสอดคล้อง) + ผลวิเคราะห์ + บทเรียนทำกราฟ

## เนื้อหาที่เพิ่มจาก aidebate (3 insight)

1. **Tiered outcome** (ฟอร์มเจ้าของ ส่วน 6) — ปลดล็อก pacing ของคอร์ส
2. **Excel/automation proxy + pre-task** (ฟอร์มผู้เรียน ส่วน 3) — ทำนายเร็ว/ช้าแม่นกว่า "เคยโค้ดไหม"
3. **(ยกเลิก)** ฟอร์มหัวหน้าแผนก — user ไม่เอา trash แล้ว 2026-06-30

## โฟลเดอร์ Files (รวมไฟล์ทั้งหมด)

รวมเข้าจาก working dir เมื่อ 2026-07-01 · 32 ไฟล์ · 864KB

| โฟลเดอร์ | ไฟล์เด่น | ใช้เมื่อไหร่ |
|---|---|---|
| `Files/Costs/` | **`Pricing-Calculator.html`** (interactive · slider+input · 5 presets · sensitivity table · benchmark vs trycloudflare/cohort/งบเจ้าของ) + `ต้นทุนต่อหัว_AI_Workshop.xlsx` | กดเปิดไฟล์ HTML ปรับค่าได้ทันที (⚠️ xlsx var cost ตั้ง ฿290 แต่เมนูจริง ฿428/หัว — calc HTML เปลี่ยนค่านี้แล้ว) |
| `Files/Data/` | `owner_recovered.csv` · `learner_recovered.csv` · `RECOVERED_responses.xlsx` + raw txt | ข้อมูลตอบแบบสำรวจจริง (เจ้าของ 1 + ผู้เรียน 11) |
| `Files/Curriculum/` | `หลักสูตรที่เหมาะกับผู้เรียน.html` · `เปรียบเทียบความต้องการ.html` · `ความคาดหวังเจ้าของธุรกิจ.html` · `สรุปแบบสำรวจ-เต็ม.html` · `BeforeAfter_Typhoon.md` · `4_แบบประเมินหลังอบรม.md` | โครงหลักสูตร + วิเคราะห์ผู้เรียน + ฟอร์มประเมินหลังอบรม |
| `Files/Dashboard/` | `AI-Workshop-รวม.html` (3 แท็บ — main) + Dashboard / OrgStructure / Rooms.html | ส่งวิทยากร · source ของ `khonkaen-ai-workshop.pages.dev` |
| `Files/Forms/` | `1_แบบสอบถามเจ้าของ.md` · `2_แบบสำรวจผู้เรียน.md` · `3_สร้างGoogleForm_AppsScript.gs` · `4_Aidebate_Gaps.md` · `FORM_URLS.md` + `clasp-deploy/` | เนื้อหาฟอร์ม + Apps Script (clasp deploy ตัวจริงยังอยู่ working dir) |
| `Files/_archive/` | `*.pre-*.bak.html` · `learner_recovered.8.bak.csv` | ก่อน-หลัง Typhoon/collapse + CSV รุ่น 8 คน (ก่อน recover เพิ่ม 3 คน) |

## Pipeline ที่ใช้ทำ project นี้

1. ดราฟต์เนื้อหา (markdown) — Claude
2. แปลงเป็น Apps Script — Claude + clasp deploy เป็น Web App
3. เกลาภาษาไทย — Typhoon (`scb10x/typhoon2.1-gemma3-12b`) 61/121 strings เปลี่ยน → `BeforeAfter_Typhoon.md`
4. หา gaps — aidebate (Codex + Typhoon2 + Claude judge) → 3 insight
5. แปลงเป็น choice-based — ลด text input จาก 15+ → 5 รายการ
6. เพิ่มเมนู catering — SHIFT เรท 70/49 บาท
