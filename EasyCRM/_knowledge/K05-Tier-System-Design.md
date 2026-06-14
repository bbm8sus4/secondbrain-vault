# K05 · Tier System Design

> **TL;DR (EN):** A good tier system creates "status aspiration" — the *climb* is more motivating than the rewards. 4 tiers max (sweet spot: 3–4). 70/20/8/2 distribution. Each tier needs (1) clear threshold, (2) clear benefit, (3) clear maintenance rule. Avoid "tier inflation" (everyone is Gold = no Gold).
>
> **สรุป (TH):** Tier ที่ดีสร้างแรงจูงใจจาก **การปีนขึ้น** ไม่ใช่แค่รางวัล Sweet spot: 3–4 tier กระจาย 70/20/8/2 แต่ละ tier ต้องชัด 3 อย่าง — เกณฑ์ขึ้น, สิทธิ์ที่ได้, เงื่อนไขรักษาระดับ ระวัง "tier inflation" (ทุกคนเป็น Gold = ไม่มีค่า)

---

## 1. ทำไม Tier ดีกว่า Points อย่างเดียว

| Points อย่างเดียว | Tier System |
|---|---|
| สะสมเพื่อแลก | สะสมเพื่อ **เป็น** |
| Transactional | Identity-based |
| ลูกค้าเลิกใช้ = ไม่มีอะไรเสีย | ลูกค้าเลิกใช้ = เสีย "สถานะ" |
| คู่แข่ง copy ง่าย | สร้าง emotional moat |

> "People will pay more, work harder, and stay longer for status than for money."
> — *Status Game*, Will Storr

---

## 2. โครงสร้าง Tier ที่ EasyCRM ใช้

```
🟢 Green     →  Entry tier (lookup ฟรี)
⚪ Silver   →  พิสูจน์ตัวแล้ว
🟡 Gold     →  ลูกค้าหลัก
🟣 Platinum →  VIP
```

**Sweet spot: 4 tier** — น้อยไปไม่มีอะไรไต่ มากไปงง

---

## 3. การกระจาย Tier (Distribution Pattern)

Best practice (industry data, Bond Brand Loyalty 2024):

| Tier | % ลูกค้า | % รายได้ |
|---|---|---|
| 🟢 Entry (Green) | ~70% | ~10% |
| ⚪ Silver | ~20% | ~25% |
| 🟡 Gold | ~8% | ~35% |
| 🟣 Platinum | ~2% | ~30% |

> **หลักการ:** Top 2% สร้างรายได้ใกล้เคียงกับ 70% ล่าง → ปฏิบัติต่อพวกเขาแบบ VIP จริง

---

## 4. 3 องค์ประกอบของ Tier ที่ดี

### ✅ (1) Threshold ที่ "อยู่ในเอื้อม แต่ต้องเอื้อม"

| Tier | ตัวอย่าง threshold (ค้าปลีก SME) |
|---|---|
| Green | 0 บาท (สมัครฟรี) |
| Silver | ฿2,000 / 6 เดือน |
| Gold | ฿10,000 / 6 เดือน |
| Platinum | ฿30,000 / ปี |

> **กฎ:** จาก tier นี้ไป tier ถัดไป ใช้จ่ายเพิ่ม **3–5 เท่า** ไม่ใช่ 10 เท่า

### ✅ (2) Benefit ที่ "เพิ่มเป็นชั้น ๆ"

| Tier | สิทธิ์ตัวอย่าง |
|---|---|
| Green | ของขวัญต้อนรับ, แต้ม 1:1 |
| Silver | แต้ม 1.2x, ฟรี shipping |
| Gold | แต้ม 1.5x, early access, birthday gift |
| Platinum | แต้ม 2x, dedicated support, exclusive event |

**Tip:** ใส่ **non-monetary perks** (recognition, exclusivity) ด้วย — ไม่ใช่แค่ส่วนลด

### ✅ (3) Maintenance Rule (เงื่อนไขรักษาระดับ)

- **Hard reset** (ทุกปี กลับเป็น Green ทั้งหมด) → จูงใจมาก แต่หยาบ
- **Rolling 12 months** → ใช้จ่ายช่วง 12 เดือนล่าสุด → ดีที่สุด
- **Lifetime tier** → ขึ้น Gold แล้วอยู่ Gold ตลอด → ดีกับลูกค้ารู้สึกผูกพัน แต่ทำให้ inflation

> **Note:** EasyCRM แนะนำใช้ **Rolling 6–12 เดือน** สำหรับ SME

---

## 5. กลไกพิเศษ (Advanced Mechanics)

### 🚀 Tier Boost / Fast Track
- "สมัครแล้วได้ Silver ทันที 3 เดือนแรก"
- ใช้กระตุ้น new customer

### 🔒 Soft Demotion
- เลื่อนลง tier แบบนุ่ม — ส่งแจ้งเตือนก่อน 30 วัน
- "เหลือใช้จ่าย ฿500 จะรักษา Gold ได้"

### 🎉 Surprise & Delight
- ลูกค้า Gold ได้ของแถมโดยไม่บอกล่วงหน้า
- **ดีกว่า** discount เพราะสร้าง emotional spike

### 🎂 Anniversary / Birthday
- Tier benefit + วันเกิด = ROI สูงมาก (response rate 2–5x ปกติ)

---

## 6. ข้อผิดพลาด (Common Mistakes)

| ❌ ผิด | ✅ ถูก |
|---|---|
| Tier 6–7 ระดับ | 3–4 ระดับพอ |
| ทุกคนได้ Gold | กระจาย 70/20/8/2 |
| Benefit ขึ้น tier เท่าเดิม | Step up เป็น exponential |
| สิทธิ์แค่ "ส่วนลด %" | ใส่ status + exclusive |
| ไม่บอก threshold ชัด | UI ที่บอกชัด: "อีก ฿850 = Gold" |
| ตัด tier ทันที | แจ้งเตือนก่อน 30 วัน |
| Tier name น่าเบื่อ | ใช้ชื่อ memorable (Insider/VIB/Rouge ของ Sephora) |

---

## 7. Pattern ที่ใช้ได้ใน EasyCRM (UI / UX)

```
[ฟ้า Tier card]
┌──────────────────────────┐
│  ⚪ Silver Member        │
│  ⭐ 2,340 / 5,000        │
│  ████████░░░░░░ 47%      │
│  อีก ฿2,660 = Gold 🥇    │
│  Gold = แต้ม 1.5x +      │
│  Birthday gift ฿500       │
└──────────────────────────┘
```

> **คีย์:** แสดง progress bar กับ "อีกเท่าไหร่ถึงขั้นถัดไป" → loss aversion + goal gradient effect

---

## 8. Tier Inflation — ปัญหาที่หลายแบรนด์เจอ

> "When everyone is Special, no one is."
> — *The Incredibles*

อาการ:
- 60%+ ของลูกค้าอยู่ Gold ขึ้นไป
- Gold member ไม่รู้สึก "พิเศษ"
- คู่แข่งให้ Gold ง่ายกว่า

วิธีแก้:
1. Tighten threshold (ค่อย ๆ เพิ่ม 10–20%/ปี)
2. เพิ่ม tier ใหม่บนสุด (เช่น Diamond) เฉพาะ top 0.5%
3. เปลี่ยน Hard reset → Rolling 12mo

---

## 🔗 อ่านต่อ

- ดู Tier ของ Starbucks/Sephora → [[K09-Global-Case-Studies]]
- วัดผล Tier → [[K06-Loyalty-Metrics-KPIs]]
- Gamification ของแต่ละ tier → [[K07-Gamification-Octalysis]]
