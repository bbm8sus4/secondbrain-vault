---
name: reference-memory-sync-system
description: "Memory auto-sync ทุก harness (4 dirs) + Obsidian — SessionStart/End hooks, backfill script, vault mirror ทุก 30 นาที"
metadata: 
  node_type: memory
  type: reference
  originSessionId: c43a0a62-0da8-4cce-b114-43e25a68201f
---

# Memory Sync System

ระบบจำของ Claude Code ที่ sync อัตโนมัติทุก harness + Obsidian vault

## ปัญหาเดิม (แก้ 2026-07-16)

- Memory แยก 4 dirs ไม่ sync กัน → session เปิดจาก Warp ไม่เห็นข้อมูลที่เขียนจาก Cmux
- SessionEnd hook เขียนแค่ `.claude/` → Warp (`.claude-warp/`) ไม่ได้ entries
- Budget $0.50 ไม่พอสรุป session ยาวๆ → โดน `Exceeded USD budget` สรุปไม่จบ
- Obsidian mirror ได้แค่ทิศเดียว (memory → vault) ทุก 30 นาที

## สถาปัตยกรรมปัจจุบัน

```
4 Harness Dirs (source of truth ร่วม):
  ~/.claude/projects/-Users-aexgee/memory/
  ~/.claude-warp/projects/-Users-aexgee/memory/
  ~/.claude-cmux/projects/-Users-aexgee/memory/
  ~/.claude-ghostty/projects/-Users-aexgee/memory/

Obsidian Mirror (read-only):
  ~/SecondBrain/30 Claude Memory/
```

## Flow

```
SessionStart → sync-memory-all-harnesses.sh (merge 4 dirs + vault sync)
Session ทำงาน (เห็น memory ล่าสุดไม่ว่าเปิดจากไหน)
SessionEnd → summarize-session.sh ($10 budget, เขียนทั้ง .claude + .claude-warp)
           → sync-memory-all-harnesses.sh (กระจายให้ทุก dir + vault)
launchd ทุก 30 นาที → sync-memory-to-vault.sh (memory → Obsidian + Meeting Notes + git push)
```

## ไฟล์สำคัญ

| ไฟล์ | หน้าที่ |
|---|---|
| `~/bin/sync-memory-all-harnesses.sh` | merge ไฟล์ล่าสุดข้าม 4 dirs + trigger vault sync |
| `~/bin/sync-memory-to-vault.sh` | shell wrapper: memory→vault + meeting-notes + git commit+push |
| `~/bin/sync-memory-to-vault.py` | Python: แปลงชื่อ EN→TH, copy ไป `30 Claude Memory/` |
| `~/.claude/hooks/summarize-session.sh` | SessionEnd: spawn headless claude สรุป 1 บรรทัด |
| `~/Library/LaunchAgents/com.aexgee.memory-vault-sync.plist` | launchd ทุก 1800s (30 นาที) |

## Settings ที่เกี่ยว

- `~/.claude/settings.json` → SessionStart hook เรียก `sync-memory-all-harnesses.sh`
- SessionEnd hook `--max-budget-usd 10.00` (ไม่เสียเงินเพิ่ม กิน token จาก Max sub)

## Backfill (one-time, 2026-07-16)

- เก็บ 78 sessions ย้อนหลัง (17 มิ.ย. - 16 ก.ค.) ที่ hook เขียนไม่จบ
- ดึง user messages จาก transcript JSONL → agent สรุป → append เข้า session_log
- ก่อน 187 entries → หลัง 263 entries

## How to apply

- ถ้าเพิ่ม harness ใหม่ (เช่น Claude Desktop) → เพิ่ม path ใน `HARNESS_DIRS` array ใน `sync-memory-all-harnesses.sh`
- ห้ามแก้ไฟล์ใน `30 Claude Memory/` ใน Obsidian → แก้ที่ต้นทาง memory dir แล้วรอ sync
- ถ้า sync พัง → ดู log ที่ `~/Library/Logs/memory-harness-sync.log` และ `~/Library/Logs/secondbrain-sync.log`
