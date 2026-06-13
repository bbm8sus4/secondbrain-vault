---
name: Deploy — use stable URL, no double-deploy
description: For Cloudflare Pages projects with GitHub auto-deploy, push only and share the stable production alias once — never the per-commit hash URL
type: feedback
originSessionId: a0805209-1bd5-49e1-adb4-ec74466ac847
---
หลัง `git push` เข้า production branch (main) ของ Cloudflare Pages project ห้ามทำสองสิ่ง:

1. **ห้ามรัน `wrangler pages deploy` ซ้ำ** — ถ้าโปรเจกต์มี GitHub integration อยู่แล้ว (เช่น `easybot-finance` connected to `bbm8sus4/easybot-finance-cockpit`) `git push` จะ trigger Cloudflare auto-build/deploy เอง การรัน wrangler ซ้ำคือ **double deploy** เปลือง build minutes และทำให้ CD pipeline สับสน
2. **ห้ามส่งลิงก์ preview URL ที่มี commit hash** เช่น `https://c67ba7ad.easybot-finance.pages.dev` — แต่ละ deploy สร้าง URL ใหม่ ทำให้ user ต้องกดลิงก์ใหม่ทุกครั้ง น่ารำคาญและไร้ประโยชน์ เพราะ Cloudflare มี **stable production alias** อยู่แล้ว (`easybot-finance.pages.dev` หรือ `main.easybot-finance.pages.dev`) ที่ชี้ deploy ล่าสุดเสมอ

**Why:** เกิดเหตุการณ์จริง 2026-04-26 — ผม commit/push/wrangler-deploy 5 รอบติดในเซสชันเดียว ส่งลิงก์ hash ใหม่ทุกครั้ง user โกรธมากเพราะต้องเปลี่ยนแท็บเปลี่ยนลิงก์ไม่หยุด

**How to apply:**
- ก่อน `wrangler pages deploy` เช็กก่อนว่าโปรเจกต์มี GitHub auto-deploy ไหม (`gh repo view --json` ดู deploy hook หรือถาม user)
- ถ้ามี: `git push` พอ ไม่ต้อง wrangler
- ส่งลิงก์ stable เพียง **ครั้งเดียวต่อเซสชัน** เช่น "เปิดที่ `easybot-finance.pages.dev` แล้ว refresh ดูได้ทุก commit"
- ถ้าจำเป็นต้องส่งลิงก์ hash (เช่น preview branch deploy ที่ยังไม่ merge) ระบุชัดเจนว่ามันเป็น preview หนึ่งครั้ง ไม่ใช่ลิงก์ที่ user จะใช้ต่อเนื่อง

**Verify auto-deploy actually fired (added 2026-04-26, corrected later same day):**

**INITIAL WRONG DIAGNOSIS:** ผมเคยเขียนว่า "CF Pages GitHub auto-deploy ไม่เชื่อถือ webhook ขาด" — **ไม่จริง** หลังไล่หาต้นตอจริง ๆ พบว่า:

1. Project `easybot-finance` ไม่มี Cloudflare-native git integration เลย (Git Provider = "No" ใน `wrangler pages project list`)
2. Deploy flow คือ **GitHub Actions** (`.github/workflows/deploy.yml`) → run Playwright tests → ถ้าผ่าน → call `wrangler pages deploy` ผ่าน `cloudflare/wrangler-action`
3. ที่ค้าง 3 commits ติดเพราะ **smoke test fail** บน selector ที่ stale (`#compareSummary` ที่ผมลบใน Compare redesign แต่ลืมอัปเดต `tests/views.spec.js`)
4. Fail → `needs: test` block deploy step → ดูเหมือน "auto-deploy ค้าง" แต่จริง ๆ คือ test gate ทำงานถูกต้องแล้ว

**Lesson — ต้องตรวจ workflow runs ก่อนสรุปว่า "webhook ขาด":**
```bash
gh run list --workflow=deploy.yml --limit 5
gh run view <id> --log-failed | head -100
```

**กฎจริง สำหรับ project นี้และ project อื่นที่ใช้ Actions-deploy pattern:**
- ก่อน push ทุกครั้ง รัน test ในเครื่อง: `npm test` ผ่านก่อนค่อย `git push`
- ถ้า push แล้ว ดู `gh run watch` หรือ `gh run list` ภายใน 2-3 นาที
- ถ้า test fail → fix test (หรือ fix code ที่ test จับ) ห้ามใช้ wrangler manual deploy bypass test gate (ทำให้โค้ดที่ test ไม่ผ่านขึ้น production)
- ถ้า workflow file ไม่มี = ไม่มี auto-deploy — ต้องตั้งใหม่หรือ accept manual flow

**Verify ด้วย `curl -s <stable-url>/<file>` หาคลาส/ฟังก์ชันใหม่** ยังเป็น verification ที่ดี แต่ใช้หลังยืนยันว่า workflow run success แล้ว
