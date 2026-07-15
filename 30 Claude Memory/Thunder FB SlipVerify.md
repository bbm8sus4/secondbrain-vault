---
name: project-thunder-fb-slipverify
description: "Thunder FB SlipVerify — โปรเจกต์ตรวจสลิปโอนเงินอัตโนมัติบน Facebook (Messenger→Comment→Live) ใช้ EasySlip/Thunder API, เฟส RESEARCH/PLANNING (ก.ค. 2026)"
metadata: 
  node_type: memory
  type: project
  originSessionId: abf9e49f-d574-48f7-853e-b9383d68259b
---

โปรเจกต์ **ตรวจสลิปโอนเงินอัตโนมัติในช่องทาง Facebook** ของ Thunder Solution — บอทรับรูปสลิปในแชท Facebook แล้วตรวจจริง/ปลอม/ซ้ำ/ยอด/บัญชีใน 2–5 วินาที ต่อยอดจาก EasySlip/Thunder API เดิม (LINE → Facebook)

**Why:** Thunder BOT บน LINE กำลังทรงตัว/ถดถอย, คู่แข่ง (ZWIZ.AI, Chatcone, Page365, Commerzy) ทำ FB ไปแล้ว, ต้อง pivot ขยายช่องทาง. Melisiem สั่งงาน 2026-07-09 ให้เริ่ม Messenger ก่อน

**How to apply:** KB ทั้งหมดอยู่ `~/SecondBrain/01 Projects/Thunder FB SlipVerify/` (14 notes + 4 เอกสารต้นฉบับ). เริ่มที่ MOC `00 แผนที่ความรู้ (MOC).md`. เฟสปัจจุบัน RESEARCH/PLANNING ยังไม่มีโค้ด. ข้อมูลเป็นความลับ (สลิป/การเงิน).

ประเด็นสำคัญ:
- KBank API ห้ามร้าน social media ต่อตรง → ต้องผ่าน EasySlip/Thunder API เท่านั้น
- Meta อนุญาต `pages_messaging` สำหรับ transactional confirmations
- แผน 3 สเตจ: Pilot (เพจเดียว) → Product → Comment/Live

Related: [[โปรเจกต์ - Thunder Solution|project_thunder_solution]], [[EasySlip API pricing + margin|reference_easyslip_api_pricing]]
