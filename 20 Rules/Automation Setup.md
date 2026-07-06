---
title: Automation Setup — ติดตั้งระบบอัตโนมัติบนเครื่องใหม่
type: schema-playbook
source: ~/bin/*.py + ~/Library/LaunchAgents/com.aexgee.*.plist (สำเนาใน 20 Rules/_automation/)
source_date: 2026-07-06
imported: 2026-07-06T21:30:00
last_verified: 2026-07-06
status: live
tags: [schema, automation, launchd, setup, portability]
related:
  - "[[WIKI]]"
  - "[[คู่มือ vault]]"
---

# Automation Setup — ติดตั้งระบบอัตโนมัติบนเครื่องใหม่

> vault นี้มี automation 4 ตัวที่รันผ่าน launchd บน macOS — เดิมผูกกับเครื่องเดียว
> ตอนนี้สำเนาสคริปต์ + plist ทั้งหมดถูก version ไว้ใน `20 Rules/_automation/` แล้ว
> ย้ายเครื่องเมื่อไหร่ ทำตามขั้นตอนล่างนี้ vault กลับมา "มีชีวิต" เหมือนเดิม

## ตาราง job ทั้งหมด

| Job (launchd label) | สคริปต์ | ความถี่ | ทำอะไร |
|---|---|---|---|
| `com.aexgee.memory-vault-sync` | `sync-memory-to-vault.py` | ทุก 30 นาที | mirror memory จาก `~/.claude-warp/projects/-Users-aexgee/memory/` → `30 Claude Memory/` (แปลชื่อเป็นไทย) + git pull/rsync meeting-notes → `40 Meeting Notes/` + git auto-commit vault |
| `com.aexgee.inbox-auto-ingest` | `inbox-auto-ingest.py` | ทุก 3 นาที | route ไฟล์ใน `00 Inbox/` ตาม frontmatter tag (เช่น `clippings` → `03 Resources/Clippings/`) + append `log.md` |
| `com.aexgee.vault-capture` | `telegram-vault-capture.py` | ต่อเนื่อง | รับข้อความ/รูปจากบอท Telegram → `00 Inbox/Telegram <วันที่>.md` ภายใน 1 นาที |
| `com.aexgee.vault-health` | `vault-health.py` | ทุกวัน 09:00 | สแกน dead links / orphans / mirror drift → เขียน `00 Inbox/_vault-health.md` |

## ติดตั้งบนเครื่องใหม่ (5 ขั้น)

```bash
# 1. clone vault (repo: secondbrain-vault) ไปที่ ~/SecondBrain
git clone <remote-url> ~/SecondBrain

# 2. วางสคริปต์
mkdir -p ~/bin
cp ~/SecondBrain/20\ Rules/_automation/*.py ~/SecondBrain/20\ Rules/_automation/*.sh ~/bin/
chmod +x ~/bin/*.py ~/bin/*.sh

# 3. secret ของ Telegram bot (ไฟล์นี้ไม่อยู่ใน git — ต้องสร้างใหม่)
cat > ~/.vault-capture.env <<'EOF'
TELEGRAM_BOT_TOKEN=<token จาก BotFather>
ALLOWED_USERS=<telegram user id, คั่นด้วย comma>
EOF

# 4. ลง launchd jobs
cp ~/SecondBrain/20\ Rules/_automation/com.aexgee.*.plist ~/Library/LaunchAgents/
for j in inbox-auto-ingest memory-vault-sync vault-capture vault-health; do
  launchctl load ~/Library/LaunchAgents/com.aexgee.$j.plist
done

# 5. ตรวจว่าทุกตัวขึ้น
launchctl list | grep aexgee
```

## เงื่อนไขที่เครื่องใหม่ต้องมี

- macOS + python3 (สคริปต์ใช้ stdlib ล้วน ไม่ต้อง pip install)
- git configured (ชื่อ/email + สิทธิ์ push repo `secondbrain-vault` และ pull repo `meeting-notes`)
- path memory ต้นทาง `~/.claude-warp/projects/-Users-aexgee/memory/` — ถ้า username เครื่องใหม่ไม่ใช่ `aexgee` ต้องแก้ path ใน `sync-memory-to-vault.py` + `vault-health.py` (ตัวแปร `MEM_SRC`) และใน plist ทุกไฟล์
- Obsidian + plugin `smart-connections` (ตัวเดียวที่ใช้)

## ตรวจสุขภาพหลังติดตั้ง

```bash
launchctl list | grep aexgee                       # ต้องเห็นครบ 4 ตัว
python3 ~/bin/vault-health.py                      # รัน lint มือหนึ่งรอบ
tail ~/Library/Logs/inbox-auto-ingest.log          # ดู route ล่าสุด
grep "^## \[" ~/SecondBrain/log.md | tail -5       # ดู log เดิน
```

## กติกาดูแลสำเนา

- **Source of truth = `~/bin/`** — แก้สคริปต์ที่นั่น แล้ว copy ทับเข้า `20 Rules/_automation/` ทุกครั้ง (กัน drift)
- plist แก้ที่ `~/Library/LaunchAgents/` แล้ว `launchctl unload` + `load` ใหม่ + copy สำเนาเข้า vault
- ห้าม commit `~/.vault-capture.env` หรือ token ใด ๆ เข้า vault เด็ดขาด
