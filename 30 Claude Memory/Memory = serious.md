---
name: feedback-memory-serious
description: ผู้ใช้ซีเรียสเรื่อง memory มาก — ต้อง sync อัตโนมัติทุก harness + Obsidian ทุก session ห้ามหลุด
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c43a0a62-0da8-4cce-b114-43e25a68201f
---

ผู้ใช้ถือเรื่อง memory เป็นเรื่องสำคัญมาก — "กูซีเรียสเรื่องนี้" — ต้องจำต่อเนื่องทุก session ไม่ว่าเปิดจาก Warp, Cmux, Ghostty หรือ Desktop

**Why:** ทำงานมาเยอะมาก (263+ sessions) แต่รู้สึกว่า Claude จำน้อย เพราะ memory แยก 4 dirs ไม่ sync กัน + session log หายไป 5 สัปดาห์ เสียเวลาอธิบายซ้ำ

**How to apply:**
- อย่าปล่อยให้ memory split — ถ้าเจอว่า harness dirs ไม่ตรงกัน แก้ทันที
- SessionEnd hook ต้องเขียนทุก dir ไม่ใช่แค่ `.claude/`
- budget ของ summarize hook ต้องสูงพอ (ตอนนี้ $10) — ไม่เสียเงินเพิ่มอยู่แล้ว อย่าประหยัด
- ถ้าผู้ใช้ถามว่า "จำได้มั้ย" ให้ไปอ่าน memory + Obsidian ก่อนตอบ อย่าตอบจากความจำเปล่า
