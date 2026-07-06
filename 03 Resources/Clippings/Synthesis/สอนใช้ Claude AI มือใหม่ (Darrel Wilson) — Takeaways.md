---
title: "สอนใช้ Claude AI มือใหม่ (Darrel Wilson) — Takeaways"
type: synthesis
source: "03 Resources/Clippings/สอนใช้ Claude AI สำหรับผู้เริ่มต้น (2026) – วิธีใช้งาน Claude AI ทีละขั้นตอน.md"
source_date: 2026-06-03
imported: 2026-07-04
last_verified: 2026-07-06
status: live
tags: [synthesis, clipping, claude, ai, onboarding, training, coo]
---

# สอนใช้ Claude AI มือใหม่ (Darrel Wilson) — Takeaways

> **TL;DR:** tutorial Claude ฉบับมือใหม่ที่ครบสุดตัวหนึ่ง — เทคนิคหลักคือ "ให้ AI เขียน prompt ให้ AI" + ใช้ Projects/Skills/Connectors เปลี่ยน Claude จาก chatbot เป็นระบบงานประจำของทีม → ใช้เป็นสื่ออบรมพนักงาน Thunder ได้เลย

Raw: [[03 Resources/Clippings/สอนใช้ Claude AI สำหรับผู้เริ่มต้น (2026) – วิธีใช้งาน Claude AI ทีละขั้นตอน|ดูตัวจริง (Darrel Wilson ภาษาไทย)]]

## Takeaways สำหรับ COO

1. **Meta-prompting คือเทคนิคที่คุ้มสุด** — อย่าถามตรง ๆ ให้บอกบริบท (เราเป็นใคร ธุรกิจอะไร อยู่ไหน) แล้วสั่งให้ Claude "สร้าง prompt ละเอียด" ก่อน ค่อยเอา prompt นั้นไปรัน → ได้ผลลึกกว่าหลายเท่า ใช้ได้ทุกอุตสาหกรรม — ควรเป็นบทแรกของการอบรม AI ภายในองค์กร
2. **Custom instructions ระดับบัญชี** — ใส่โปรไฟล์ตัวเอง/ธุรกิจ/สิ่งที่ห้ามทำไว้ครั้งเดียว ทุกแชทจะอ้างอิงตาม → ทำ template กลางให้พนักงานแต่ละแผนกกรอก (ตำแหน่ง, งานประจำ, ข้อห้าม) ลดคำตอบกว้าง ๆ
3. **Projects = คำสั่งเฉพาะงานที่ทำซ้ำ** — ตั้ง Project ต่อ workflow (เช่น "ร่างอีเมลแจ้งโปรโมชั่น" กำหนดน้ำเสียง+ความยาว+ข้อห้าม แนบ PDF guideline ได้) แล้วสั่งงานซ้ำได้เรื่อย ๆ โทนคงที่ → ตรงกับงานร่างประกาศลูกค้า/CS ของเรา (เทียบ skill `/announce` ที่มีอยู่)
4. **Skills = โครงร่าง output มาตรฐาน** — เช่น skill โพสต์ LinkedIn ที่ล็อกฟอร์แมตไว้ สั่ง "หาข่าวล่าสุดเรื่อง X" ก็ได้โพสต์ฟอร์แมตเดิมพร้อมข้อมูลใหม่ → ทีม marketing/CS ทำ skill ต่อช่องทาง (LINE broadcast, FB post) ให้ format นิ่งโดยไม่ต้องบรีฟซ้ำ
5. **Vision ใช้ตรวจงานได้จริง** — screenshot landing page ให้วิจารณ์ (headline คลุมเครือ, ไม่มี social proof, CTA แข่งกันเอง, เมนูเยอะไป) → ใช้รีวิวหน้าเว็บ EasySlip/หน้า pricing ก่อน launch ได้ทันที ต้นทุนศูนย์
6. **Artifacts สร้าง mini-app แจกลูกค้าได้** — ตัวอย่างในคลิป: เครื่องมือสร้าง Privacy Policy/ToS ที่ผู้ใช้กรอกเองแล้ว publish เป็นลิงก์/ฝังเว็บ → ไอเดียทำเครื่องมือฟรีเป็น lead magnet (เช่น "เช็กสลิปปลอมเบื้องต้น", SMS cost calculator ของ BoostSMS)
7. **Connectors ต่อ Gmail/Calendar/Stripe/PayPal** — สั่งเช็กบิล สรุปรายงานรายเดือน เทียบเดือนต่อเดือนได้ในแชท → ลดงาน admin ของทีม finance/ops (ต้องคุมสิทธิ์การเข้าถึงข้อมูลด้วย)
8. **Desktop app > browser** — เร็วกว่า, ลง plugin/MCP ได้, จัดการ skills ง่ายกว่า และ Cowork/Dispatch ควบคุมคอมได้ (เปิดโปรแกรม ทำงานแทน) → ถ้าจะ roll out ให้ทีม ให้ลง desktop app เป็นมาตรฐาน
9. **แผน Pro ขึ้นไปถึงคุ้ม** — เวอร์ชันฟรีไม่มีโมเดลตัวท็อป (Opus) ซึ่งต่างจากฟรีชัดเจน → งบ AI ต่อหัวสำหรับพนักงานที่ใช้จริงควรเป็น Pro เป็นอย่างต่ำ
10. **เปิด web search เสมอเมื่อทำ research/การตลาด** — ให้คำตอบอิงเทรนด์/ข้อมูลปัจจุบันแทนความรู้เก่าของโมเดล
