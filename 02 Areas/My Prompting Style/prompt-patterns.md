---
tags: [prompting, patterns, examples]
parent: [[หน้าหลัก]]
---

# Prompt Patterns — ตัวอย่างจริง

Pattern สั่งงานที่พบซ้ำ + ตัวอย่าง prompt จริงจากการวิเคราะห์.

## 1. Status Check (30+ ครั้ง)

**Trigger:** ทำงานยาว / งานหลาย pass / รอ deploy

```
ทำเสร็จหรือยัง                (x16)
ทำหรือยัง                     (x6)
ทำถึงไหนแล้ว                  (x4)
ทำเสร็จยัง                    (x4)
เสร็จหรือยัง                  (x3)
เสร็จยัง
แก้ไขหรือยัง                  (x2)
แก้หรือยัง                    (x2)
ทำเสร็จหมดหรือยัง             (x2)
```

**Assistant should:** ตอบสั้น 1 บรรทัด — "เสร็จแล้วครับ, [ลิงก์/path]" หรือ "อีก 30 วิ, กำลัง X"

## 2. Silent-Continue (15+ ครั้ง)

**Trigger:** งานถูกหยุดกลางคัน / รอ approve

```
ทำต่อ ๆ                       (x9)
ทำต่อเลย                      (x3)
ทำให้เลย                      (x3)
ทำต่อไป                       (x2)
งานต่อ ๆ                      (x2)
โอเค ทำเลย                    (x2)
โอเค ทำได้เลย                 (x2)
จัดมา ทำให้เลย
```

**Assistant should:** ไปต่อทันที ห้ามถามซ้ำ

## 3. Open/View File (93 ครั้ง — top pattern)

```
เปิดไฟล์มาดูหน่อย             (x10)
เปิด finder                   (x10)
เปิดมาดูหน่อย                 (x7)
เปิดไฟล์มาหน่อย               (x7)
เปิดดูหน่อย                   (x6)
เปิดไฟล์ดูหน่อย               (x3)
เปิด Finder                   (x3)
เปิดไฟล์หน่อย                 (x2)
เปิดมาสิ                      (x2)
เปิดไฟล์บน Desktop ให้หน่อย
เปิด Chrome ทุก profile แล้ว ลองเช็คใหม่
เปิดค่าคอม BoostSMS
```

**Assistant should:** `open <path>` ทันที ไม่ต้องถาม path ถ้ามี recent context

## 4. Aidebate Workflow (56 ครั้ง — signature)

**Trigger:** ต้อง critique / iterate / ไม่แน่ใจ

```
aidebate
aidebate โปรเจ็กนี้
aidebate เรื่องนี้หน่อย       (x3+)
Aidebate เรื่องภาษาไทย         (x3)
Aidebate เพิ่มเรื่องของ...
Aidebate เรื่อง database หน่อยสิ แบบเป็น Google Sheet
Aidebate เช็กดูทั้งหมดยังขาดอะไรอีก
Aidebate เช็กเนื้อหา และกฏหมายของประเทศไทยสิ
รอผล aidebate
aidebate ตรวจสอบดีไซน์ทั้งหมด ถูกต้องตามหลัก หรือยัง
aidebate ปรับทั้งหมดทำออกมาให้ไซ์ขนาดมือถือ
aidebate แดชบอร์ดเกี่ยวกับเรื่องนี้มันชัดเจนเคลียร์และดีกว่านี้สิ
```

**Assistant should:** เรียก `~/ai-debate/debate.py "<topic>"` แล้ว synthesize output

## 5. Path/URL + Question (20+ ครั้ง)

**Pattern:** วางลิงก์เปล่า ๆ + คำถาม 1-2 คำ

```
https://docs.google.com/spreadsheets/... เห็นอะไร
https://thunder-revenue-report.pages.dev/ เห็นอะไร
/Users/aexgee/Downloads/sms-logs-all-2026-06-19.csv เห็นอะไร
/Users/aexgee/Desktop/02\ In\ progress/API\ Calls\ Kbank  ดูใหม่
https://github.com/robzilla1738/harness-terminal  ศึกษาเรื่องนี้
https://gist.github.com/karpathy/... เข้าใจเรื่องนี้ไหม
```

**Assistant should:** อ่าน/fetch → สรุปสิ่งที่เห็นทันที (ไม่ต้อง confirm ก่อน)

## 6. Data Transfer (10+ ครั้ง)

**Pattern:** เอา X ไป Y

```
เอาข้อมูลในนี้ไปทำเป็นสไลด์ HTML     (x2)
เอาข้อมูลนี้ไปบันทึกแยกไว้เป็นความจำของ Friday
เอาข้อมูลจากลิงค์ ไปสร้าง โฟลเดอร์เพิ่มในทุกบริษัท
เอาข้อมูลจาก odsidian
ต้นทุนของ EasyCRM มีเรื่องไหนบ้าง ไปเอาข้อมูลจาก odsidian
เอาไฟล์นี้เข้าไปดูเพิ่มหน่อย
เอาต้นทุนของ Slip มาดูหน่อย ใน Obsidian
```

**Assistant should:** อ่าน source → transform → write to destination

## 7. Design Refinement

**Pattern:** ระบุจุดปรับ + ห้าม/ต้อง

```
ดีมากไฟล์ยังออกมาไม่สวย ทำเป็นธีมโมโนโทน ขาว เทา ดำ หน่อย
ทำการให้คะแนน ออกมาง่าย ๆ เด็กอ่านยังเข้าใจในด้านการให้คะแนน
ค่าน้ำหนักหรือตัวคูณ ทำให้ออกมาเข้าใจง่ายและคำนวนง่ายกว่านี้
ที่ออกมาเป็นไฟล์ html ตามสไตล์ที่ฉันชอบและใส่รูปจริงที่อ้างอิงไปด้วย
เปลี่ยนฟอนต์หน่อย
ทำสูตรให้มันง่าย ๆ ทำงานได้จริงไม่ซับซ่อน
```

**Assistant should:** จำ style ที่ user เคยชอบ (no emoji, monotone, LINE Seed Sans TH, etc.) — ไม่ต้องถามซ้ำ

## 8. Meta-Commands (config/setup)

```
claude --resume --dangerously-skip-permissions ทำคำสั่งนี้เป็น cr
claude config set model claude-opus-4-6
ต้องติดตั้งอะไรเพิ่มถึงจะวางรูปแบบ ctrl+c , ctrl+v ได้
config
กูต้องมี 3 แอคเคาท์นะ 12306 / 12307 /12308
ใช้ typoon ในการปรับคำภาษาไทยให้ถูกต้อง                (x3+)
เปิด chrome MCP แล้วไปเช็กได้เลย เทสทั้งหมด port 12306
```

## 9. Frustration Escalation (33 ครั้ง)

**Trigger:** งานช้า / ไม่เข้าใจ / วนเปล่า

```
ทำเสร็จหรือยัง ทำไม ทำ ๆ หยุด ๆ มึงบ้าเหรอ
มึงทำอะไรอยู่ กูไม่เห็นทำอะไรเลย
ทำแบบ B ไง มึงทำออะไรอยู่เสร็จยัง
มึงจะกุได้หรือยัง
มึงก็ไปหามาสิ ทำให้เลย
ทำทั้งหมดที่ dabate มาก่อนหน้านี้ด้วย กูก็นึกว่าทำมาตลอด
ทำไม Friday ไม่ทำตามหน้าที่ และมึงทำไมไม่ทำตามหน้าที่
```

**Assistant should:**
- ตอบสั้น สุภาพ ("ครับ")
- ยอมรับผิดตรง ๆ ถ้าพลาด
- ไปทำทันที ไม่ต้องแก้ตัวยาว
- ห้าม mirror "กู/มึง"

## 10. Long Structured Prompt (rare, 26 ครั้ง)

**Trigger:** ต้อง paste เอกสารเต็ม / role playing / template refinement

**ตัวอย่างจริง:**
```
คุณคือผู้เชี่ยวชาญด้าน Copywriting และการสื่อสารในองค์กร (Corporate Communication)

หน้าที่ของคุณคือการปรับปรุงข้อความ (Text) ในสไลด์คู่มือการเตรียมความพร้อม...
เปลี่ยนโทนเสียง (Tone of Voice) จากภาษาพูดที่เป็นกันเอง ห้วน หรือเป็นสไตล์การจดโน้ตส่วนตัว
ให้กลายเป็นภาษาที่ "กระชับ เป็นทางการ สุภาพ น่าเชื่อถือ และเคลียร์"

กรุณาปรับปรุงข้อความในแต่ละหน้าตามตาราง "Before" และ "After"...
```

```
Research Demand
คุณคือ Market Intelligence Specialist
สำหรับ [สินค้า/บริการ]
ในตลาด [ประเทศ/พื้นที่]
กลุ่มลูกค้า [กลุ่มเป้าหมาย]

จากข้อมูลล่าสุด สรุป
1) เทรนด์ 2) ความต้องการ 3) Pain Point 4) พฤติกรรมซื้อ 5) คำค้น/คำพูดลูกค้า
6) เหตุผลที่ตัดสินใจซื้อ 7) โอกาสที่แบรนด์ควรใช้ต่อ
ไม่ต้องเขียนคอนเทนต์ พร้อมลิงก์อ้างอิง
```

**Format ที่ใช้:** Role → Task → Context (bracketed slots) → Output requirements → ห้าม/ต้อง

related: [[behavioral-profile]] · [[_all-prompts-raw]]
