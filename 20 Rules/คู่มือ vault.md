# คู่มือ vault — วิธีดูแลสมองที่สอง

> เอกสารกำกับว่า vault นี้ทำงานยังไง · อะไรอัตโนมัติ · อะไรห้ามแตะ · กู้คืนยังไง
> AI agent + คนอ่านอันนี้ก่อนจัดการโครงสร้าง vault · อัปเดต 2026-06-13

---

## 1. โครงสร้างโฟลเดอร์

| โฟลเดอร์ | เก็บอะไร | ใครเขียน |
|---|---|---|
| `00 Inbox` | ของใหม่ยังไม่จัด · Telegram capture · รายงาน `_vault-health.md` | คน + อัตโนมัติ |
| `01 Projects` | โปรเจกต์มี deadline | คน (ตอนนี้ delegate ไป brand folders) |
| `02 Areas` | งานต่อเนื่องไม่จบ | คน |
| `03 Resources` | ความรู้อ้างอิง · playbook · แผนที่ความรู้ (MOC) | คน |
| `04 Archive` | จบ/เลิกแล้ว เก็บไว้ค้น | คน |
| `10 Daily` | daily note | คน |
| `20 Rules` | กติกา AI + คู่มือนี้ | คน |
| `30 Claude Memory` | 🔒 **mirror อัตโนมัติ** จาก Claude memory | **ห้ามแก้** |
| `40 Meeting Notes` | 🔒 **mirror อัตโนมัติ** จาก repo `meeting-notes` | **ห้ามแก้** |
| `EasyCRM / EasyBOT / BoostSMS / EasySlip / Thunder Solution / Friday` | knowledge base รายแบรนด์ | คน + agent |

`01/02/04/10` เว้นว่างโดยตั้งใจ — งานจริงไป brand folders + memory แล้ว (มี `.gitkeep` กันลืม)

## 2. กติกาการตั้งชื่อ

- **Brand folders:** เลขนำ + kebab-case อังกฤษ → `01-Overview.md`, `02-Packages-Pricing.md` … + `หน้าหลัก.md` (index ไทย) + `_assets/` `_chats/`
- **โน้ตทั่วไป (คน):** ภาษาไทยอ่านง่าย ใช้ prefix หมวด → `แผนที่ - X`, `คู่มือ - X`, `กติกา - X`, `โปรเจกต์ - X`
- **Memory mirror (`30 Claude Memory`):** ชื่อไทยอัตโนมัติ — **อย่าตั้งเอง** (ดูข้อ 4)
- **ลิงก์:** ใช้ `[[wikilink]]` เสมอ (ไม่ใช่ markdown link) เพราะรองรับวงเล็บ/ช่องว่าง และต่อ graph ได้ · cross-folder ใช้ absolute เช่น `[[Thunder Solution/หน้าหลัก|Thunder]]` ไม่ใช่ `../`

## 3. ระบบอัตโนมัติ (launchd)

| งาน | สคริปต์ | ความถี่ | log |
|---|---|---|---|
| memory → `30 Claude Memory` + meeting-notes → `40 Meeting Notes` + auto-commit | `~/bin/sync-memory-to-vault.sh` | ทุก 30 นาที | `~/Library/Logs/secondbrain-sync.log` |
| Telegram forward → `00 Inbox` | `~/bin/telegram-vault-capture.py` | ทุก 60 วิ | `~/Library/Logs/vault-capture.log` |
| Friday weekly/monthly recap | `Friday/_scripts/friday_recap.sh` | 23:55 ทุกวัน | `Friday/_logs/recap.log` |
| ตรวจสุขภาพ vault | `~/bin/vault-health.py` | ทุกวัน 09:00 | `~/Library/Logs/vault-health.log` |

## 4. ระบบชื่อไทยแบบ self-healing (สำคัญ)

ไฟล์ใน `30 Claude Memory` แปลงชื่ออังกฤษ → ไทยอัตโนมัติ ตามลำดับ:
1. `~/.claude-warp/projects/-Users-aexgee/memory/.display-names.json` — ชื่อไทยที่ curate ไว้ (**แก้ที่นี่ ไม่ใช่ในโค้ด**)
2. ถ้าไม่มี → ใช้ title จาก `MEMORY.md` (`- [Title](file.md)`) อัตโนมัติ
3. ถ้ายังไม่มี → ชื่ออังกฤษ + เตือนใน log

→ **memory ใหม่ไม่เคยพัง** ขึ้นชื่ออ่านรู้เรื่องเองทันที · อยากได้ชื่อไทยสวย ๆ ค่อยเติม 1 บรรทัดใน `.display-names.json` (ไม่ต้องแตะ Python อีก)

`sync` ยัง rewrite `[[english_slug]]` ในเนื้อ memory → `[[ชื่อไทย|slug]]` ให้ graph เชื่อมกันด้วย

## 5. ห้ามทำ ❌

- **ห้ามแก้ไฟล์ใน `30 Claude Memory/` และ `40 Meeting Notes/`** — เป็น mirror โดน sync เขียนทับทุก 30 นาที แก้ memory ที่ต้นทาง `~/.claude-warp/projects/-Users-aexgee/memory/` เท่านั้น
- ห้ามแก้ชื่อไทยใน `sync-memory-to-vault.py` — ไปแก้ `.display-names.json`
- ห้าม commit `.smart-env/` (50MB embedding cache, gitignore แล้ว)

## 6. Backup & กู้คืน

- vault เป็น **git repo ของตัวเอง** (`~/SecondBrain/.git`) แยกจาก home repo
- **Backup นอกเครื่อง:** private GitHub `bbm8sus4/secondbrain-vault` — `sync.sh` auto-push ทุกรอบ (เน็ตหลุดไม่เป็นไร รอบหน้า push สะสมให้)
- ทุก sync auto-commit → `git -C ~/SecondBrain log` เห็นประวัติทุก 30 นาที
- กู้ไฟล์ที่เผลอลบ/พัง: `git -C ~/SecondBrain checkout <commit> -- "path"`
- **กู้ทั้งเครื่องใหม่:** `git clone https://github.com/bbm8sus4/secondbrain-vault.git ~/SecondBrain`
- ⚠️ repo นี้ **ต้อง private เสมอ** (มีสัญญา/การเงิน/security audit) — ห้ามเปลี่ยนเป็น public
- ดูสุขภาพตอนนี้: `python3 ~/bin/vault-health.py` แล้วเปิด `00 Inbox/_vault-health.md`

## 7. เพิ่มความรู้ใหม่ควรไปไหน

- ข้อมูลแบรนด์ (EasyCRM/EasyBOT/BoostSMS/Friday) → brand folder ตรง ๆ (memory เก็บแค่ pointer)
- ความรู้/playbook ทั่วไป → `03 Resources` + ใส่ `[[link]]` จากแผนที่ที่เกี่ยว
- preference/feedback/pointer ของ Claude → memory ต้นทาง (เดี๋ยว mirror เอง)
- ของเลิกแล้ว → `04 Archive` หรือ mark `(เลิกแล้ว)` ในชื่อ
