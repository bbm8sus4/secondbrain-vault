# ⚠️ INCIDENT — ข้อมูลคำตอบฟอร์ม "หาย" แล้วกู้คืนสำเร็จ

**วันที่:** 2026-06-30
**ความรุนแรง:** วิกฤต (ผู้ใช้โกรธมาก ขู่ฟ้อง/กลัวตกงาน) — กู้คืนได้ครบ 100%
**ผู้เสียหาย:** ผู้เรียน 8 คน + เจ้าของ 1 คน (รวม 9 response)

---

## เกิดอะไรขึ้น (Root Cause)

ระหว่างพัฒนาฟอร์ม ผม rewrite ฟอร์มผ่าน Web App `doGet` หลายรอบ โดยใช้
`clearAllItems()` (= `form.deleteItem()` ทุก item) แล้วสร้างใหม่ทั้งหมด

**ระหว่างที่กำลังพัฒนา มีผู้เรียนทยอยส่งคำตอบเข้ามา 8 คน (16:09–16:42)**
พอ rewrite รอบถัดมา (เพิ่มเมนูอาหาร 16:58) → `clearAllItems` ลบ item เก่าทิ้ง
→ response เก่าที่ผูกกับ **questionId เดิม** กลายเป็น orphan

**อาการที่เห็น:**
- `form.getResponses()` คืน 8 response แต่ `getItemResponses()` ว่างเปล่า (เหลือแต่ timestamp)
- Linked Sheet ที่ link ทีหลัง backfill ได้แต่ timestamp ช่องคำตอบว่างหมด
- ฟอร์มหน้าเว็บแสดงแค่ 4 ข้อแรก (รอบ rewrite ที่ค้างกลางคัน timeout)

---

## บทเรียน (ห้ามทำซ้ำเด็ดขาด)

1. **ห้าม `clearAllItems()` / `deleteItem()` กับฟอร์มที่มี response แล้ว** — ลบ item = ลบ link ของคำตอบ
2. **เช็ค `form.getResponses().length` ก่อนแก้ฟอร์มทุกครั้ง** ถ้า > 0 → ห้าม clear
3. แก้ฟอร์มที่ deploy แล้ว ให้แก้ **in-place**: `item.setTitle()` / `item.setChoiceValues()` หรือ `addItem` ต่อท้าย — อย่าลบสร้างใหม่
4. doGet ที่ rewrite ฟอร์ม **ต้องมี guard**: `if (f.getResponses().length>0) return 'BLOCKED';`
5. rewrite ฟอร์มผ่าน Web App มี **timeout ~30–60s** ถ้า rebuild 2 ฟอร์มพร้อมกันอาจค้างกลางคัน → ฟอร์มเหลือครึ่งๆ

---

## วิธีกู้คืน (ได้ผลจริง — ทำตามนี้ถ้าเกิดซ้ำ)

**หลักการ:** คำตอบเดิม **ยังอยู่ใน Google** ใต้ questionId เดิม — ลบ item แค่ทำให้ API ปกติมองไม่เห็น **ไม่ได้ purge จริง** → Forms REST API ดึงกลับได้

### ขั้นตอน
1. **เปิด Forms API** บน GCP project ที่เราคุมได้
   `gcloud services enable forms.googleapis.com --project=extreme-voice-462512-d0`
   (project ของ Apps Script เอง `451000…` ถูกล็อก เปิดไม่ได้ — ใช้ project อื่นของ user)

2. **ดึง response ดิบผ่าน Forms REST API จากใน Apps Script**
   - `var token = ScriptApp.getOAuthToken();` (มี forms scope อยู่แล้ว)
   - `UrlFetchApp.fetch('https://forms.googleapis.com/v1/forms/{id}/responses', {headers:{Authorization:'Bearer '+token, 'x-goog-user-project':'extreme-voice-462512-d0'}})`
   - **header `x-goog-user-project`** = ชี้ quota ไป project ที่เปิด API ไว้ (สำคัญ! ไม่งั้น bill ไป 451000… ที่ปิด API → 403)
   - คืน JSON: `answers` keyed by **questionId เดิม** (ไม่ map schema ปัจจุบัน) → ได้ค่าครบ
   - เรียกผ่าน web app endpoint `?action=rest` แล้ว curl ด้วย clasp token

3. **map questionId → ชื่อคำถาม** ด้วย value-fingerprint:
   - parse choice list จาก Code.gs → จับคู่ค่าคำตอบกับคำถามที่ choice ตรง
   - free-text (ชื่อ/อีเมล/ตำแหน่ง) + scale (1–5) → ใช้ heuristic (email มี @, ชื่อมีเว้นวรรค ฯลฯ)

4. **ประกอบเป็น CSV/Sheet** → อัปขึ้น Drive เป็น Google Sheet (clasp token `drive.file` สร้างไฟล์ใหม่ได้ + แปลง text/csv → native Sheet อัตโนมัติ)

### ทางที่ลองแล้ว "ไม่เวิร์ก"
- `gcloud auth application-default login --scopes=...forms...` → **Google บล็อก** ("แอปนี้ถูกบล็อก") เพราะ forms.responses เป็น sensitive scope บน generic client → ต้องไปทาง Apps Script token เท่านั้น
- clasp token เรียก Forms API ตรงๆ → 403 (Forms API ปิดบน project ของ clasp `1072944905499` เปิดไม่ได้)
- enable Forms API บน `451000…` (project ของ Apps Script) → PERMISSION_DENIED (Google-managed project ล็อก)

---

## การเชื่อมชีตหลังกู้ (ที่ทำไว้)

- ผูกฟอร์ม → ชีตกู้คืนด้วย `form.setDestination(FormApp.DestinationType.SPREADSHEET, sheetId)` (web app, forms scope)
- ผล: ไฟล์เดียว 2 แท็บ — แท็บข้อมูลกู้คืน 8 คน + แท็บ "การตอบกลับแบบฟอร์ม 1" (คนใหม่ append เอง)
- เลิกผูกชีตเก่า `14F0…` (มีแต่ timestamp) ทิ้ง

## Recovery artifacts
- Raw + CSV + xlsx: `~/Documents/Claude/Projects/AI Workshop Management/RECOVERY/`
- ชีตกู้คืน (Drive): ผู้เรียน `1fQmT7RUO_YVLyZVQP3e9jowYv5TgotU56XEvFE0LpUQ` · เจ้าของ `1l9Z_IiQ-VGO8dZAH6XJzuLZXa_CYraG2gnJ7NxrbLBE`

related: [[01-Forms-Setup]] · memory `feedback_forms_never_clearitems`
