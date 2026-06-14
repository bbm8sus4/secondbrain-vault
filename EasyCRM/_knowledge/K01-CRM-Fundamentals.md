# K01 · CRM Fundamentals

> **TL;DR (EN):** CRM = system + strategy to manage relationships across the whole customer lifecycle (acquire → engage → convert → retain → advocate). It splits into Operational (sales/service automation), Analytical (data + insights), and Collaborative (cross-channel sync) — modern SME loyalty tools like EasyCRM blend all three.
>
> **สรุป (TH):** CRM ไม่ใช่แค่ระบบ "เก็บข้อมูลลูกค้า" แต่คือ **กลยุทธ์ + เทคโนโลยี** บริหารความสัมพันธ์ตลอดวงจรชีวิตลูกค้า แบ่งเป็น 3 แกน — Operational / Analytical / Collaborative ซึ่ง EasyCRM ครอบทั้งสามแกนผ่าน LINE OA

---

## 1. นิยาม (Definition)

**CRM = Customer Relationship Management**

> "A combination of practices, strategies, and technologies that companies use to manage and analyze customer interactions and data throughout the customer lifecycle."
> — Salesforce definition

| มุมมอง | คำอธิบาย |
|---|---|
| **Strategy** | ปรัชญาที่เอาลูกค้าเป็นศูนย์กลาง (Customer-centric) |
| **Process** | กระบวนการมาตรฐานในการดูแลลูกค้าทุก touchpoint |
| **Technology** | ซอฟต์แวร์ที่เก็บ + วิเคราะห์ + ทำงานอัตโนมัติ |

---

## 2. CRM 3 ประเภท (3 Types of CRM)

### 🔹 Operational CRM
ระบบที่ "ทำงานแทนคน" — Sales force automation, Marketing automation, Service automation
- ตัวอย่าง: ส่ง welcome message อัตโนมัติ, จ่ายแต้มเมื่อสลิปผ่าน, ส่งโปรวันเกิด

### 🔹 Analytical CRM
ระบบ "วิเคราะห์พฤติกรรม" — Data warehouse, OLAP, Dashboards
- ตัวอย่าง: RFM segmentation, Churn prediction, Best customer report

### 🔹 Collaborative CRM
ระบบ "เชื่อมหลายช่องทาง" — Multi-channel communication, Partner network
- ตัวอย่าง: LINE OA + เว็บ + หน้าร้าน ใช้ฐานข้อมูลเดียวกัน

> **💡 EasyCRM** = Operational (auto จ่ายแต้ม) + Analytical (Dashboard + RFM) + Collaborative (LINE OA + Admin Portal + Customer Portal)

---

## 3. Customer Lifecycle / Journey

โมเดลที่ใช้กันแพร่หลายคือ **AARRR (Pirate Metrics)** ของ Dave McClure:

| ขั้น | EN | TH | ตัวอย่างใน EasyCRM |
|---|---|---|---|
| 1 | **A**cquisition | หาลูกค้า | Add LINE OA, สแกน QR |
| 2 | **A**ctivation | ใช้งานครั้งแรก | ลงทะเบียน + ส่งสลิปแรก |
| 3 | **R**etention | กลับมาซ้ำ | สะสมแต้ม, เลื่อนระดับ |
| 4 | **R**eferral | แนะนำเพื่อน | คะแนนแนะนำเพื่อน (Refer-a-friend) |
| 5 | **R**evenue | สร้างรายได้ | แลกของรางวัล + ซื้อซ้ำ |

> **Note:** บางแหล่งใช้ **TOFU/MOFU/BOFU** (Top/Middle/Bottom of Funnel) หรือ **5A** ของ Philip Kotler (Aware → Appeal → Ask → Act → Advocate)

---

## 4. Funnel vs Flywheel

### 🌪 Traditional Funnel (เก่า)
```
   Awareness → Consideration → Decision → Purchase ──▶ ⛓ จบ
```
- ปัญหา: ปฏิบัติต่อลูกค้าเดิมเหมือนจบเกมส์แล้ว
- ไม่จับ momentum ของ referral / word-of-mouth

### 🔄 Flywheel (ใหม่, HubSpot 2018)
```
        ┌──────────┐
   ATTRACT → ENGAGE → DELIGHT
        └──── (loop) ────┘
```
- ลูกค้าเก่า = แรงขับเคลื่อนหาลูกค้าใหม่
- ทุก touchpoint สร้าง momentum (แรงเหวี่ยง) เพิ่ม
- **EasyCRM = เครื่องมือสร้าง Delight stage** (สะสมแต้ม + รางวัล + Tier)

---

## 5. หลักการสำคัญที่ทุก CRM ควรรู้

### 📊 80/20 Rule (Pareto Principle)
> **80% ของรายได้** มาจาก **20% ของลูกค้า** — โฟกัสที่ลูกค้ากลุ่มนี้ผ่าน Tier system + VIP perks

### 💰 5x Rule
> ค่าหาลูกค้าใหม่ (CAC) **แพงกว่า 5–25 เท่า** ของค่ารักษาลูกค้าเดิม
> — Bain & Company research

### 📈 5% Retention = 25–95% Profit
> เพิ่ม retention rate แค่ **5%** อาจดันกำไรเพิ่ม **25–95%**
> — Frederick Reichheld, *The Loyalty Effect*

### ⚖️ Customer-centric > Product-centric
> "เริ่มจาก needs ของลูกค้า แล้วถอยกลับมาที่ product ไม่ใช่กลับกัน"
> — Jeff Bezos, Amazon

---

## 6. คำศัพท์พื้นฐาน (Glossary)

| ศัพท์ | ความหมาย |
|---|---|
| **CAC** | Customer Acquisition Cost — ต้นทุนการได้ลูกค้าใหม่ 1 คน |
| **CLV / LTV** | Customer Lifetime Value — มูลค่าตลอดอายุของลูกค้า ดู [[K03-Customer-Lifetime-Value]] |
| **ARPU** | Average Revenue Per User — รายได้เฉลี่ยต่อลูกค้า 1 คน |
| **Churn Rate** | อัตราการสูญเสียลูกค้า (%/เดือน) |
| **Retention Rate** | อัตราลูกค้าที่ยังอยู่ (%/เดือน) |
| **NPS** | Net Promoter Score — "จะแนะนำเพื่อนไหม?" 0–10 |
| **CSAT** | Customer Satisfaction — % พึงพอใจ |
| **CES** | Customer Effort Score — "ใช้งานยากแค่ไหน?" |
| **MAU/DAU** | Monthly / Daily Active Users |
| **Cohort** | กลุ่มลูกค้าที่ลงทะเบียนช่วงเวลาเดียวกัน |

---

## 🔗 อ่านต่อ

- Segmentation จริงจัง → [[K02-RFM-Segmentation]]
- คำนวณมูลค่าลูกค้า → [[K03-Customer-Lifetime-Value]]
- รักษาลูกค้าเดิม → [[K13-Retention-Churn]]
