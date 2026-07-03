---
title: Prompt Library — Index
type: resource
source: Apple Notes import 2026-06-21 (31 prompts created 2026-02-18)
source_date: 2026-02-18
imported: 2026-06-21
last_verified: 2026-06-21
status: live
tags: [resource, prompt-library, ai, index]
---

# Prompt Library

> คลังพรอมต์ภาษาไทยสำหรับงาน 30+ ประเภท · สร้างโดย Bob (COO) 2026-02-18 · import จาก Apple Notes 2026-06-21

## วิธีใช้
1. ระบุงานที่ต้องทำ → จับคู่หมวด
2. เปิดไฟล์หมวดนั้น → copy prompt → แปะ ChatGPT/Claude/Gemini
3. เติม context ของพี่ลงไป
4. ถ้า prompt อันไหนใช้แล้วเวิร์ก → mark ไว้ที่ frontmatter ของไฟล์นั้น

## โครงสร้าง 2 ชั้น
1. **เทมเพลตตามประเภทงาน** (ไฟล์ที่ root นี้) — pattern กลาง 30+ ประเภท ใช้เริ่มงานอะไรก็ได้ (import จาก Apple Notes)
2. **พรอมป์แยกตามบริบท** (โฟลเดอร์ย่อย) — พรอมป์เฉพาะงานจริงที่ Bob สร้างสะสม แยกตาม domain เพิ่มเรื่อยๆ

## รากฐาน (อ่านก่อน)
- [[UNIVERSAL MASTER PROMPT]] ⭐ — pattern กลางสำหรับทุกงาน
- [[คลัง Prompt Repos ดัง (GitHub)]] — repo พรอมป์/prompt engineering ดังบน GitHub (awesome-chatgpt-prompts, dair-ai guide, system prompts หลุด ฯลฯ) — ของคนอื่นที่เอาไว้หยิบใช้/เรียนรู้
- [[Caveman Prompting (ประหยัด token)]] — เทคนิคตอบห้วนแบบมนุษย์ถ้ำ ลด token 60-75% · ติดตั้ง Claude Code output-style แล้ว (`/output-style Caveman`)

## แยกตามบริบท (โฟลเดอร์ย่อย · เพิ่มได้เรื่อยๆ)
- [[Marketing/_index|Marketing]] — พรอมป์งานการตลาด (KuanGolf GTM plan, …)
- [[HR/_index|HR]] — พรอมป์งาน HR / คน / องค์กร _(ว่าง พร้อมเติม)_
- _เพิ่มบริบทใหม่: สร้างโฟลเดอร์ + `_index.md` + ลิงก์บรรทัดนี้ (เช่น Sales, Product, Ops, Finance, Legal)_

### กติกาการตั้งชื่อ/จัดไฟล์ (สำหรับพรอมป์บริบทใหม่)
- 1 พรอมป์ = 1 ไฟล์ วางในโฟลเดอร์บริบทที่ตรงที่สุด
- frontmatter ต้องมี: `type: prompt`, `context: <marketing|hr|…>`, `use:`, `created:`
- เนื้อพรอมป์วางในกล่อง ``` code fence ``` ให้ copy ทั้งก้อนได้
- อัปเดตลิงก์ใน `_index.md` ของโฟลเดอร์นั้น

## หมวดงาน (30 อัน)

### คิด · ตัดสินใจ
- [[คิดเชิงกลยุทธ์_สถานการณ์ (Strategy _ Scenario)|Strategy / Scenario]]
- [[ตัดสินใจแบบมีกรอบ (Decision Support)|Decision Support]]
- [[เปรียบเทียบ_เลือกทาง (Compare _ Decide)|Compare / Decide]]
- [[ให้คะแนน_ประเมินด้วยรูบริก (Score _ Evaluate)|Score / Evaluate]]

### วางแผน · แตกงาน
- [[วางแผน _ แตกงาน (Planning & Breakdown)|Planning & Breakdown]]
- [[วางแผน_แตกงานระดับระบบ (Plan _ Ops)|Plan / Ops]]
- [[บริหารโครงการ_ประชุม (PM)|PM]]
- [[ทำความเข้าใจโจทย์ให้คม (Clarify _ Scope) ถามกลับเพื่อเก็บ requirement…|Clarify / Scope]]

### สังเคราะห์ข้อมูล
- [[สรุป _ ย่อยข้อมูล (Summarize)|Summarize]]
- [[สกัด_ดึงข้อมูลจากข้อความ (Extract)|Extract]]
- [[ค้นหา_อัปเดตข้อมูล + อ้างอิง (Research)|Research]]
- [[จัดหมวด_ติดแท็ก_คัดแยก (Classify _ Tag _ Filter)|Classify / Tag / Filter]]
- [[แปลงรูปแบบข้อมูล (Transform)|Transform]]
- [[วิเคราะห์ข้อมูล (Data)|Data]]
- [[คำนวณ _ วิเคราะห์ตัวเลข|คำนวณ / วิเคราะห์ตัวเลข]]

### เขียน · สื่อสาร
- [[เขียนงานเอกสาร_สื่อสาร (Drafting)|Drafting]]
- [[งานเอกสารธุรกิจ (Docs)|Docs]]
- [[งานสื่อสาร_เจรจา_รับมือข้อโต้แย้ง (Comms)|Comms]]
- [[ครีเอทีฟ_แบรนด์_คอนเทนต์ (Creative)|Creative]]
- [[ไอเดีย _ ครีเอทีฟ (Ideation)|Ideation]]

### โค้ด · ระบบ
- [[โค้ด_ระบบ_ออโตเมชัน (Technical)|Technical]]
- [[วิศวกรรมซอฟต์แวร์ (Engineering)|Engineering]]
- [[ออโตเมชัน_เวิร์กโฟลว์ (Automation)|Automation]]
- [[วิเคราะห์_ตรวจงาน (Critique _ QA)|Critique / QA]]

### คน · สอน · สวมบทบาท
- [[HR_คน_องค์กร (HR)|HR]]
- [[สอน_โค้ช (Tutor _ Coach)|Tutor / Coach]]
- [[การสอน_ฝึกทักษะ (Tutor _ Drill)|Tutor / Drill]]
- [[สวมบทบาท (Role _ Persona)|Role / Persona]]

### โดเมนเฉพาะ
- [[UX_Product_การวิจัย (UX _ Research)|UX / Research]]
- [[การเงิน_ตัวเลขขั้นสูง (Finance _ Quant)|Finance / Quant]]

## หมายเหตุ
- ทุกไฟล์เก็บไว้ตามชื่อที่ใช้ใน Apple Notes (มี `_` แทน `/` เพื่อเลี่ยง filesystem) — Obsidian alias resolve ให้ใน frontmatter ของแต่ละไฟล์ (ถ้ามี)
- เนื้อหาแต่ละ prompt ยังไม่ได้ standardize template — ใครจะใช้ตัวไหนก่อนเปิดอ่านก่อนปรับ
