#!/usr/bin/env bash
# ============================================================================
#  Claude Code — Multi-row Status Line Installer
#  แถว: [โมเดล + context bar] [Current/5h] [Weekly/7d] [PR] [📁 project ⎇ branch]
#
#  วิธีใช้บนเครื่องอื่น:
#     bash claude-statusline-installer.sh
#  ต้องมี: jq (สคริปต์จะพยายามลงให้อัตโนมัติผ่าน brew/apt)
#  หลังรันเสร็จ: restart Claude Code
# ============================================================================
set -e

CLAUDE_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
SCRIPT="$CLAUDE_DIR/statusline.sh"
SETTINGS="$CLAUDE_DIR/settings.json"
mkdir -p "$CLAUDE_DIR"

# ── 1) dependency: jq ────────────────────────────────────────────────────────
if ! command -v jq >/dev/null 2>&1; then
  echo "• jq ไม่พบ — กำลังติดตั้ง…"
  if   command -v brew    >/dev/null 2>&1; then brew install jq
  elif command -v apt-get >/dev/null 2>&1; then sudo apt-get update && sudo apt-get install -y jq
  elif command -v dnf     >/dev/null 2>&1; then sudo dnf install -y jq
  else echo "!! ลง jq เองก่อนแล้วรันใหม่ (https://jqlang.github.io/jq/)"; exit 1
  fi
fi

# ── 2) เขียนสคริปต์ statusline (heredoc ครอบด้วย 'quote' = เขียนดิบ ไม่ตีความ) ──
cat > "$SCRIPT" <<'STATUSLINE_EOF'
#!/usr/bin/env bash
# Claude Code status line — multi-row layout
# Rows: [Model + context bar] [Current/5h] [Weekly/7d] [PR] [Project/Git]

input=$(cat)

# ── helpers ──────────────────────────────────────────────────────────────────
make_bar() {                       # ASCII progress bar 20 chars
  local pct="${1:-0}" width=20
  local filled=$(( (pct * width + 99) / 100 ))
  (( filled > width )) && filled=$width
  local empty=$(( width - filled )) bar="" i
  for (( i=0; i<filled; i++ )); do bar="${bar}█"; done
  for (( i=0; i<empty;  i++ )); do bar="${bar}░"; done
  printf '%s' "$bar"
}
format_epoch() {                   # unix epoch → "Jul 10, 6:10 PM"
  local epoch="$1"
  [[ -z "$epoch" || "$epoch" == "null" ]] && { echo ""; return; }
  date -r "$epoch" "+%b %-d, %-I:%M %p" 2>/dev/null \
    || date -d "@$epoch" "+%b %-d, %-I:%M %p" 2>/dev/null || echo ""
}
fmt_tokens() {                     # 107000 → "107k" · 1000000 → "1.0m"
  local n="$1"
  if   (( n >= 1000000 )); then awk "BEGIN{printf \"%.1fm\", $n/1000000}"
  elif (( n >= 1000    )); then awk "BEGIN{printf \"%.0fk\", $n/1000}"
  else echo "$n"; fi
}

# ── parse JSON (fed by Claude Code on stdin) ─────────────────────────────────
model_name=$(echo "$input" | jq -r '.model.display_name // "Claude"')
ctx_total=$(echo "$input"  | jq -r '.context_window.context_window_size // 0')
ctx_used=$(echo "$input"   | jq -r '.context_window.total_input_tokens // 0')
ctx_pct=$(echo "$input"    | jq -r '.context_window.used_percentage // 0')
five_pct=$(echo "$input"   | jq -r '.rate_limits.five_hour.used_percentage // empty')
five_reset=$(echo "$input" | jq -r '.rate_limits.five_hour.resets_at // empty')
week_pct=$(echo "$input"   | jq -r '.rate_limits.seven_day.used_percentage // empty')
week_reset=$(echo "$input" | jq -r '.rate_limits.seven_day.resets_at // empty')

# ── Row 1 — Model + context window ───────────────────────────────────────────
if (( ctx_total >= 1000000 )); then
  ctx_label=$(awk "BEGIN{printf \"%.0fM context\", $ctx_total/1000000}")
else
  ctx_label=$(awk "BEGIN{printf \"%.0fk context\", $ctx_total/1000}")
fi
ctx_pct_int=$(printf '%.0f' "${ctx_pct:-0}")
ctx_bar=$(make_bar "$ctx_pct_int")
row1="${model_name} (${ctx_label})  ${ctx_bar}  ${ctx_pct_int}% | $(fmt_tokens "$ctx_used")/$(fmt_tokens "$ctx_total")"

# ── Row 2 — Current / 5-hour rate limit ──────────────────────────────────────
row2=""
if [[ -n "$five_pct" ]]; then
  five_pct_int=$(printf '%.0f' "$five_pct")
  row2="Current  $(make_bar "$five_pct_int")  ${five_pct_int}% | $(format_epoch "$five_reset")"
fi

# ── Row 3 — Weekly / 7-day rate limit ────────────────────────────────────────
row3=""
if [[ -n "$week_pct" ]]; then
  week_pct_int=$(printf '%.0f' "$week_pct")
  row3="Weekly   $(make_bar "$week_pct_int")  ${week_pct_int}% | $(format_epoch "$week_reset")"
fi

# ── Row 4 — Pull Request (ถ้ามี) ─────────────────────────────────────────────
row4=""
pr_number=$(echo "$input" | jq -r '.pr.number // empty')
[[ -n "$pr_number" ]] && row4="PR #${pr_number}"

# ── Row 5 — Project / Git ────────────────────────────────────────────────────
row5=""
cwd=$(echo "$input" | jq -r '.workspace.current_dir // .cwd // empty')
session_id=$(echo "$input" | jq -r '.session_id // empty')
if [[ -n "$cwd" ]]; then
  proj=$(basename "$cwd")
  branch=$(cd "$cwd" 2>/dev/null && git rev-parse --abbrev-ref HEAD 2>/dev/null | head -c 30)
  dirty=""
  if [[ -n "$branch" ]]; then
    if   cd "$cwd" 2>/dev/null && ! git diff        --quiet 2>/dev/null; then dirty="*"
    elif cd "$cwd" 2>/dev/null && ! git diff --cached --quiet 2>/dev/null; then dirty="*"; fi
  fi
  # จำนวนไฟล์ที่แก้ใน session นี้ — ต้องมี hook track-file-writes ถึงจะโชว์ (ไม่มีก็ข้ามเงียบ ๆ)
  touched=0
  if [[ -n "$session_id" && -f "/tmp/claude-file-tracking/$session_id.txt" ]]; then
    touched=$(sort -u "/tmp/claude-file-tracking/$session_id.txt" 2>/dev/null | wc -l | tr -d ' ')
  fi
  row5="📁 $proj"
  [[ -n "$branch" ]]    && row5="$row5  ⎇ ${branch}${dirty}"
  [[ "$touched" -gt 0 ]] && row5="$row5  ✎ ${touched} files"
fi

# ── Output ────────────────────────────────────────────────────────────────────
output="$row1"
for r in "$row2" "$row3" "$row4" "$row5"; do [[ -n "$r" ]] && output="${output}\n${r}"; done
printf '%b\n' "$output"
STATUSLINE_EOF
chmod +x "$SCRIPT"
echo "• เขียนสคริปต์แล้ว: $SCRIPT"

# ── 3) ต่อ statusLine เข้า settings.json (สำรองก่อน) ─────────────────────────
python3 - "$SETTINGS" "$SCRIPT" <<'PY'
import json, os, sys, shutil
settings, script = sys.argv[1], sys.argv[2]
data = {}
if os.path.isfile(settings):
    shutil.copy2(settings, settings + ".bak")
    try: data = json.load(open(settings))
    except Exception: data = {}
data["statusLine"] = {"type": "command", "command": f"bash {script}", "padding": 0}
with open(settings, "w", encoding="utf-8") as fh:
    json.dump(data, fh, indent=2, ensure_ascii=False); fh.write("\n")
print(f"• ต่อ statusLine เข้า {settings} (backup: {os.path.basename(settings)}.bak)")
PY

echo
echo "เสร็จ — restart Claude Code (ปิด-เปิดใหม่) เพื่อเห็น status line ใหม่"
