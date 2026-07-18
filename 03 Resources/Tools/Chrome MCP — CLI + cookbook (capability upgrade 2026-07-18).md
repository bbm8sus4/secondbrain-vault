# Chrome MCP — CLI + cookbook (capability upgrade 2026-07-18)

รอบที่ 2 ของงาน Chrome MCP. รอบแรก = **ความเสถียร** (doctor/auto-heal, ดู note "doctor autonomy stack").
รอบนี้ = **ความสามารถ**: กว้างขึ้น ฉลาดขึ้น ใช้จริงนอก Claude ได้.

## สิ่งที่ค้นพบ
Server มี **27 tools** แต่ที่ผ่านมาใช้จริงไม่ถึงครึ่ง. ของแรงที่ไม่เคยแตะ:
- `chrome_network_capture` — ดัก XHR/fetch พร้อม response body (reverse-engineer เว็บ)
- `chrome_network_request` — ยิง HTTP ผ่าน browser → ใช้ cookie ที่ login ค้างไว้
- `performance_*` — Core Web Vitals, `chrome_history`, `chrome_bookmark_*`, `chrome_gif_recorder`

Upstream check: `git remote add upstream hangwin/mcp-chrome` → fetch → **0 commit behind**. fork itorz7 ไม่ตกรุ่น.

## 1. `~/bin/chrome` — CLI ขับ Chrome จาก shell ไหนก็ได้
ไม่ต้องมี Claude session อีกต่อไป — cron / script / ccgram / terminal ขับ Chrome ได้หมด.
verbs บนชั้น JSON-RPC เดิม, auto-heal พอร์ตก่อนเรียกทุกครั้ง.

```bash
chrome tabs                              # ดู tab ทั้งหมด (id/url/title)
chrome js <id> 'return document.title'   # รัน JS เอา return (ต้อง return!)
chrome text <id|url>                     # ดึง readable text
chrome capture <id> --secs 15            # ดัก network 15 วิ (API sniff)
chrome fetch <url> --method POST --body '{}'   # ยิง HTTP ผ่าน live cookies ← ทดสอบแล้ว 200
chrome console <id> --errors             # debug web app
chrome perf <id> --secs 5                # Core Web Vitals
chrome shot <id> out.png --full          # screenshot
chrome dialog arm --accept               # กันแฮงค์: arm ก่อน trigger dialog
chrome help                              # verb เต็ม
```

- `--port 12307` / `CHROME_MCP_PORT=12307` = โปรไฟล์ 2
- **ไม่แตะ `mcp-chrome-curl.py`** (skills พึ่งพา) — เพิ่มชั้นบน ปลอดภัย ย้อนกลับได้ด้วยการลบ `~/bin/chrome`

## 2. Playbook: reverse-engineer private API (ethical scope — บัญชีตัวเอง/ที่ได้รับอนุญาต)
1. `chrome tabs` → tab id, login ปกติ
2. `chrome capture <id> --secs 15` → กดฟีเจอร์ที่อยากเข้าใจ
3. อ่าน request ที่ดัก: endpoint / headers / payload / response
4. `chrome fetch <endpoint> --method POST --body '<json>'` — replay ด้วย session cookies, loop จาก shell = bulk pull โดยไม่ต้อง juggle token

## 3. Skill `/chrome-mcp-cookbook`
`~/.claude/skills/chrome-mcp-cookbook/SKILL.md` — ทุก session ฉลาดขึ้นทันที:
- capability map 27 tools (ตารางว่าแต่ละตัวใช้ทำอะไร)
- **dialog trap**: native alert/confirm/prompt = แช่แข็ง extension → `chrome dialog arm` ก่อน trigger เสมอ
- สูตรเว็บที่พิสูจน์แล้ว: Sheets (pbcopy+Cmd+V จริง, ห้าม CDP paste), Docs (Version History undo), claude.ai (ProseMirror execCommand), LINE OA, Telegram protected photos, Canva 403
- ลงทะเบียน trigger ใน CLAUDE.md ทั้ง warp + .claude

## Permissions
allow `chrome:*` + curl helper + doctor ครบ 4 harness → zero prompt.

## Rollback
- ลบ `~/bin/chrome` (ไฟล์ใหม่ล้วน)
- ลบ `~/.claude/skills/chrome-mcp-cookbook/`
- settings.json มี backup `.bak-chromemcp` (จากรอบแรก) — permissions ที่เพิ่มรอบนี้ถอดได้ด้วยมือถ้าต้องการ
- CLAUDE.md: ลบ block `# chrome-mcp-cookbook`

## เกี่ยวข้อง
- รอบเสถียร: `Chrome MCP — doctor autonomy stack + rollback (2026-07-18).md`
- curl fallback: `Chrome MCP — curl fallback + ขับ claude.ai (วิธีแก้ tools ไม่โหลด).md`
