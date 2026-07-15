# Google Forms — Course Intake Kit (MASTER)

สร้างเมื่อ: 2026-07-15 11:44 (Asia/Bangkok) · บัญชี: bobbysomporn@gmail.com
สคริปต์: `google-form-deploy/` · ดูวิธีทำสำเนาต่อลูกค้าที่ `google-form-deploy/DEPLOY_NOTES.md`

> **ห้ามส่งลิงก์ MASTER ให้ลูกค้าตอบตรงๆ** — ทำสำเนา (Make a copy) ใน Drive ก่อนทุกครั้ง

## ฟอร์ม 1 — แบบสอบถามผู้ว่าจ้าง (Needs Analysis)
- แก้ไข: https://docs.google.com/forms/d/1cYdXESM_HIjMz7d-2xog8veExmMtIAwI6iY5FNutRwo/edit
- ตอบ: https://docs.google.com/forms/d/e/1FAIpQLSdDfhenWv8aLcGc0loZ5rdL4lIp_6sK4m_Q2d080Oo-RQo8vw/viewform

## ฟอร์ม 2 — แบบสำรวจผู้เรียนก่อนอบรม (Pre-training)
- แก้ไข: https://docs.google.com/forms/d/1othirDkuz8r2vnGgKZzx6k4IhRaQOk9cI5hOPxwF-lg/edit
- ตอบ: https://docs.google.com/forms/d/e/1FAIpQLSd2DZ1nJ1A1Y2j77R_8d8bK98mHBmmEpQxGveKlYja_Msym-g/viewform

## ฟอร์ม 3 — แบบประเมินหลังอบรม (Post-training)
- แก้ไข: https://docs.google.com/forms/d/1VwoeLEeQDpPa_xw3qPcA8S7Zj8VmkFpAxJlzvoy6NJk/edit
- ตอบ: https://docs.google.com/forms/d/e/1FAIpQLSdappGK4G44FQXEi3Ws_xmrc0Kd-0s1SXKOiEmnzJ2sXYo24w/viewform

## ฟอร์ม 4 — แบบติดตามผล 30–60 วัน (Follow-up)
- แก้ไข: https://docs.google.com/forms/d/1URwoQ4cVf9eZdMV6FwSN2KFf2ol-XbHOXXa384MNnIk/edit
- ตอบ: https://docs.google.com/forms/d/e/1FAIpQLSeTmouk0MfbxyG6M4z7X3iEuLXhm5Q4u6-WNYMj_h8gnRA-3A/viewform

---

## Log

- 2026-07-15: สร้างครั้งแรกผ่าน Web App doGet — โดน trigger ซ้อน 3 รอบ ได้ 12 ฟอร์ม (เกิน 8)
  → trash duplicate ทั้ง 8 ผ่าน `?action=cleanup` แล้ว (อยู่ในถังขยะ Drive กู้ได้ 30 วัน)
  → แก้ root cause: เพิ่ม LockService ใน `createAllForms` (push + redeploy @2 แล้ว)
