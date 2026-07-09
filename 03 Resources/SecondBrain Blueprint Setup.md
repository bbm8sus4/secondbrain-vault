---
title: SecondBrain Blueprint Setup
type: resource
source: โครงสร้างจริงของ ~/SecondBrain (Bob/aexgee) ณ 2026-07-06 หลัง cleanup sprint + upgrade รอบ 2
source_date: 2026-07-06
imported: 2026-07-06T22:20:00
last_verified: 2026-07-09
status: live
delivered: ส่งให้เพื่อนแล้ว 2026-07-06 (mark-ai รับไปดำเนินการ) · ปิดโปรเจกต์ 2026-07-09
tags: [resource, blueprint, obsidian, second-brain, export]
---

# SecondBrain Blueprint — คู่มือเซต Obsidian vault ให้โครงสร้างเหมือนต้นฉบับเป๊ะ

> **ไฟล์นี้เขียนถึง AI agent ที่ดูแล vault ปลายทางโดยตรง** (เช่น mark-ai)
> เป้าหมาย: ทำให้ vault ของคุณมี **โครงสร้าง + กฎ + ระบบอัตโนมัติ** เหมือน vault ต้นฉบับทุกประการ
> โดย **เนื้อหาความรู้เป็นของเจ้าของ vault คุณเอง** — ไม่ต้อง copy เนื้อหาใด ๆ จากต้นฉบับ

---

## 0) กติกาความปลอดภัย — อ่านก่อนลงมือ (สอดคล้อง red-lines ของคุณ)

Blueprint นี้ออกแบบให้ **ทุกขั้นตอนเป็น additive เท่านั้น** คุณไม่จำเป็นต้องลบหรือเขียนทับอะไรเลย:

1. **ห้ามลบ/ย้าย/เขียนทับของเดิม** — โฟลเดอร์เดิมของ vault คุณ (เช่น `raw/`, `wiki/`, `Daily Logs/`) ให้ **map เข้า Layer** (ดู §2) ไม่ใช่รื้อ ถ้าเห็นว่าควร rename/ย้ายจริง ๆ → ลิสต์เป็นข้อเสนอให้มนุษย์อนุมัติก่อน ห้ามทำเอง
2. **commit git ก่อนเริ่มทุก Phase และหลังจบทุก Phase** — ทุกอย่างต้องย้อนได้ 1 คำสั่ง
3. ไฟล์ที่ blueprint ให้สร้าง ถ้า**ชื่อชนกับไฟล์ที่มีอยู่** → สร้างเป็น `<ชื่อ> (blueprint).md` แล้ว flag ให้มนุษย์ตัดสิน ห้ามทับ
4. **ห้ามใส่ secret ลง vault/git เด็ดขาด** (token, API key) — automation ทุกตัวอ่าน secret จากไฟล์ `.env` นอก vault เท่านั้น
5. ระบบนอก vault (launchd/cron, สคริปต์ใน `~/bin`) ติดตั้งได้เฉพาะที่ระบุใน §7 และต้องแจ้งมนุษย์ว่าติดตั้งอะไรไปบ้าง
6. รัน verify (ของคุณเอง หรือ health scan ตาม §7.3) **หลังจบทุก Phase** — ตัวเลขต้องไม่แย่ลงกว่าก่อนเริ่ม

---

## 1) ปรัชญาของระบบ (ทำไมถึงเวิร์ก)

Vault นี้ไม่ใช่ที่จดโน้ตของมนุษย์ แต่เป็น **"สมองกลางที่ AI agent เป็นคนดูแล"** ตามแนว Karpathy LLM Wiki:

- **มนุษย์ curate + ถาม** / **LLM ทำ bookkeeping ทั้งหมด** (เขียนหน้า, อัพเดต index, ลง log, lint)
- ทุกความรู้ต้อง **ตรวจย้อนได้**: มาจากไหน (`source:`) เช็คล่าสุดเมื่อไหร่ (`last_verified:`) ใครแตะอะไรเมื่อไหร่ (`log.md`)
- ระบบต้อง **ดูแลตัวเอง**: สแกนสุขภาพทุกวัน แจ้งเตือนเมื่อพัง ย่อยความรู้ใหม่เป็น synthesis อัตโนมัติ
- **Vault = source of truth ที่ version ด้วย git** — commit + push อัตโนมัติ ของหายกู้ได้เสมอ

---

## 2) สถาปัตยกรรม 3 ชั้น (หัวใจของทั้งระบบ)

| Layer | คืออะไร | กฎ |
|---|---|---|
| **A — Raw Sources** | ของดิบที่ไหลเข้ามา (inbox, capture, mirror จากระบบอื่น) | **immutable** — ห้ามลบ ห้ามแก้ ห้าม restructure อ่านอย่างเดียว |
| **B — Wiki** | ความรู้ที่ LLM เขียน/สังเคราะห์จาก raw | LLM เขียน มนุษย์อ่าน · เจอหน้าขัดกัน → flag ก่อน ห้ามเขียนทับ |
| **C — Schema** | กฎของ vault เอง (โฟลเดอร์ `20 Rules/`) | แก้ได้เมื่อมนุษย์สั่ง · agent ทุกตัวต้องอ่านก่อนทำงาน |

**สำคัญ:** vault คุณมีโฟลเดอร์เดิมอยู่แล้ว → ทำ "ตาราง mapping" ว่าโฟลเดอร์เดิมไหนคือ Layer ไหน แล้วเขียนตารางนี้ไว้ใน `20 Rules/WIKI.md` ของคุณ เช่น `raw/` = Layer A, `wiki/` = Layer B — **ไม่ต้องย้ายไฟล์**

## 3) โครงสร้างโฟลเดอร์มาตรฐาน

```
<Vault>/
├── หน้าหลัก.md          ← dashboard สำหรับ agent (ดู §4.1)
├── index.md             ← catalog ทุกหน้าสำคัญ (ดู §4.2)
├── log.md               ← timeline append-only (ดู §4.3)
├── browse.base          ← Obsidian Bases dashboard (ดู §8.2)
├── _attachments/        ← รูป/ไฟล์แนบรวมศูนย์
├── 00 Inbox/            ← [A] ของใหม่ยังไม่จัด — auto-router กวาดทุก 3 นาที
├── 01 Projects/         ← [B] งานมี deadline (1 โฟลเดอร์/โปรเจกต์ มี README.md เป็น hub)
├── 02 Areas/            ← [B] งานต่อเนื่องไม่มีวันจบ (การเงิน ทีม สุขภาพ)
├── 03 Resources/        ← [B] ความรู้อ้างอิง playbook แผนที่ความรู้ Clippings
├── 04 Archive/          ← [B] จบแล้วเก็บค้น (มี README.md เป็น manifest รวมทุกไฟล์)
├── 10 Daily/            ← daily note (ถ้าไม่ใช้ ให้เขียนบอกตรง ๆ ใน index ว่า "ยังไม่ใช้")
├── 20 Rules/            ← [C] กฎ wiki + templates + สำเนา automation
│   ├── WIKI.md                      ← master schema
│   ├── WIKI - Ingest Playbook.md
│   ├── WIKI - Query Playbook.md
│   ├── WIKI - Lint Playbook.md
│   ├── WIKI - Page Templates.md
│   ├── Automation Setup.md          ← คู่มือติดตั้ง automation บนเครื่องใหม่
│   ├── _templates/                  ← template จริงของ core Templates plugin
│   └── _automation/                 ← สำเนาสคริปต์+plist (version ใน git, ห้ามมี secret)
├── 30 Claude Memory/    ← [A] mirror อัตโนมัติจาก memory ของ AI (read-only ฝั่ง vault)
├── 40 Meeting Notes/    ← [A] mirror จากระบบ meeting notes (read-only)
└── <Brand หรือ Domain>/ ← [B] knowledge base ต่อแบรนด์/โดเมนใหญ่ ที่ root
    ├── หน้าหลัก.md      ← hub ของแบรนด์ ลิงก์ทุกหน้าลูก
    ├── 01-Overview.md   ← หน้าเลขเรียงหัวข้อ 01, 02, 03…
    └── _knowledge/ _assets/ ตามต้องการ
```

หลักตั้งชื่อ: **ภาษาเดียวกับตัว entity** (แบรนด์อังกฤษ→อังกฤษ, เรื่องไทย→ไทย) · ตัวคั่นคือ ` — ` (em-dash) · หน้า MOC ขึ้นต้น `แผนที่ - ` · หน้าเลขในแบรนด์ใช้ `01-`, `02-` … · **ห้ามใช้ตัวอักษร `^` `|` `[` `]` ในชื่อไฟล์** (ทำ wikilink พัง — บทเรียนจริงจากต้นฉบับ)

## 4) ไฟล์ root 3 ตัว — กระดูกสันหลัง

### 4.1 `หน้าหลัก.md` — dashboard ที่เขียนให้ AI อ่าน ไม่ใช่คน
ต้องมี section ตามลำดับนี้:
1. **Agent ต้องอ่านก่อน (Schema)** — ลิงก์ [[WIKI]], [[index]], [[log]] + กติกาสั้น ๆ
2. **งานที่กำลังทำ (Active Work Index)** — ลิสต์โปรเจกต์ active + one-liner (agent เปิดมารู้บริบททันที ไม่ต้องถาม)
3. **แผนที่ความรู้** — ลิงก์ MOC ทุกตัว
4. **โครงสร้าง Vault** — ตารางโฟลเดอร์ + ใช้ทำอะไร (บอกตามจริง รวมทั้งอันที่ "ยังไม่ใช้")
5. **ระบบ** — automation แต่ละตัวทำอะไร รันถี่แค่ไหน สคริปต์อยู่ไหน

### 4.2 `index.md` — catalog
- frontmatter: `type: index`, `maintained_by: agent`, `last_verified:`
- จัด section ตาม PARA + Brand · ทุกรายการ = `- [[Page]] — one-liner · last_verified: YYYY-MM-DD`
- กฎอัพเดต: สร้าง/ลบ/ย้ายหน้าใหญ่ → ต้องอัพเดต index ทันที · section เกิน 30 รายการ → แตก sub-page

### 4.3 `log.md` — timeline append-only
- frontmatter: `type: log`, `append_only: true`
- entry ใหม่แทรก **บนสุด** (ใต้ `---` แรก) รูปแบบบังคับ:
```
## [YYYY-MM-DD HH:MM] <op> | <subject>
- รายละเอียด bullet สั้น ๆ
- agent: <ใครทำ>
```
- `<op>` มีแค่: `ingest` · `query` · `lint` · `rename` · `delete` · `conflict` · `decision` · `auto-ingest`
- ห้ามแก้ entry เก่า · grep ได้ด้วย `grep "^## \[" log.md | head`

## 5) Schema กลาง — `20 Rules/` (Layer C)

### 5.1 Frontmatter บังคับทุกหน้า wiki ที่สร้างใหม่
```yaml
title:           # ชื่อแสดง
type:            # ดู taxonomy ล่าง
source:          # ต้นทาง: path / URL / "chat YYYY-MM-DD" / "agent synthesis YYYY-MM-DD"
source_date:     # วันที่ของ source
imported:        # YYYY-MM-DDTHH:MM:SS
last_verified:   # YYYY-MM-DD — อัพเดตทุกครั้งที่แตะหน้านี้
status:          # draft | live | archived
tags:            # [domain, type, ...]
```
ฟิลด์เลือก: `related:` `memory_pointer:` `deprecates:` `review_after:` `owner:`

### 5.2 Taxonomy — `type`
`project` (01) · `area` (02) · `resource` / `concept` (03) · `entity` (brand/คน/บริษัท) · `event` · `decision` · `synthesis` (ผลจาก ratchet) · `vendor-quote` · `schema` / `schema-playbook` (20 Rules) · `archived` (04)

### 5.3 สี่ Playbook — เขียนเป็นไฟล์แยกใน 20 Rules สาระสำคัญ:
- **Ingest**: รับ source ใหม่ → **search ก่อนเสมอ**ว่ามีหน้าเกี่ยวข้องไหม (กัน contradiction) → diff กับของเดิม → เขียน/อัพเดตหน้า → อัพเดต index → ลง log
- **Query**: ค้น index → อ่านหน้า → ตอบพร้อม cite → ถามตัวเอง **"คำตอบนี้ file back เป็นหน้า synthesis ได้ไหม"** (ratchet) → ลง log
- **Lint**: รายสัปดาห์/เดือน เช็ค contradiction · stale · orphan · dead link · gap
- **Page Templates**: frontmatter ตาม §5.1 + โครงหน้าแต่ละ type

### 5.4 กฎเหล็กที่ถอดจากบทเรียนจริง
- แตะหน้าไหน → อัพเดต `last_verified:` ของหน้านั้น + ลง log เสมอ
- เจอข้อมูลขัดกัน 2 หน้า → สร้างหมายเหตุ `conflict` ใน log + flag ในหน้า ห้ามเลือกเองเงียบ ๆ
- ข้อเท็จจริงที่ยังไม่ชัวร์ → เขียน `⚠️ ต้อง verify` ในหน้า (health scan จะรวบเป็นคิวทวงมนุษย์ทุกวัน)
- ลิงก์ไปโฟลเดอร์ด้วย `[[ชื่อโฟลเดอร์]]` = พัง (Obsidian ลิงก์โฟลเดอร์ไม่ได้) → ใช้ inline code หรือลิงก์ README ของโฟลเดอร์นั้น

## 6) Memory ↔ Wiki Bridge (ถ้าเครื่องคุณมี AI memory store)

| | Memory (ไฟล์ฝั่ง AI harness) | Wiki (vault) |
|---|---|---|
| เก็บ | สถานะปัจจุบัน · preference · **pointer** | ความรู้เต็ม · ประวัติ · synthesis |
| ขนาด | สั้น 1 ย่อหน้า/ไฟล์ | ยาวได้ |

- sync memory → โฟลเดอร์ mirror ใน vault (ฝั่ง vault **read-only** — แก้ที่ต้นทางเท่านั้น)
- **ถ้า AI รันหลาย harness/หลาย config dir → รวมทุก dir เข้า mirror เดียว** (slug ซ้ำเอาไฟล์ mtime ใหม่สุด) — ต้นฉบับเคยพลาดข้อนี้ ความรู้หล่นหายไป 7 ไฟล์โดยไม่รู้ตัว
- memory ที่ชี้เข้า wiki ใช้ pointer path ตรง ๆ · หน้า wiki ที่อยากให้ memory จำ ใส่ `memory_pointer:` ใน frontmatter

## 7) Automation 5 ตัว (สเปค — เขียนสคริปต์ใหม่ตามเครื่องคุณ อย่า copy path ต้นฉบับ)

> ทั้งหมดรันผ่าน launchd (macOS) หรือ cron · สคริปต์อยู่ `~/bin/` · **สำเนา version เข้า `20 Rules/_automation/`** ทุกครั้งที่แก้ · เขียนคู่มือติดตั้งเครื่องใหม่ไว้ที่ `20 Rules/Automation Setup.md`

### 7.1 sync + backup (ทุก 30 นาที) — ตัวสำคัญสุด
1. sync memory ทุก harness → mirror (ดู §6)
2. sync แหล่ง raw อื่น (เช่น meeting notes) — **rsync แบบมี guard: source ว่าง = ไม่ mirror** (กัน `--delete` ล้าง vault)
3. `git add -A && git commit -m "auto-sync <timestamp>"` (ถ้ามีของเปลี่ยน)
4. `git fetch` → ถ้า origin นำหน้า → `git pull --rebase --autostash` (fail → abort rebase + log, **ห้าม force push**) → `git push`
   **บทเรียนจริง:** ต้นฉบับ push fail เงียบอยู่ครึ่งวันเพราะไม่มี rebase — backup บน GitHub ค้างโดยไม่มีใครรู้

### 7.2 inbox auto-router (ทุก 3 นาที) — rule-based ห้ามใช้ AI
- อ่าน frontmatter ของไฟล์ใน `00 Inbox/` → route ตามตาราง tag→ปลายทาง (เริ่มที่ `clippings` → `03 Resources/Clippings/`)
- safety: ข้ามไฟล์ mtime < 30 วิ (กำลังเขียนอยู่) · ชื่อชน → ต่อ suffix ไม่ทับ · route แล้วอัพเดต `last_verified` + ลง log
- **sanitize clippings: ถอด `[[wikilink]]` ใน frontmatter** (Web Clipper ชอบเขียน `author: "[[ชื่อช่อง]]"` = dead link ทุกใบ)

### 7.3 vault-health (ทุกวันเช้า) — หมอประจำ vault
สแกนแล้วเขียนรายงาน `00 Inbox/_vault-health.md`:
- dead links (ต้อง resolve **ไฟล์แนบทุกนามสกุล** ไม่ใช่แค่ .md — ไม่งั้น false positive เพียบ) · orphans · ไฟล์ว่าง
- mirror drift (นับ source ทุก harness เทียบ mirror) · อายุ commit ล่าสุด · **จำนวน commit ที่ยังไม่ push** · **launchd jobs ครบไหม**
- frontmatter ขาด `type`/`last_verified` (backlog) · หน้า `last_verified` เก่าเกิน 90 วัน · **คิว `ต้อง verify`** (grep ทุกหน้า — ทวงมนุษย์ทุกวันจนเคลียร์)
- **มีปัญหา hard (ลิงก์เสีย/mirror เพี้ยน/job ตาย/push ค้าง) → แจ้ง Telegram/ช่องทางที่เจ้าของอ่านจริง** · สถานะเขียว = เงียบ

### 7.4 capture channel (ต่อเนื่อง) — ทางลัดจดเข้า vault
ข้อความ/รูปจากมือถือ (Telegram bot ฯลฯ) → ไฟล์ใน `00 Inbox/` ภายใน 1 นาที → auto-router จัดต่อ · token อยู่ `.env` นอก vault

### 7.5 ratchet loop (รายสัปดาห์) — เปลี่ยน "ที่เก็บ" เป็น "ที่ย่อย"
- clippings ที่ยังไม่สรุป → รัน AI headless (จำกัด ≤5 ชิ้น/รอบ + tool allowlist แคบ ๆ) สร้างหน้า Takeaways ใน `Clippings/Synthesis/` (type: synthesis)
- กติกาเนื้อหา: สกัดเฉพาะประเด็นที่ actionable ต่อธุรกิจเจ้าของ vault · คลิปไม่มีสาระ → เขียนตรง ๆ ว่า "ไม่มีประเด็น" พร้อมเหตุผล ห้ามยัดเยียด
- state file กันทำซ้ำ · จบแล้วอัพเดต Clippings README + ลง log `query | ratchet`

## 8) Obsidian app config

- **Plugin ชุมชน: ตัวเดียวพอ** — `smart-connections` (semantic search) · อย่าลง plugin เพิ่มถ้าไม่มีเหตุผล
- **Core Templates**: ตั้ง folder เป็น `20 Rules/_templates/` · สร้าง template 5 แบบ (Project README / Resource / Entity / Synthesis / Decision) ที่ frontmatter ครบ §5.1 ใช้ `{{title}}` `{{date}}` `{{time}}`
- **Bases** (`browse.base`): 4 views — ทุกหน้าเรียง `last_verified` DESC · หน้า `!note.type` (schema debt) · `type == "project"` · `status != "live"`
- **Graph**: colorGroups ใช้ `path:"<โฟลเดอร์>"` (อย่าใช้คำลอย ๆ — จับไม่ติด) แยกสีต่อแบรนด์/Layer + เปิด showTags
- `.gitignore`: `workspace.json`, cache ของ plugin (เช่น `.smart-env/`), `.DS_Store`, `*.tmp`

## 9) แผนติดตั้ง 6 Phase (ทำตามลำดับ · commit ก่อน-หลังทุก Phase · verify ทุก Phase)

| Phase | ทำอะไร | Definition of done |
|---|---|---|
| **1. Schema** | สร้าง `20 Rules/` ทั้งชุด (WIKI + 4 playbooks + ตาราง mapping โฟลเดอร์เดิม→Layer) | มนุษย์รีวิวตาราง mapping แล้ว |
| **2. กระดูกสันหลัง** | สร้าง/ปรับ `หน้าหลัก.md` `index.md` `log.md` ตาม §4 (ของเดิมมีอยู่ → เติม section ที่ขาด ห้ามลบของเขา) | ทั้ง 3 ไฟล์มี section ครบ + log entry แรกบันทึกการติดตั้ง |
| **3. จัดบ้าน** | สร้างโฟลเดอร์ PARA ที่ยังไม่มี · README/manifest ใน Archive + hub ที่จำเป็น · **ของเดิมไม่ย้าย** (เสนอ mapping พอ) | index ครอบคลุมทุกหน้าสำคัญ · orphan ลดลง |
| **4. Obsidian config** | templates + browse.base + graph groups + .gitignore ตาม §8 | เปิดใน app แล้วทุกอันทำงาน |
| **5. Automation** | เขียนสคริปต์ตามสเปค §7 (ปรับ path ให้เครื่องคุณ) · ติดตั้ง launchd/cron · สำเนาเข้า `_automation/` · เขียน `Automation Setup.md` | ทุก job โผล่ใน `launchctl list` · sync รอบแรก commit+push สำเร็จ · alert ทดสอบส่งถึงจริง |
| **6. Verify + ส่งมอบ** | รัน health scan เต็ม + แก้จนตัวเลขสะอาด | ✅ checklist ล่าง |

### Checklist ส่งมอบ (ต้องผ่านครบ)
- [ ] dead links = 0 · orphans = 0 (หรือมีเหตุผลจดไว้) · ไฟล์ว่าง = 0
- [ ] `หน้าหลัก` / `index` / `log` ครบ format §4 · log มี entry การติดตั้งครบทุก Phase
- [ ] หน้าใหม่ทุกหน้าที่สร้างมี frontmatter ครบ §5.1
- [ ] automation ≥ 3 ตัวแรก (sync / router / health) รันจริง มีหลักฐานใน log ของมันเอง
- [ ] git: commit อัตโนมัติทำงาน · push ขึ้น remote สำเร็จ · **ไม่มี secret ใน repo** (grep ก่อน push)
- [ ] แจ้งเตือนทดสอบส่งถึงเจ้าของ vault จริง 1 ครั้ง
- [ ] รายงานสรุปให้เจ้าของ: ทำอะไรไป · เสนอ mapping/rename อะไรที่รอเขาอนุมัติ · อะไรยังไม่ได้ทำเพราะติด red-line

## 10) สิ่งที่ **ไม่ต้อง** เอาจากต้นฉบับ
- เนื้อหาความรู้ทุกชนิด (แบรนด์, ตัวเลขธุรกิจ, memory) — ของใครของมัน
- path เฉพาะเครื่อง (`/Users/aexgee/...`) — เขียนใหม่ตามเครื่องคุณทั้งหมด
- token/secret ใด ๆ · ชื่อ repo GitHub (สร้าง private repo ของตัวเอง)
- โฟลเดอร์แบรนด์ของต้นฉบับ (Thunder/EasySlip/ฯลฯ) — สร้างตามโดเมนธุรกิจของเจ้าของ vault คุณเอง

---
*Blueprint v1.0 · สร้างจาก vault จริงที่รันระบบนี้อยู่ (357+ หน้า, health 🟢, automation 5 ตัว) · คำถาม/ติดขัด → ให้เจ้าของ vault คุยกับเจ้าของต้นฉบับ*
