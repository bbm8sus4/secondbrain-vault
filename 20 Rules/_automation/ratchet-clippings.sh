#!/bin/zsh
# Weekly "ratchet" — turn raw web clippings into COO takeaway pages, per the
# Query Playbook rule the vault never actually executed until now.
#
# Runs Sunday 19:00 via launchd com.aexgee.ratchet-clippings.
# Guardrails: max 5 clippings per run · headless claude with a fixed tool
# allowlist · processed files tracked in .ratchet-done.txt so nothing repeats.
set -u

VAULT="$HOME/SecondBrain"
CLIPS="$VAULT/03 Resources/Clippings"
SYNTH="$CLIPS/Synthesis"
STATE="$CLIPS/.ratchet-done.txt"
LOG="$HOME/Library/Logs/ratchet-clippings.log"
MAX_PER_RUN=5

# claude lives inside the cmux bundle on this machine; fall back to PATH
CLAUDE="/Applications/cmux.app/Contents/Resources/bin/claude"
[[ -x "$CLAUDE" ]] || CLAUDE="$(command -v claude || true)"

mkdir -p "$SYNTH" "$(dirname "$LOG")"
touch "$STATE"
log() { print -r -- "$(date '+%F %T') $*" >>"$LOG"; }

if [[ -z "$CLAUDE" ]]; then
  log "ERROR: claude CLI not found — skipping run"
  exit 1
fi

# pending = clippings not yet ratcheted (skip README, synthesis pages, done list)
typeset -a pending
while IFS= read -r f; do
  base="${f:t}"
  [[ "$base" == "README.md" ]] && continue
  [[ "$base" == *"Takeaways"* ]] && continue
  grep -qxF "$base" "$STATE" && continue
  pending+=("$base")
done < <(find "$CLIPS" -maxdepth 1 -name "*.md" | sort)

if (( ${#pending[@]} == 0 )); then
  log "nothing to ratchet — all clippings done"
  exit 0
fi

typeset -a batch
batch=("${(@)pending[1,$MAX_PER_RUN]}")
log "ratcheting ${#batch[@]} of ${#pending[@]} pending: ${(j:, :)batch}"

FILES_LIST=""
for b in "${(@)batch}"; do FILES_LIST+="- 03 Resources/Clippings/$b"$'\n'; done

PROMPT="คุณคือ agent ดูแล SecondBrain vault ตามกฎใน '20 Rules/WIKI - Query Playbook.md' (ratchet clippings เป็น synthesis)

ทำทีละไฟล์ตามลิสต์นี้:
$FILES_LIST
สำหรับแต่ละไฟล์:
1. อ่าน clipping แล้วสกัดเฉพาะประเด็นที่มีประโยชน์ต่อ COO ของ Thunder Solution/EasySlip (ธุรกิจ slip verification, LINE chatbot, SMS, CRM, การใช้ AI ในองค์กร)
2. สร้างไฟล์ '03 Resources/Clippings/Synthesis/<ชื่อสั้นกระชับ> — Takeaways.md' เขียนเป็นภาษาไทย มี frontmatter: title, type: synthesis, source: (path ไฟล์ clipping), source_date, imported, last_verified (วันนี้), status: live, tags
3. เนื้อหา: TL;DR 1 บรรทัด + takeaways 5-10 ข้อ (เฉพาะที่ actionable/เกี่ยวกับธุรกิจจริง ไม่ยัดทุกอย่าง) + ลิงก์กลับไฟล์ต้นทางด้วย wikilink
4. ถ้า clipping ไหนไม่มีสาระพอ (เช่น โฆษณาล้วน) ให้สร้างไฟล์ Takeaways สั้น ๆ ระบุว่า 'ไม่มีประเด็นสำหรับ COO' พร้อมเหตุผล 1 บรรทัด

เสร็จทุกไฟล์แล้ว:
5. อัพเดต '03 Resources/Clippings/README.md' — เพิ่ม section Synthesis (ถ้ายังไม่มี) แล้วลิงก์หน้า Takeaways ใหม่ทุกหน้า
6. เติม log entry ที่ต้นรายการใน log.md (หลัง '---' แรก): '## [$(date '+%Y-%m-%d %H:%M')] query | ratchet clippings (${#batch[@]} หน้า synthesis)' พร้อม bullet รายชื่อ
ห้ามแตะไฟล์อื่นนอกเหนือจากที่ระบุ ห้ามลบอะไรทั้งสิ้น"

cd "$VAULT" || exit 1
if "$CLAUDE" -p "$PROMPT" \
    --allowedTools "Read,Write,Edit,Glob,Grep" \
    --add-dir "$VAULT" \
    --max-turns 80 >>"$LOG" 2>&1; then
  for b in "${(@)batch}"; do print -r -- "$b" >>"$STATE"; done
  log "done — marked ${#batch[@]} clippings as ratcheted"
else
  log "ERROR: claude run failed (exit $?) — state not advanced, will retry next week"
fi
