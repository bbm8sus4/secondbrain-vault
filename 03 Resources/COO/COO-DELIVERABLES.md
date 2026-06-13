# COO All-Hands Briefing Pack · พฤษภาคม 2569

จัดทำเสร็จ 8 พ.ค. 2569 · ใช้ภายในเท่านั้น

---

## 📂 ไฟล์ในชุดนี้

ทุกไฟล์อยู่ที่ `/Users/aexgee/`

| File | ใช้เมื่อไหร่ | คำอธิบาย |
|---|---|---|
| `coo-index.html` | **เปิดก่อน** | หน้า landing — รวม link ทุกไฟล์ + TL;DR + KPI |
| `coo-allhands-2026-05.html` | **ระหว่างประชุม** | เอกสารหลัก 16 sections — ใช้ฉาย/อ่าน · มี timer + presenter mode |
| `coo-onepage-2026-05.html` | **ในมือ ระหว่างประชุม** | สรุป A4 หน้าเดียว · พิมพ์เก็บไว้ดู |
| `coo-pocket-card.html` | **ในกระเป๋าเสื้อ** | การ์ด A6 · 2 หน้า (front + back) · พิมพ์แล้วพับ |
| `coo-speech-script.md` | **เตรียมตัว / ส่งทีม** | สคริปต์เต็ม markdown · copy ลง Slack/email ได้ตรง |
| `coo-data-snapshot.html` | **Backup ตัวเลข** | ทุกตัวเลขจาก dashboard ใน 1 หน้า · ใช้ถ้า live dashboard ขัดข้อง |
| `coo-assets/chart.umd.min.js` | (auto) | Chart.js สำหรับ offline |
| `coo-server-start.sh` | (ถ้า server หยุด) | Bash script ช่วย start HTTP server ใหม่ → `bash /Users/aexgee/coo-server-start.sh` |

---

## 🚀 วิธีใช้ · ขั้นตอน

### ก่อนนอน (1 นาที)
1. เปิดไฟล์ `coo-index.html` ทบทวนสรุป

### Server URL (ถ้าใช้ผ่าน HTTP)
- หลัก: **http://localhost:8989/coo-index.html**
- ถ้า server หยุด: `bash /Users/aexgee/coo-server-start.sh`
- ถ้าไม่มี server: เปิดผ่าน `file:///Users/aexgee/coo-index.html` ก็ได้ (ฟอนต์อาจ fallback ระบบ)

### ตื่นมา · ก่อนประชุม 30 นาที
1. เปิด `coo-onepage-2026-05.html` → **กด Cmd+P → Save as PDF** → พิมพ์ (เก็บใส่กระเป๋า)
2. เปิด `coo-pocket-card.html` → **กด Cmd+P** → พิมพ์ A6 (พับใส่กระเป๋าเสื้อ)
3. เปิด `coo-allhands-2026-05.html` → ดูส่วน **Q&A Prep** (#qa-prep) ทบทวน 7 คำถาม
4. ดูส่วน **Toolkit** (#toolkit) — เช็คลิสต์ก่อนเริ่ม + confidence affirmations

### ระหว่างประชุม
1. เปิด `coo-allhands-2026-05.html` ให้ฉายขึ้นจอ
2. กด **`P`** เข้า presenter mode (sticky scroll-snap + dim topbar)
3. กด **`⏱ Timer`** บน topbar เพื่อนับถอยหลัง 10 นาที
4. ใช้ **`↓`/`↑`** เปลี่ยน slide
5. ถ้าต้องดู notes กด **`N`**
6. ถ้า tech ล่ม → ดู `coo-onepage-2026-05.html` ที่อยู่ในมือ + พูดต่อ
7. ถ้าเวลาเหลือน้อย → กระโดดไป **5-min Backup Script** (#backup-5min)

### หลังประชุม
1. เปิด `coo-allhands-2026-05.html#email-template` → กด **📋 Copy Email Body**
2. Paste ลง email/Slack ส่งให้ทีม
3. (option) Edit personal touches แล้วส่ง

### เดือนหน้า
1. เปิด `coo-allhands-2026-05.html#watch` (KPI Tracker)
2. นำ metrics ไปประกอบประชุมเดือนหน้า → check progress vs targets

---

## 🎯 สรุป Key Messages

### TL;DR
1. โต **+28% YoY** · on-track ปิดปีตามเป้า
2. ฮีโร่: **Thunder API +180%, EasySlip +28%, Flex +71%**
3. 30 วัน: **ปลุกฐาน · ดัน EasySlip API · เปลี่ยนสมัคร→จ่าย**

### Frame งาน
> "เครื่องเราดีอยู่แล้ว — งานของเดือนหน้าคือใช้เครื่องนี้ให้คุ้ม"

### ปิดที่ไพ่ตาย
> "เดือนนี้เราพิสูจน์ว่า **เครื่องเราเดินได้** — เดือนหน้าเราจะพิสูจน์ว่า **เครื่องเราเร่งได้**"

---

## ⚠️ ข้อควรระวัง

- **ห้ามแชร์ตัวเลขรายได้เป็นบาทใน slide** — ใช้ % เท่านั้น
- **Risk Register** (#risk-register) **ห้ามแชร์ในที่ประชุม** — ใช้สำหรับ Board/CEO sync เท่านั้น
- **ตัวเลขจาก Master Dashboard** อัปเดต real-time — ตัวเลขในเอกสารอาจขยับ ±0.5% ระหว่างทำเอกสาร
- หาก dashboard อัปเดตใหม่ก่อน 7AM → ตรวจ `https://master-dashboard-eight-nu.vercel.app/` ก่อนพูด

---

## 📋 Checklist Final ก่อนเข้าประชุม

- [ ] Print one-page briefing (A4)
- [ ] Print pocket card (A6) แล้วพับ
- [ ] เปิด presenter deck ในเครื่อง · กดทดลอง P (presenter mode)
- [ ] ทดลอง timer · เห็นว่าเริ่ม-หยุด-รีเซ็ตได้
- [ ] ทบทวน Q&A 7 ข้อ อย่างน้อย 2 รอบ
- [ ] อ่าน Toolkit (confidence affirmations)
- [ ] ดื่มน้ำ · เข้าห้องน้ำ · ตรวจไมค์
- [ ] Open dashboard tab ไว้สำรอง — เผื่อมีคนถามตัวเลขสด
- [ ] Email template เตรียมไว้ → ส่งหลังประชุมภายใน 24 ชม.

---

*จัดทำโดย AI Operator · 8 พ.ค. 2569 · v3 · ใช้ภายในเท่านั้น*
