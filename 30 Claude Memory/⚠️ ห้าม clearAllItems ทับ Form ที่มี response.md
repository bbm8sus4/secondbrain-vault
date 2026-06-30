---
name: feedback-forms-never-clearitems
description: ห้ามใช้ clearAllItems/deleteItem ทับ Google Form ที่มี response แล้ว — มันทำให้คำตอบ orphan. วิธีกู้ผ่าน Forms REST API
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee3243ee-719d-43e0-bff1-37e9a5221f48
---

**ห้ามเด็ดขาด:** อย่าใช้ `clearAllItems()` / `form.deleteItem()` rewrite Google Form ที่มีคนตอบแล้ว — การลบ item ทำให้ response เก่า (ผูกกับ questionId เดิม) หลุด link → `getItemResponses()` คืนค่าว่าง + linked Sheet ที่ link ทีหลัง backfill ได้แต่ timestamp

**Why:** 2026-06-30 ทำ AI Workshop form rewrite ผ่าน Web App หลายรอบ ระหว่างนั้นมีผู้เรียน 8 คน + เจ้าของ 1 คนตอบเข้ามา รอบ rewrite ถัดมา clearAllItems ทับ → ข้อมูลดู "หาย" user โกรธมาก (ขู่ฟ้อง/กลัวตกงาน)

**How to apply:**
- ก่อนแก้ฟอร์มที่ deploy แล้ว **เช็ค `form.getResponses().length` ก่อนเสมอ** ถ้า > 0 ห้าม clearAllItems
- จะแก้ฟอร์มมี response: ใช้ `item.setTitle()`/`setChoiceValues()` แก้ในที่ (in-place) อย่าลบสร้างใหม่ หรือถ้าต้องเพิ่มข้อ ให้ `addItem` ต่อท้ายเฉยๆ ไม่ clear
- ทุก doGet ที่ rewrite ฟอร์ม ต้องมี guard: `if (f.getResponses().length>0) return 'BLOCKED — has responses';`

**วิธีกู้ (ได้ผลจริง 2026-06-30):**
1. คำตอบเดิม **ยังอยู่ใน Google** ใต้ questionId เดิม — ลบ item แค่ทำให้ API ปกติมองไม่เห็น ไม่ได้ purge
2. ดึงผ่าน **Forms REST API** `GET https://forms.googleapis.com/v1/forms/{id}/responses` — มันคืน answers keyed by questionId ดิบ (ไม่ map schema ปัจจุบัน) → ได้ค่ากลับครบ
3. Forms REST API ต้องเปิดบน GCP project: `gcloud services enable forms.googleapis.com --project=<proj>` (project ของ Apps Script เอง 451000... ล็อก เปิดไม่ได้ → เปิดบน project อื่นของ user แล้วใส่ header `x-goog-user-project: <proj>` ตอนเรียก)
4. เรียกจากใน Apps Script ด้วย `ScriptApp.getOAuthToken()` (มี forms scope อยู่แล้ว) + header quota project → ผ่าน web app `?action=rest` ดึง JSON
5. map questionId→title ด้วย value-fingerprint (จับคู่ค่าคำตอบกับ choice list ที่รู้) แล้วประกอบเป็น CSV/Sheet
- gcloud `auth application-default login --scopes=...forms...` **โดน Google บล็อก** (sensitive scope, generic client) — ใช้ไม่ได้ ต้องไปทาง Apps Script token
- Recovery files: `~/Documents/Claude/Projects/AI Workshop Management/RECOVERY/`

related: [[AI Workshop — บ.ขอนแก่นอิเล็คทริค|project_ai_workshop_khonkaen]] [[clasp Apps Script + Web App workaround|reference_clasp_apps_script_webapp]]
