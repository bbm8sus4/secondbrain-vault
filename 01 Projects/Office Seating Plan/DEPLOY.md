---
name: SeatMap Deploy Record
version: 3.8.0
deployed: 2026-07-03
type: private (edge-auth gated)
---

# SeatMap — Deploy Record (private, gated)

## 🔗 URL + Login
- **URL:** https://seatmap-bb85fd28.pages.dev
- **User:** `thunder`
- **Password:** `KlagCABGACgejgR0`
- เข้าครั้งแรก browser จะเด้ง popup ให้กรอก user/password (HTTP Basic Auth)

## ทำไมปลอดภัย (กันข้อมูลหลุดแบบครั้งก่อน)
ไฟล์นี้ฝังชื่อพนักงานจริง 54 ชื่อใน source โดยตรง → password แบบ JS (client-side) ไร้ประโยชน์เพราะ view-source อ่านได้.
เลยใช้ **edge gate**: `_worker.js` เช็ค auth ที่ Cloudflare edge ทุก request. ถ้าไม่ผ่าน → คืน 401 **ไฟล์ไม่ถูกส่งออกเลยสักไบต์**.
- gate ติดมาพร้อม deploy ตั้งแต่ request แรก → ไม่มีหน้าต่างเวลาที่หลุด
- ทุก path (รวม `/index.html`, `/_worker.js`, path มั่ว) → 401 ถ้าไม่ auth (verified)
- password อยู่ใน worker ฝั่ง server เท่านั้น ไม่โผล่ใน HTML ที่ส่งให้ browser (verified)
- `X-Robots-Tag: noindex` + `robots.txt Disallow: /` กัน search engine
- deploy เป็น project ชื่อใหม่ (`seatmap-bb85fd28`) ไม่ใช่ `office-seating-plan` เดิมที่เคยถูกถอน

## จัดการ (ทุกอย่างที่ ~/Work/office-seating-deploy/)
- **อัปเดตแอป:** `cp ~/Desktop/office-seating-overview.html ~/Work/office-seating-deploy/dist/index.html` แล้ว
  `cd ~/Work/office-seating-deploy && CLOUDFLARE_ACCOUNT_ID=59d609e09e10c2d25c1173eaef1b67bc wrangler pages deploy dist --project-name seatmap-bb85fd28 --branch main --commit-dirty=true`
- **เปลี่ยนรหัส:** แก้ `const P = "..."` ใน `dist/_worker.js` แล้ว deploy ซ้ำ (คำสั่งบน)
- **ถอด/ปิดถาวร:** `wrangler pages project delete seatmap-bb85fd28`

## ข้อจำกัดที่ควรรู้
- Basic Auth = **รหัสเดียวใช้ร่วมกันทั้งทีม** (ไม่ใช่ล็อกอินรายคน, ไม่มี log ว่าใครเข้า)
- อยากได้ล็อกอิน Google รายคน / เห็นว่าใครเข้าเมื่อไหร่ → ต้องใช้ **Cloudflare Access (Zero Trust)** ซึ่งตั้งผ่าน dashboard (token ปัจจุบันตั้งไม่ได้). เป็น step ถัดไปถ้าต้องการ.
