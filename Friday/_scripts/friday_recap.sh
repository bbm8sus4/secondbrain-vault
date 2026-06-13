#!/bin/bash
# Friday recap dispatcher — runs every day at 23:55 via launchd.
# Decides whether to generate weekly (Thursday) or monthly (last day) recap.
#
# Manual usage:
#   ./friday_recap.sh weekly                  # current week (Fri prev → today)
#   ./friday_recap.sh weekly 2026-06-12       # week ending 2026-06-12
#   ./friday_recap.sh monthly                 # current month
#   ./friday_recap.sh monthly 2026-05         # specific month
#   ./friday_recap.sh auto                    # decide based on today's date

set -euo pipefail

FRIDAY_DIR="$HOME/SecondBrain/Friday"
SCRIPTS_DIR="$FRIDAY_DIR/_scripts"
LOG_DIR="$FRIDAY_DIR/_logs"
LOG_FILE="$LOG_DIR/recap.log"

mkdir -p "$LOG_DIR"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

generate_weekly() {
  local end_date="${1:-$(date +%Y-%m-%d)}"
  local start_date
  start_date=$(date -j -v-6d -f "%Y-%m-%d" "$end_date" +%Y-%m-%d)

  # ISO week label
  local week_label
  week_label=$(date -j -f "%Y-%m-%d" "$end_date" "+%Y-W%V")
  local out_md="$FRIDAY_DIR/Weekly Recaps/${week_label}.md"
  local source_md="$FRIDAY_DIR/_source/weekly_${week_label}.md"
  mkdir -p "$FRIDAY_DIR/_source"

  log "WEEKLY: $start_date → $end_date (label: $week_label)"

  python3 "$SCRIPTS_DIR/pull_summaries.py" \
    --start "$start_date" \
    --end "$end_date" \
    --out "$source_md" \
    --label "$start_date → $end_date" 2>&1 | tee -a "$LOG_FILE"

  if [ ! -s "$source_md" ]; then
    log "WEEKLY: source empty, skipping synthesis"
    return
  fi

  local source_size
  source_size=$(wc -c < "$source_md")
  log "WEEKLY: source size = $source_size chars"

  if [ "$source_size" -lt 500 ]; then
    log "WEEKLY: source too small (<500 chars), skipping"
    return
  fi

  log "WEEKLY: invoking Claude for synthesis → $out_md"

  local prompt="อ่านไฟล์ที่ $source_md (Friday bot summaries จาก Telegram groups รอบสัปดาห์ $start_date → $end_date).

สังเคราะห์เป็น Weekly Recap ภาษาไทย สำหรับ COO ของ Thunder Solution / EasySlip group. โทนครับ แบบเพื่อนร่วมงานเก่งสรุปบนมือถือ.

โครงสร้าง:
- หัวข้อ # Weekly Recap — $week_label ($start_date → $end_date)
- 4-6 หมวด business (Thunder Ops, EasySlip+Finance, EasyBOT+Marketing, Product/Dev, EasyCRM+Sales+HR, SHIFT+Bob) — ข้ามหมวดที่ไม่มี signal
- แต่ละหมวดมี bullet points: เหตุการณ์สำคัญ, ตัวเลข, ชื่อคน, decisions
- ⚠️ Watch list ที่ค้างปลายสัปดาห์
- ✅ Highlights ที่สำเร็จ

เน้น: รายละเอียดมาก ตัวเลข/วันที่/ชื่อต้องตรง code/proper nouns ภาษาอังกฤษ.

เขียนผลลัพธ์ลงไฟล์ $out_md (ใช้ Write tool). เสร็จแล้วตอบสั้นๆ DONE."

  cd "$FRIDAY_DIR"
  claude -p "$prompt" \
    --permission-mode acceptEdits \
    --output-format text \
    --model claude-sonnet-4-6 \
    2>&1 | tee -a "$LOG_FILE" || log "WEEKLY: claude exit $?"

  if [ -f "$out_md" ]; then
    log "WEEKLY: ✅ wrote $(wc -c < "$out_md") chars → $out_md"
  else
    log "WEEKLY: ⚠️ output file not created"
  fi
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
  mkdir -p "$FRIDAY_DIR/_source"

  log "MONTHLY: $start_date → $end_date (label: $month_label)"

  python3 "$SCRIPTS_DIR/pull_summaries.py" \
    --start "$start_date" \
    --end "$end_date" \
    --out "$source_md" \
    --label "$month_label" 2>&1 | tee -a "$LOG_FILE"

  if [ ! -s "$source_md" ]; then
    log "MONTHLY: source empty, skipping"
    return
  fi

  local source_size
  source_size=$(wc -c < "$source_md")
  log "MONTHLY: source size = $source_size chars"

  log "MONTHLY: invoking Claude for synthesis → $out_md"

  local prompt="อ่านไฟล์ที่ $source_md (Friday bot summaries จาก Telegram groups เดือน $month_label).

สังเคราะห์เป็น Monthly Recap ภาษาไทย สำหรับ COO ของ Thunder Solution / EasySlip group. โทนครับ แบบเพื่อนร่วมงานเก่งสรุปบนมือถือ.

โครงสร้าง:
- หัวข้อ # Friday — Monthly Recap $month_label
- 7 หมวด:
  1. Thunder Solution Operations (incidents, customer cases, withdraw bonus, sales, Flex)
  2. EasySlip + Accounting/Finance (P&L, tax, banking, expenses, closing books)
  3. EasyBOT + Marketing (performance, Affiliate, Ads, Graphic, campaigns, BoostSMS launch)
  4. Product / Project / Development (BoostSMS, banking integration, billing, API metrics, infra)
  5. EasyCRM + Sales + HR (CRM dev, deals, sales pipeline, hiring, leaves)
  6. SHIFT + Talk to Bob + Other (Bob decisions, cafe ops, legal, equipment)
  7. ⚠️ Master Watch List ที่ค้างสิ้นเดือน + ✅ Highlights สำเร็จ

เน้น: ละเอียดมาก เอาเข้าประชุมได้ ใส่ครบทุก ตัวเลข ชื่อ วันที่ ดีล decisions code/proper nouns ภาษาอังกฤษ.

เขียนผลลัพธ์ลงไฟล์ $out_md (ใช้ Write tool). เสร็จแล้วตอบสั้นๆ DONE."

  cd "$FRIDAY_DIR"
  claude -p "$prompt" \
    --permission-mode acceptEdits \
    --output-format text \
    --model claude-sonnet-4-6 \
    2>&1 | tee -a "$LOG_FILE" || log "MONTHLY: claude exit $?"

  if [ -f "$out_md" ]; then
    log "MONTHLY: ✅ wrote $(wc -c < "$out_md") chars → $out_md"
  else
    log "MONTHLY: ⚠️ output file not created"
  fi
}

# --- Dispatch ---

MODE="${1:-auto}"

case "$MODE" in
  weekly)
    generate_weekly "${2:-}"
    ;;
  monthly)
    generate_monthly "${2:-}"
    ;;
  auto)
    # Today's day of week (1=Mon...7=Sun) and day of month
    DOW=$(date +%u)
    DOM=$(date +%d)
    TOMORROW_DOM=$(date -j -v+1d +%d)

    log "AUTO: DOW=$DOW DOM=$DOM TOMORROW=$TOMORROW_DOM"

    # Thursday = 4 → weekly recap
    if [ "$DOW" = "4" ]; then
      log "AUTO: Thursday detected → weekly"
      generate_weekly
    fi

    # Last day of month → tomorrow is day 01 → monthly recap
    if [ "$TOMORROW_DOM" = "01" ]; then
      log "AUTO: Last day of month → monthly"
      generate_monthly
    fi
    ;;
  *)
    echo "Usage: $0 {weekly|monthly|auto} [date|YYYY-MM]"
    exit 1
    ;;
esac

log "DONE: $MODE"
