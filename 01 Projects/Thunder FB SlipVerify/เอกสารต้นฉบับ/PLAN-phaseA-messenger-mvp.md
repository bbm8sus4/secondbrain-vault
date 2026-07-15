---
title: แผนสร้าง Product ตรวจสลิปใน Facebook — Messenger (Pilot → Product) + outline คอมเมนต์/ไลฟ์
project: facebook-verify (Thunder Solution)
decision: วุทธเลือก "ทำแนวทาง A (Messenger) ก่อน B (คอมเมนต์/ไลฟ์) ตาม" + "เริ่มแบบ Pilot เพจเดียวก่อน" (2026-07-09)
status: DESIGN — รอ approve · ยังไม่เขียนโค้ด
based_on: RESEARCH-facebook-slip-verify.md
---

# 🏗️ แผนสร้างบอทตรวจสลิปใน Messenger

> **โครง 3 stage:**
> • **Stage 1 — Pilot เพจเดียว** _(เริ่มทันที ไม่ต้องรอ Meta review)_ ← ทำอันนี้ก่อน
> • **Stage 2 — ขยายเป็น Product multi-tenant** _(ร้านหลายเจ้าเชื่อมเพจตัวเอง — ต้อง App Review)_
> • **Stage 3 — คอมเมนต์/ไลฟ์/IG** _(แนวทาง B ในรายงานวิจัย)_
>
> **เป้าหมาย Stage 1 (Pilot):** พิสูจน์ให้เห็นจริงว่า *สลิปเข้าแชทเพจ → บอทตรวจถูก → ตอบผลถูก → กันซ้ำได้* บนเพจของเราเอง 1 เพจ

---

## 🎯 Stage 1 — Pilot เพจเดียว (โฟกัสตอนนี้)

**ทำบนเพจของเราเอง 1 เพจ** (เพจ Thunder/EasySlip หรือเพจร้านตัวอย่าง) — จุดประสงค์คือพิสูจน์ flow ให้เห็นกับตา ยังไม่ใช่ของขาย

**ทำไม pilot ไม่ต้องรอ Meta review:** ทดสอบด้วยบัญชี admin/tester ของแอปเราเอง (Standard Access) ส่งสลิปทดสอบเข้าเพจตัวเอง — ไม่ต้องขอ Advanced Access จนกว่าจะรับลูกค้าจริง (= Stage 2)

**สิ่งที่ต้องทำใน pilot (ผอมสุด):**
- สร้าง Facebook App + เอา **Page Access Token ของเพจเราเอง** (ผ่าน App Dashboard — ไม่ต้องทำ OAuth onboarding)
- subscribe เพจเข้า webhook `messages`
- Webhook receiver → เรียก **EasySlip API (key เดิมที่มีอยู่)** → ตอบผลในแชทด้วย Send API
- ตรวจครบ: กันซ้ำ + เช็คยอด + เช็คบัญชี
- ดูผลจาก log ตรงๆ (ยังไม่ต้องมี dashboard)

**สิ่งที่ยัง _ไม่_ ทำใน pilot:** OAuth/onboarding หลายร้าน · App Review · Business Verification · billing per-merchant · dashboard · คอมเมนต์/ไลฟ์/IG → ทั้งหมดนี้ไป Stage 2-3

**เกณฑ์ว่า pilot สำเร็จ:** ส่งสลิปจริง 10-20 ใบ (มีทั้งของจริง/ปลอม/ซ้ำ/ยอดผิด) แล้วบอทตอบถูกทุกเคส + หน่วงเวลารับได้

---

## ⚙️ Assumption ที่ตั้งไว้ (โปรดยืนยัน/แก้)
1. **reuse ของเดิมของ Thunder** — ใช้ EasySlip/Thunder Slip Verification API + key/โควตาที่มีอยู่ ไม่สร้าง engine ใหม่
2. **มีทีม dev พร้อม** — แผนนี้เขียนระดับ "สถาปัตยกรรม + ลำดับงาน" ให้ทีม dev รับไปทำต่อ
3. **Pilot ใช้เพจของเราเอง 1 เพจ** — มีเพจที่ใช้ทดสอบได้
4. **นิติบุคคล Thunder เป็นผู้ยื่น App Review** ตอนขึ้น Stage 2 (มีบริษัทจดทะเบียนแล้ว)

---

## 📦 Stage 2-3 (ภาพรวม — ทำหลัง pilot ผ่าน)
ด้านล่าง (ข้อ 1-8) คือสถาปัตยกรรม **เต็ม** ของ product multi-tenant — Stage 1 pilot ใช้แค่ core (component 2,3,4 + EasySlip) ส่วนที่เหลือ (OAuth, dashboard, billing per-merchant, App Review) เพิ่มตอน Stage 2

---

## 1. สถาปัตยกรรมภาพรวม

```
[ร้านค้า] --เชื่อมเพจผ่าน Facebook Login--> [ระบบเรา เก็บ Page Access Token]

[ลูกค้าปลายทาง] --ส่งรูปสลิปในแชทเพจร้าน-->
   [Meta] --webhook "messages" (มี url รูป)--> [Webhook Receiver ของเรา (1 endpoint รับทุกเพจ)]
      → ระบุว่าเป็นเพจร้านไหน (page_id) → ดึง config ร้าน (บัญชีปลายทาง, โควตา)
      → ตอบ Meta 200 ภายใน 5 วิ + โยนงานเข้า queue
   [Verification Worker]
      → ยิง EasySlip: POST /v2/verify/bank { url, checkDuplicate, matchAccount, matchAmount }
      → ได้ผล (ยอด/บัญชี/ซ้ำไหม/ตรงไหม)
      → ตอบลูกค้าในแชท (Send API) + อัปเดตสถานะ + หักโควตา (billing เดิม)
      → เก็บ log ธุรกรรม (ไม่เก็บรูปถาวร — ตาม Platform Terms/PDPA)
```

**หลักคิด:** งานหนัก (เรียก EasySlip) ต้องไม่ค้าง webhook — รับ webhook แล้วตอบ 200 ทันที โยนเข้า queue ให้ worker ทำ (เพราะ Meta บังคับตอบใน 5 วิ)

---

## 2. องค์ประกอบระบบ (แต่ละตัวมีหน้าที่เดียว ชัดเจน)

| # | Component | หน้าที่ | พึ่งพา |
|---|-----------|--------|--------|
| 1 | **Merchant Onboarding (OAuth)** | ร้านล็อกอิน Facebook, ขอ permission, เก็บ+รีเฟรช Page Token, subscribe เพจเข้า webhook ของแอป | Facebook Login, Graph API |
| 2 | **Webhook Receiver** | รับ event ทุกเพจที่ 1 endpoint, verify signature (`X-Hub-Signature-256`), แยกตาม page_id, ตอบ 200 เร็ว, push เข้า queue | Meta webhook |
| 3 | **Verification Worker** | ดึงรูป/URL, เรียก EasySlip API, ตีความผล (ซ้ำ/ยอด/บัญชี), retry เมื่อ bank API ล่ม | EasySlip API, queue |
| 4 | **Reply / Notify** | ตอบผลในแชทด้วย Send API (ในกรอบ 24 ชม.); เผื่อ Utility Message นอกกรอบ | Send API |
| 5 | **Merchant Dashboard** | ร้านเชื่อมเพจ, ตั้งบัญชีปลายทาง (ไว้ matchAccount), ดูประวัติ+โควตา — extend portal เดิม | ระบบเดิม Thunder |
| 6 | **Billing/Quota** | หักโควตาต่อการตรวจ, reuse pre-paid เดิม | ระบบเดิม Thunder |
| 7 | **Data handler** | pass-through รูป (ไม่เก็บถาวร), เก็บเฉพาะ metadata จำเป็น, ลบตามกำหนด | — |

---

## 3. ขอบเขต MVP (YAGNI — ตัดให้ผอมที่สุดที่ยัง "ขายได้")

### ✅ อยู่ใน MVP
- Onboarding: ร้านเชื่อม **1 เพจ** ผ่าน Facebook Login
- รับสลิปในแชท → ตรวจ → **ตอบผลในแชท**
- ตรวจครบ 3 อย่าง: กันซ้ำ (`checkDuplicate`) + เช็คยอด (`matchAmount`) + เช็คบัญชีปลายทาง (`matchAccount`)
- หักโควตา (reuse billing เดิม)
- Dashboard ขั้นต่ำ: เชื่อมเพจ + ตั้งบัญชีร้าน + ดูประวัติ/โควตา

### ❌ ยังไม่ทำใน MVP (ไว้เฟสถัดไป)
- คอมเมนต์ใต้โพสต์ / ไลฟ์ → **= เฟส B**
- Instagram DM
- หลายเพจต่อร้าน, รายงานเชิงลึก, ตั้งค่าข้อความตอบแบบซับซ้อน
- Utility Message (ตอบนอก 24 ชม.) → **optional** ใส่ถ้าจำเป็น (งานตรวจสลิปเกิดในไม่กี่นาที อยู่ในกรอบ 24 ชม. อยู่แล้ว)

---

## 4. 🔴 Stage 2 — งานคอขวดที่ต้องเริ่มขนานแต่เนิ่นๆ (Critical Path)
_(ไม่ต้องรอสำหรับ pilot Stage 1 — แต่พอตัดสินใจไป Stage 2 ต้องเริ่มทันทีเพราะรออนุมัตินาน)_

**(ก) เคลียร์ฐานกฎหมาย/นโยบายก่อนลงทุนหนัก**
- ยืนยันว่าเงื่อนไขบริการ EasySlip/Thunder + ข้อตกลงกับ ITMX/ธนาคาร **รองรับ use case "บน Facebook"** (KBank ห้ามร้าน social media ต่อ API ตรง — เราเป็นตัวกลาง แต่ต้องมั่นใจว่าโมเดลตัวกลางครอบ Facebook ได้)
- PDPA: เตรียมนโยบายความเป็นส่วนตัว + ฐานการประมวลผลข้อมูลสลิป

**(ข) Business Verification + App Review (เริ่มขนานวันแรก)**
- ทำ **Business Verification** ด้วยเอกสารบริษัท Thunder Solution
- ขอ **Advanced Access** สิทธิ์: `pages_show_list`, `pages_manage_metadata`, `pages_messaging`, `pages_read_engagement`, `business_management`
- เตรียม: วิดีโอ use-case, privacy policy, แอปที่ทดสอบได้จริงบนเพจ dev
- ⚠️ อันนี้กินเวลารออนุมัติ — **ยิ่งเริ่มเร็วยิ่งดี** (build core ไปพร้อมกันได้ ไม่ต้องรอ review เสร็จก่อน)

---

## 5. ลำดับงาน (Milestones)

1. **เคลียร์กฎหมาย + เริ่ม Business Verification** _(ขนาน, เริ่มทันที)_
2. **Build core บนเพจ dev ของเราเอง** — webhook + เรียก EasySlip + ตอบในแชท _(ไม่ต้องรอ review; ทดสอบด้วย tester ได้)_
3. **Merchant onboarding (OAuth) + Dashboard ขั้นต่ำ**
4. **ยื่น App Review** พร้อม demo ที่ทำงานจริง
5. **Closed beta** กับร้านจริง 2-3 ร้าน (หลัง Advanced Access ผ่าน)
6. **เปิดตัว** + เก็บ feedback

_ลำดับนี้เอา "งานที่ไม่ต้องรอ Meta" (ข้อ 2-3) มาทำระหว่างรอ review (ข้อ 1,4) → ไม่เสียเวลาเปล่า_

---

## 6. การรับมือข้อมูล (PDPA + Meta Platform Terms)
- **รูปสลิป = pass-through** — ส่ง URL/รูปเข้า EasySlip แล้ว **ไม่เก็บรูปถาวร**
- เก็บเฉพาะ metadata ที่จำเป็นต่อธุรกิจ (transRef, ยอด, สถานะ, เวลา) เพื่อกันซ้ำ/ตรวจสอบ
- ลบข้อมูลเมื่อไม่จำเป็น + รองรับคำขอลบ (Meta/ผู้ใช้)
- ในฐานะ "ผู้ประมวลผลแทนร้านค้า" — แยกข้อมูลรายร้าน ไม่เอาไปใช้ประโยชน์อื่น

---

## 7. การทดสอบ
- **Unit:** ตรรกะตีความผล EasySlip (ซ้ำ/ยอดไม่ตรง/บัญชีผิด/สลิปหมดอายุ)
- **Integration:** เรียก EasySlip (sandbox/mock), จัดการ error (bank API ล่ม, quota หมด, รูปเสีย)
- **Webhook:** verify signature, ตอบ 200 ใน 5 วิ, กัน event ซ้ำ
- **E2E:** ส่งสลิปจริงในแชทเพจ dev → เห็นผลตอบกลับถูกต้อง + โควตาถูกหัก

---

## 8. Stage 3 — คอมเมนต์/ไลฟ์/IG (outline — แนวทาง B ในรายงานวิจัย, ทำหลัง Messenger นิ่ง)
- เพิ่ม subscribe webhook field **`feed`** (คอมเมนต์) — ⚠️ รูปคอมเมนต์ต้องเรียก Graph API เพิ่ม 1 ครั้ง (`GET /{comment-id}?fields=attachment`), ระวัง CDN ย่อรูป
- ตอบด้วย **Private Reply** (1 ข้อความ, ภายใน 7 วัน, text-only) เด้งลูกค้าเข้าแชท → เข้า flow เดิมของเฟส A
- รองรับ **Facebook Live** (volume พุ่ง ต้องเทสต์ load)
- ต่อยอด **Instagram DM** (reuse core, เพิ่มสิทธิ์ IG)
- reuse component 2-7 ของเฟส A ได้เกือบทั้งหมด (เปลี่ยนแค่ "ทางเข้า" ของรูป)

---

## ❓ จุดที่อยากให้วุทธ/ทีมยืนยัน (สำหรับ Pilot Stage 1)
1. Assumption ข้อ 1-4 — reuse API/key เดิม, ใช้เพจเราเอง 1 เพจ, มีทีม dev — โอเคไหม
2. เพจไหนใช้ทำ pilot (เพจ Thunder / EasySlip / เพจร้านตัวอย่าง)
3. มี key + โควตา EasySlip ให้ dev ใช้ทดสอบเลยไหม
4. Pilot นี้อยากให้ dev เริ่มเลย หรือรอ approve แผนก่อน (ตอนนี้ผม standby ไม่เขียนโค้ด)
