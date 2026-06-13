# 06 — Research & Strategy

> Market research 19 พ.ค. 2026 + LINE OA Roadmap + 9bomb affiliate research

## ไฟล์หลัก

ใน `_source/06_Research_and_Strategy/`:

- `EasyBOT_Market_Research_2026-05-19.md` — Market research ฉบับเต็ม
- `EasyBOT_LINE_OA_Roadmap.pdf` + `easybot_line_oa_roadmap.html` — LINE OA Roadmap
- `9bomb-affiliate-research/9bomb-affiliate-research.md` — 9bomb affiliate research
- `9bomb-affiliate-research/api-endpoints.md` — API endpoints reverse-engineered

## ตลาด LINE ไทย (สรุปจาก market research)

| ตัวชี้วัด | ตัวเลข |
|---|---|
| LINE MAU ไทย | 54-56 ล้าน (~80% ประชากร) |
| LINE OpenChat MAU | 20 ล้าน (1 ใน 3 คนไทย) |
| LINE OA ที่ active | 6 ล้านบัญชี |
| Chat commerce 2028 | 1.14 ล้านล้านบาท (CAGR 19.2%) |
| ตลาด Bot ไทย | $125.5M (2024) → $442M (2030), CAGR 23.6% |

**TAM:** ถ้า 1% ของ active ใช้บอทป้องกัน = **240-480 ล้านบาท/ปี**

## Pain Point ที่ตลาดยืนยัน

- LINE group ไม่มี permission system — ใครก็เตะ/เชิญ/ลบสมาชิกได้
- ทรอลทำลายกลุ่มได้ภายใน 3 นาที — ข้อมูลหายถาวร กู้ไม่ได้
- "ทัวร์ลง" + "บอทยึดกลุ่ม" = ปรากฏการณ์ที่รู้กันดี
- มิจฉาชีพ/แก๊งคอลเซ็นเตอร์ใช้ LINE group เป็นช่องทางหลัก
- เยาวชน 17-23 ปี เป็น target (18 เคส ธ.ค. 25 – ก.พ. 26 จาก Thaipoliceonline)

## คู่แข่ง

| คู่แข่ง | ราคา/เดือน | ฟีเจอร์ | จุดเด่น |
|---|---|---|---|
| TopBotLine | ~฿200 | 7-8 ระบบ | ใหญ่สุด หลายประเภท |
| NuneBotLine | ฿200 | 7 ระบบ | รับประกันตลอดชีพ |
| BotLine88 | ฿200 | 7+ ระบบ | 2 แอดมิน/กลุ่ม |
| KirinBotLine | ฿150-300 | บางตัวฟรี | ขาย Netflix/YouTube ด้วย |
| SiriChan Bot v10 | ฿200-250 | 10 ระบบ | Weebly site |
| LINE OA Unlimited | ไม่เปิดเผย | ? | broadcast + บอทป้องกัน |

→ EasyBOT ชนะที่ feature count (~2 เท่า) + ราคาเริ่ม ฿149 ถูกกว่า แต่ยังไม่มี dashboard ที่เป็น differentiator ชัด

## Technical Moat

- LINE Messaging API ทางการ **ไม่มี endpoint เตะสมาชิก**
- ทุกเจ้าใช้ unofficial API / selfbot — moat แต่เสี่ยง crackdown
- จับตา: **LINE BOT MARKETPLACE** (ประกาศ LINE Conf TH 2025), Restricted Admin API hint (OAuth 2.0 + 24h cooling-off), LINE MINI App, LINE Notify ปิด 31 มี.ค. 2025

## บทเรียนจาก Discord Moderation Bots

| บอท | ราคา | บทเรียน |
|---|---|---|
| MEE6 | $6.49-11.95/m | Freemium ได้ผล แต่ paywall เยอะ = เสีย reputation |
| Dyno | $4.99/m | Free tier ดีสุด, automation 64% |
| Carl-bot | Free + premium | auto-mod, reaction roles เด่น |

→ **Freemium ได้ผลจริง** — ฟรี basic, เก็บเงิน premium

## 9bomb Affiliate Research

API endpoints ของ 9bomb ที่ reverse-engineered ไว้อยู่ที่ `_source/06_Research_and_Strategy/9bomb-affiliate-research/api-endpoints.md`
