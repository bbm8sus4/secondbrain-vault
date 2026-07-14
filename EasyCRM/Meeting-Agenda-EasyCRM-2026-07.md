# EasyCRM Meeting Agenda

**วันที่:** กรกฎาคม 2026
**ผู้เรียกประชุม:** COO
**ผู้เข้าร่วม:** ทีม Sales, Marketing, Dev, Support, Designer
**ระยะเวลา:** 60-90 นาที

---

## 1. สถานะยอดขาย & Pipeline (15 นาที)

- ดีลปัจจุบัน — กี่ราย, แพ็กเกจอะไรบ้าง
- Pipeline ที่กำลังเปิด — จำนวน + มูลค่ารวม
- Conversion rate (Lead → ปิดดีล)
- เป้ารายได้ไตรมาสนี้ vs ตัวเลขจริง

**เตรียมมา:** ข้อมูลจาก Sale Record + Sales Alerts

---

## 2. Margin & ต้นทุนจริง (15 นาที)

- Margin ในชีต 71-77% แต่หลังต้นทุนแฝงเหลือ ~28-36%
- ต้นทุนแฝงที่ยังไม่ได้คำนวณจริง:
  - Onboarding / Training
  - Customer Support
  - Server / DB / Infra
  - SMS / LINE messaging
  - Marketing CAC
  - Dev maintenance
  - Risk / Refund (2-5%)
- Premium margin ต่ำสุด (~28%) เพราะ scope งานออกแบบ+support เยอะ

**ต้องเคาะ:** มอบหมายใครคำนวณ Cost per Deal จริง + deadline

---

## 3. ระบบค่าคอม — Action Items ค้าง (10 นาที)

ฟีดแบ็ก Mark (คุณวุทธอนุมัติแนวทางแล้ว) ยังไม่ได้ทำ:

- [ ] เพิ่ม Lead Source เป็นตัวตัดสินแบ่ง (70/30 vs 100%)
- [ ] Report ดึงจาก Sale Record อัตโนมัติ (แก้ data mismatch)
- [ ] ยืนยันเรตค่าคอม — คงที่ 10% ทุกแพ็กเกจ หรือกลับไป 10/12/15
- [ ] ทำ Google Sheet เวอร์ชันใหม่ก่อนแก้ไฟล์จริง

**ต้องเคาะ:** ใครรับทำ + เมื่อไหร่เสร็จ

---

## 4. Onboarding & Operations (10 นาที)

- SOP 14 วัน 5 phases — ทำได้จริงไหม มี bottleneck ตรงไหน
- Dev สร้างร้านค้าใหม่ — ใช้เวลากี่วัน (ยังเป็น manual)
- Graphic Designer capacity — พอไหมถ้าดีลเพิ่ม
- CS response time target <1 ชม. — วัดจริงหรือยัง ทำได้ไหม

---

## 5. Product & Feature Gaps (10 นาที)

ฟีเจอร์ที่ปิดอยู่ทุกแพ็กเกจ:

| ฟีเจอร์ | สถานะ | คำถาม |
|---|---|---|
| Segmentation | ปิดทุกแพ็กเกจ | ลูกค้าถามบ่อยไหม? เปิดเมื่อไหร่? |
| ของรางวัลจัดส่ง | ปิดทุกแพ็กเกจ | มี demand จริงไหม? |
| Dashboard | พื้นฐานทุกแพ็กเกจ (ยกเว้น Enterprise) | แผนอัปเกรด? |

ประเด็นอื่น:

- Trial 14 วันไม่มี Broadcast LINE — ลูกค้าทดลองแล้วไม่เห็นคุณค่า?
- Roadmap ฟีเจอร์ถัดไปคืออะไร

---

## 6. ทีม & Capacity (10 นาที)

ทีมปัจจุบัน:

| บทบาท | คน |
|---|---|
| Sales | Mizteen, Olive |
| Marketing | Jadi |
| Support | Support team |
| Dev | Dev team |
| Designer | Graphic Designer |

- กำลังคนรับลูกค้าใหม่ได้อีกกี่รายต่อเดือน?
- KPI ที่ตั้งไว้ (CSAT >=4.5, setup <=3 วัน) — วัดจริงหรือยัง?
- ต้องเพิ่มคนตำแหน่งไหนก่อนถ้า scale?

---

## 7. สรุปข้อตัดสินใจ & Action Items (10 นาที)

| # | เรื่อง | ตัวเลือก | ผู้รับผิดชอบ | Deadline |
|---|---|---|---|---|
| 1 | เรตค่าคอม | 10% คงที่ หรือ 10/12/15 | | |
| 2 | Lead Source model | เริ่มใช้เมื่อไหร่ | | |
| 3 | Cost per Deal จริง | มอบหมายใครคำนวณ | | |
| 4 | Capacity plan | รับได้กี่รายต่อเดือน | | |
| 5 | Feature roadmap | Segmentation / Dashboard | | |

---

## เอกสารอ้างอิง

- Google Sheets: `Final_EasyCRM_Commission` (ระบบค่าคอม)
- Admin Portal: https://easycrm-two.vercel.app
- Telegram: EasyCRM Sales Alerts / Alert Center
- คู่มือค่าคอม: `EasyCRM-คอม-v2-คู่มือ.html`
- ฟีดแบ็ก Mark: `EasyCRM_Commission_Update_Summary_For_Secretary_Marketing.pdf`
