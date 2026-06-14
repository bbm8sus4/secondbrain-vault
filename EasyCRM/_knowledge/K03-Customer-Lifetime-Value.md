# K03 · Customer Lifetime Value (CLV / LTV)

> **TL;DR (EN):** CLV = the total profit a customer generates over their entire relationship with you. Simple version: `(AOV × Purchase Frequency × Gross Margin) / Churn Rate`. Knowing CLV tells you how much you can spend to acquire a customer (CAC ceiling), which segments to invest in, and whether loyalty programs are worth it.
>
> **สรุป (TH):** CLV / LTV = กำไรรวมที่ลูกค้า 1 คนสร้างให้ตลอดการเป็นลูกค้า สูตรง่าย: **(ยอดต่อบิล × ความถี่ × อัตรากำไร) ÷ Churn rate** ใช้ตัดสินใจว่า "จะลงทุนหาลูกค้าใหม่ได้สูงสุดเท่าไหร่" และ "ลูกค้ากลุ่มไหนคุ้มลงทุน"

---

## 1. ทำไม CLV สำคัญ

> 💡 "ถ้าคุณไม่รู้ CLV คุณกำลังเดิน Marketing แบบหลับตา"
> — Peter Fader, Wharton Professor, *Customer Centricity*

3 เหตุผลที่ทุก SME ต้องรู้ CLV:

1. **กำหนด CAC ceiling** — รู้ว่าจะใช้เงินหาลูกค้าใหม่ได้สูงสุดเท่าไหร่ (rule: **CAC < CLV / 3**)
2. **เลือกกลุ่มลงทุน** — Loyalty perks ให้ลูกค้า CLV สูงคุ้มเสมอ ลูกค้า CLV ต่ำคิดให้ดี
3. **Justify โปรแกรม Loyalty** — ROI = (CLV ใหม่ − CLV เดิม) − ต้นทุนโปรแกรม

---

## 2. สูตรพื้นฐาน (Basic Formula)

### 🧮 Simple CLV
```
CLV = AOV × Purchase Frequency × Customer Lifespan
```
- **AOV** = Average Order Value (ยอดเฉลี่ยต่อบิล)
- **Purchase Frequency** = จำนวนครั้ง/ปี
- **Customer Lifespan** = อายุการเป็นลูกค้าเฉลี่ย (ปี)

### 🧮 Profit CLV (ใช้กำไรขั้นต้น)
```
CLV = (AOV × Frequency × Gross Margin %) × Lifespan
```

### 🧮 Discounted CLV (สำหรับ Subscription)
```
CLV = Monthly ARPU × Gross Margin / Churn Rate
```
(หลักการเดียวกับ perpetuity ใน finance)

---

## 3. ตัวอย่างจริง (Thai SME context)

### ☕ ร้านกาแฟ
- AOV = ฿85
- Frequency = 3 ครั้ง/สัปดาห์ × 50 สัปดาห์ = 150 ครั้ง/ปี
- Margin = 60%
- Lifespan = 2.5 ปี

```
CLV = 85 × 150 × 0.6 × 2.5 = ฿19,125
```
→ ลงทุนหาลูกค้าใหม่ได้ถึง **฿6,375 ต่อคน** ก่อนขาดทุน

### 💇 ร้านทำเล็บ
- AOV = ฿800
- Frequency = 1 ครั้ง/เดือน = 12 ครั้ง/ปี
- Margin = 70%
- Lifespan = 1.5 ปี

```
CLV = 800 × 12 × 0.7 × 1.5 = ฿10,080
```

---

## 4. CLV จากมุม Cohort (Cohort-based CLV)

แทนที่จะคำนวณค่าเฉลี่ย ใช้ cohort analysis:

| Cohort | Month 1 | Month 6 | Month 12 | Month 24 |
|---|---|---|---|---|
| Jan 2025 | ฿500 | ฿2,800 | ฿4,500 | ฿7,200 |
| Feb 2025 | ฿520 | ฿2,900 | ฿4,700 | — |
| Mar 2025 | ฿480 | ฿2,750 | — | — |

→ **CLV @ Month 12** = ฿4,500–4,700
→ Project แต่ละ cohort ด้วย retention curve

---

## 5. CLV : CAC Ratio (ตัวชี้วัดสำคัญ)

| Ratio | สถานะ |
|---|---|
| **< 1:1** | 🔴 ขาดทุน — ยิ่งหาลูกค้ายิ่งเจ๊ง |
| **1:1 – 3:1** | 🟡 พอใช้ได้ แต่ขยายช้า |
| **3:1** | 🟢 **ระดับเป้าหมาย** (industry standard) |
| **> 5:1** | 🔵 อาจลงทุน growth ได้มากกว่านี้ |

> **Note:** Saas industry มัก aim ที่ **3:1** ส่วน E-commerce ที่ **3–5:1**

---

## 6. CLV กับ Loyalty Program

CLV เป็นเหตุผลหลักของ Loyalty:

| Lever | ผลต่อ CLV |
|---|---|
| ⬆️ เพิ่ม AOV | Upsell, bundle, premium tier |
| ⬆️ เพิ่ม Frequency | Reward, gamification, surprise gift |
| ⬆️ เพิ่ม Lifespan | ลด churn → ดู [[K13-Retention-Churn]] |
| ⬆️ เพิ่ม Margin | Personalized full-price (ไม่ต้อง discount) |

> **Rule of thumb:** Loyalty program ที่ดี ควรเพิ่ม CLV อย่างน้อย **15–25%**

---

## 7. ข้อระวัง

- **อย่าใช้ค่าเฉลี่ย** — Pareto 80/20 ทำให้ลูกค้า top 20% มี CLV สูงกว่า bottom 20% หลาย 10 เท่า → ใช้ median หรือแยก segment
- **Churn ที่ผันผวน** ทำให้สูตรใช้ไม่ได้ (โดยเฉพาะธุรกิจตามฤดูกาล)
- **Cohort สั้นไป** จะทำให้ CLV ต่ำกว่าจริง — Lifespan ต้องมีข้อมูลอย่างน้อย 12 เดือน

---

## 🔗 อ่านต่อ

- ลด churn → [[K13-Retention-Churn]]
- Loyalty program design → [[K04-Loyalty-Program-Types]]
- KPI Dashboard → [[K06-Loyalty-Metrics-KPIs]]
