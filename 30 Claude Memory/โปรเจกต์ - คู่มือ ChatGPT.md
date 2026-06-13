---
name: project-chatgpt-onboarding-guide
description: "Thai visual guide for trainees to sign up ChatGPT before a training course — live at chatgpt-setup.pages.dev, single self-contained HTML built from a Python script."
metadata: 
  node_type: memory
  type: project
  originSessionId: b64db310-fcd9-46d4-94a9-ae4582fba8e8
---

คู่มือ "วิธีสมัคร ChatGPT ก่อนเข้าอบรม" (ภาษาไทย, มีภาพ) สำหรับแจกผู้เข้าอบรมที่ไม่ถนัด AI สร้างเสร็จ + deploy แล้ว 2026-06-05.

**Live (stable link to share):** https://chatgpt-setup.pages.dev — Cloudflare Pages project `chatgpt-setup` (CF account bobbysomporn@gmail.com, wrangler already logged in). QR at `~/chatgpt-onboarding-guide/chatgpt-setup-QR.png`. ใช้ลิงก์ถาวร ไม่แชร์ลิงก์ hash รายครั้ง (ตาม [[feedback_deploy_link]]).

**Build (DON'T edit the HTML directly — it's generated):**
- Source of truth: `~/chatgpt-onboarding-guide/build_visual_guide.py` → `python3 build_visual_guide.py` writes `ChatGPT-Onboarding-Guide-TH-Visual.html` (single self-contained file, ~2.6MB, base64 images + embedded Thai webfont). Also `cp` to `~/Desktop/` for the user.
- Screenshots in `~/chatgpt-onboarding-guide/shots/` (9 used). Thai webfont CSS (base64 woff2) in `thai_font.css`, read+injected by builder.
- **Redeploy after rebuild:** copy HTML as `index.html` into a temp dir → `wrangler pages deploy <dir> --project-name=chatgpt-setup --branch=main --commit-dirty=true`. macOS has no `timeout`; use `perl -e 'alarm N; exec @ARGV' wrangler ...`.

**Key design decisions (already applied — keep):**
- 2 signup methods kept visible (NOT folded): **วิธีที่ 1 Plus (ฟรี 1 เดือน, แนะนำ)** first → **วิธีที่ 2 Go (สำรอง, ฿259 จ่ายทันที)**. Plus-free-first because Free isn't enough during training.
- "Free Plus then cancel + remove card" technique included (Claim → Settings>Billing>Cancel plan → ⋮ menu>Remove).
- Screenshots captured live via Chrome MCP (port 12307, KUAN Golf profile); user-supplied billing screenshots had **PII redacted** (name/address cropped, card last-4 boxed) — re-redact any new ones.
- Mobile/typography hardened: clamp() type, line-height 1.72, `word-break:normal` (NOT break-word — that cut Thai mid-word), overflow-x:clip, min-width:0.
- **Thai font embedded** = IBM Plex Sans Thai (base64 woff2, @font-face `unicode-range` Thai-only so Latin stays SF). This fixed "ฟอนต์ไม่เหมือนกันทุกเครื่อง" (system fonts differ: Mac=Sukhumvit, iOS=SF Thai). Verified identical iPhone vs Mac.
- ChatGPT/OpenAI logomark (inline SVG, light gray #c7c7cc) in hero, subtle.
- Thai proofread via Typhoon (Ollama) + Gemini — kept casual/concise for beginners; rejected their "make it more formal/wordy" suggestions.

Built with the [[reference_ai_debate_harness]] (aidebate) used repeatedly for review/typography/missing-pieces. Audience constraint = non-technical office workers; keep language simple, short, no jargon.
