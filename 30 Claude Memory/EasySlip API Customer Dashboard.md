---
name: project-easyslip-api-dashboard
description: EasySlip API top-up/customer analytics dashboard (3-page HTML on Desktop) + knowledge base in Obsidian EasySlip/Revenue
metadata: 
  node_type: memory
  type: project
  originSessionId: 21184b42-831d-4358-b3b8-24a89577ab5e
---

# EasySlip API — Customer Analytics Dashboard

วิเคราะห์ลูกค้า **EasySlip API** จากข้อมูลเติมเครดิต 6 เดือน (`~/Desktop/topup 6 เดือน.csv`, ม.ค.–มิ.ย. 2569 · ฿33.6M · 1,250 คน). ลูกค้าเติมเครดิตเพื่อเรียก API ตรวจสลิป. **ไม่ใช่หวย/lotto** (เคยเข้าใจผิด — user ยืนยันเป็น EasySlip API).

- **Dashboard 3 หน้า** (single-file HTML, vanilla JS, no backend) บน `~/Desktop/`: `topup_dashboard.html` (การเงิน) · `crm_dashboard.html` (CRM 6 แท็บ) · `monthly_dashboard.html` (รายเดือน/เทียบ).
- **Regenerate:** `python3 topup_analyze.py / crm_analyze.py / crm_advanced.py / crm_deep.py / monthly_analyze.py` → แล้ว `build_*.py` (ทั้งหมดบน Desktop).
- **นิยาม churn = เงียบ >60 วัน** (จาก cadence จริง median 11 วัน, 98% เติมซ้ำใน 60 วัน). RFM 7 กลุ่ม · Gini 0.888 · บัญชี #1 = 31% ของรายได้ · รายชื่อลูกค้า CSV ที่ `~/Desktop/topup_customer_lists/`.
- **PII 1,250 ชื่อ+อีเมล ฝังใน HTML → ห้าม deploy public โดยไม่มี auth** (Desktop gitignored แล้ว).

**KB เต็ม (Obsidian):** `~/SecondBrain/EasySlip/Revenue/EasySlip API - วิเคราะห์ลูกค้า Top-up 6 เดือน.md`. เนื้อหา EasySlip อื่นๆ ดู [[EasySlip API pricing + margin|reference_easyslip_api_pricing]] · [[โปรเจกต์ - Thunder Solution|project_thunder_solution]]. แก้เนื้อหาที่ Obsidian ไม่ใช่ memory.
