---
title: EasySlip API — Dashboard วิเคราะห์ลูกค้า Top-up 6 เดือน
product: EasySlip > EasySlip API
created: 2026-07-02
type: project / analysis
source: topup 6 เดือน.csv (1 ม.ค. – 30 มิ.ย. 2569)
---

# EasySlip API — Dashboard วิเคราะห์ลูกค้า (Top-up 6 เดือน)

รายงาน + dashboard วิเคราะห์พฤติกรรมการเติมเครดิตของลูกค้า **EasySlip API** 6 เดือน (ม.ค.–มิ.ย. 2569).
ลูกค้าเติมเครดิตเพื่อใช้เรียก API ตรวจสลิป — วิเคราะห์ retention/churn/มูลค่า/การกระจุกตัว.

> **ที่มาไฟล์:** `~/Desktop/topup 6 เดือน.csv` · **ผลลัพธ์:** dashboard 3 หน้า HTML ไฟล์เดียวจบ บน `~/Desktop/`
> **PII:** ไฟล์มีชื่อ+อีเมลลูกค้าจริง 1,250 คน → **ห้าม deploy public โดยไม่มี auth** (gitignored แล้ว)

## ตัวเลขหลัก (ม.ค.–มิ.ย. 2569)

- **ยอดเติมรวม ฿33,639,506** · 6,371 รายการ (สำเร็จทั้งหมด) · ลูกค้า 1,250 คน
- โต **+45%** (ม.ค. ฿4.79M → มิ.ย. ฿6.95M) — โตทุกเดือน
- เฉลี่ย ฿5,280/ครั้ง · **มัธยฐาน ฿1,500** (mean เบ้จากรายใหญ่มาก) · เติมสูงสุด/ครั้ง ฿800,140
- เติมซ้ำ 63.8% · เฉลี่ย 5.1 ครั้ง/คน · เติมทุก ~26 วัน (repeaters) · **จังหวะจริง median 11 วัน**
- ประเภท: อัตโนมัติ (ลูกค้าจ่ายเอง) ฿20.1M / เพิ่มโดยแอดมิน ฿13.5M

## การกระจุกตัว (สำคัญสุด)

- **Gini = 0.888** (กระจุกสุดขั้ว)
- ลูกค้า **Top 1% = 50%** ของรายได้ · Top 10% = 81% · ครึ่งล่าง < 1%
- **บัญชี #1 = ฿10.4M = 31% ของทั้งหมด** (ถ้าเสียรายเดียว รายได้เหลือ ฿23.2M)
- Decile บนสุด (125 คน) = 81% ของรายได้

## นิยาม "ลูกค้าหายไป (Churn)" — คิดจากพฤติกรรมจริง ไม่ใช่เดา

**Churn = เงียบเกิน 60 วัน** นับจากเติมล่าสุด. ตั้งเส้นจาก distribution ของช่องว่างการเติมจริง (5,121 คู่):
- median gap 11 วัน · **96% ของการเติมซ้ำเกิดภายใน 45 วัน · 98% ภายใน 60 วัน** → เกิน 60 แทบไม่กลับ
- (เส้น 90 วันที่เดาตอนแรก = หลวมเกินไป)

**Lifecycle:** Active ≤30 · จับตา(Cooling) 31–45 · เสี่ยงหลุด(At-Risk) 46–60 · หาย(Churn) >60

**แยก churn 2 แบบ (คนละปัญหา):**
- **เคยเติมประจำแล้วเลิก (Lapsed)** = 173 คน · ฿1.14M — retention problem, เจ็บสุด
- **เติมครั้งเดียวแล้วหาย** = 225 คน · ฿349k — onboarding/activation problem

## RFM Segmentation (7 กลุ่ม, ณ 30/6/2569)

| กลุ่ม | คน | % รายได้ | เกณฑ์ |
|---|---|---|---|
| VIP | 122 | **80%** | ยอดสะสม ≥ ฿45,000 (top 10%) + active ≤45 วัน |
| ประจำ (Loyal) | 260 | 11% | เติม ≥5 ครั้ง + active |
| เสี่ยงหลุด (At-Risk) | 52 | — | เงียบ 46–60 วัน |
| ใหม่ (New) | 187 | — | เติมครั้งแรกใน 31 วัน + ≤2 ครั้ง |
| ทั่วไป (Regular) | 197 | — | active, 2–4 ครั้ง |
| เติมครั้งเดียว | 34 | — | เติม 1 ครั้ง (ยังไม่หาย) |
| หาย (Churn) | 398 | — | เงียบ >60 วัน |

## Insight เชิงลูกค้า

- **Cohort churn สูงขึ้นเรื่อยๆ** (เชื่อได้เฉพาะรุ่นสังเกต ≥90 วัน): ม.ค. 38% → ก.พ. 47% → **มี.ค. 54%** = คุณภาพ acquisition/onboarding เดือนหลังแย่ลง
- **Activation 72%** กลับมาเติมครั้งที่ 2 (48% ใน 30 วัน) · window ~46 วัน
- **โตจากจำนวนคน ไม่ใช่ยอดต่อคน** — ARPU คงที่ ~฿10k/เดือน
- ความเสี่ยงจริง = กระจุกที่ VIP/รายใหญ่ ไม่ใช่ churn รายเล็ก (มูลค่า at-risk+dormant แค่ ~5%)
- Engagement span: 55% ยังอยู่ถึง 30 วัน → 36%@90 → ~0@180 · 36% เติมครั้งเดียว
- NRR มิ.ย. 107% · money bridge reconcile กับรายได้จริงทุกเดือน

## Dashboard (3 หน้า, single-file HTML, vanilla JS, no backend)

1. **`topup_dashboard.html`** — ภาพรวมการเงิน (รายได้/trend/รายใหญ่/top customers)
2. **`crm_dashboard.html`** — CRM 6 แท็บ: ภาพรวม · คิวงานวันนี้ · วิเคราะห์ · เจาะลึกทั้งฐาน · รายชื่อลูกค้า · นิยาม
   - Today action queue (localStorage) · early-warning ราย cadence · watchlist รายใหญ่ · activation · money bridge · RFM transition · Lorenz/Gini · decile · RFM grid · cohort LTV · engagement · explorer ค้นหา 1,250 คน (virtualized) · CSV export
3. **`monthly_dashboard.html`** — MoM matrix · เจาะรายเดือน · เทียบ A/B

design: no emoji, light default + dark toggle, ไทย(English) gloss pattern, underline tabs, palette สะอาด

## วิธี regenerate (สคริปต์บน ~/Desktop/)

```
python3 topup_analyze.py     # -> topup_stats.json  (หน้าการเงิน)
python3 crm_analyze.py       # -> crm_stats.json    (RFM/segment/cohort + เขียน CSV topup_customer_lists/)
python3 crm_advanced.py      # -> crm_advanced.json (Today/watchlist/bridge/RFM transition/forecast)
python3 crm_deep.py          # -> crm_deep.json     (Lorenz/Gini/decile/RFM grid/percentiles/LTV curve)
python3 monthly_analyze.py   # -> monthly_stats.json
python3 build_dashboard.py && python3 build_crm_dashboard.py && python3 build_monthly_dashboard.py
```

รายชื่อลูกค้าครบทุกกลุ่ม (พร้อมอีเมล) export เป็น CSV ที่ `~/Desktop/topup_customer_lists/` (lapsed/at-risk/VIP/new/master).

## หมายเหตุ / ข้อควรระวัง
- Churn รายรุ่นเชื่อได้เฉพาะ ม.ค.–มี.ค. (มีเวลาสังเกต ≥90 วัน) · Cohort ม.ค. left-censored
- ตัวเลขทุก aggregate reconcile ที่ ฿33,639,506 (money bridge = รายได้จริงรายเดือน)

---

## อัพเดต 2026-07-02 — คุณภาพการโตรายเดือน + คาดการณ์ + refactor menu

### คำตัดสินรายเดือน (โตจริง/โตหลอก)
| เดือน | รายได้ | ตัดสิน |
|---|---|---|
| ม.ค. | ฿4.79M | ฐานตั้งต้น |
| ก.พ. | ฿5.14M (+7.3%) | ปนๆ · 57% ของส่วนเพิ่มมาจาก whale |
| มี.ค. | ฿5.20M (+1.1%) | **อ่อนสุด** — whale ชั้นรองพักมือพร้อมกัน (jettfx90 −288k, westwood −110k) + contraction −738k · ไม่ใช่ปัญหาลูกค้าใหม่ |
| เม.ย. | ฿5.65M (+8.7%) | **โตหลอก** — 89% ของส่วนเพิ่ม = whale เติมพุ่ง (top-1 กิน 35.4%) |
| พ.ค. | ฿5.89M (+4.2%) | **แข็งแรงจริงสุด** — whale ลด ฿400k แต่รวมยัง +4.2% · ex-whale +17.5% · retention 73.9% สูงสุด · พึ่ง whale น้อยสุด 27.2% |
| มิ.ย. | ฿6.95M (+18%) | ดีจริง (มี lump) — คุณภาพชนะทุกมิติ (ใหม่ 185, ARPU สูงสุด) แต่ 4 บัญชี = 80% ของส่วนเพิ่ม |

### ฐานจริง (ex-top1) โตเร็วกว่ายอดรวม
- ม.ค. ฿3.39M → มิ.ย. ฿4.75M = **+40%** (yeต่อยอดรวม +45.1%)
- เพิ่มเป็นแถวใน MoM matrix แล้ว = ตัด whale ออกเห็นฐานจริง

### คาดการณ์ ก.ค.–ปี 2569
- **ก.ค. 2569: ฿6.6–7.5M** (จุดกลาง ~฿7.2M, +5% ถึง +8% จาก มิ.ย.)
- **ทั้งปี 2569: ~฿75–83M** — อย่า commit 86M+ (ฉากนั้นพึ่ง มิ.ย. ที่มี lump)
- **สัญญาณ mean reversion (r=-0.71):** เดือนไหน whale เติมหนัก เดือนถัดไปมักโตช้า
- **ตัวชี้เดือนดี = ลูกค้าใหม่+winback ของเดือนนั้นเอง** ไม่ใช่ retention
- **ฉากเสี่ยง:** ถ้า whale หายไป = รายได้ปีหาย ~฿19–26M

### Customer-focus view (ในหน้ารายเดือน)
- แผงใหม่ "ลูกค้ามาจากไหนแต่ละเดือน" — stacked bars 3 สี (ใหม่ + กลับมาต่อ + winback)
- 3 การ์ด KPI: ลูกค้าใหม่/เดือน (เฉลี่ย), Winback รวม, ฐาน active โตสุทธิ
- MoM matrix แบ่ง 2 กลุ่ม header: **ลูกค้า** ขึ้นก่อน (users/new/retained/winback/churn_out/net_growth/retention) → **รายได้** ตามหลัง (revenue/ex_top1/txn/avg/arpu) — เล่าเรื่องลูกค้าเป็นตัวเอก รายได้เป็นผลตาม

### Menu refactor (4 หน้า)
- แยกก้อน "สรุปประเด็นสำคัญ" ทุกหน้าออก → รวมเป็นหน้าที่ 4: **`insights_dashboard.html`** (เมนู "สรุป")
- Nav ทุกหน้าตอนนี้: ภาพรวมการเงิน → CRM ลูกค้า → รายเดือน → สรุป (ลำดับเดียวกันหมด)
- ปุ่มโหมดมืด: text "โหมดมืด" → icon moon/sun (40×40) ทุกหน้า
- Grid สมดุล: monthly KPI 6 ใบเปลี่ยน 4-col → 3-col (3+3 ไม่มีใบห้อยเหวิ่น) · ตรงกับความกว้าง 3 การ์ด cfCard ด้านบน
