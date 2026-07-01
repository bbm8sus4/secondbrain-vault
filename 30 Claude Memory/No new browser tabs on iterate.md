---
name: feedback-no-new-browser-tabs
description: อย่าเปิด browser tab ใหม่ทุกครั้งที่แก้ไฟล์ HTML/dashboard — user มีแท็บเปิดอยู่แล้ว จะ refresh เอง
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6ca654f6-8024-4c1d-9cda-3d23a2f6bf36
---

**อย่าเรียก `open <file>` หรือ `open <url>` ซ้ำๆ ทุกครั้งที่แก้ไฟล์** — user เปิดแท็บ browser ค้างไว้แล้ว จะกด Cmd+R refresh เอง การเปิดแท็บใหม่ทุกครั้ง = แท็บล้น + user รำคาญ

**Why:** ผู้ใช้ complain 2026-07-01 ตอน iterating บน `Pricing-Calculator.html` — ทุก edit ผมรัน `open <file>` เปิดแท็บใหม่ทีละอัน · แท็บสะสม

**How to apply:**
- แก้ไฟล์ HTML local → **ไม่ต้องเปิด** · แจ้ง user "refresh ในแท็บเดิมได้เลย" หรือแค่บอกว่า deploy/edit เสร็จ
- Deploy Cloudflare Pages → **ไม่ต้องเปิด URL** · user refresh แท็บเดิม
- **เปิดครั้งแรกเท่านั้น** (ตอนสร้างไฟล์ใหม่) หรือเมื่อ user บอกชัดเจน ("เปิดให้หน่อย", "ขอดู")
- ถ้าอยากให้ user เช็คตอนแก้เสร็จ → บอก "ลอง refresh ดู" ไม่ใช่ `open`
- ถ้า user เปลี่ยน URL/ไปหน้าอื่น → ถามก่อนว่าจะเปิดไหม อย่าเปิดเอง

Related: [[กติกา - Deploy ใช้ stable URL|feedback_deploy_link]] — deploy link ก็ share ครั้งเดียว ไม่ต้องเปิดทุกครั้ง
