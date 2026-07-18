# Chrome MCP — Learning Log

บันทึกอัตโนมัติจาก `chrome-learn` (loop เรียนรู้ของ Chrome MCP). recipe=pattern ใหม่ · gotcha=กับดัก+ทางแก้ · gap=ทำไม่ได้ (ต้องแก้) · win=สำเร็จ.
หมวดเครื่องมือ Chrome MCP. เกี่ยว: [[reference_chrome_mcp_cli]], /chrome-usecases, /chrome-mcp-cookbook.

- `2026-07-19 01:07` ⚠️ **gotcha** — chrome_javascript ตัด output ~10KB
    - แก้: ส่ง maxOutputBytes (observe ตั้ง 200000). อาการ: JSON ขาด Unterminated string
- `2026-07-19 01:07` ⚠️ **gotcha** — extension รับเฉพาะ http/https ไม่รับ file:// / data: URL
    - navigate file:// = 'Invalid url pattern'. เทสต์หน้า controlled ใช้ https จริง (httpbin.org/forms/post)
- `2026-07-19 01:07` ⚠️ **gotcha** — chrome_userscript create ต้องเปิด toggle Allow user scripts
    - chrome://extensions → Details ก่อน ไม่งั้น error 'Cannot read properties of undefined reading indexOf'. list/get/rm ใช้ได้เสมอ
- `2026-07-19 01:07` ✅ **win** — chrome_javascript await Promise + async/await ได้
    - ทำให้ actionability polling ทำใน 1 call ได้ (visible+stable+enabled+hit-test)
- `2026-07-19 01:07` 🧩 **recipe** — actionability-gated click กัน overlay
    - wait_actionable ก่อน click: elementFromPoint กลางปุ่ม=ตัวมันเอง. covered→hit:false→abort exit 4. อยู่ใน chrome click/fill/ready แล้ว
- `2026-07-19 01:07` 🕳️ **gap** — 12307 (โปรไฟล์ 2) ยังไม่มีโปรไฟล์ไหนลง extension จริง
    - two-profile authz matrix (recipe A9) ยังใช้ไม่ได้จนกว่าจะ load extension + ตั้งพอร์ต 12307
- `2026-07-19 01:07` 🕳️ **gap** — Master Dashboard ย้าย URL เป็น jetder.com (memory ยังเป็น vercel)
    - จริงคือ master-dashboard-1188573204505198593.cluster-1.jetder.com — ถ้า URL เปลี่ยนอีก parser ต้องอัปเดต
- `2026-07-19 01:17` ✅ **win** — chrome extract --schema ดึง meta/og/SEO tags ได้
    - อ่าน getAttribute('content') → title/og:title/description/og:image จากหน้าจริง (YouTube) ครบ
- `2026-07-19 01:17` 🧩 **recipe** — SEO/meta tag extraction
    - chrome extract <tab> --schema meta selectors → ตรวจ SEO ของหน้าตัวเอง/คู่แข่งเป็น batch
- `2026-07-19 01:17` ⚠️ **gotcha** — skill ที่เพิ่งสร้าง เรียกผ่าน Skill tool ไม่ได้จน session ใหม่
    - registration ตอนเปิด session. ทางแก้: รัน protocol manual + chrome-learn ได้เลย ไม่ต้องรอ
- `2026-07-19 01:25` ✅ **win** — chrome fetch --headers = authz test ไม่ต้อง 2 profile
    - replay endpoint ด้วย token คนละตัวใน profile เดียว. httpbin echo ยืนยัน server เห็น Authorization ที่ override. recipe A9 เขียนใหม่แล้ว
- `2026-07-19 01:25` ✅ **win** — master_dashboard auto-detect origin จาก tab
    - detect_origin(): env MD_DASHBOARD_URL > tab ที่ title มี Thunder Group > fallback. URL เปลี่ยนอีกก็หาเจอเอง
- `2026-07-19 01:40` ⚠️ **gotcha** — shlex.quote ชนกับ shell template ที่ครอบ {r} ด้วย quote อยู่แล้ว
    - แก้ injection ด้วย metachar guard (skip recipient ที่มี ;$`|&><) แทน quote — ไม่ชน template
- `2026-07-19 01:40` ⚠️ **gotcha** — JS ที่ return ข้อมูลใหญ่ต้องส่ง maxOutputBytes เสมอ (ไม่ใช่แค่ observe)
    - master_dashboard js() ฝัง innerText ทั้งหน้า → ถ้าโตเกิน 10KB truncate → false fail. ใส่ maxOutputBytes 500000
- `2026-07-19 02:14` ✅ **win** — chrome act = NL action + observe→cache→replay self-heal (claude -p)
    - รอบ1 claude เลือก+cache, รอบ2 replay ~1s ไม่เรียก LLM. cache: state/act_cache.json keyed host+intent
- `2026-07-19 02:14` ✅ **win** — chrome extract-ai = LLM extraction หน้ารก (claude -p)
    - page text → claude → validated JSON ตาม schema
- `2026-07-19 02:14` ✅ **win** — smoke_test.py engine จริงของ recipe B1
    - open/click-text/fill/wait(js-poll bg tab)/assert + screenshot-on-fail(base64→OUT) + Telegram
- `2026-07-19 02:14` ✅ **win** — chrome-mcp-toolkit เป็น git repo แล้ว
    - ~/chrome-mcp-jobs/.git, bin/* symlink→~/bin, out/state/PII gitignored, test.sh 24 checks
- `2026-07-19 02:14` ⚠️ **gotcha** — chrome js คืน boolean เป็น string 'true' (CDP stringify)
    - parse ต้องเทียบ str(res).lower()=='true' ไม่ใช่ === true
- `2026-07-19 02:14` ⚠️ **gotcha** — gitignore ไม่รองรับ inline comment ท้ายบรรทัด
    - 'out/  # x' ไม่ ignore out/ → PII leak. comment ต้องบรรทัดแยก
- `2026-07-19 02:45` ✅ **win** — แก้ session ใหม่เชื่อม Chrome MCP ไม่ติด
    - SessionStart hook (4 harness) heal พอร์ต + บอก Claude ใช้ ~/bin/chrome ห้ามบอก disconnected + launchd keepalive 120s (heal เฉพาะ Chrome เปิด). ต้นตอ: warp/ghostty/cmux ไม่มี SessionStart hook + http MCP ไม่ retry ตอน startup fail
- `2026-07-19 02:45` ⚠️ **gotcha** — อย่าบอก user ว่า Chrome MCP เชื่อมไม่ได้ — ใช้ ~/bin/chrome แทนเสมอ
    - CLI ต่อตรง HTTP 12306 + heal เอง ทำงานได้แม้ mcp tools ไม่ load. ผู้ใช้โกรธเรื่องนี้ 2026-07-19
