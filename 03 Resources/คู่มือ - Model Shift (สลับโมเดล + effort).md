---
title: คู่มือ - Model Shift (สลับโมเดล + effort)
type: reference
tags: [tool, claude-code, cmux, tmux, electron, model-switch]
saved: 2026-07-03
---

# Model Shift — คันเกียร์สลับโมเดล Claude Code

Electron widget ลอยหน้าจอ รูป "คันเกียร์รถยนต์" กดเข้าเกียร์แล้วยิงคำสั่ง `/model` (และ `/effort`) เข้าเซสชัน Claude Code ที่รันใน terminal — ต้นฉบับจาก GitHub `milind-soni/stickshift-claude` รองรับแค่ tmux. เราแพตช์ให้รองรับ [[คู่มือ - Cmux|cmux]] ด้วย + เพิ่มแถบปรับ effort.

> ต้นฉบับ DMG: `~/Downloads/ModelShift-1.0.0.dmg` · ซอร์สที่แพตช์แล้ว: `~/Code/modelshift-cmux/src/`

## โครงสร้าง (Electron, โค้ดจริงแค่ ~68KB)
- `main.js` — main process: หา tmux/cmux binary, list panes/surfaces, ยิงคำสั่งผ่าน `execFile` (ไม่ผ่าน shell = ไม่มี injection)
- `preload.js` — expose 5 ฟังก์ชันผ่าน contextBridge (contextIsolation เปิด)
- `renderer/app.js` — UI คันเกียร์ H-pattern ลากได้จริง + tachometer + เสียงเข้าเกียร์

## ผังเกียร์ (map → `/model`)
1 = Haiku 4.5 · 2 = Sonnet 4.6 · 3 = Sonnet 1M · 4 = Opus 4.8 · 5 = Fable 5 · R = Default

## สิ่งที่แพตช์เพิ่ม (2026-07-03)
1. **cmux backend** — list surfaces ผ่าน `cmux --json --id-format both tree --all` (recursive walk แบบ defensive), ยิงด้วย `cmux send --surface <uuid>` + `cmux send-key --surface <uuid> enter`, ปุ่ม kill map เป็น `close-surface`. tmux + cmux รวมใน picker เดียว claude-likely ขึ้นก่อน
2. **แถบ EFFORT** — ปุ่ม 5 อัน LOW/MED/HIGH/XHI/MAX ยิง `/effort <low|medium|high|xhigh|max>` (คำสั่งจริงของ Claude Code — verify จาก binary; xhigh/max มีเฉพาะบางโมเดลเช่น Opus 4.7+) · จำค่าล่าสุดใน localStorage · เข็มวัดรอบกวาดตาม effort
3. **Warp backend + ปุ่มเลือก terminal (2026-07-04)** — แถวปุ่ม `ALL / cmux / Warp / tmux` กรอง target ตาม backend (ปุ่มที่ไม่มี target จะจาง). Warp ไม่มี CLI/socket → ยิงด้วย System Events keystroke เข้า **แท็บ Warp ที่ active** (`osascript`: activate Warp → keystroke คำสั่ง → key code 36). **ต้องเปิด Accessibility permission ให้ Model Shift** (ไม่งั้น error 1002 → widget โชว์ "enable Accessibility"). เลือกเจาะจงแท็บ Warp ไม่ได้ ได้แค่แท็บที่ active. ปุ่ม kill ใช้กับ Warp ไม่ได้.
4. หน้าต่างสูง 530→564→590px (ต้องแก้ทั้ง `main.js` BrowserWindow และ `#chrome` CSS ให้ตรงกัน)

## วิธี build ใหม่หลังแก้ซอร์ส
```bash
cd ~/Code/modelshift-cmux
npx @electron/asar pack src app.asar
cp app.asar "/Applications/Model Shift.app/Contents/Resources/app.asar"
codesign --force --deep --sign - "/Applications/Model Shift.app"   # ad-hoc (Developer ID เดิมหายเพราะแก้ไฟล์)
```

## Gotchas
- cmux socket ขึ้น **Broken pipe** ถ้า process cmux ที่รันอยู่เป็น build เก่า (เปิดค้างข้าม `brew upgrade`) → restart cmux.app แก้ได้
- cmux CLI: key name เป็นตัวเล็ก `enter` · global flag ต้องมาก่อน command (`cmux --json tree --all`) · `cmux version` ใช้ได้โดยไม่ต้องมี socket
- debug log: `~/gearshift.log`

เกี่ยวข้อง: [[คู่มือ - Cmux]]
