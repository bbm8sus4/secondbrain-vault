# LOG — สร้าง Google Forms MASTER ทั้ง 4 ใบ + บทเรียน (2026-07-15)

## สรุปงาน

สร้างชุดแบบฟอร์มกลางสำหรับลูกค้าคอร์สอบรม AI ทุกราย (ถอดแบบจากงาน บ.ขอนแก่นอิเล็คทริค แล้วทำให้เป็นกลาง)

- **เทมเพลต markdown 4 ฟอร์ม + README** — อยู่ในโฟลเดอร์นี้
- **Google Forms MASTER จริง 4 ใบ** — สร้างผ่าน Apps Script (clasp) ลิงก์ครบใน `FORM_URLS.md`
- ฟอร์ม 4 (ติดตามผล 30–60 วัน) เป็นของใหม่ — งานขอนแก่นไม่มี ใช้วัด ROI จริง
- จุดขาย: **เส้นความมั่นใจ 3 จุด** ก่อนเรียน → หลังเรียน → 30–60 วัน (ฟอร์ม 2 ข้อ 18 → ฟอร์ม 3 ข้อ 10 → ฟอร์ม 4 ข้อ 8)

## วิธีใช้ต่อลูกค้า 1 ราย (ย่อ)

1. เปิดฟอร์ม MASTER ใน Drive → **ทำสำเนา** (ห้ามส่ง MASTER ให้ลูกค้าตอบตรง — response จะปนกันทุกราย)
2. แก้ในสำเนา: รายชื่อแผนก · หัวข้อคอร์ส (เหลือเฉพาะที่สอนจริง) · รายการบัญชีบริการ · เอา `[MASTER]` ออกจากชื่อ ใส่ชื่อบริษัทลูกค้า
3. ลำดับส่ง: ฟอร์ม 1 ก่อนเสนอราคา → ฟอร์ม 2 ≥1 สัปดาห์ก่อนอบรม → ฟอร์ม 3 วันจบก่อนแยกย้าย → ฟอร์ม 4 ตั้ง reminder 30–60 วัน

## เหตุการณ์: ฟอร์มเกิน 8 ใบ + วิธีแก้

**อาการ:** รันครั้งแรกผ่าน Web App doGet ระหว่างรอ authorize หน้า exec โดนโหลดซ้อน 3 รอบพร้อมกัน → สคริปต์สร้างฟอร์ม 3 ชุด (12 ใบ แทนที่จะเป็น 4)

**สาเหตุจริง:** กันซ้ำด้วย ScriptProperties check เดี่ยวๆ ไม่พอ — 2 execution เช็ค property พร้อมกันก่อนที่ฝั่งไหนจะเขียนเสร็จ (race condition แบบ check-then-set)

**วิธีแก้:**
1. Trash ฟอร์มซ้ำทั้ง 8 ผ่าน `?action=cleanup` ที่เพิ่มเข้าไปในสคริปต์ (ย้ายลงถังขยะ Drive — กู้ได้ 30 วัน) — เช็คผ่าน Drive API แล้วเหลือ 4 ใบพอดี
2. แก้ root cause: ครอบ `createAllForms` ด้วย **`LockService.getScriptLock()`** ให้ check-then-create เป็น atomic แล้ว push + redeploy (@2)

**กฎจำ:** Apps Script Web App ที่ "สร้างของ" ใน doGet ต้องใช้ LockService เสมอ — doGet โดน trigger ซ้อนได้ตลอด (retry ของ browser, หลาย tab, redirect ระหว่าง auth)

## เทคนิคที่ใช้ (เผื่อทำซ้ำ)

- ฟอร์มถูกสร้างใน sandbox iframe (googleusercontent) — `chrome_javascript`/`get_web_content` อ่านไม่ทะลุ ใช้ **screenshot อ่าน + Drive API ยืนยัน ID เป๊ะๆ**
- ดึง published URL (`/d/e/.../viewform`) จาก form ID: `curl -L https://docs.google.com/forms/d/<ID>/viewform` แล้วดู url_effective (redirect ไปเอง)
- clasp token ใช้ list ไฟล์ Drive ได้ (refresh ผ่าน `~/.clasprc.json`) แต่ **trash/delete ไม่ได้** (drive.file scope) → ลบต้องทำผ่าน Apps Script เอง

## ไฟล์เกี่ยวข้อง

- `0-README-วิธีใช้.md` — workflow + คำถามกุญแจห้ามตัด
- `FORM_URLS.md` — ลิงก์ฟอร์มทั้ง 4 (แก้ไข + ตอบ)
- `google-form-deploy/` — Code.gs + DEPLOY_NOTES (scriptId, deployment, วิธี push ใหม่)
- โปรเจกต์ต้นแบบ: `01 Projects/AI-101 for บ.ขอนแก่นอิเล็คทริค/`
