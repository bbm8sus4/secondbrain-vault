---
brand: EasySlip
type: revenue-report
period: 2569-01 to 2569-05
created: 2026-06-12
source: https://thunder-revenue-report.pages.dev/
---

# EasySlip — Revenue Report ม.ค.–พ.ค. 2569

## สรุปรวม EasySlip Brand

| Month | Revenue (฿) | MoM | Jan→Month |
|-------|-------------|------|-----------|
| มกราคม | 4,976,692 | — | — |
| กุมภาพันธ์ | 5,244,288 | +5.4% | +5.4% |
| มีนาคม | 5,325,680 | +1.6% | +7.0% |
| เมษายน | 5,391,009 | +1.2% | +8.3% |
| **พฤษภาคม** | **6,417,845** | **+19.0%** | **+29.0%** |

**สัดส่วนในกลุ่ม (พ.ค.):** 55.7% ของรายได้ทั้งกลุ่ม (แบรนด์ใหญ่กว่า Thunder)

---

## EasySlip API (Core Revenue Engine)

| Month | Revenue (฿) | MoM | Jan→Month | % ของ EasySlip |
|-------|-------------|------|-----------|----------------|
| มกราคม | 4,792,380 | — | — | 96.3% |
| กุมภาพันธ์ | 5,144,094 | +7.3% | +7.3% | 98.1% |
| มีนาคม | 5,202,141 | +1.1% | +8.6% | 97.7% |
| เมษายน | 5,248,614 | +0.9% | +9.5% | 97.3% |
| **พฤษภาคม** | **6,257,833** | **+19.2%** | **+30.6%** | **97.5%** |

**% ของกลุ่มทั้งหมด (พ.ค.): 54.3%** — สินค้าตัวเดียวกินรายได้ครึ่งกลุ่ม

```
Jan: ████████████ 4.79M
Feb: ███████████░ 5.14M (+7%)
Mar: ███████████░ 5.20M (+1%)
Apr: ███████████░ 5.25M (+1%)
May: ████████████░ 6.26M (+19%)
↑ Consistent monthly growth, no erosion
```

⚠️ **CONCENTRATION RISK** — ก้อน ฿6.26M/เดือนกระจุกตัวที่ EasySlip API คนเดียว ถ้า top-3 ลูกค้าหลุดเป้าพัง

---

## EasySlip BOT (Secondary Product)

| Month | Revenue (฿) | MoM | Jan→May |
|-------|-------------|------|---------|
| มกราคม | 176,796 | — | — |
| กุมภาพันธ์ | 145,476 | −17.7% | −17.7% |
| มีนาคม | 167,259 | +15.0% | −5.4% |
| เมษายน | 169,038 | +1.1% | −4.4% |
| **พฤษภาคม** | **200,827** | +18.8% | **+13.6%** |

---

## BoostSMS (Flat/Dormant)

| Month | Revenue (฿) | Status |
|-------|-------------|--------|
| ม.ค.–พ.ค. | ~12,908 | 0% (flat fee) |

⚠️ **ตลอด 5 เดือนยอดเท่าเดิม** = น่าจะเป็น flat fee ไม่ใช่ metered → ต้องตัดสินใจ **reprice หรือ kill**

หมายเหตุ: BoostSMS มี knowledge base แยกที่ [[../../BoostSMS/หน้าหลัก|BoostSMS folder]]

---

## Key Insights — EasySlip

1. **EasySlip API = เครื่องปั๊มเงินหลักของทั้งกลุ่ม** (54% ของรายได้รวม)
2. **Concentration เพิ่มขึ้น** — % ใน EasySlip ขึ้นจาก 96.3% → 97.5% (Jan→May)
3. **Steady power engine** — โตทุกเดือน ไม่มีถดถอย
4. **Spike พ.ค.** — EasySlip API contribute +฿1,009,219 ของ MoM growth (ใหญ่สุดในกลุ่ม)
5. **EasySlip BOT** — มี momentum (+13.6% YTD) แต่ขนาดเล็ก
6. **BoostSMS dormant** — ตัดสินใจ reprice/kill

---

## ⚠️ Critical Risks — EasySlip

### 1. Single-point-of-failure (กระจุกตัวสูงมาก)
- EasySlip API = 97.5% ของแบรนด์
- = 54.3% ของกลุ่มทั้งหมด
- **ลูกค้า top-3 crisis เดียว = พลาดเป้าทั้งปี**

### 2. Spike พ.ค. น่าสงสัย
- 85% ของ growth พ.ค. มาจาก API 2 ก้อน
- อาจเป็น **prepay รายปี** ไม่ใช่ recurring
- ต้อง validate ก่อน lock forecast

### 3. Sub-segment Reconciliation Issue
- Reported EasySlip พ.ค.: ฿6,417,845
- Component sum: ฿6,471,568
- **Variance: +฿53,723** (ยังไม่ reconcile)

---

## Critical Action Items — EasySlip

1. **Week 1:** Validate May spike — recurring vs one-off prepay
2. **Week 1:** Map customer concentration ของ EasySlip API (top-10 %)
3. **This month:** Unit economics audit (margin pressure check)
4. **This quarter:** BoostSMS — reprice หรือ kill
5. **Post-validation:** Re-forecast ก่อน commit ตัวเลข board

---

## Context: Group-Level (ทั้งสองแบรนด์รวม)

- รวม 5 เดือน: **฿51,002,710** | เฉลี่ย ฿10.2M/เดือน
- เป้าปี: **฿125M** (YTD 40.8%) → ต้องเฉลี่ย ฿10.57M/เดือนในอีก 7 เดือน
- พ.ค. 69 สูงสุดในรอบ 5 เดือน: ฿11,523,721

### Scenario Projections (ทั้งปี 2569)

| Scenario | Monthly Assumption | Year-End | % เป้า ฿125M |
|----------|------------------|----------|--------------|
| Bear | ฿10.0M (spike one-off) | ~฿121M | 97% |
| Base | ฿10.8M (moderate API growth) | ~฿126–127M | 101% |
| Bull | ฿11.5M + sustained API | ~฿132–140M | 105–112% |

Related: [[../../Thunder Solution/Revenue/2569-01-to-05 Revenue Report|Thunder รายงานเดียวกัน]]
