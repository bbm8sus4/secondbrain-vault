---
title: "08 — Master Dashboard Integration"
type: entity
source: "BoostSMS/_assets/ source files (brand KB session 2026-06)"
source_date: 2026-06-13
imported: 2026-06-13T22:49:35
last_verified: 2026-07-06
status: live
tags: [boostsms, brand]
---

# 08 — Master Dashboard Integration

**Master Dashboard:** https://master-dashboard-eight-nu.vercel.app/

## ตำแหน่ง BoostSMS ใน Master Dashboard

- **`/` (ภาพรวมวันนี้)** — มี Bot/Flex/Thunder API/EasyBot/EasySlip API แต่ **ไม่มี BoostSMS**
- **`/easyslip`** — BoostSMS revenue อยู่ใต้ **tab "Boost SMS"** ของ /easyslip เท่านั้น (เป็น tab แยกใน drill-down ของแบรนด์ EasySlip)
- **`/thunder`** — ไม่มี BoostSMS (BoostSMS อยู่ใต้แบรนด์ EasySlip ไม่ใช่ Thunder)

## Taxonomy ของ products

- **Thunder brand:** Bot (BOT) + Thunder API + Flex (small)
- **EasySlip brand:** Easy Bot (BOT) + EasySlip API + **Boost SMS**
- EasySlip API ≈ 96.9% ของ EasySlip revenue (dashboard flag concentration risk)
- **BoostSMS data ปัจจุบันเป็น placeholder-like** (0 sent, "ยังไม่มี log") — ยังไม่ live ใน dashboard

## วิธีดึงข้อมูล BoostSMS (Chrome MCP)

1. ไปที่ `/easyslip` (ไม่ใช่ `/`)
2. ตั้ง date picker หลังจาก navigate (location.href RESETS picker) — ใช้ preset "เดือนที่แล้ว"
3. เปิด tab **"Boost SMS"**
4. อ่าน "เปรียบเทียบสินค้า → รายได้เดือนนี้"

**Date picker (ส่วนยากสุด):**
- header button มี dynamic id (เช่น `#base-ui-_R_pidb_`)
- หาด้วย: `[...document.querySelectorAll('header button')].find(x=>/\d{2}\/\d{2}/.test(x.textContent))`
- JS `.click()` ไม่เปิด popover (Base UI ignores untrusted clicks) → ต้อง **tag element ด้วย id แล้ว `chrome_click_element` กับ `#thatid`**
- Click "เดือนที่แล้ว" preset เพื่อได้เดือนก่อนหน้า (เชื่อถือได้กว่า prev-arrow+day1+day30+apply)
- Verify โดย re-read picker button text → ควรเป็น "01/04 - 30/04/2026"

**Anti-hallucination warning:** harness tool results delivered a turn late / batched บน session นี้ — รายงานเฉพาะตัวเลขที่ปรากฏใน real tool output cross-check brand product-sums vs root overview totals + MoM % badges ก่อนเชื่อ

## Related notes

- [[คู่มือ - ดึงข้อมูล Master Dashboard]] — playbook ฉบับเต็ม
- [[โปรเจกต์ - Thunder Solution]] — parent brand context
