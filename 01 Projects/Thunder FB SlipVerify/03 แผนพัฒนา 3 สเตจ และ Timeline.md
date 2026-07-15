---
title: แผนพัฒนา 3 สเตจ และ Timeline
project: facebook-verify
type: plan
tags: [facebook-verify, plan, roadmap, timeline]
updated: 2026-07-15
confidential: true
---

# 🏗️ แผนพัฒนา 3 สเตจ และ Timeline

> กลับไป [[00 แผนที่ความรู้ (MOC)]] · ทิศที่เคาะแล้ว: ทำ Messenger ก่อน คอมเมนต์/ไลฟ์ตาม · เริ่ม Pilot เพจเดียว

## ภาพรวม 3 สเตจ
| สเตจ | ทำอะไร | ต้องรอ Meta? | Timeline คร่าวๆ |
|------|--------|:-----------:|------|
| **1. Pilot เพจเดียว** | พิสูจน์ flow บนเพจเราเอง: รับสลิป→ตรวจ→ตอบ | ❌ เริ่มได้เลย | **~1–2 สัปดาห์** |
| **2. Product หลายร้าน** | ร้านเชื่อมเพจตัวเอง + dashboard + billing | ✅ App Review | **~1.5–3 เดือน** |
| **3. คอมเมนต์/ไลฟ์/IG** | ตรวจสลิปใต้คอมเมนต์/ไลฟ์ + Instagram | ✅ App Review | **~3–6 สัปดาห์** |

> ⚠️ ประมาณการคร่าวๆ สมมุติ dev โฟกัส 1 คน · เวลารอ **Meta App Review คุมไม่ได้** (คือคอขวด) · ตัวเลขไว้คุยทีม ยังไม่ใช่ commitment

## 🎯 Stage 1 — Pilot เพจเดียว (โฟกัสตอนนี้) · ~1–2 สัปดาห์
ทำบนเพจของเราเอง 1 เพจ — จุดประสงค์คือพิสูจน์ flow ให้เห็นกับตา ยังไม่ใช่ของขาย

**ทำไมไม่ต้องรอ Meta review:** ทดสอบด้วยบัญชี admin/tester ของแอปเราเอง (Standard Access) ส่งสลิปเข้าเพจตัวเอง — ไม่ต้องขอ Advanced Access จนกว่าจะรับลูกค้าจริง (= Stage 2)

**สิ่งที่ต้องทำ (ผอมสุด):**
- สร้าง Facebook App + เอา Page Access Token ของเพจเราเอง (ผ่าน App Dashboard)
- subscribe เพจเข้า webhook `messages`
- Webhook receiver → เรียก EasySlip API (key เดิม) → ตอบผลในแชทด้วย Send API
- ตรวจครบ: กันซ้ำ + เช็คยอด + เช็คบัญชี
- ดูผลจาก log ตรงๆ (ยังไม่ต้องมี dashboard)

**เกณฑ์สำเร็จ:** ส่งสลิปจริง 10–20 ใบ (จริง/ปลอม/ซ้ำ/ยอดผิด) แล้วบอทตอบถูกทุกเคส + หน่วงเวลารับได้

## 📦 Stage 2 — Product หลายร้าน · ~1.5–3 เดือน
- **Build** (OAuth onboarding + dashboard + billing per-merchant): ~3–5 สัปดาห์
- **Business Verification + App Review**: ~2–6 สัปดาห์ (ทำขนาน เป็นคอขวด)
- ขอ Advanced Access สิทธิ์: `pages_show_list`, `pages_manage_metadata`, `pages_messaging`, `pages_read_engagement`, `business_management`
- เตรียม: วิดีโอ use-case, privacy policy, แอปที่ demo ได้จริง (ดู [[04 สิ่งที่ต้องเตรียม]])

## 🔵 Stage 3 — คอมเมนต์/ไลฟ์/IG · ~3–6 สัปดาห์ (หลัง Messenger นิ่ง)
- เพิ่ม subscribe webhook field `feed` (คอมเมนต์) — รูปคอมเมนต์ต้องเรียก Graph API เพิ่ม, ระวัง CDN ย่อรูป
- ตอบด้วย Private Reply (1 ข้อความ, 7 วัน, text-only) เด้งลูกค้าเข้าแชท → เข้า flow เดิม
- รองรับ Facebook Live (volume พุ่ง ต้องเทสต์ load) + Instagram DM (reuse core)
- reuse component 2–7 ของเฟส A ได้เกือบทั้งหมด (เปลี่ยนแค่ "ทางเข้า" ของรูป)

## 🔴 Critical Path — เริ่มขนานแต่เนิ่นๆ
1. **เคลียร์ฐานกฎหมาย/นโยบาย** ก่อนลงทุนหนัก (ดู [[09 กฎหมาย ความเสี่ยง และคำถามเปิด]])
2. **Business Verification + App Review** — เริ่มขนานตั้งแต่วันแรกของ Stage 2 เพราะรออนุมัตินาน ยิ่งเริ่มเร็วยิ่งดี

## ลำดับงาน (Milestones)
1. เคลียร์กฎหมาย + เริ่ม Business Verification _(ขนาน, เริ่มทันที)_
2. Build core บนเพจ dev — webhook + เรียก EasySlip + ตอบในแชท _(ไม่ต้องรอ review)_
3. Merchant onboarding (OAuth) + Dashboard ขั้นต่ำ
4. ยื่น App Review พร้อม demo ที่ทำงานจริง
5. Closed beta กับร้านจริง 2–3 ร้าน (หลัง Advanced Access ผ่าน)
6. เปิดตัว + เก็บ feedback

## ขอบเขต MVP (YAGNI)
**✅ อยู่ใน MVP:** เชื่อม 1 เพจ · รับสลิป→ตรวจ→ตอบในแชท · ตรวจครบ 3 (ซ้ำ/ยอด/บัญชี) · หักโควตา · dashboard ขั้นต่ำ
**❌ ยังไม่ทำ:** คอมเมนต์/ไลฟ์ (=เฟส B) · Instagram DM · หลายเพจต่อร้าน · รายงานเชิงลึก · Utility Message (optional)
