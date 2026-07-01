---
tags: [skills, automation, hooks, voice-input]
parent: [[หน้าหลัก]]
created: 2026-07-01
---

# Skills Built — ลด typing (2026-07-01)

5 skills ที่สร้างเพื่อลด prompts ซ้ำ ๆ ที่พี่พิมพ์ (จากการวิเคราะห์ 901 prompts ใน [[behavioral-profile]]).

---

## 1. Auto-open Hook (Stop hook) — แก้ 93 ครั้ง "เปิดไฟล์ดูหน่อย"

**ไฟล์:**
- `~/.claude/hooks/track-file-writes.sh` (PostToolUse — บันทึก path)
- `~/.claude/hooks/auto-open-recent.sh` (Stop — เปิด file/finder อัตโนมัติ)

**ทำงานยังไง:**
- ทุกครั้ง Claude ใช้ Write/Edit/MultiEdit → log path ลง `/tmp/claude-file-tracking/<session_id>.txt`
- เมื่อ agent หยุด (Stop hook) → อ่าน log, filter (มีอยู่จริง, modified ใน 5 นาทีล่าสุด), เปิด:
  - **HTML/PDF/PNG/xlsx/docx/mp4** → `open` ใน default app
  - **โค้ด/.md/.json** → `open -R` reveal ใน Finder
- Cap 3 ไฟล์/รอบ · Cooldown 45s (ไม่เปิดซ้ำถ้าพี่พิมพ์ "ทำต่อ" หลาย ๆ ครั้ง)

**Disable ชั่วคราว:** `touch /tmp/claude-auto-open-disabled`
**Re-enable:** `rm /tmp/claude-auto-open-disabled`

**Config:** อยู่ใน `~/.claude/settings.json` → `hooks.PostToolUse` + `hooks.Stop`

---

## 2. Voice Input — `voice2clip.sh` + Karabiner F5 hotkey

**ไฟล์:** `~/bin/voice2clip.sh`
**Hotkey:** **F5** (via Karabiner-Elements)
**Model:** `~/whisper-models/ggml-small.bin` (466MB) หรือ `ggml-medium.bin` (1.5GB, กำลัง download)

**ทำงานยังไง:**
1. กด **F5** → sox บันทึกเสียง (max 30s, stop on 2s silence)
2. Whisper-cli transcribe เป็นภาษาไทย
3. คัดลอกลง clipboard (+ auto-paste ผ่าน cliclick ถ้ามี)
4. Notification แสดง preview

**Requires:**
- `whisper-cpp` (binary: `whisper-cli`)
- `sox`
- `cliclick` (สำหรับ auto-paste)
- **Karabiner-Elements ต้องเปิด** (start Karabiner-Elements.app)
- **Microphone permission** สำหรับ Terminal/whisper (System Settings → Privacy → Microphone)

**ปรับ config:**
```bash
# เปลี่ยน model
export WHISPER_MODEL=~/whisper-models/ggml-medium.bin

# เปลี่ยนภาษา
export WHISPER_LANG=en

# เรียก manual (แทน F5)
~/bin/voice2clip.sh 60   # record max 60s
```

**Karabiner rule** อยู่ใน `~/.config/karabiner/karabiner.json` (backup: `.backup-*`)

**เปลี่ยน hotkey:** แก้ `key_code` ใน karabiner.json — เช่น `right_option` แทน `f5`

---

## 3. Statusline Enhancement — แก้ 30+ ครั้ง "ทำถึงไหนแล้ว"

**ไฟล์:** `~/.claude/statusline.sh` (แก้เพิ่ม row 5)

**เพิ่มบรรทัด:** `📁 <project>  ⎇ <branch>*  ✎ <n> files`

- **project** = basename ของ cwd
- **branch** = git branch + `*` ถ้า dirty
- **files** = จำนวนไฟล์ที่ session นี้ touched (จาก track-file-writes log)

→ พี่เห็นทุกครั้งใน statusline ว่า session แก้ไฟล์ไปกี่ตัว **ไม่ต้องถาม**

---

## 4. Pathdrop Auto-Expand — แก้ 20+ ครั้ง "URL/path เดี่ยว ๆ + เห็นอะไร"

**ไฟล์:** `~/.claude/hooks/pathdrop-expand.sh` (UserPromptSubmit hook)

**ทำงานยังไง:**
- ถ้า prompt = **URL เดียว** (เช่น `https://docs.google.com/...`) → auto-inject context ให้ Claude "อ่าน+สรุปสิ่งที่เห็น"
- ถ้า prompt = **path เดียว** (เช่น `/Users/aexgee/Desktop/foo.xlsx`) → auto-inject context "อ่านไฟล์+สรุป"
- ถ้า prompt มีคำอื่นเยอะกว่า 80 chars → skip (ถือว่าพี่ระบุคำสั่งเองแล้ว)

**ผลลัพธ์:** พี่ paste URL เปล่า ๆ → Claude ไปอ่านและสรุปทันที ไม่ต้องพิมพ์ "เห็นอะไร"

---

## 5. `/keep-going` — Autonomous Mode (already ON)

**Settings ที่เปิดอยู่แล้วใน `~/.claude/settings.json`:**
```json
{
  "skipDangerousModePermissionPrompt": true,
  "alwaysThinkingEnabled": true,
  "effortLevel": "xhigh"
}
```

**ผลลัพธ์:**
- ไม่ prompt ขอ approval ทุก Bash/Edit
- Thinking mode เปิดตลอด (คิดก่อนตอบ)
- Effort สูงสุด (ไม่ประหยัด token)

**คู่กับ feedback memory:** [[feedback_vibe_hacker_mode]] Standing Order #8 "Take initiative, don't wait" — Claude ทำต่อโดยไม่หยุดถาม เว้นแต่งานเสี่ยงจริง ๆ

---

## Impact Summary

| Skill | Prompts saved | Setup time |
|---|---|---|
| #1 Auto-open | 93 | 5 นาที |
| #2 Voice input | ~600+ (typing overhead) | 15 นาที |
| #3 Statusline | 30+ | 3 นาที |
| #4 Pathdrop | 20+ | 5 นาที |
| #5 Autonomous | 15+ ("ทำต่อ ๆ") | 0 (already on) |

**Total เท่ากับ ~158 prompts + typing overhead ทั้งหมด** (จาก 901 total → ประหยัด ~18% + speed 60% ผ่านเสียง)

## Rollback

**ปิด hook ชั่วคราว:** edit `~/.claude/settings.json` เอา entry ออก + restart Claude Code
**Restore full settings:** `cp ~/.claude/settings.json.backup-20260701-114047 ~/.claude/settings.json`
**Restore Karabiner:** `cp ~/.config/karabiner/karabiner.json.backup-20260701-* ~/.config/karabiner/karabiner.json`

## User Actions Required (เตรียมพร้อมใช้)

1. **เปิด Karabiner-Elements.app** — F5 hotkey จะทำงานเมื่อ Karabiner run
2. **ให้ Microphone permission** ครั้งแรกที่กด F5 (System Settings จะถาม)
3. **Restart Claude Code** — hooks ใหม่จะ load
4. **Wait for medium model** (1.5GB) เพื่อความแม่นภาษาไทยดีขึ้น — check: `ls -la ~/whisper-models/`

related: [[behavioral-profile]] · [[prompt-patterns]]
