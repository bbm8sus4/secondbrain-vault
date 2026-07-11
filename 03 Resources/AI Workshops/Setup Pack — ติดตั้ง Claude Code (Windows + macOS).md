---
title: Setup Pack — ติดตั้ง & ตั้งค่า Claude Code (Windows + macOS)
type: reference
tags: [ai-workshops, teaching, setup, claude-code, windows, macos, copy-paste]
saved: 2026-07-11
related: [[Reference — Claude Code คำสั่ง built-in (ฉบับสอน)]], [[Prompt สอน — Use Case ง่ายๆ (ผู้เริ่มต้น)]]
source: code.claude.com/docs/en/setup (verified 2026-07-11)
---

# Setup Pack — ติดตั้ง & ตั้งค่า Claude Code

ก็อปทีละบล็อกไปวางได้เลย · แยก **macOS** กับ **Windows** ชัดเจน · จบด้วย prompt เดียวให้ Claude ตั้งค่าที่เหลือให้เอง

> [!warning] ต้องมีก่อน
> **Claude Pro / Max / Team subscription** — แพลนฟรีของ Claude.ai **ใช้ Claude Code ไม่ได้** · macOS 13+ หรือ Windows 10 (1809+)

---

## A · macOS

### A1. ติดตั้ง Claude Code (เลือกวิธีเดียว)
วิธีแนะนำ — native installer (อัปเดตตัวเองอัตโนมัติ):
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
หรือถ้าใช้ Homebrew อยู่แล้ว:
```bash
brew install --cask claude-code
```
(ยังไม่มี Homebrew? ติดตั้งก่อนด้วยบรรทัดนี้)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### A2. ติดตั้ง jq (จำเป็นถ้าจะใช้ status line)
```bash
brew install jq
```

### A3. เริ่มใช้ + ล็อกอิน (เปิดเบราว์เซอร์ให้ล็อกอิน)
```bash
claude
```

### A4. ตรวจว่าติดตั้งสำเร็จ
```bash
claude --version
claude doctor
```

---

## B · Windows

> ใช้ **PowerShell** (มี native support แล้ว ไม่ต้องพึ่ง WSL) · แนะนำติดตั้ง Git for Windows ด้วย เพื่อเปิดใช้ Bash tool

### B1. ติดตั้ง Claude Code (เลือกวิธีเดียว) — วางใน PowerShell
วิธีแนะนำ — native installer (อัปเดตตัวเองอัตโนมัติ):
```powershell
irm https://claude.ai/install.ps1 | iex
```
หรือผ่าน winget:
```powershell
winget install Anthropic.ClaudeCode
```

### B2. ติดตั้ง Git for Windows (แนะนำ — เปิดใช้ Bash tool)
```powershell
winget install Git.Git
```
ถ้า Claude หา bash ไม่เจอ ให้เพิ่มบรรทัดนี้ใน `~/.claude/settings.json`:
```json
{ "env": { "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe" } }
```

### B3. ติดตั้ง jq (จำเป็นถ้าจะใช้ status line)
```powershell
winget install jqlang.jq
```

### B4. เริ่มใช้ + ล็อกอิน (เปิดเบราว์เซอร์ให้ล็อกอิน)
```powershell
claude
```

### B5. ตรวจว่าติดตั้งสำเร็จ
```powershell
claude --version
claude doctor
```

---

## C · ตั้งค่าให้พร้อมใช้ — วิธีง่ายสุด (วางในแชท Claude Code)

หลังติดตั้ง+ล็อกอินเสร็จ พิมพ์ `claude` เปิดขึ้นมา แล้ววาง prompt นี้ให้ Claude ตั้งค่าที่เหลือให้เอง (มันจะดู OS แล้วทำให้เหมาะเอง):
```
ช่วยตั้งค่า Claude Code บนเครื่องนี้ให้พร้อมใช้งาน ตรวจ OS ก่อนแล้วทำให้เหมาะกับเครื่อง ห้ามแก้ไฟล์อื่นนอกจากที่จำเป็น:
1. สำรอง ~/.claude/settings.json ก่อน (ถ้ายังไม่มีให้สร้างใหม่)
2. ตั้งโมเดลเริ่มต้นเป็น Opus รุ่นล่าสุด (เพิ่ม key "model" ใน settings.json) — ถ้าฉันอยากได้รุ่นเจาะจงจะบอกทีหลัง
3. ตั้ง status line หลายแถว (โมเดล + context + usage + git branch) ให้รองรับ OS ปัจจุบัน และเช็คว่ามี jq แล้ว
4. ตรวจ claude doctor ว่าไม่มี error
5. สรุปว่าตั้งอะไรไปบ้าง ค่าเดิมคืออะไร และต้อง restart ไหม
```
> อยากล็อกโมเดลเป็นรุ่นเจาะจง (เช่น Opus 4.6)? ดูวิธี pin แบบละเอียดใน [[Reference — Claude Code คำสั่ง built-in (ฉบับสอน)]] หมวด 9

---

## D · ตั้งค่าแบบ Manual (ถ้าไม่อยากพึ่ง prompt)

แก้ไฟล์ `~/.claude/settings.json` (Windows: `C:\Users\<ชื่อ>\.claude\settings.json`) ใส่ค่านี้:
```json
{
  "model": "claude-opus-4-6[1m]",
  "statusLine": { "type": "command", "command": "bash ~/.claude/statusline.sh", "padding": 0 }
}
```
- ตัดโมเดลรุ่นเจาะจงได้ ถ้าอยากใช้ค่า default → ลบบรรทัด `"model"` ออก
- status line ต้องมีไฟล์สคริปต์ด้วย — ดูตัวติดตั้งสำเร็จรูปที่ [[Reference — Claude Code คำสั่ง built-in (ฉบับสอน)]] หมวด 10 (`claude-statusline-installer.sh`)
- แก้ settings.json แล้วต้อง **restart** Claude Code

---

## สรุปคำสั่งที่ใช้บ่อย (ทั้ง 2 OS)

| ต้องการ | คำสั่ง |
|---|---|
| เปิด Claude Code | `claude` |
| สั่งงานทีเดียวจบ | `claude "แก้บั๊กให้หน่อย"` |
| ถามแล้วออกเลย | `claude -p "อธิบายโค้ดนี้"` |
| ทำงานต่อจากที่ค้าง | `claude -c` |
| ดูเวอร์ชัน | `claude --version` |
| ตรวจปัญหาการติดตั้ง | `claude doctor` |
| ดูคำสั่งในแอป | พิมพ์ `/help` |

---

อ้างอิงทางการ: `code.claude.com/docs/en/setup` (เช็ค 2026-07-11) · related: [[Reference — Claude Code คำสั่ง built-in (ฉบับสอน)]]
