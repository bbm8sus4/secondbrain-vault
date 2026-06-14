# K04 · Loyalty Program — 6 ประเภท

> **TL;DR (EN):** There are 6 main loyalty program archetypes — Points, Tiered, Paid (subscription), Value-based (mission), Coalition (multi-brand), and Hybrid. Each fits a different business model. EasyCRM is primarily Points + Tiered (the most common SME format).
>
> **สรุป (TH):** Loyalty program หลัก ๆ มี 6 แบบ — แต้ม / ระดับ / สมัครจ่าย / สังคม / กลุ่มแบรนด์ / ผสม EasyCRM = Points + Tiered (รูปแบบที่ SME ไทยใช้กันมากที่สุด)

---

## 1. 🎯 Points Program (โปรแกรมแต้ม)

**หลักการ:** ซื้อ → ได้แต้ม → แลกของรางวัล/ส่วนลด

| ข้อดี | ข้อเสีย |
|---|---|
| เข้าใจง่าย, implement ง่าย | ลูกค้าซื้ออะไรก็ได้แต้ม (ไม่จูงพฤติกรรม) |
| Flexible reward | "point inflation" — สะสมเยอะแต่แลกไม่ได้ |
| วัดผลตรง | ทุกร้านมี → ไม่ unique |

**ตัวอย่าง:** Starbucks Rewards (Stars), The1 Card, Café Amazon

**เหมาะกับ:** ค้าปลีก, F&B, e-commerce — ธุรกิจที่ซื้อบ่อยและซ้ำ

> **EasyCRM = Points + Tiered hybrid** — แต้มผูกกับ Tier (Green/Silver/Gold/Platinum)

---

## 2. 🪜 Tiered Program (ระดับสมาชิก)

**หลักการ:** ใช้จ่ายมาก → เลื่อนขั้น → ได้สิทธิ์มากขึ้น

| ข้อดี | ข้อเสีย |
|---|---|
| สร้าง "aspiration" (อยากเป็น Gold) | คนที่ไม่ถึง tier อาจ disengage |
| Lock-in สูง (กลัวเสียระดับ) | ต้อง balance tier benefit ให้ดี |
| สมาชิก top tier มี CLV สูงมาก | ต้องสื่อสาร tier rules ชัดเจน |

**ตัวอย่าง:** Sephora Beauty Insider (Insider/VIB/Rouge), Nike Membership, สายการบิน (Silver/Gold/Platinum)

**เหมาะกับ:** Beauty, Fashion, Airlines, ธุรกิจ premium

> **ดู [[K05-Tier-System-Design]] สำหรับวิธีออกแบบให้ดี**

---

## 3. 💳 Paid / Subscription Loyalty

**หลักการ:** ลูกค้าจ่ายค่าสมาชิก → ได้สิทธิ์ทันที (ไม่ต้องสะสม)

| ข้อดี | ข้อเสีย |
|---|---|
| Cash flow เข้าก่อน | Hard sell — ต้องคุ้มจริง |
| ลูกค้าเสีย "sunk cost" จึงใช้ต่อ | คนสมัครคือคนซื้อบ่อยอยู่แล้ว |
| ลูกค้า paid spend สูงกว่า 60–70% | Risk: คนสมัครแล้วไม่ใช้ |

**ตัวอย่าง:**
- **Amazon Prime** ($139/ปี → Prime members ใช้จ่าย 2x กว่า non-Prime)
- **Costco** (ค่าสมาชิก $60/ปี → 90%+ ของกำไรมาจากค่าสมาชิก)
- **GrabFood Unlimited** (สมัครรายเดือน → ส่งฟรี)

**เหมาะกับ:** ธุรกิจซื้อบ่อย, ส่งเร็ว, brand strong

---

## 4. 🌱 Value-based / Mission-driven

**หลักการ:** ลูกค้าซื้อ → แบรนด์ทำดี (บริจาค, ปลูกต้นไม้, ลด carbon)

| ข้อดี | ข้อเสีย |
|---|---|
| สร้าง emotional bond | ต้อง "ของจริง" — ไม่งั้นถูกจับเรื่อง greenwashing |
| Gen Z / Millennial ชอบมาก | ROI วัดยาก |
| Differentiation จากคู่แข่ง | ไม่เหมาะกับธุรกิจ commodity |

**ตัวอย่าง:**
- **TOMS** (Buy 1, give 1)
- **Patagonia** (1% for the planet)
- **The Body Shop** (cruelty-free + community trade)

**เหมาะกับ:** Premium brand, lifestyle, audience Gen Z/Millennial

---

## 5. 🤝 Coalition / Multi-brand Loyalty

**หลักการ:** หลายแบรนด์ใช้ระบบแต้มร่วม ลูกค้าสะสมจากร้าน A แลกที่ร้าน B ได้

| ข้อดี | ข้อเสีย |
|---|---|
| Reach กว้าง | Brand identity แชร์กับคู่แข่ง |
| Share cost | Loyalty ไม่ผูกกับแบรนด์เดียว |
| ดึง data partner ได้ | กลไกซับซ้อน |

**ตัวอย่าง:**
- **The 1** (Central Group — Tops, Robinson, Power Buy, Café Amazon …)
- **PTT Blue Card** (PTT + Café Amazon + 7-Eleven บางสาขา)
- **Air Miles** (Canada — หลายแบรนด์)
- **Payback** (Germany)

**เหมาะกับ:** Conglomerate ที่มีหลายแบรนด์ในเครือ

---

## 6. 🔀 Hybrid (ผสม)

**หลักการ:** เอา 2–3 แบบมารวมกัน

ตัวอย่างผสม:
- **Points + Tiered** → EasyCRM, Starbucks, Sephora
- **Paid + Tiered** → Amazon Prime + tier perks
- **Points + Value-based** → ใช้แต้มบริจาคได้

> **Industry trend (2024–2026):** 80%+ ของ loyalty program ใหม่เป็น hybrid — pure points กำลังตาย

---

## 7. 🎮 ทางเลือกอื่นที่กำลังมา (Emerging)

### 🌐 Token / Web3 Loyalty
- ใช้ blockchain เก็บแต้ม ลูกค้าเป็นเจ้าของจริง โอนได้
- ตัวอย่าง: Starbucks Odyssey (NFT), Nike .Swoosh
- **ไทย:** ยังไม่ค่อยมี mass adoption

### 🎯 Behavior-based Loyalty
- ให้รางวัลจาก behavior ไม่ใช่แค่ purchase
- เช่น "ใช้แอป 5 วันต่อกัน +50 แต้ม", "เขียนรีวิว +100 แต้ม"

### 🤖 AI / Personalized Loyalty
- ส่วนลด/สิทธิ์ที่ระบบ AI generate เฉพาะคน
- ตัวอย่าง: Stitch Fix, Sephora's Color IQ

---

## 8. เปรียบเทียบเร็ว (Quick Decision Matrix)

| ธุรกิจ | แนะนำ Loyalty แบบ |
|---|---|
| ร้านกาแฟ / F&B | Points + Tiered (EasyCRM) |
| Beauty / Skincare | Tiered + Birthday perks |
| E-commerce ใหญ่ | Paid (Prime-style) |
| ห้างสรรพสินค้า | Coalition |
| Premium brand | Tiered + Mission |
| SME ทั่วไป | Points อย่างเดียวพอ |
| Subscription product | Hybrid (Paid + Points) |

---

## 🔗 อ่านต่อ

- ออกแบบ Tier ให้ดี → [[K05-Tier-System-Design]]
- วัดผลโปรแกรม → [[K06-Loyalty-Metrics-KPIs]]
- Case study → [[K09-Global-Case-Studies]] · [[K10-Thai-Case-Studies]]
