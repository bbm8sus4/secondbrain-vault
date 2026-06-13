# 01 — EasyBOT Overview

> บอทป้องกันกลุ่ม LINE — **13 ระบบ + 3 ชั้น Member Control** — เริ่ม ฿149/เดือน
> LINE OA: **@easybot**

## ทำไมต้องมี EasyBOT

LINE group **ไม่มีระบบ admin** เหมือน Facebook — ใครก็ลบสมาชิก/เชิญคนนอก/ลบโน้ตได้
"ทัวร์ลง" + "บอทยึดกลุ่ม" = ปัญหาที่เกิดในไทยทุกวัน (เคสมิจฉาชีพ 18 เคสใน ธ.ค. 25 – ก.พ. 26)

## ฟีเจอร์หลัก (13 ระบบป้องกัน)

- กันลบสมาชิก / กันเชิญคนนอก / กันยกเลิกเชิญ
- กรองลิงก์ / QR / รูป / Flex Message / contact card / สติกเกอร์สแปม
- กันแก้โน้ต / อัลบั้ม / โทรในกลุ่ม / แชร์โพสต์
- Whitelist คนสำคัญ + **Blacklist ข้ามทุกกลุ่ม** (จุดที่คู่แข่งไม่มี)
- **Keyword Filter ไม่จำกัดจำนวน** (LINE native จำกัด 200)
- 5-20 บอท/กลุ่ม (คู่แข่ง 1-2 ตัว)

## EasyBOT vs คู่แข่ง

| | EasyBOT | คู่แข่ง |
|---|---|---|
| ฟีเจอร์ | **13 ระบบ** | 5-8 ระบบ |
| ราคาเริ่ม | **฿149/เดือน** | ฿200/เดือน flat |
| Tier | Basic / Premium | Flat เดียว |
| บอท/กลุ่ม | 5-20 | 1-2 |
| Blacklist ข้ามกลุ่ม | ✅ | ❌ |
| Keyword | ไม่จำกัด | ตาม LINE (200) |
| Affiliate | 4 Tiers 15-30% + bonus | flat 20% หรือไม่มี |

**คู่แข่งหลัก:** TopBotLine · NuneBotLine · BotLine88 · KirinBotLine · SiriChan v10 · LINE OA Unlimited

## Technical Moat

- LINE Messaging API อย่างเป็นทางการ **ไม่มี endpoint เตะสมาชิก**
- บอทป้องกันทุกเจ้า (รวม EasyBOT) ใช้ unofficial / selfbot API
- ⚠️ ความเสี่ยง: ละเมิด LINE ToS 4.3 → อาจโดน crackdown
- จับตา: LINE BOT MARKETPLACE (ประกาศใน LINE Conf TH 2025) + Restricted Admin API hint (ต้อง OAuth + 24h cooling-off)

## Source files

- `_source/01_Organization_and_Founding/EasyBOT_Product_Brief.docx`
- `_source/from_gdrive/FAQ_Easy_BOT.docx`
- ดู [[06-Research-Strategy]] สำหรับ market research ฉบับเต็ม
