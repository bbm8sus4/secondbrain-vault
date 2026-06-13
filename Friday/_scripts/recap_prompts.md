# Recap synthesis prompts

## Weekly prompt template

```
อ่านไฟล์ที่ {source_path} (Friday bot summaries จาก Telegram groups รอบสัปดาห์ {label}).

สังเคราะห์เป็น **Weekly Recap ภาษาไทย** สำหรับ COO ของ Thunder Solution / EasySlip group. โทน "ครับ" แบบเพื่อนร่วมงานเก่งสรุปบนมือถือ.

โครงสร้าง:
- หัวข้อ "# Weekly Recap — {label}"
- 4-6 หมวด business (Thunder Ops, EasySlip+Finance, EasyBOT+Marketing, Product/Dev, EasyCRM+Sales+HR, SHIFT+Bob) — ข้ามหมวดที่ไม่มี signal
- แต่ละหมวดมี bullet points: เหตุการณ์สำคัญ, ตัวเลข, ชื่อคน, decisions
- ⚠️ Watch list ที่ค้างปลายสัปดาห์
- ✅ Highlights ที่สำเร็จ

เน้น:
- รายละเอียดมาก ไม่สรุปทั่วไป
- ตัวเลข/วันที่/ชื่อต้องตรง
- Code/proper nouns ภาษาอังกฤษ
- ไม่ใส่ meta-comment

Output ถึงไฟล์ {output_path} แบบ Markdown ตรงๆ. ไม่ต้องอธิบายอะไรเพิ่ม. แค่เขียนไฟล์เสร็จก็พอ.
```

## Monthly prompt template

```
อ่านไฟล์ที่ {source_path} (Friday bot summaries จาก Telegram groups เดือน {label}).

สังเคราะห์เป็น **Monthly Recap ภาษาไทย** สำหรับ COO ของ Thunder Solution / EasySlip group. โทน "ครับ" แบบเพื่อนร่วมงานเก่งสรุปบนมือถือ.

โครงสร้าง:
- หัวข้อ "# Friday — Monthly Recap {label}"
- 7 หมวด:
  1. Thunder Solution Operations (incidents, customer cases, withdraw bonus, sales, Flex)
  2. EasySlip + Accounting/Finance (P&L, tax, banking, expenses, closing books)
  3. EasyBOT + Marketing (performance, Affiliate, Ads, Graphic, campaigns, BoostSMS launch)
  4. Product / Project / Development (BoostSMS, banking integration, billing, API metrics, infra)
  5. EasyCRM + Sales + HR (CRM dev, deals, sales pipeline, hiring, leaves)
  6. SHIFT + Talk to Bob + Other (Bob decisions, cafe ops, legal, equipment)
  7. ⚠️ Master Watch List ที่ค้างสิ้นเดือน + ✅ Highlights สำเร็จ

เน้น:
- ละเอียดมาก เอาเข้าประชุมได้
- ใส่ครบทุก: ตัวเลข, ชื่อคน, วันที่, ดีล, decisions
- กลุ่ม pending แยกชัดเจน
- Code/proper nouns ภาษาอังกฤษ
- ไม่ใส่ meta-comment

Output ถึงไฟล์ {output_path} แบบ Markdown ตรงๆ. ไม่ต้องอธิบายอะไรเพิ่ม. แค่เขียนไฟล์เสร็จก็พอ.
```
