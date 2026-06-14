# K02 · RFM Segmentation

> **TL;DR (EN):** RFM = Recency, Frequency, Monetary — the oldest and still most effective customer segmentation. Score each axis 1–5, get a 3-digit code (e.g., 555 = Champion, 111 = Lost). Cheap to compute, easy to act on. EasyCRM uses RFM under the hood for "แคมเปญเฉพาะบุคคล".
>
> **สรุป (TH):** RFM = แบ่งกลุ่มลูกค้าด้วย 3 ตัวเลข — **มาซื้อล่าสุดเมื่อไหร่ × มาซื้อบ่อยแค่ไหน × จ่ายเงินเท่าไหร่** ให้คะแนน 1–5 แต่ละแกน รวมเป็นรหัส 3 หลัก (เช่น 555 = ขั้นเทพ, 111 = หายไปแล้ว) — เป็น "ดาบมือเดียว" ที่ทุก CRM ต้องมี

---

## 1. ที่มา (Origin)

RFM ถูกพัฒนาขึ้นปี **1995** โดย **Jan Roelf Bult** และ **Tom Wansbeek** ในงาน direct mail marketing สมัยก่อน Amazon — ใช้บอกว่า "ควรส่ง catalog ให้ใครก่อน"

ปัจจุบันถูก adopt ไปใช้ใน:
- E-commerce (Amazon, Shopee)
- Loyalty programs (Starbucks, Sephora)
- LINE OA / Chatbot CRM (PointSpot, EasyCRM)
- Banking / Insurance

---

## 2. แกน RFM (3 Axes)

### 🕐 R = Recency
**ลูกค้าซื้อครั้งล่าสุดเมื่อไหร่?** (วันที่ผ่านไปนับจากการซื้อล่าสุด)
- น้อย = ดี (เพิ่งซื้อ → engaged)
- มาก = แย่ (หายนาน → เสี่ยง churn)

### 🔁 F = Frequency
**ซื้อบ่อยแค่ไหน?** (จำนวนครั้งใน period ที่กำหนด, มัก 1 ปี)
- มาก = ดี (loyal)
- น้อย = ไม่ผูกพัน

### 💰 M = Monetary
**ใช้จ่ายรวมเท่าไหร่?** (ยอดรวมใน period)
- มาก = ดี (high-value)
- น้อย = low-value

---

## 3. วิธีให้คะแนน (Scoring)

**วิธีมาตรฐาน: Quintile (แบ่งเป็น 5 กลุ่มเท่ากัน)**

1. เรียงลูกค้าตาม R, F, M แยกกัน
2. แบ่งเป็น 5 quintile → ให้คะแนน 1–5
3. รวมเป็นรหัส 3 หลัก เช่น `R5F4M5`

```
ตัวอย่าง:
ลูกค้า A: ซื้อล่าสุด 2 วัน, 20 ครั้ง/ปี, ฿80,000 → R5 F5 M5 = 555 = Champion
ลูกค้า B: ซื้อล่าสุด 250 วัน, 1 ครั้ง/ปี, ฿200    → R1 F1 M1 = 111 = Lost
```

---

## 4. RFM Segments (กลุ่มมาตรฐาน 11 segments)

> Industry-standard groupings — ใช้กันแพร่หลายในวงการ CRM

| Segment | RFM Code Pattern | กลยุทธ์ที่ใช้ |
|---|---|---|
| 🏆 **Champions** | 5-5-5, 5-5-4 | Reward, ขอ review, recruit เป็น brand ambassador |
| 💎 **Loyal Customers** | 4-5-X, 5-4-X | Upsell premium, exclusive perks |
| ⭐ **Potential Loyalists** | 5-3-X, 4-4-X | สร้าง engagement, แนะนำ membership |
| 🌱 **New Customers** | 5-1-X | Welcome onboarding, ช่วยซื้อครั้งที่ 2 |
| ✨ **Promising** | 4-1-1 | ส่งโปรกระตุ้น, demo product |
| 😴 **Need Attention** | 3-3-3 | Reactivate campaign, แบบสอบถาม |
| 💤 **About to Sleep** | 3-2-X | Limited-time offer |
| ⚠️ **At Risk** | 2-X-5 หรือ 1-5-5 | Win-back campaign (high-value!) |
| 🚨 **Can't Lose Them** | 1-5-5 | คุยตัวต่อตัว, special discount |
| 🛌 **Hibernating** | 1-2-2 | Cheap reactivation email |
| ❌ **Lost** | 1-1-1 | ปล่อย หรือ last-chance campaign |

---

## 5. RFM ในบริบทไทย / Loyalty บน LINE

| ปัญหาทั่วไป | วิธีแก้ |
|---|---|
| **Monetary ไม่ครบ** (เก็บเฉพาะยอดที่ผ่านสลิป) | ใช้ **RF** หรือ **RFE** (E = Engagement บน LINE) |
| **SME เล็กไม่มี data เยอะ** | ลดเป็น 3 quintile (RFM แบบ 1–3) |
| **เริ่มต้นไม่มี baseline** | ใช้ **percentile relative** ของลูกค้าตัวเอง ไม่ใช่ industry |
| **ค้าปลีกแบบ FMCG ที่ซื้อบ่อยจริง** | ปรับ window ของ R ให้สั้นลง (30 วัน แทน 90) |

---

## 6. ข้อจำกัด (Limitations)

- **เป็น lagging indicator** — ดูอดีตอย่างเดียว ไม่ predict อนาคต
- **ไม่นับ context** — ไม่รู้ว่าทำไมลูกค้า churn (ราคา? คุณภาพ? คู่แข่ง?)
- **ไม่นับสินค้า** — ลูกค้าซื้อของแพง 1 ครั้งกับซื้อของถูก 10 ครั้ง อาจ M เท่ากันแต่ profile ต่างกัน
- **ไม่ดี กับลูกค้าใหม่** — F ต่ำเพราะเพิ่งมา ไม่ใช่เพราะไม่ดี

> **แนวทาง modern:** ใช้ RFM + **CLV prediction** (ML model) + **product affinity** → ครบทุกมุม

---

## 7. ต่อยอด: RFM + อื่น ๆ

- **RFM-T** — เพิ่ม Tenure (อายุการเป็นลูกค้า)
- **RFM-E** — เพิ่ม Engagement (interaction บน LINE, click rate)
- **RFM-D** — เพิ่ม Diversity (ความหลากหลายของสินค้า)
- **RFM + Cohort** — ดู RFM แยกตาม cohort ของเดือนที่ลงทะเบียน

---

## 🔗 อ่านต่อ

- คำนวณมูลค่าลูกค้า → [[K03-Customer-Lifetime-Value]]
- ใช้ RFM ผสม Tier → [[K05-Tier-System-Design]]
- KPI ของแคมเปญ → [[K06-Loyalty-Metrics-KPIs]]
