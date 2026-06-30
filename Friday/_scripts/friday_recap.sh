#!/bin/bash
# Friday recap dispatcher — runs daily at 23:55 via launchd (+ catchup at 09:00).
# Generates weekly (Thursday) and monthly (last day of month) recaps from Friday bot D1.
#
# Manual usage:
#   ./friday_recap.sh weekly                  # current week (Fri prev → today)
#   ./friday_recap.sh weekly 2026-06-12       # week ending 2026-06-12
#   ./friday_recap.sh monthly                 # current month
#   ./friday_recap.sh monthly 2026-05         # specific month
#   ./friday_recap.sh auto                    # decide based on today's date
#   ./friday_recap.sh catchup                 # run any missed weekly/monthly

set -uo pipefail   # NOT -e: we handle errors via notify() and continue

FRIDAY_DIR="$HOME/SecondBrain/Friday"
SCRIPTS_DIR="$FRIDAY_DIR/_scripts"
LOG_DIR="$FRIDAY_DIR/_logs"
LOG_FILE="$LOG_DIR/recap.log"
ENV_FILE="$SCRIPTS_DIR/.env"
STATE_FILE="$LOG_DIR/last_runs.json"

MAX_SOURCE_BYTES=80000
CODEX_RETRIES=3
RETRY_SLEEP=30

mkdir -p "$LOG_DIR"

# Load optional .env (may define TG_BOT_TOKEN, TG_BOSS_ID for Telegram alerts)
if [ -f "$ENV_FILE" ]; then
  # shellcheck disable=SC1090
  set -a; . "$ENV_FILE"; set +a
fi

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# Send alert via macOS notification + Telegram (if configured).
notify() {
  local title="$1"
  local body="$2"
  log "ALERT: $title — $body"

  # macOS notification (always available)
  osascript -e "display notification \"$body\" with title \"Friday recap\" subtitle \"$title\"" 2>/dev/null || true

  # Telegram alert (optional — needs TG_BOT_TOKEN + TG_BOSS_ID in .env)
  if [ -n "${TG_BOT_TOKEN:-}" ] && [ -n "${TG_BOSS_ID:-}" ]; then
    curl -sS --max-time 15 \
      "https://api.telegram.org/bot${TG_BOT_TOKEN}/sendMessage" \
      --data-urlencode "chat_id=${TG_BOSS_ID}" \
      --data-urlencode "text=🚨 Friday recap: ${title}%0A${body}" \
      >/dev/null 2>&1 || log "ALERT: telegram send failed"
  fi
}

preflight() {
  local missing=()
  command -v python3 >/dev/null 2>&1 || missing+=("python3")
  command -v npx     >/dev/null 2>&1 || missing+=("npx")
  command -v codex   >/dev/null 2>&1 || missing+=("codex")
  command -v osascript >/dev/null 2>&1 || true   # nice-to-have
  if [ ${#missing[@]} -gt 0 ]; then
    notify "preflight FAIL" "missing binaries: ${missing[*]}"
    return 1
  fi
  return 0
}

# Truncate source if too big — keeps top of file (highest-volume chats first).
guard_source_size() {
  local file="$1"
  local size
  size=$(wc -c < "$file")
  if [ "$size" -gt "$MAX_SOURCE_BYTES" ]; then
    log "SIZE GUARD: source $size > $MAX_SOURCE_BYTES → truncating to top $MAX_SOURCE_BYTES bytes"
    local tmp
    tmp=$(mktemp)
    head -c "$MAX_SOURCE_BYTES" "$file" > "$tmp"
    echo -e "\n\n[... truncated $(( size - MAX_SOURCE_BYTES )) bytes — lowest-volume chats omitted ...]" >> "$tmp"
    mv "$tmp" "$file"
  fi
}

# Run codex with retry. Args: prompt out_md kind_label
run_codex_with_retry() {
  local prompt="$1"
  local out_md="$2"
  local kind="$3"

  local attempt
  for attempt in $(seq 1 "$CODEX_RETRIES"); do
    log "$kind: codex attempt $attempt/$CODEX_RETRIES → $out_md"
    rm -f "$out_md"
    if codex exec \
         --skip-git-repo-check \
         --output-last-message "$out_md" \
         "$prompt" 2>&1 | tail -25 | tee -a "$LOG_FILE"; then
      if [ -s "$out_md" ]; then
        log "$kind: ✅ wrote $(wc -c < "$out_md") chars → $out_md"
        return 0
      fi
      log "$kind: attempt $attempt produced empty file"
    else
      log "$kind: attempt $attempt exited non-zero"
    fi
    if [ "$attempt" -lt "$CODEX_RETRIES" ]; then
      log "$kind: sleeping ${RETRY_SLEEP}s before retry"
      sleep "$RETRY_SLEEP"
    fi
  done

  notify "$kind FAIL" "codex failed after $CODEX_RETRIES attempts → $out_md"
  return 1
}

# Persist last successful run dates.
record_run() {
  local kind="$1"   # weekly | monthly
  local label="$2"  # 2026-W26 or 2026-06
  python3 - "$STATE_FILE" "$kind" "$label" <<'PY'
import json, sys
path, kind, label = sys.argv[1:]
try:
    with open(path) as f: state = json.load(f)
except Exception:
    state = {}
state[kind] = label
with open(path, "w") as f: json.dump(state, f, indent=2)
PY
}

generate_weekly() {
  local end_date="${1:-$(date +%Y-%m-%d)}"
  local start_date
  start_date=$(date -j -v-6d -f "%Y-%m-%d" "$end_date" +%Y-%m-%d)

  local week_label
  week_label=$(date -j -f "%Y-%m-%d" "$end_date" "+%Y-W%V")
  local out_md="$FRIDAY_DIR/Weekly Recaps/${week_label}.md"
  local source_md="$FRIDAY_DIR/_source/weekly_${week_label}.md"
  mkdir -p "$FRIDAY_DIR/_source" "$FRIDAY_DIR/Weekly Recaps"

  log "WEEKLY: $start_date → $end_date (label: $week_label)"

  if ! python3 "$SCRIPTS_DIR/pull_summaries.py" \
       --start "$start_date" \
       --end "$end_date" \
       --out "$source_md" \
       --label "$start_date → $end_date" 2>&1 | tee -a "$LOG_FILE"; then
    notify "WEEKLY $week_label" "D1 pull failed after retries — see recap.log"
    return 1
  fi

  if [ ! -s "$source_md" ]; then
    log "WEEKLY: source empty, skipping synthesis"
    return 0
  fi

  guard_source_size "$source_md"

  local source_size
  source_size=$(wc -c < "$source_md")
  log "WEEKLY: source size = $source_size chars"

  if [ "$source_size" -lt 500 ]; then
    log "WEEKLY: source too small (<500 chars), skipping"
    return 0
  fi

  local source_content
  source_content=$(cat "$source_md")

  local prompt="คุณคือ COO chief-of-staff สังเคราะห์ Weekly Recap ภาษาไทย จาก Friday bot Telegram summaries รอบสัปดาห์ $start_date → $end_date (label $week_label).

**Output:** Markdown ตรง ๆ (ไม่ต้อง preamble/postamble, ไม่ต้องบอก DONE)

**โครงสร้าง:**
- # Weekly Recap — $week_label ($start_date → $end_date)
- 4-6 หมวด business (Thunder Ops, EasySlip+Finance, EasyBOT+Marketing, Product/Dev, EasyCRM+Sales+HR, SHIFT+Bob) — ข้ามหมวดที่ไม่มี signal
- แต่ละหมวด: bullets เหตุการณ์สำคัญ + ตัวเลข + ชื่อคน + decisions
- ⚠️ Watch list ค้างปลายสัปดาห์
- ✅ Highlights สำเร็จ

**สำคัญ:** ตัวเลข/วันที่/ชื่อ ต้องตรง 100% · code/proper nouns ภาษาอังกฤษ · โทนกระชับแบบเพื่อนร่วมงานสรุปบนมือถือ

**Source content:**
\`\`\`
$source_content
\`\`\`"

  cd "$FRIDAY_DIR"
  if run_codex_with_retry "$prompt" "$out_md" "WEEKLY"; then
    record_run weekly "$week_label"
    return 0
  fi
  return 1
}

generate_monthly() {
  local ym="${1:-$(date +%Y-%m)}"
  local year="${ym:0:4}"
  local month="${ym:5:2}"
  local start_date="${year}-${month}-01"
  local end_date
  end_date=$(date -j -v+1m -v-1d -f "%Y-%m-%d" "$start_date" +%Y-%m-%d)

  local thai_months=("" "มกราคม" "กุมภาพันธ์" "มีนาคม" "เมษายน" "พฤษภาคม" "มิถุนายน" "กรกฎาคม" "สิงหาคม" "กันยายน" "ตุลาคม" "พฤศจิกายน" "ธันวาคม")
  local thai_month="${thai_months[$((10#$month))]}"
  local month_label="${ym} ${thai_month}"

  local out_md="$FRIDAY_DIR/Monthly Recaps/${month_label}.md"
  local source_md="$FRIDAY_DIR/_source/monthly_${ym}.md"
  mkdir -p "$FRIDAY_DIR/_source" "$FRIDAY_DIR/Monthly Recaps"

  log "MONTHLY: $start_date → $end_date (label: $month_label)"

  if ! python3 "$SCRIPTS_DIR/pull_summaries.py" \
       --start "$start_date" \
       --end "$end_date" \
       --out "$source_md" \
       --label "$month_label" 2>&1 | tee -a "$LOG_FILE"; then
    notify "MONTHLY $month_label" "D1 pull failed after retries — see recap.log"
    return 1
  fi

  if [ ! -s "$source_md" ]; then
    log "MONTHLY: source empty, skipping"
    return 0
  fi

  guard_source_size "$source_md"

  local source_size
  source_size=$(wc -c < "$source_md")
  log "MONTHLY: source size = $source_size chars"

  local source_content
  source_content=$(cat "$source_md")

  local prompt="คุณคือ COO chief-of-staff สังเคราะห์ Monthly Recap ภาษาไทย จาก Friday bot Telegram summaries เดือน $month_label.

**Output:** Markdown ตรง ๆ (ไม่ต้อง preamble/postamble)

**โครงสร้าง:**
- # Friday — Monthly Recap $month_label
- 7 หมวด:
  1. Thunder Solution Operations (incidents, customer cases, withdraw bonus, sales, Flex)
  2. EasySlip + Accounting/Finance (P&L, tax, banking, expenses, closing books)
  3. EasyBOT + Marketing (performance, Affiliate, Ads, Graphic, campaigns, BoostSMS launch)
  4. Product / Project / Development (BoostSMS, banking integration, billing, API metrics, infra)
  5. EasyCRM + Sales + HR (CRM dev, deals, sales pipeline, hiring, leaves)
  6. SHIFT + Talk to Bob + Other (Bob decisions, cafe ops, legal, equipment)
  7. ⚠️ Master Watch List ค้างสิ้นเดือน + ✅ Highlights สำเร็จ

**สำคัญ:** ละเอียดมาก เอาเข้าประชุมได้ · ตัวเลข/ชื่อ/วันที่/ดีล/decisions ครบ · code/proper nouns ภาษาอังกฤษ

**Source content:**
\`\`\`
$source_content
\`\`\`"

  cd "$FRIDAY_DIR"
  if run_codex_with_retry "$prompt" "$out_md" "MONTHLY"; then
    record_run monthly "$ym"
    return 0
  fi
  return 1
}

# Catchup: look for missed runs (e.g. Mac was asleep on Thursday or last-of-month).
# Strategy: walk back up to 14 days; for each Thursday + each "last day of month"
# check whether the corresponding recap file exists. If not, generate it.
catchup() {
  log "CATCHUP: scanning past 14 days for missed runs"
  local i d dow dom next_dow week_label ym month_label out_md
  for i in $(seq 1 14); do
    d=$(date -j -v-${i}d +%Y-%m-%d)
    dow=$(date -j -f "%Y-%m-%d" "$d" +%u)
    next_dom=$(date -j -v+1d -f "%Y-%m-%d" "$d" +%d)

    # Missed weekly (Thursday recap, file not present)
    if [ "$dow" = "4" ]; then
      week_label=$(date -j -f "%Y-%m-%d" "$d" "+%Y-W%V")
      out_md="$FRIDAY_DIR/Weekly Recaps/${week_label}.md"
      if [ ! -s "$out_md" ]; then
        log "CATCHUP: missed weekly $week_label (date $d) — generating"
        generate_weekly "$d" || notify "CATCHUP weekly $week_label" "still failing — manual check needed"
      fi
    fi

    # Missed monthly (last day of month, file not present)
    if [ "$next_dom" = "01" ]; then
      ym=$(date -j -f "%Y-%m-%d" "$d" "+%Y-%m")
      month=${ym:5:2}
      local thai_months=("" "มกราคม" "กุมภาพันธ์" "มีนาคม" "เมษายน" "พฤษภาคม" "มิถุนายน" "กรกฎาคม" "สิงหาคม" "กันยายน" "ตุลาคม" "พฤศจิกายน" "ธันวาคม")
      month_label="${ym} ${thai_months[$((10#$month))]}"
      out_md="$FRIDAY_DIR/Monthly Recaps/${month_label}.md"
      if [ ! -s "$out_md" ]; then
        log "CATCHUP: missed monthly $month_label (date $d) — generating"
        generate_monthly "$ym" || notify "CATCHUP monthly $month_label" "still failing — manual check needed"
      fi
    fi
  done
}

# --- Dispatch ---

MODE="${1:-auto}"

if ! preflight; then
  log "FATAL: preflight failed — exiting"
  exit 1
fi

case "$MODE" in
  weekly)
    generate_weekly "${2:-}" || exit 1
    ;;
  monthly)
    generate_monthly "${2:-}" || exit 1
    ;;
  catchup)
    catchup
    ;;
  auto)
    DOW=$(date +%u)
    DOM=$(date +%d)
    TOMORROW_DOM=$(date -j -v+1d +%d)

    log "AUTO: DOW=$DOW DOM=$DOM TOMORROW=$TOMORROW_DOM"

    # Always run catchup first — heals missed runs from Mac sleep / failures
    catchup

    # Thursday = 4 → weekly recap for current week
    if [ "$DOW" = "4" ]; then
      log "AUTO: Thursday detected → weekly"
      generate_weekly || true
    fi

    # Last day of month → tomorrow is day 01 → monthly recap
    if [ "$TOMORROW_DOM" = "01" ]; then
      log "AUTO: Last day of month → monthly"
      generate_monthly || true
    fi
    ;;
  *)
    echo "Usage: $0 {weekly|monthly|catchup|auto} [date|YYYY-MM]"
    exit 1
    ;;
esac

log "DONE: $MODE"
