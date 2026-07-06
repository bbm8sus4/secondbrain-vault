# Forms Setup — Apps Script + Web App

## Form IDs

| ฟอร์ม | ID | Title ที่ user เห็น |
|------|----|----|
| 1. เจ้าของธุรกิจ | `1oEUefpyYqe1MQPpbwyM_lrkzReq02ZaETM50rUf-bvw` | แบบสอบถามความคาดหวังเจ้าของธุรกิจ — Claude AI Workshop (Needs Analysis) |
| 2. ผู้เรียน 15 ท่าน | `1ekrJsyjnlVluHixcDwyJy0AcTnwO9vuYYfzfkw81G7o` | แบบสำรวจผู้เข้าอบรม — Claude AI Workshop |
| ~~3. หัวหน้าแผนก~~ | ~~`1Cfru3TdRoDEcLZ4Uidqf28sKxXJWufrD2q3uZFPlfwU`~~ | TRASHED 2026-06-30 |

## Published URLs (ส่งให้ผู้ตอบ)

- **Owner:** https://docs.google.com/forms/d/e/1FAIpQLSd5MbOlD6K34VBNTGPXq0PMEDd1mYKzpkEp0pi48YcMy9qRBQ/viewform
- **Learner:** https://docs.google.com/forms/d/e/1FAIpQLSeBCuLJ6zUNICcylKvQTfng_lrnSPt10BhYijD-76ow9MJfTw/viewform

## Apps Script Project

- **Script ID:** `1r5GYtrTrwvdmfF6EKlbmg-9iHT-zVC_rg2yqo-e7u0pj_8Xk3aRitrsc`
- **Editor:** https://script.google.com/d/1r5GYtrTrwvdmfF6EKlbmg-9iHT-zVC_rg2yqo-e7u0pj_8Xk3aRitrsc/edit
- **Local clasp dir:** `~/Documents/Claude/Projects/AI Workshop Management/clasp-deploy/`
- **บัญชี:** bobbysomporn@gmail.com (ไม่ใช่ 9bomqu)

## Web App Deployment

Apps Script เป็น Web App + doGet → trigger rewrite ฟอร์มทั้ง 2

**Current deployment URL (v14):** `https://script.google.com/macros/s/AKfycbymU7yf-ww9mbR5J4333dXiD5C-Ih0sj96yr22rItAd3CWt8_shKBHQxHhrZlEDfhoU/exec`

URL params:
- `?form=owner` — rebuild แค่ฟอร์มเจ้าของ
- `?form=learner` — rebuild แค่ฟอร์มผู้เรียน
- `?action=status` — count items + show titles (debug)
- `?action=status&f=l` — dump items ทั้งหมดของ learner form (debug)

## Pitfalls ที่เจอ

- **doGet มี timeout** ~30-60s — ถ้า rebuild ทั้ง 2 ฟอร์มพร้อมกันอาจ hang → ใช้ `?form=owner` หรือ `?form=learner` แยกได้
- **Google Forms publish cache** — แก้ฟอร์มแล้วต้อง refresh หรือเปิดแท็บใหม่ (browser แท็บเก่าจะค้าง draft)
- **Form title (in body) ≠ file name (Drive)** — user สามารถ rename title ใน Form editor ไม่กระทบ file name
- **Duplicate forms รอบแรก** — `1hLEg4...` (learner-dup) + `1mLALx...` (owner-dup) — ยังไม่ถูกลบ (clasp token ไม่มีสิทธิ์), user ต้องลบเองที่ drive.google.com
- **clasp run ใช้ไม่ได้** ต้องใช้ Web App + doGet workaround → ดู [[clasp Apps Script + Web App workaround]] ในหลัก memory

## Reference workflow

ดูที่ memory: `reference_clasp_apps_script_webapp.md`
