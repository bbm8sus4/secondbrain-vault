# Chrome MCP — doctor autonomy stack + rollback (2026-07-18)

เป้าหมายตามคำสั่ง: **ทำงานเต็มที่ + เร็วขึ้น + อิสระไม่ต้องควบคุม ห้ามแย่ลง**
หลักการ: ไม่แตะ native server / extension เลย (ของเดิมดีอยู่แล้ว — fork `itorz7/mcp-chrome` มี auto-connect + keepalive + reconnect ในตัว) — เพิ่มเฉพาะชั้น "รอบๆ" ให้ระบบดูแลตัวเอง

## ของใหม่ 5 ชิ้น

| ชิ้น | ที่อยู่ | ทำอะไร |
|---|---|---|
| `chrome-mcp-doctor` | `~/bin/chrome-mcp-doctor` | เช็ค+ซ่อมพอร์ต: เปิด Chrome โปรไฟล์ที่ map ไว้ รอพอร์ตขึ้น ≤30s. โหมด `--status` / `--quiet` / `--port N` / `--hook` |
| Port map | `~/.config/chrome-mcp/doctor.conf` | `12306=Profile 1` (โปรไฟล์ "A"). 12307 comment ไว้ |
| Statusline row 6 | `~/.claude/statusline.sh` | `⚙ Chrome MCP 12306 ✓/✗` — ทุก harness ใช้ไฟล์เดียวกัน |
| PreToolUse hook | settings.json ทั้ง 4 harness | matcher `mcp__chrome-mcp.*` → `doctor --hook` → พอร์ตตาย = เปิด Chrome ให้เองก่อน tool call วิ่ง (lazy heal, exit 0 เสมอ ไม่ block) |
| Permissions + registration | settings.json + .claude.json ทั้ง 4 harness | allow chrome-mcp tools/curl helper/doctor (7 รายการ) + ลงทะเบียน chrome-mcp, chrome-mcp-kuan ครบ → หมดปัญหา "tools not loaded" |

## การใช้งาน

```bash
chrome-mcp-doctor            # เช็คทุกพอร์ต + ซ่อมตัวที่ตาย
chrome-mcp-doctor --status   # เช็คเฉยๆ
```

ปกติไม่ต้องเรียกเอง — hook ซ่อมให้ตอนกำลังจะใช้ tool, statusline โชว์สถานะตลอด

## สิ่งที่ตั้งใจ "ไม่ทำ" (บันทึกเหตุผลไว้)

- **ไม่เพิ่ม auth token** บน native server — user สั่งชัด: อิสระ/เร็วมาก่อน ห้ามเพิ่ม friction (ความเสี่ยง: process ในเครื่องเรียก port 12306 ได้ — ยอมรับได้เพราะเครื่องส่วนตัว)
- **ไม่มี background watchdog** เปิด Chrome เอง — น่ารำคาญ ใช้ lazy heal ผ่าน hook แทน
- **ไม่แตะโค้ด server/extension** — ไม่ต้อง rebuild ไม่ต้อง reload extension ไม่มีความเสี่ยงพัง

## เวอร์ชั่นเก่า (ก่อนแก้ 2026-07-18) — สำหรับ rollback

ทุกไฟล์ที่แก้มี backup นามสกุล `.bak-chromemcp` วางข้างไฟล์จริง:

| ไฟล์ | สภาพก่อนแก้ |
|---|---|
| `~/.claude/statusline.sh` | 5 rows ไม่มี Chrome MCP row (bak = ต้นฉบับเป๊ะ, diff เฉพาะ block row 6) |
| `~/.claude/settings.json` | ไม่มี permissions.allow, PreToolUse มีแค่ gitnexus hook |
| `~/.claude-warp/settings.json` | ไม่มี permissions.allow, hooks 4 events เดิม |
| `~/.claude-ghostty/settings.json` | ไม่มี permissions.allow |
| `~/.claude-cmux/settings.json` | ไม่มี permissions.allow |
| `~/.claude-warp/.claude.json` | mcpServers มีแค่ `obsidian` |
| `~/.claude-ghostty/.claude.json` | mcpServers ว่าง `{}` |
| `~/.claude-cmux/.claude.json` | **ไม่มีไฟล์** (สร้างใหม่ทั้งไฟล์ — rollback คือลบทิ้ง) |
| `~/.claude.json` (global) | **ไม่ได้แก้** — มี chrome-mcp + chrome-mcp-kuan อยู่แล้ว |
| `~/bin/chrome-mcp-doctor`, `~/.config/chrome-mcp/doctor.conf` | **ไฟล์ใหม่** — rollback คือลบทิ้ง |

### คำสั่ง rollback ทั้งชุด

```bash
for f in ~/.claude/settings.json ~/.claude-warp/settings.json \
         ~/.claude-ghostty/settings.json ~/.claude-cmux/settings.json \
         ~/.claude-warp/.claude.json ~/.claude-ghostty/.claude.json; do
  cp "$f.bak-chromemcp" "$f"
done
cp ~/.claude/statusline.sh.bak-chromemcp ~/.claude/statusline.sh
rm ~/.claude-cmux/.claude.json          # ไฟล์นี้สร้างใหม่ ไม่มี bak
rm ~/bin/chrome-mcp-doctor
rm -r ~/.config/chrome-mcp
```

## เกี่ยวข้อง

- คู่มือ curl fallback + ขับ claude.ai: `Chrome MCP — curl fallback + ขับ claude.ai (วิธีแก้ tools ไม่โหลด).md` (มี section สรุป doctor ต่อท้ายแล้ว)
- 12307 (โปรไฟล์ 2 / Kuan): ณ วันนี้ไม่มีโปรไฟล์ไหนลง extension จริง — จะใช้เมื่อไหร่: load unpacked extension ในโปรไฟล์นั้น → ตั้งพอร์ต 12307 ในป๊อปอัพ → เปิดบรรทัด `12307=Profile XX` ใน doctor.conf
