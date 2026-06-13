#!/usr/bin/env python3
"""
Pull Friday bot summaries from D1 for a date range, group by chat, write Markdown.

Usage:
    pull_summaries.py --start 2026-05-01 --end 2026-05-31 --out /tmp/source.md
"""
import argparse
import json
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

BOT_DIR = Path.home() / "my-ai-bot"
DB_NAME = "my-ai-bot-db"


def run_d1(sql: str) -> list:
    """Run a D1 query via wrangler, return list of result rows."""
    result = subprocess.run(
        ["npx", "wrangler", "d1", "execute", DB_NAME, "--remote",
         "--command", sql, "--json"],
        cwd=BOT_DIR,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(f"D1 query failed: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    # wrangler prints status before JSON — extract JSON only
    stdout = result.stdout
    json_start = stdout.find("[")
    if json_start < 0:
        print(f"No JSON in output: {stdout[:500]}", file=sys.stderr)
        sys.exit(1)
    data = json.loads(stdout[json_start:])
    return data[0]["results"]


def fetch(start: str, end: str) -> tuple[list, list]:
    """Fetch weekly + daily summaries for [start, end]."""
    weekly_sql = (
        "SELECT summary_date, chat_title, week_start, week_end, summary_text "
        f"FROM summaries WHERE summary_type='weekly' "
        f"AND summary_date BETWEEN '{start}' AND '{end}' "
        "ORDER BY summary_date, chat_title;"
    )
    daily_sql = (
        "SELECT summary_date, chat_title, summary_text, message_count "
        f"FROM summaries WHERE summary_type='daily' "
        f"AND summary_date BETWEEN '{start}' AND '{end}' "
        "ORDER BY summary_date, chat_title;"
    )
    return run_d1(weekly_sql), run_d1(daily_sql)


def build_markdown(weekly: list, daily: list, period_label: str) -> str:
    """Group by chat_title, emit Markdown with weekly + daily interleaved."""
    chats = defaultdict(lambda: {"weekly": [], "daily": []})
    for row in weekly:
        chats[row["chat_title"]]["weekly"].append(row)
    for row in daily:
        chats[row["chat_title"]]["daily"].append(row)

    def total_len(c):
        return sum(len(r["summary_text"] or "") for r in c["weekly"] + c["daily"])

    chats_sorted = sorted(chats.items(), key=lambda kv: -total_len(kv[1]))

    out = []
    out.append(f"# Friday — Source summaries ({period_label})")
    out.append(f"\nWeekly: {len(weekly)} | Daily: {len(daily)} | Chats: {len(chats)}\n")
    for chat_title, data in chats_sorted:
        tlen = total_len(data)
        if tlen == 0:
            continue
        out.append(f"\n{'=' * 80}")
        out.append(f"## {chat_title}  ({tlen} chars)")
        out.append("=" * 80)
        if data["weekly"]:
            out.append("\n### WEEKLY")
            for w in data["weekly"]:
                out.append(f"\n**Week {w['week_start']} → {w['week_end']}**")
                out.append((w["summary_text"] or "").strip())
        if data["daily"]:
            out.append("\n### DAILY")
            for d in sorted(data["daily"], key=lambda x: x["summary_date"]):
                text = (d["summary_text"] or "").strip()
                if text:
                    out.append(f"\n**{d['summary_date']}** ({d['message_count']} msgs)")
                    out.append(text)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM-DD")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD")
    ap.add_argument("--out", required=True, help="Output markdown path")
    ap.add_argument("--label", default="", help="Period label for header")
    args = ap.parse_args()

    weekly, daily = fetch(args.start, args.end)
    label = args.label or f"{args.start} → {args.end}"
    md = build_markdown(weekly, daily, label)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(md, encoding="utf-8")
    print(f"Wrote {args.out} — {len(md):,} chars, {len(weekly)} weekly, {len(daily)} daily")


if __name__ == "__main__":
    main()
