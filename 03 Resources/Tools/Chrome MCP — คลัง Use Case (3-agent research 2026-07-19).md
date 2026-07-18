# Chrome MCP — คลัง Use Case (3-agent research 2026-07-19)

วิจัย 3 สายขนานกัน (~48 ไอเดีย) กรองเหลือ 31 อันที่ใช้ได้จริงกับ stack + ตัดที่เคยทำ (Dashboard/churn/LINE/FB/Sheets/Docs/Telegram). Catalog HTML: `~/chrome-mcp-usecases.html`. map ทุกอันเข้า `~/bin/chrome` verbs จริง.

**จุดแข็งหลักที่ทุกสาย converge:** ขับ Chrome ที่ login จริง = แตะหน้า authed/paywalled/ภาษาไทยที่ SaaS ต่างชาติเข้าไม่ถึง, ไม่ต้อง re-login, ไม่ต้องดึง token, real fingerprint (ไม่ติด JA3/JA4), data อยู่ในเครื่อง (PII-safe fintech).

## Security (authorized: แอปตัวเอง + CTF)
Burp Repeater + Autorize ในเซสชันสด ไม่ต้องลง cert:
- **API-surface mapping** — `chrome capture` คลิกเล่น → inventory endpoint ทั้งหมด
- **IDOR/BOLA test** — `chrome fetch /api/x/{id}` loop replay ในเซสชัน login (slip/invoice EasySlip)
- **Userscript = Burp-lite** — hook fetch/XHR ถาวร log/แก้ กลางอากาศ
- **JWT inspect** — decode + tamper + replay ดู server verify จริงไหม
- **CTF automation** — brute-force อ่าน CSRF ใหม่ทุกรอบ, grep flag DOM/net/console
- **Client storage audit** — dump localStorage/IndexedDB (CTF flag / PII leak)
- **Rate-limit probe** — หา threshold 429 บน staging ตัวเอง (own infra only)
- **CSP/headers audit** · **Two-profile authz matrix** (12306/12307 cross-session = Autorize) · **CVE watch** stack (Next/Supabase/CF/LINE, มี RSC RCE CVSS10 2025-26)

## Business/Ops/Finance (COO)
- **Smoke-test แอปตัวเองทุกเช้า** ⭐ — click-text+wait+ready+shot กัน API ล่มเงียบ (SLA ลูกค้าจ่ายเงิน)
- **ยื่นภาษี/ประกันสังคม** — ภ.พ.30/ภ.ง.ด.1,3,53/สปส.1-10 (OTP ครั้งแรก manual, ที่เหลือ auto)
- **โหลด statement/ใบเสร็จข้ามคืน** · **Reconcile ข้ามระบบ** · **Morning ops brief** (กวาดหลาย dashboard → Telegram) · **Meeting prep** · **SaaS seat audit** · **Bulk status update** (queue engine)

## Marketing/Content
- **Ad Library miner → swipe file** ⭐ — Meta/TikTok copy+creative, flag winner รัน 30 วัน → คลัง 100-hooks
- **Product GIF factory** ⭐ NEW — click flow → GIF+screenshot annotated เข้าสไลด์/workshop
- **Competitor pricing radar** — kpi+extract+shot เตือนตอนราคาขยับ
- **Hook harvester** · **SERP tracker** · **Social listening ไทย** (Pantip/FB group ที่ SaaS เข้าไม่ถึง) · **Research report N แหล่ง** (authed)

## Superpower (แทบไม่มี commercial equivalent)
- **Userscript = productivity layer ถาวร** NEW — ปุ่ม copy-row บน dashboard, preset เดือนที่แล้ว, เตือน export เสร็จ
- **Semantic tab search** NEW — 40 tab ถามไทย "แท็บที่พูดถึงราคาคู่แข่ง"
- **Price watch** · **Fitness tracker** · **Lead scraper** (public) · **Record-replay in-browser cron**

## เริ่มก่อนคุ้มสุด
1. Smoke-test แอปตัวเอง (กัน SLA ล่ม) 2. IDOR replay test (เรียน pentest บนแอปจริง) 3. Ad Library miner (ป้อน content machine)

เกี่ยว: [[reference_chrome_mcp_cli]] · verbs ที่ใช้ทั้งหมดมีจริงใน `~/bin/chrome` (32 verbs)
