---
title: EasySlip และ Thunder API
project: facebook-verify
type: reference
tags: [facebook-verify, easyslip, thunder-api, slip-verification, itmx]
updated: 2026-07-15
confidential: true
source_confidence: first-party (document.easyslip.com) — ยืนยันตัวเลขซ้ำก่อนลงทุน
---

# 🏦 EasySlip และ Thunder API

> กลับไป [[00 แผนที่ความรู้ (MOC)]]
> **ข่าวดี: EasySlip API v2 แทบออกแบบมาให้ต่อ Facebook พอดี**

## API หลัก
- **`POST https://api.easyslip.com/v2/verify/bank`** — Bearer token (UUID v4) + **IP whitelist**
- API เดียวปล่อย 2 แบรนด์: `api.thunder.in.th` + `api.easyslip.com` (ตัวเดียวกัน · v2 ปัจจุบัน, v1 legacy)

## รับ input ได้ 4 แบบ
| แบบ | ใช้เมื่อ |
|-----|---------|
| `payload` | สตริง QR (จากการสแกน miniQR) |
| `image` | อัปโหลดไฟล์ (multipart) |
| **`url`** | **ส่ง URL รูป ≤4MB ให้มันไปดึงเอง** ← ต่อ Facebook ง่ายสุด |
| Base64 | ฝัง base64 |

> ฝั่ง Messenger เอา URL จาก webhook ยิงเข้า `url` ตรงๆ **ไม่ต้องโหลดรูปมาเก็บเอง** (ลดภาระ + ลดประเด็น PDPA) · ฝั่ง IG/คอมเมนต์ที่ลิงก์หมดอายุ → ใช้ `image` แบบ pass-through (โหลด-ยิง-ทิ้ง)

## Options ที่ตรงความต้องการร้าน
| option | ทำอะไร |
|--------|--------|
| `checkDuplicate` | กันสลิปซ้ำ (สลิปเก่าเอามาใช้ใหม่) |
| `matchAmount` | เช็คยอดโอนตรงกับออเดอร์ไหม |
| `matchAccount` | เช็คว่าโอนเข้าบัญชีร้านจริง |
| `remark` | หมายเหตุ |

**Output คืน:** `transRef`, `date`, `amount`, sender/receiver (bank + account name), `isDuplicate`, `isAmountMatched`

## เทคโนโลยีตรวจทำงานยังไง
- **ใช้ QR payload เป็นหลัก ไม่ใช่ OCR ล้วน** — สลิปธนาคารมี **miniQR (มาตรฐาน EMVCo/Thai-QR)** ฝังกันปลอม, EasySlip อ่าน payload แล้วตรวจกับธนาคารผ่าน **ITMX** (ระบบกลางธนาคารใต้ ธปท.)
- ถ้า ITMX/ธนาคารล่ม → การตรวจกระทบ (เป็นเคส CS ที่เจอบ่อย)

## ข้อจำกัดที่ต้องรู้
- รองรับ **18+ ธนาคาร**
- **อายุสลิปที่ตรวจได้จำกัด:** KBANK/PromptPay **180 วัน** · SCB/BBL/กรุงศรี **90 วัน** · TrueMoney **30 วัน**
- ต้อง whitelist IP + เก็บ API key ฝั่ง server เท่านั้น (ห้าม client-side)
- ⚠️ **"99.98%" ที่เว็บเคลม = คำโฆษณา ยังไม่มีการวัดอิสระ** — อย่าใช้อ้างอิงจริง
- ⚠️ ทุกตัวกลาง (รวม EasySlip) **พึ่ง bank API** → ธนาคารเปลี่ยน/ล่ม บริการกระทบ

## ราคาที่เปิดสาธารณะ (EasySlip)
- ฿99 / 250 สลิป → ฿40,000 / 320,000 สลิป (~0.11–0.25 บาท/สลิป), ทดลองฟรี 7 วัน
- ช่องทางปัจจุบัน: LINE OA / LINE Group / WooCommerce / API — **ไม่มี Facebook** ← ช่องว่างที่โปรเจกต์นี้เติม
- _⚠️ ตัวเลขการเงินภายใน (ต้นทุน/margin/ราคาทุน) = ความลับ ไม่อยู่ในเอกสารนี้_

## ของที่ Thunder/EasySlip ปล่อยจริงตอนนี้
- LINE chatbot เช็คสลิป · Slip Verification REST API (เรือธง) · ปลั๊กอิน WooCommerce · TrueMoney Wallet verification · n8n community node (`n8n-nodes-easyslip`)
- 💡 **ยังไม่มีตัวไหนเป็น Facebook** — ทุกช่องทางคือ LINE/เว็บ/ปลั๊กอิน

## สถาปัตยกรรมที่เสนอ (Messenger)
```
ลูกค้าส่งสลิปในแชท → Facebook webhook (มี URL รูป) → server เอา URL ยิงเข้า
POST /v2/verify/bank { url, checkDuplicate:true, matchAmount, matchAccount }
→ EasySlip คืนผล → บอทตอบในแชท + อัปเดตออเดอร์
```
→ ดู flow เต็มใน [[02 Flow การทำงาน]]
