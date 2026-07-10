---
title: Claude Code — คู่มือสอนครบชุด (คำสั่ง + โหมด + pin โมเดล + status line)
type: reference
tags: [ai-workshops, claude-code, teaching, cheatsheet, slash-commands, settings, statusline, model-config]
saved: 2026-07-10
updated: 2026-07-10
related: [[Reference-Anthropic-Claude-101-Curriculum]], [[คอร์สสอน AI ด้วย Claude - โครงคอร์ส]]
html: claude-code-commands-guide.html
installer: claude-statusline-installer.sh
---

# Claude Code — คู่มือสอนครบชุด

รวมทุกอย่างสำหรับสอน Claude Code ในไฟล์เดียว:
1. **คำสั่ง slash built-in** (มากับทุกเครื่อง) — แตกหลายมิติ ทำอะไร/ใช้เมื่อไร/บริบท
2. **โหมด permission** (shift+tab) — Plan → bypass
3. **วิธี pin โมเดล** (เช่น Opus 4.6) ให้ติดถาวรทุกเครื่อง
4. **วิธีตั้ง status line** หลายแถว (โมเดล + usage + git) พร้อม installer

ไฟล์ประกอบในโฟลเดอร์เดียวกัน: `claude-code-commands-guide.html` (ชีตปรินต์/ฉาย) · `claude-statusline-installer.sh` (installer status line)

> [!note] แยกให้ออก
> คำสั่งอย่าง `/Chrome-MCP-Owly` · `/CRUD-basic` · `/codex:*` เป็นของที่ **ผู้ใช้เซตเพิ่มเอง** (custom skill / plugin) ไม่ได้ติดมากับพื้นฐาน · built-in มีทั้งหมด **~45 คำสั่ง**

---

## 01 · เริ่มต้น & ขอความช่วยเหลือ

| คำสั่ง | ทำอะไร | ใช้เมื่อไร–เป้าหมาย | ตัวอย่าง |
|---|---|---|---|
| `/help` | ดูคำสั่งทั้งหมด | นึกคำสั่งไม่ออก อยากเห็นเมนูรวม | เพิ่งเปิดใช้ครั้งแรก |
| `/status` | เวอร์ชัน โมเดล บัญชีที่ล็อกอิน | อยากรู้ว่าใช้โมเดล/บัญชีอะไรอยู่ | งงว่าทำไมช้า — เช็คว่า Opus หรือ Sonnet |
| `/doctor` | ตรวจสุขภาพการติดตั้ง | มีอะไรพัง อยากหาสาเหตุ | MCP/เน็ตไม่ทำงาน |
| `/release-notes` | ดูของใหม่ที่เพิ่งอัปเดต | อัปเวอร์ชันแล้วอยากรู้มีอะไรเพิ่ม | เห็นปุ่มใหม่ในเมนู |

## 02 · จัดการบทสนทนา & context

| คำสั่ง | ทำอะไร | ใช้เมื่อไร–เป้าหมาย | ตัวอย่าง |
|---|---|---|---|
| `/clear` (= /new /reset) | ล้างแชท เริ่มใหม่หมด | เปลี่ยนเรื่องคุย กันเรื่องเก่ามากวน/เปลืองโทเคน | คุยงาน A เสร็จ จะเริ่มงาน B |
| `/compact` | บีบอัดบทสนทนาให้สั้น (เก็บใจความ) | คุยยาวมาก context ใกล้เต็ม แต่ยังทำต่อ | แก้โค้ดมาเป็นชั่วโมง เริ่มช้า |
| `/context` | ดูว่าใช้ context ไปเท่าไหร่ | อยากรู้ว่าเหลือที่คุยอีกแค่ไหน | รู้สึกมันเริ่มลืม |
| `/resume` (= /continue) | กลับไปทำงานที่คุยค้างไว้ | ปิดไปแล้ว อยากสานต่อของเดิม | เมื่อวานแก้บั๊กค้าง |
| `/rewind` (= /undo /checkpoint) | ย้อนกลับไปจุดก่อนหน้า | มันทำพลาด อยากถอยกลับก่อนพัง | Claude แก้ผิดไฟล์ |
| `/export` | บันทึกบทสนทนาเป็นไฟล์ | อยากเก็บบันทึก/ส่งต่อ | คุยได้คำตอบดีๆ เก็บไว้ |

## 03 · โมเดล & การตั้งค่า

| คำสั่ง | ทำอะไร | ใช้เมื่อไร–เป้าหมาย | ตัวอย่าง |
|---|---|---|---|
| `/model` | สลับโมเดล AI | อยากฉลาดขึ้น (Opus) หรือเร็ว/ประหยัด (Sonnet/Haiku) | งานคิดหนัก → Opus · งานง่าย → Haiku |
| `/config` | เปิดหน้าตั้งค่า (ธีม โมเดล ฯลฯ) | อยากปรับหน้าตา/ค่าเริ่มต้น | เปลี่ยนธีมมืด-สว่าง |
| `/permissions` (= /allowed-tools) | ตั้งกฎว่าให้รันอะไรได้บ้าง | ลดการถาม yes/no ซ้ำๆ กับคำสั่งที่ไว้ใจ | มันถาม npm ทุกครั้ง → อนุญาตถาวร |
| `/vim` | เปิดโหมดพิมพ์แบบ vim | ถนัด vim อยากใช้คีย์ลัดเดิม | คนคุ้น vim |

## 04 · โปรเจกต์ & ความจำ

| คำสั่ง | ทำอะไร | ใช้เมื่อไร–เป้าหมาย | ตัวอย่าง |
|---|---|---|---|
| `/init` | สร้าง CLAUDE.md อธิบายโปรเจกต์ | เริ่มใช้กับ repo ใหม่ ให้มันรู้จักโครงสร้าง | โคลนโปรเจกต์มา |
| `/memory` | แก้ไฟล์ความจำถาวร | ให้จำสไตล์/กฎของเรา ข้ามแชท | อยากให้ตอบไทยเสมอ |
| `/add-dir` | เพิ่มโฟลเดอร์ให้เข้าถึงไฟล์ | ต้องใช้ไฟล์นอกโฟลเดอร์ปัจจุบัน | โค้ดอยู่คนละที่กับ config |

## 05 · งานโค้ด & รีวิว

| คำสั่ง | ทำอะไร | ใช้เมื่อไร–เป้าหมาย | ตัวอย่าง |
|---|---|---|---|
| `/plan` | เข้าโหมดวางแผนก่อนลงมือ | งานใหญ่/ซับซ้อน อยากเห็นแผนก่อนแก้จริง | จะรื้อฟีเจอร์ใหญ่ |
| `/code-review` | รีวิวโค้ดที่เพิ่งแก้ หาบั๊ก | แก้เสร็จ อยากให้ตรวจก่อน commit | เขียนฟังก์ชันใหม่ |
| `/security-review` | ตรวจช่องโหว่ความปลอดภัย | ก่อนขึ้น production | มีฟอร์มรับข้อมูลผู้ใช้ |
| `/review` | รีวิว Pull Request บน GitHub | มี PR รอ อยากดูก่อน merge | เพื่อนส่ง PR มา |

## 06 · เครื่องมือ & การเชื่อมต่อ

| คำสั่ง | ทำอะไร | ใช้เมื่อไร–เป้าหมาย | ตัวอย่าง |
|---|---|---|---|
| `/mcp` | จัดการ MCP server (เครื่องมือเสริม) | ต่อ Claude กับ Chrome/Drive/DB ฯลฯ | จะให้คุมเบราว์เซอร์ |
| `/agents` | จัดการ subagent (ผู้ช่วยย่อย) | อยากมีผู้ช่วยเฉพาะทางแยกงาน | งานหลายด้านพร้อมกัน |
| `/hooks` | ดู/ตั้ง automation อัตโนมัติ | ให้ทำอะไรเองทุกครั้งที่เกิดเหตุ X | เปิดไฟล์ผลลัพธ์อัตโนมัติ |

## 07 · บัญชี & ค่าใช้จ่าย

| คำสั่ง | ทำอะไร | ใช้เมื่อไร–เป้าหมาย | ตัวอย่าง |
|---|---|---|---|
| `/usage` (= /cost /stats) | ดูยอดใช้งาน/ค่าใช้จ่าย | อยากรู้ใช้ไปเท่าไหร่ เหลือโควตาแค่ไหน | ใกล้สิ้นเดือน |
| `/login` `/logout` | เข้า/ออกจากบัญชี | สลับบัญชี หรือเครื่องใหม่ | เปลี่ยนไปบัญชีบริษัท |
| `/feedback` (= /bug) | รายงานปัญหา/ส่งความเห็น | เจอบั๊ก อยากแจ้งทีม Anthropic | คำสั่งทำงานเพี้ยน |

---

## 08 · โหมด Permission — กด `shift + tab` วนสลับ

คุมว่า Claude ต้องขออนุญาตก่อนลงมือแค่ไหน · **เขียว = ระวังสุด, แดง = ปล่อยสุด**

| โหมด | แก้ไฟล์เอง? | รันคำสั่งเอง? | ความเสี่ยง | ใช้เมื่อ |
|---|---|---|---|---|
| **Plan** ⏸ | ไม่ | ไม่ | ต่ำสุด | งานใหญ่/สำคัญ/production · อยากให้คิดก่อนทำ · มือใหม่ |
| **Default** | ถามก่อน | ถามก่อน | ต่ำ | อยากคุมทุกก้าว · งานทั่วไปที่ยังไม่ไว้ใจ |
| **accept edits** | ใช่ | ถามก่อน | กลาง | แก้โค้ดเยอะๆ ที่ไว้ใจได้ แต่ยังคุมคำสั่งอันตราย |
| **auto** | ใช่ | ใช่ (เกือบหมด) | สูง | งานไหลยาว อยากให้เดินเองจนจบ · เชื่อมือแล้ว |
| **bypass permissions** | ใช่ | ใช่ (ทั้งหมด) | สูงสุด | มั่นใจจริงๆ หรืออยู่ใน sandbox/เครื่องแยกเท่านั้น · ไม่แนะนำมือใหม่ |

- **Plan mode** = อ่าน/วิเคราะห์อย่างเดียว เสนอแผนมาให้ดูก่อน รออนุมัติค่อยลงมือ
- **accept edits** = อนุมัติการแก้ไฟล์ให้เอง แต่ยังถามก่อนรัน shell ที่เสี่ยง
- **auto** = อนุมัติเกือบทุกอย่างเอง รวมรันคำสั่ง ทำงานต่อเนื่อง
- **bypass** = ไม่ถามอะไรเลย รันอะไรก็ได้โดยไม่เตือน (สีแดง = อันตราย)

---

## คำสั่ง built-in อื่นๆ ที่ควรรู้

`/effort` (ระดับความคิดหนัก low→max) · `/copy` (คัดลอกคำตอบล่าสุด) · `/cd` (ย้ายโฟลเดอร์) · `/diff` (ดูความต่างโค้ด) · `/skills` (ดู skill ที่มี) · `/ide` (เชื่อม VS Code/JetBrains) · `/terminal-setup` (คีย์ลัด terminal) · `/plugin` (จัดการปลั๊กอิน) · `/loop` (รันซ้ำเป็นรอบ) · `/background` (แยกไปรันเบื้องหลัง) · `/powerup` (บทเรียนฟีเจอร์แบบโต้ตอบ)

---

## 09 · วิธี pin โมเดลให้ติดถาวร (เช่น Opus 4.6)

**หลักการ:** `/model` เลือกได้ก็จริง แต่ **ค่าใน `settings.json` ชนะทุกครั้งตอน restart** — ถ้า pin ผิดที่ จะรู้สึกว่า "มันดื้อ ไม่ยอมเปลี่ยน" · precedence: managed > `--model` (flag) > `settings.local.json` > `settings.json` (project) > `settings.json` (user)

> [!warning] ข้อจำกัด
> เมนู `/model` เป็นลิสต์ตายตัวฝังในแอป (Default/Opus/Fable/Sonnet/Haiku) — **เพิ่มโมเดลรุ่นเก่าเป็นบรรทัดให้เลือกไม่ได้** แต่ pin ทำให้มันเป็นตัวที่รันจริงทุกครั้ง (บรรลุเป้าหมาย) สลับ on-demand ด้วย `/model claude-opus-4-6[1m]` หรือ `--model`

**แบบ A — Prompt (วางในแชท Claude Code เครื่องไหนก็ได้):**
```
ช่วยตั้งค่าให้ Claude Code ใช้โมเดล Opus 4.6 (1M context) เป็นค่าเริ่มต้นถาวร ทำตามนี้เป๊ะ ห้ามแก้ไฟล์อื่น ห้ามลบอะไร:
1. สำรอง ~/.claude/settings.json เป็น settings.json.bak ก่อน (ถ้ายังไม่มีไฟล์ ให้สร้างใหม่เป็น {})
2. ตั้ง key "model" = "claude-opus-4-6[1m]" — มีแล้วแก้ค่า ยังไม่มีให้เพิ่ม คง key อื่นไว้ (JSON ถูก syntax)
3. เช็คว่าไม่มี ~/.claude/settings.local.json ที่มี key "model" มาทับ ถ้ามีให้ลบเฉพาะ key นั้น
4. ทดสอบว่ายิงติด: claude --model 'claude-opus-4-6[1m]' -p "reply OK"
5. สรุปว่าตั้งที่ไฟล์ไหน ค่าเก่าคืออะไร และบอกให้ restart
ถ้าเทส error ว่าไม่มีโมเดลนี้ ให้เปลี่ยนเป็น "claude-opus-4-6" (ไม่มี [1m]) แล้วลองใหม่
```

**แบบ B — คำสั่งเดียว (Terminal ตรงๆ ไม่ต้องพึ่ง AI):**
```bash
python3 - <<'PY'
import json, os, shutil
f = os.path.expanduser("~/.claude/settings.json")
os.makedirs(os.path.dirname(f), exist_ok=True)
data = {}
if os.path.isfile(f):
    shutil.copy2(f, f + ".bak")           # สำรองก่อน
    try: data = json.load(open(f))
    except: data = {}
old = data.get("model", "(ยังไม่มี)")
data["model"] = "claude-opus-4-6[1m]"     # <-- เปลี่ยนโมเดลตรงนี้
json.dump(data, open(f, "w"), indent=2, ensure_ascii=False)
print(f"pinned {f}\n  model: {old} -> {data['model']}\n  backup: {f}.bak")
PY
claude --model 'claude-opus-4-6[1m]' -p "reply OK"   # ทดสอบว่ายิงติด
```

**หลังตั้ง:** ต้อง **restart** · เช็คด้วย `/status` · ถอยกลับ `cp ~/.claude/settings.json.bak ~/.claude/settings.json`
**ไม่มีแพ็ก 1M?** ตัด `[1m]` เหลือ `claude-opus-4-6` เฉยๆ
**หมายเหตุ:** เครื่องที่ต่อหลาย terminal อาจมีหลาย config dir (`~/.claude`, `~/.claude-cmux`, …) ต้อง pin ให้ครบทุกอันที่ใช้จริง

---

## 10 · วิธีตั้ง Status line หลายแถว

**หลักการ:** ตั้ง `statusLine` แบบ `type: "command"` → Claude Code **ป้อน JSON ข้อมูล session เข้า stdin** ของสคริปต์ (โมเดล, context, usage, git) → เอา**ข้อความที่สคริปต์ print**ไปแสดง แต่ละบรรทัด = 1 แถว

ผลลัพธ์ (ตรงกับที่ใช้จริง):
```
Opus 4.6 (1M context)  ███░░░░░░░░░░░░░░░░░  15% | 150k/1.0m
Current  ███░░░░░░░░░░░░░░░░░  15% | Jul 10, 6:10 PM
Weekly   ███░░░░░░░░░░░░░░░░░  14% | Jul 12, 8:00 PM
📁 aexgee  ⎇ main*
```

**วิธี 1 — Installer ไฟล์เดียว (แนะนำ):** ก็อป `claude-statusline-installer.sh` ไปเครื่องอื่นแล้วรัน
```bash
bash claude-statusline-installer.sh
```
มันจะ: ลง `jq` อัตโนมัติ → เขียน `~/.claude/statusline.sh` → ต่อเข้า `settings.json` → สำรอง `.bak` ครบในตัว

**วิธี 2 — Prompt (ให้ AI ติดตั้งให้):**
```
ช่วยตั้ง status line หลายแถวให้ Claude Code ห้ามแตะไฟล์อื่น:
1. เช็ค/ลง jq ถ้ายังไม่มี
2. สร้าง ~/.claude/statusline.sh อ่าน JSON จาก stdin แล้ว print 4 แถว:
   - แถว1: ชื่อโมเดล + ขนาด context + progress bar + % + tokens (.model.display_name, .context_window)
   - แถว2: "Current" = usage 5 ชม. + เวลารีเซ็ต (.rate_limits.five_hour)
   - แถว3: "Weekly" = usage 7 วัน (.rate_limits.seven_day)
   - แถว4: 📁 โฟลเดอร์ + ⎇ git branch + * ถ้ามีไฟล์ค้าง (.workspace.current_dir)
   ใช้ jq ดึงค่า, bar ใช้ █/░ กว้าง 20, รองรับ date ทั้ง macOS (-r) และ Linux (-d)
3. chmod +x
4. เพิ่ม key statusLine ใน ~/.claude/settings.json = {"type":"command","command":"bash ~/.claude/statusline.sh","padding":0} สำรองไฟล์เดิมก่อน คง key อื่นไว้
5. บอกให้ restart
```

**วิธี 3 — Manual (3 ขั้น):**
1. ลง jq — `brew install jq` (Mac) / `sudo apt install jq` (Linux)
2. วางสคริปต์ที่ `~/.claude/statusline.sh` แล้ว `chmod +x`
3. ต่อ config ใน `~/.claude/settings.json`:
```json
{ "statusLine": { "type": "command", "command": "bash ~/.claude/statusline.sh", "padding": 0 } }
```

**เตือนผู้เรียน:**
- ต้อง **restart** ถึงเห็นผล · ต้องมี `jq` (เช็ค `jq --version`) ไม่งั้นแถวว่าง
- แถว Current/Weekly โผล่เฉพาะแพ็กที่มี rate limit (Max/Team) — ไม่มี field สคริปต์ซ่อนแถวให้เอง
- แถว "✎ N files" ต้องมี hook แยก (track-file-writes) — ไม่มีก็ข้ามเงียบๆ

---

อ้างอิงทางการ: `code.claude.com/docs/en/commands` · `code.claude.com/docs/en/statusline` · `code.claude.com/docs/en/model-config`
