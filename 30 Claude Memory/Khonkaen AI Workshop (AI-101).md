---
name: project_khonkaen_ai_workshop
description: "AI Workshop for Khonkaen Electric — status, deliverables, and where the files live"
metadata: 
  node_type: memory
  type: project
  originSessionId: c25a2b2a-038e-44d1-aaab-2832fc3e8ae9
---

**AI-101 for บ.ขอนแก่นอิเล็คทริค** (Claude AI workshop) · ผู้ว่าจ้าง คุณป๊อบ · ผู้เรียน 15 คน (คละแผนก, 9/11 สายการตลาด, มั่นใจเฉลี่ย 2.7/5) · หลักสูตร 1 วัน Core/Advanced/Demo track.

**สถานะ:** งานเตรียม ✅ เสร็จ (2026-07-09) · ตอนนี้ 🎬 กำลังทำสไลด์ (มี Part1–4 + Setup outline ที่ `Files/Slides/`). โฟลเดอร์ rename จาก "AI Workshop - ขอนแก่นอิเล็คทริค" → "AI-101 for บ.ขอนแก่นอิเล็คทริค" เมื่อ 2026-07-09 เพื่อรวมทุกอย่างไว้ที่เดียว.

Thunder เป็นผู้ให้บริการ (ราคา 2,499/คน × 15 = 37,485 + VAT = **40,108.95**, จ่ายเต็มครั้งเดียว).

โปรเจกต์อยู่ที่ `~/SecondBrain/01 Projects/AI-101 for บ.ขอนแก่นอิเล็คทริค/`:
- `Files/Costs/` — ใบเสนอราคา PDF 5 หน้า + Word (.docx) แบบ Cotactic + Pricing-Calculator
- `Files/Forms/` — Apps Script สร้าง Google Form; ฟอร์มอาหาร (เบรก+กลางวัน) deploy จริงแล้ว ดู `FORM_URLS.md` + `catering-form-deploy/DEPLOY_NOTES.md`
- `Files/Curriculum` `Files/Slides` `Files/Dashboard` — หลักสูตร/สไลด์/dashboard

⚠️ Google Form ที่มี response แล้ว **ห้าม clearAllItems/rebuild** (เคยมี incident ข้อมูลหาย). งานเตรียม QA PASS หมด เหลือรันคลาสหน้างาน. วิธีทำเอกสาร: [[Thai doc generation|reference_thai_doc_generation]].
