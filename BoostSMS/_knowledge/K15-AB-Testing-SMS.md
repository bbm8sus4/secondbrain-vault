---
source: agent synthesis 2026-07-06
last_verified: 2026-07-06
status: live
---

# K15 · A/B Testing สำหรับ SMS Campaigns

> **TL;DR (EN):** SMS has no open tracking — you can only measure clicks, conversions, replies, and opt-outs. So A/B testing lives on CTR/conversion via **unique short links per variant**. Test one variable at a time: copy (offer framing, CTA, personalization), sender name, send time, link style. Sample size is the catch: at ~10% baseline CTR you need roughly **1,500–2,500 recipients per variant** to reliably detect a 20% relative lift — small lists should only test big, bold differences. Standard play: split 10–20% of the list for the test, wait for significance, blast the winner to the rest.
>
> **สรุป (TH):** SMS ไม่มี open rate ให้วัด — วัดได้แค่ click, conversion, reply, opt-out ดังนั้น A/B test ต้องอาศัย **short link แยกตาม variant** ทดสอบทีละตัวแปร: copy (วิธีเสนอ offer, CTA, ใส่ชื่อ), sender name, เวลาส่ง, รูปแบบลิงก์ จุดตายคือขนาดกลุ่มตัวอย่าง: ที่ CTR ฐาน ~10% ต้องใช้ราว **1,500–2,500 คนต่อ variant** ถึงจะจับ lift 20% ได้จริง list เล็กควรทดสอบเฉพาะความต่างแบบชัด ๆ สูตรมาตรฐาน: แบ่ง 10–20% ของ list มาทดสอบ ได้ผู้ชนะแล้วค่อยยิงที่เหลือ

---

## 1. ทำไม A/B Test ของ SMS ไม่เหมือน Email

| | Email | SMS |
|---|---|---|
| Open rate | ✅ วัดได้ (pixel) | ❌ วัดไม่ได้ |
| Click | ✅ | ✅ (ผ่าน short link) |
| Conversion | ✅ | ✅ (link/โค้ดส่วนลด) |
| Reply | บางระบบ | ✅ (2-way SMS) |
| ต้นทุนต่อข้อความ | ~0 | ฿0.2–0.8 → **ทุก variant มีต้นทุนจริง** |

ผลที่ตามมา 2 ข้อ:
1. **ตัววัดหลักคือ CTR + conversion** — subject line test แบบ email ไม่มีในโลก SMS
2. SMS มีค่าส่งต่อข้อความ → ออกแบบ test ให้เล็กที่สุดที่ยังได้คำตอบ ไม่ใช่ยิงครึ่ง list เล่น ๆ

---

## 2. ทดสอบอะไรได้บ้าง (เรียงตาม impact ที่มักเจอ)

### 1️⃣ Offer / Value Framing (แรงสุด)
- "ลด 50%" vs "ลด ฿500"
- ส่วนลด vs ของแถม vs ฟรีค่าส่ง
- มี deadline vs ไม่มี

### 2️⃣ เวลาส่ง (Timing)
- 10:00 vs 19:00 / วันธรรมดา vs เสาร์-อาทิตย์
- ต้องอยู่ในกรอบ 08:00–21:00 เสมอ → กรอบเวลา + peak ของไทยดู [[K07-Timing-Frequency]]

### 3️⃣ CTA & Link
- "ดูดีล: [link]" vs "รับสิทธิ์: [link]"
- Branded short URL (`s.brand.co/x`) vs generic (`bit.ly/..`)
- ตำแหน่งลิงก์ กลางข้อความ vs ท้ายข้อความ

### 4️⃣ Copy Style
- ใส่ชื่อลูกค้า vs ไม่ใส่ (personalization)
- 1 segment (สั้น 70 ตัว) vs 2 segments (รายละเอียดครบ — แพงขึ้นเท่าตัว คุ้มไหม?)
- Emoji vs ไม่มี / Brand ต้นข้อความ vs ท้าย
- Idea copy เพิ่ม → ตาราง variant ใน [[K03-SMS-Copywriting]]

### 5️⃣ Sender Name
- ชื่อแบรนด์หลัก vs ชื่อ sub-brand (ต้อง approve แล้วทั้งคู่)

### 6️⃣ Segment × Message Fit
- ข้อความเดียวกันกับคนละ segment ผลต่างกันมาก → ออกแบบคู่กับ [[K05-Segmentation-Targeting]]

> **กฎเหล็ก: เปลี่ยนทีละ 1 ตัวแปร** — เปลี่ยนทั้ง offer + เวลา + CTA พร้อมกัน = ชนะก็ไม่รู้เพราะอะไร

---

## 3. ขนาดกลุ่มตัวอย่าง (Sample Size) — จุดที่พลาดกันมากสุด

### หลักคิด
ยิ่ง (ก) baseline ต่ำ และ (ข) ความต่างที่อยากจับเล็ก → ยิ่งต้องใช้คนเยอะ

### ตารางประมาณการ (per variant, 95% confidence / 80% power)

| Baseline CTR | อยากจับ lift | ต้องใช้ ~คน/variant |
|---|---|---|
| 10% | +50% relative (10→15%) | ~350–400 |
| 10% | +20% relative (10→12%) | ~1,800–2,000 |
| 10% | +10% relative (10→11%) | ~7,000+ |
| 5% | +20% relative (5→6%) | ~4,000+ |
| 2% (conversion) | +20% relative | ~10,000+ |

### แปลเป็นภาษาคน
- **List < 2,000:** อย่า test เรื่องจุกจิก — test เฉพาะความต่างใหญ่ (offer คนละแบบ) หรือสะสมผลข้ามหลายแคมเปญ
- **List 5,000–20,000:** test CTR ได้สบาย, test conversion เริ่มไหว
- **Conversion test ต้องการคนมากกว่า CTR test เสมอ** เพราะ base rate ต่ำกว่า
- Rule of thumb เร็ว ๆ: อยากได้ผลที่เชื่อได้ ควรเห็น **คลิกจริง ≥ 100 ครั้งต่อ variant**

---

## 4. โครงสร้าง Test มาตรฐาน (10/10/80)

```
List 20,000 คน
├─ 10% (2,000) → Variant A ┐
├─ 10% (2,000) → Variant B ┤→ วัดผล 2–24 ชม → หา winner
└─ 80% (16,000) → ส่ง winner
```

### เงื่อนไขให้ผลไม่เพี้ยน
- **สุ่มจริง** — ห้ามแบ่งตามลำดับใน list (เบอร์เก่าอยู่ต้น list = bias)
- ส่ง A และ B **เวลาเดียวกัน** (ยกเว้น test เวลา)
- รอให้ครบ window ก่อนตัดสิน — คลิก SMS ~90% เกิดใน 1–3 ชม แรก แต่ conversion อาจลากถึง 24–48 ชม
- ❌ ห้าม "แอบดูแล้วรีบสรุป" (peeking) ตอนข้อมูลยังน้อย — ผลชั่วโมงแรกกลับตาลปัตรได้

### Holdout Group (ขั้น advanced)
- กัน 5% ไม่ส่งอะไรเลย → วัดว่าแคมเปญ **เพิ่มยอดจริง** เท่าไหร่เทียบกับไม่ส่ง (incremental lift)

---

## 5. การวัดผล (Measurement Setup)

### ต่อ variant ต้องแยกให้ได้
| เครื่องมือ | ใช้วัด |
|---|---|
| **Unique short link ต่อ variant** | CTR — หัวใจของทั้งระบบ |
| UTM parameters (`utm_content=varA`) | พฤติกรรมต่อบน web/analytics |
| โค้ดส่วนลดคนละโค้ด (SAVE-A / SAVE-B) | conversion offline/หน้าร้าน |
| เบอร์/keyword ตอบกลับต่างกัน | reply-based campaign |

### Metrics ที่ดูประกอบกัน
- **CTR** = ตัวตัดสินหลัก
- **Conversion rate** = ตัวตัดสินจริงทางธุรกิจ (ถ้า volume พอ)
- **Opt-out rate** = guardrail — variant ที่ CTR ชนะแต่คน opt-out พุ่ง = แพ้
- **Cost per conversion** = สำคัญเมื่อเทียบ 1 vs 2 segments (ต้นทุนต่างเท่าตัว)
- นิยาม + benchmark ของทุกตัว → [[K06-SMS-Metrics-KPIs]]

---

## 6. ตัวอย่าง Test Plan 1 หน้า

```
Test: Offer framing — "ลด 30%" vs "ลด ฿300"
Hypothesis: จำนวนเงินชัด ๆ ทำ CTR ดีกว่า % ในสินค้าราคา ~฿1,000
List: 12,000 (มี consent, ตัด suppression แล้ว)
Split: A 1,800 / B 1,800 / Winner 8,400
ส่ง: อังคาร 10:30 พร้อมกันทั้ง A/B
วัด: CTR ผ่าน s.brand.co/a vs /b · ตัดสินที่ 4 ชม
Guardrail: opt-out ต่าง > 0.3% = ยกเลิกผล
Winner rollout: 19:00 วันเดียวกัน (ยังอยู่ในกรอบ 8–21 น.)
บันทึกผลลง test log ทีม
```

---

## 7. ข้อผิดพลาดที่เจอบ่อย

| ❌ พลาด | ✅ ที่ถูก |
|---|---|
| เปลี่ยนหลายตัวแปรพร้อมกัน | ทีละ 1 ตัวแปร |
| Sample เล็กแล้วสรุปมั่นใจ | เช็คตาราง sample size ก่อนออกแบบ |
| ส่ง A เช้า B เย็น (แต่ตั้งใจ test copy) | ส่งเวลาเดียวกันเสมอ |
| ดู CTR อย่างเดียว | ดู opt-out + conversion ประกอบ |
| ชนะครั้งเดียว = จริงตลอดไป | ผลเสื่อมตามเวลา/ฤดูกาล — re-test ทุก 1–2 quarter |
| ไม่จดผล | เก็บ test log กลาง — learning ทบต้นได้ทั้งทีม |
| Test กับ list ที่ไม่มี consent | compliance มาก่อนเสมอ → [[K14-Compliance-AntiSpam]] |

---

## 8. ลำดับความสำคัญ ถ้าเพิ่งเริ่ม

1. **Offer framing** — ผลแรงสุด เห็นความต่างง่ายสุด
2. **เวลาส่ง** — ฟรี ไม่ต้องแก้ copy
3. **CTA + link style** — ปรับเล็ก ได้ CTR เพิ่มเรื่อย ๆ
4. **Personalization / ความยาว** — เมื่อ volume มากพอให้จับความต่างเล็ก ๆ
5. **Sender name** — นาน ๆ ครั้ง เพราะต้องขึ้นทะเบียนล่วงหน้า

---

## 🔗 อ่านต่อ

- Metrics ที่ใช้ตัดสิน → [[K06-SMS-Metrics-KPIs]]
- เวลา + ความถี่ → [[K07-Timing-Frequency]]
- Idea copy สำหรับ variant → [[K03-SMS-Copywriting]]
- แบ่งกลุ่มก่อน test → [[K05-Segmentation-Targeting]]
- กติกาที่ test ห้ามละเมิด → [[K14-Compliance-AntiSpam]]
