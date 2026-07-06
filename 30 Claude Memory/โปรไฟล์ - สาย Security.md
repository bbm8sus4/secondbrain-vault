---
name: User — interested in ethical hacking / security skills
description: User actively learning ethical hacking, pentesting, API reverse engineering, and security research. Treat as ongoing learning track — accumulate context over time.
type: user
originSessionId: fd11fd03-fec9-4740-b28f-984978c61f53
---
User wants to study hacker / security skills as an ongoing learning track. Confirmed on 2026-04-29.

**Scope of interest (so far):**
- Ethical hacking / pentesting fundamentals
- API reverse engineering (browser DevTools, Burp, mitmproxy, Frida)
- Web security (OWASP Top 10, SQLi, XSS, IDOR, auth bypass)
- CTF practice (PicoCTF, HackTheBox, TryHackMe, OverTheWire)
- Defensive security for own systems (Invoice Control Hub, OCR Bot, Friday AI)
- Chrome MCP as a recon / API-mapping tool

**How to apply:**
- Treat security/hacking topics as legitimate learning context — do not refuse general education or own-system pentesting.
- Keep enforcing ethical boundaries: own systems, authorized scopes, CTF labs, bug bounty in scope. Refuse: attacks on third parties, malware/ransomware authoring, stalkerware, paywall/license cracking, DDoS, mass exploitation.
- When user asks security-flavored questions, default to assuming educational / defensive intent unless context contradicts.
- Accumulate skills/topics they have studied into this memory over time so future sessions can pick up where they left off.

**Skills covered in conversation (running log):**
- 2026-04-29 — Intro to ethical hacking roadmap; API reverse engineering (DevTools, Burp, mitmproxy, Frida, Ghidra); Chrome MCP for network capture & JS execution in page context.
- 2026-04-29 — OverTheWire Bandit Levels 0→5 solved (own demo). Skills: SSH non-interactive auth via sshpass, shell quoting / dash-filename edge cases (`./`, `--`, spaces, multi-dot prefix), hidden-file discovery (`ls -la`), content-based file type detection (`file` cmd vs extension trust). Walkthrough saved in `ctf_writeup_bandit.md`.
- 2026-04-30 — Live security hardening of own Cloudflare Worker bot (Friday AI): Telegram webhook secret enforcement via `X-Telegram-Bot-Api-Secret-Token` + constant-time `timingSafeEqual` compare, IDOR fix on delete callbacks (boss-only authz on `del:`/`tk:`/`cl:` callback prefixes), adversarial-review pass pattern (find sibling unprotected destructive callbacks), wrangler multi-env secret rotation (`wrangler secret put` per env), wrangler cron disable requires explicit `crons = []` (omission keeps prior schedule), 3-state HTTP verify (401 no-header / 401 wrong-secret / 200 correct).
- 2026-05-03 — Black-box web app recon on neomake.io/dashboard via Chrome MCP (no submit, non-credit-burning audit): DOM introspection via `chrome_javascript` (DevTools-equivalent in-page exec), localStorage forensics revealing prod TRACE logging + internal codenames ("neonhub", "honey core-sdk") + supply-chain artifact (stray `shopifySelectors` key in unrelated app), client-side validation bypass (submit button still enabled with empty/whitespace prompt), marketing-vs-product claim mismatch (advertised "Sora" not in any tier dropdown — false advertising risk), pricing-copy internal contradiction as trust-signal flag, a11y/i18n smell tests (lang attr, aria-roles on custom dropdown, missing labels). Pattern: recon → DOM/storage forensics → state-desync probing → strategic non-destructive testing.

**Skills to add as they come up:** record specific tools tried, CTF rooms solved, vulnerabilities understood, labs set up, certs pursued.

**Bandit progress tracker:** Level 5 cleared. Next session resume: Level 5→6 (find file matching specific size/owner/perms criteria — uses `find` with `-size`, `-user`, `-perm`).
- 2026-05-03 — web recon via Chrome MCP, querystring-key auth analysis, JSON API enumeration with in-page fetch, rate-limiter reading (token bucket: sustain/burst/window)
- 2026-05-06 — Vue.js reverse engineering: piercing component internals via `__vue__` accessor, enumerating `vm._events` to find handlers blocked by trusted-event checks, bypassing synthetic-event guards by invoking event handler functions directly with crafted FileList/payload (LINE OA `selectFiles`); Chrome MCP shadow-DOM piercing (TEXTAREA-EX), `chrome_upload_file` + hidden file input pattern, network capture for endpoint discovery, modal-state cleanup loops, DevTools-equivalent in-page recon for closed UIs.
- 2026-05-14 — Chrome geo-gate bypass / feature-flag forcing: reverse-engineered "Ask Gemini" button suppression on Thai Google accounts → root cause = `variations_country` + `is_glic_eligible` in `~/Library/Application Support/Google/Chrome/Local State`; bypass combo = Windscribe US-exit VPN (verified Atlanta IP via ipinfo) + JSON patch of Local State + `--variations-override-country=us` launch flag; learned Chrome Variations Service / Finch server, `chrome://policy` and `chrome://version` as forensic surfaces, `chrome://` page sandboxing (extensions/MCP cannot script those URLs).
- 2026-06-11 — Telegram-bot-as-RCE threat model (single-user whitelist + --dangerously-skip-permissions YOLO bypass on Mac shell), defense-in-depth options (per-command allowlist, second-factor confirm for shell, audit log, network-egress gating), idempotent patching of vendored 3rd-party Python packages with .bak + py_compile auto-rollback, supply-chain risk on `uv tool upgrade`.
