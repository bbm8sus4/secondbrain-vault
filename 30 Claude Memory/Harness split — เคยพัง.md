---
name: feedback-memory-harness-split
description: 4 harness dirs (.claude/.claude-warp/.claude-cmux/.claude-ghostty) ต้อง sync กัน — เคยแยกกันทำให้หาย 79 sessions
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c43a0a62-0da8-4cce-b114-43e25a68201f
---

Claude Code สร้าง memory dir แยกตาม terminal: `.claude/` (default), `.claude-warp/` (Warp), `.claude-cmux/` (Cmux), `.claude-ghostty/` (Ghostty)

**Why:** เคย split กัน 5 สัปดาห์ — hook เขียนแค่ `.claude/` แต่ Warp อ่านจาก `.claude-warp/` → session log หายไป 79 entries, memory files ต่างกัน 62 ไฟล์ ผู้ใช้รู้สึกว่า Claude จำอะไรไม่ได้

**How to apply:**
- `sync-memory-all-harnesses.sh` รันทุก SessionStart + SessionEnd — merge ไฟล์ล่าสุดข้ามทุก dir
- ถ้าเพิ่ม harness ใหม่ (เช่น Claude Desktop) → เพิ่มใน `HARNESS_DIRS` array
- ถ้าเจอว่า file count ต่างกันระหว่าง dirs → รัน sync ทันที
- SessionEnd hook ต้องเขียน session_log ทั้ง `.claude/` + `.claude-warp/` (+ sync กระจายที่เหลือ)
