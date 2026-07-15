---
title: ช่องทาง Facebook และนโยบาย Meta
project: facebook-verify
type: reference
tags: [facebook-verify, meta-policy, channels, permissions, webhook]
updated: 2026-07-15
confidential: true
source_confidence: high (เอกสารทางการ Meta + ตรวจสอบไขว้ 3 เสียง)
---

# 📘 ช่องทาง Facebook และนโยบาย Meta

> กลับไป [[00 แผนที่ความรู้ (MOC)]]
> ⚠️ ข้อมูล ณ ก.ค. 2026 — **Meta เปลี่ยนกฎบ่อย** verify ซ้ำก่อนลงมือจริง

## 4 ช่องทางที่รับรูปสลิปได้ (ดีสุด → ยากสุด)

### 🟢 A — Messenger Bot (แชทอินบ็อกซ์) ← แนะนำที่สุด
- ลูกค้าส่งรูปสลิปเข้าแชท → webhook event `messages` มี attachment รูป
- payload: `{ "type":"image", "payload":{ "url":"..." } }`
- **Meta บอกเองให้ "capture and store any webhook payload content that you want to keep"** → ฝั่ง Messenger เก็บ/ประมวลผลรูปได้ ไม่ติดข้อห้าม
- สิทธิ์: `pages_messaging` + `pages_manage_metadata`
- ✅ ควบคุมได้เต็ม, รูปเข้าถึงได้, ตรง use case "transactional confirmations"

### 🟡 B — ตอบใต้คอมเมนต์ (Comment → Private Reply)
- คอมเมนต์มาในรูป webhook field **`feed`** (item=`comment` — ไม่มี field `comments` แยก)
- ⚠️ รูปในคอมเมนต์ **webhook มักไม่ส่ง URL ตรงๆ** — ต้องยิง Graph API เพิ่ม: `GET /{comment-id}?fields=attachment` → `data.attachment.media.image.src`
- ⚠️ **CDN อาจย่อขนาดรูป** → กระทบการอ่าน QR/OCR — ต้องเทสต์จริง
- ⚠️ URL รูป **หมดอายุ** (signed CDN link) — ต้องรีบดึง/ยิงเข้า EasySlip ทันที
- **ตอบกลับ Private Reply:** ได้แค่ **1 ข้อความ ภายใน 7 วัน เป็น text ล้วน** (แนบรูปไม่ได้) — พอแจ้งผล คุยต่อได้เมื่อลูกค้าตอบ (เปิดกรอบ 24 ชม.)
- สิทธิ์: `pages_manage_metadata` + `pages_messaging` (+ อาจ `pages_manage_engagement`/`pages_read_user_content`)

### 🟡 C — Facebook Live (คอมเมนต์สด)
- ต่อยอดจาก B — ช่วงไลฟ์ขายของ ลูกค้าโอนแล้วส่งสลิปใต้ไลฟ์
- ⚠️ volume พุ่งสูง ต้องระวัง rate limit + ลิงก์รูปหมดอายุเร็ว

### 🔴 D — Instagram Messaging (แถม)
- IG วิ่งบน Messenger Platform เดียวกัน — DM รูปสลิป (png/jpeg ≤8MB) มาเป็น `{type:"image", payload:{url}}` กรอบ 24 ชม. เดียวกัน
- Private Reply: 1 ข้อความ ภายใน 7 วัน
- ⚠️ **รูปแบบ "view-once/ephemeral" ของ IG มาโดยไม่มี url** → ต้องบอกลูกค้าส่งรูปปกติ
- ⚠️ IG **ห้าม download/retain/store + ห้าม circumvent expiry** (เข้มกว่า Messenger) — รูปมาจาก `lookaside.fbsbx.com/ig_messaging_cdn`
- สิทธิ์เพิ่ม: `instagram_basic` + `instagram_manage_messages`

## นโยบาย/ข้อจำกัด Meta ที่กระทบ

### ✅ ทำได้
- **ยืนยันธุรกรรม/ชำระเงิน** — `pages_messaging` ระบุ use case "transactional confirmations" ตรงตัว
- **เก็บ webhook payload ฝั่ง Messenger ได้** — Meta แนะนำให้เก็บเอง

### ⚠️ เงื่อนไข
1. **App Review + Business Verification** — เทสต์บนเพจเราเอง (admin/tester) ไม่ต้อง review; รับลูกค้าจริง multi-tenant → ต้อง Advanced Access = บังคับทั้ง App Review + Business Verification (+อาจ Data Protection Assessment) → คอขวด เริ่มเนิ่นๆ
2. **message tag เดิมตายแล้ว** — `POST_PURCHASE_UPDATE`, `CONFIRMED_EVENT_UPDATE`, `ACCOUNT_UPDATE` **ยกเลิก 27 เม.ย. 2026** (ยิงแล้ว error 100) → ตัวแทนคือ **Utility Messages / Utility Templates** เปิดใช้ในไทยแล้ว (ไทย/ฟิลิปปินส์/สหรัฐฯ/เวียดนาม), ต้องมีสิทธิ์ `page_utility_messaging`, template อนุมัติในไม่กี่วินาที, **ห้ามมีเนื้อหาการตลาด**, ส่งนอก 24 ชม. ได้
3. **กรอบ 24 ชม. (Standard Messaging Window)** — ตอบฟรีได้ใน 24 ชม. หลังลูกค้าทัก; เกินนั้นใช้ Utility Message หรือ Human Agent tag (7 วัน). งานตรวจสลิปเกิดในไม่กี่นาที → อยู่ในกรอบอยู่แล้ว
4. **Meta Platform Terms** (อัปเดต ก.พ. 2026) — ต้องลบ Platform Data (รวมรูปสลิป) "ทันทีที่ทำได้" เมื่อไม่จำเป็น (Sec 3.d); ในฐานะ "Tech Provider" ประมวลผลได้ "ในนามและตามคำสั่งของร้านค้าเท่านั้น" + แยกข้อมูลรายร้าน (Sec 5.b) → ดู [[09 กฎหมาย ความเสี่ยง และคำถามเปิด]]

## Rate limit + webhook
| API | เพดาน (ต่อ 24 ชม.) |
|-----|-----|
| Messenger | 200 × จำนวน engaged users |
| Pages (page token) | 4,800 × จำนวน engaged users |
| IG private replies (live) | 100 ครั้ง/วินาที |

- ⏱️ **webhook ต้องตอบ HTTP 200 ภายใน 5 วินาที** ไม่งั้นถูกตัด subscription
- _⚠️ ตัวเลข rate limit ยังไม่ได้ cross-verify รอบสอง — เช็คใหม่ตอนออกแบบจริง_
