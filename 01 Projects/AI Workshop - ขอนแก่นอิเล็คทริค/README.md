# AI Workshop — บ.ขอนแก่นอิเล็คทริค

**ผู้ว่าจ้าง:** คุณป๊อบ (เจ้าของบริษัท)
**ผู้เรียน:** 15 คน คละแผนก — บัญชี/การเงิน · การตลาด · วิศวกร · ช่าง/เทคนิค
**หลักสูตร:** Claude AI + ทำเว็บ deploy + ฐานข้อมูล + GitHub
**สถานะ:** เตรียม pre-training survey (ยังไม่กำหนดวัน)
**Working dir:** `~/Documents/Claude/Projects/AI Workshop Management/`

## ความท้าทายหลัก

**ความต่างระดับสูงมาก** — บางคนไม่เคยเขียนโค้ดเลย บางคนทำเว็บได้
เจ้าของอยากให้ทุกคนทำเว็บ + DB ได้จริง → ต้อง tiered outcome หรือลดเพดาน

## โครงสร้างไฟล์

- [[01-Forms-Setup]] — Apps Script + Form IDs + Web App deployment
- [[02-Survey-Content]] — เนื้อหาฟอร์มทั้ง 2 (เจ้าของ + ผู้เรียน)
- [[03-Gaps-Analysis]] — จาก aidebate: 3 insight สำคัญที่ใส่เพิ่มแล้ว
- [[04-Menu-Catering]] — เมนูอาหาร/เครื่องดื่ม/ขนมเบรค (SHIFT 2026-06-30)

## เนื้อหาที่เพิ่มจาก aidebate (3 insight)

1. **Tiered outcome** (ฟอร์มเจ้าของ ส่วน 6) — ปลดล็อก pacing ของคอร์ส
2. **Excel/automation proxy + pre-task** (ฟอร์มผู้เรียน ส่วน 3) — ทำนายเร็ว/ช้าแม่นกว่า "เคยโค้ดไหม"
3. **(ยกเลิก)** ฟอร์มหัวหน้าแผนก — user ไม่เอา trash แล้ว 2026-06-30

## Pipeline ที่ใช้ทำ project นี้

1. ดราฟต์เนื้อหา (markdown) — Claude
2. แปลงเป็น Apps Script — Claude + clasp deploy เป็น Web App
3. เกลาภาษาไทย — Typhoon (`scb10x/typhoon2.1-gemma3-12b`) 61/121 strings เปลี่ยน → `BeforeAfter_Typhoon.md`
4. หา gaps — aidebate (Codex + Typhoon2 + Claude judge) → 3 insight
5. แปลงเป็น choice-based — ลด text input จาก 15+ → 5 รายการ
6. เพิ่มเมนู catering — SHIFT เรท 70/49 บาท
