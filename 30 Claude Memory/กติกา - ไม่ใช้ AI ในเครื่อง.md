---
name: No local AI in workflows
description: User rejects local AI (Ollama, Gemma, on-device models) for /ai-loop and general workflows. Use cloud subscriptions only.
type: feedback
originSessionId: 0f03386f-e7a6-475f-9c21-fd6f5e11a928
---
User does NOT want local AI (Ollama / Gemma / on-device models) in `/ai-loop`, pipeline.ts, or any recommended workflow.

**Why:** User pays for premium cloud subscriptions (Claude Max 20x, ChatGPT Plus, Gemini Pro/Ultra) and wants quality + speed those provide. Local AI on M5 Pro 24GB works but gives lower-quality output and slower response than the cloud tier they're already paying for. They explicitly said "ไม่เอา AI ที่รันบนเครื่อง ไม่เอา" on 2026-05-01 after I added Ollama+Fabric providers to /ai-loop.

**How to apply:**
- Do NOT propose `provider: ollama` or `provider: fabric` (when fabric uses Ollama backend) in `jobs.yaml`.
- Do NOT suggest installing/using local model runners (Ollama, llama.cpp, MLX, LM Studio, etc.) for productivity work.
- When recommending AI tooling, default to: `claude` (Max sub) → `codex` (Plus sub) → `gemini` (web/CLI when wired) → `neomake.io` for video/image gen.
- Existing skills `gemma-review` and `full-check-gemma4` exist in their setup but treat as legacy — don't proactively recommend.
- If a use case genuinely needs offline (no internet, sensitive data must not leave device), surface the tradeoff explicitly first instead of silently picking a local model.

**Exception — Typhoon for Thai language (2026-06-04):** User explicitly asked to use **Typhoon** for Thai proofreading. It's installed locally: `alias typhoon` in ~/.zshrc → Ollama model `scb10x/typhoon2.1-gemma3-12b` (7.8GB, pulled). This is a deliberate, named exception to the no-local-AI rule — when the user names Typhoon, just use it (don't refuse or push cloud). Call via Ollama API `http://localhost:11434/api/chat`. **Caveat:** the 12B is unreliable at structured JSON proofreading (echoes segments as no-op "corrections"); always post-filter (`wrong != right` AND substring exists in source) and cross-verify with deterministic checks before applying. For its 2026-06-04 run the Thai was already clean (0 real errors). Still do NOT proactively suggest other local models (Gemma etc.).
