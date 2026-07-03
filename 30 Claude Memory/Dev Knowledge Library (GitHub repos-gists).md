---
name: reference-dev-knowledge-library
description: Curated library of popular GitHub repos/gists (Clean Code style) that the user collects. Lives in SecondBrain 03 Resources/Engineering as md + web page. Add new finds here.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1f995c76-07d7-4e94-8d25-4e118177716b
---

User ชอบสะสม GitHub repos/gists แนว "ความรู้ที่คนช่วยกันแชร์" (จุดเริ่มคือ gist Clean Code ของ wojteklu). เก็บทั้งหมดที่ `~/SecondBrain/03 Resources/Engineering/`:

- `Clean Code (Robert C. Martin) — สรุป.md` — สรุป Clean Code แบบ **verbatim** (raw จาก gist wojteklu)
- `คลังความรู้ GitHub สำหรับนักพัฒนา (Dev Knowledge Library).md` — index markdown 20+ repos/gists แบ่ง 5 หมวด (Gist / Best Practices / System Design / เรียน+สัมภาษณ์ / Awesome Lists) พร้อมลิงก์ + ดาว
- `dev-knowledge-library.html` — หน้าเว็บ light B/W tech theme + search filter (เปิดในเบราว์เซอร์เพื่อกดลิงก์)

Vault = git repo `bbm8sus4/secondbrain-vault` (push แล้วทุกไฟล์).

**How to apply:** เจอ repo/gist ดี ๆ ใหม่ → เพิ่มให้ครบทั้ง 3 ไฟล์ให้ตรงกัน. ถ้าจะเก็บเนื้อหา verbatim ตัวใหม่ (แบบ Clean Code) ต้องดึง raw ผ่าน `curl` — WebFetch มันสรุปทิ้ง ได้ไม่ครบ. ดาว = ตัวเลขประมาณ mid-2026.

**Auto-injection hook (2026-07-03):** `~/.claude/hooks/inject-repo-library.py` = UserPromptSubmit hook ที่ดึงไฟล์ md index มาใส่ context อัตโนมัติเมื่อ prompt มีคีย์เวิร์ด repo/github/gist/library/คลัง/roadmap/cheatsheet ฯลฯ (prompt อื่นเงียบ). ลงทะเบียนใน settings.json ของ **4 config dir**: `.claude`, `.claude-warp`, `.claude-ghostty`, `.claude-cmux`. Idempotent — เช็ค `inject-repo-library` ก่อน append. มีผลกับ session ใหม่ (restart ถึงจะโหลด hook).

Related: [[โปรเจกต์ - Second Brain|project_second_brain]]
