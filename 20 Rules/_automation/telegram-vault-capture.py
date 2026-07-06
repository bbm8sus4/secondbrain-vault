#!/usr/bin/env python3
"""Telegram -> Obsidian vault quick capture.

Polls getUpdates on a dedicated capture bot and appends every message the
owner sends/forwards into `00 Inbox/Telegram YYYY-MM-DD.md`. Photos are
downloaded into `00 Inbox/แนบ/` and embedded. Runs from launchd every 60s.

Config: ~/.vault-capture.env   TELEGRAM_BOT_TOKEN, ALLOWED_USERS (comma ids)
State:  ~/.vault-capture.state.json  (last processed update_id)
Exits silently when no token is configured yet.
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ENV = Path.home() / ".vault-capture.env"
STATE = Path.home() / ".vault-capture.state.json"
INBOX = Path.home() / "SecondBrain/00 Inbox"
ATTACH = INBOX / "แนบ"


def load_env():
    cfg = {}
    if ENV.exists():
        for line in ENV.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                cfg[k.strip()] = v.strip()
    return cfg


cfg = load_env()
TOKEN = cfg.get("TELEGRAM_BOT_TOKEN", "")
if not TOKEN:
    sys.exit(0)
ALLOWED = {u.strip() for u in cfg.get("ALLOWED_USERS", "").split(",") if u.strip()}
API = f"https://api.telegram.org/bot{TOKEN}"


def api(method, **params):
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(f"{API}/{method}", data=data, timeout=30) as r:
        return json.load(r)


def download(file_id, stem):
    info = api("getFile", file_id=file_id)
    fp = info["result"]["file_path"]
    ext = os.path.splitext(fp)[1] or ".jpg"
    ATTACH.mkdir(parents=True, exist_ok=True)
    dest = ATTACH / f"{stem}{ext}"
    url = f"https://api.telegram.org/file/bot{TOKEN}/{fp}"
    with urllib.request.urlopen(url, timeout=60) as r, open(dest, "wb") as f:
        f.write(r.read())
    return dest.name


state = {"offset": 0}
if STATE.exists():
    try:
        state = json.loads(STATE.read_text())
    except Exception:
        pass

resp = api("getUpdates", offset=state["offset"] + 1, timeout=0)
for u in resp.get("result", []):
    state["offset"] = u["update_id"]
    msg = u.get("message")
    if not msg:
        continue
    uid = str(msg.get("from", {}).get("id", ""))
    if ALLOWED and uid not in ALLOWED:
        continue
    text = msg.get("text") or msg.get("caption") or ""
    if text.startswith("/start"):
        api("sendMessage", chat_id=msg["chat"]["id"],
            text="พร้อมแล้วครับ ✅ ส่งหรือ forward อะไรมาก็ได้ เดี๋ยวเก็บเข้า Second Brain ให้")
        continue

    ts = datetime.fromtimestamp(msg["date"])
    INBOX.mkdir(parents=True, exist_ok=True)
    day_file = INBOX / f"Telegram {ts:%Y-%m-%d}.md"
    entry = [f"## {ts:%H:%M}"]

    fo = msg.get("forward_origin")
    if fo:
        src = (fo.get("sender_user", {}).get("first_name")
               or fo.get("chat", {}).get("title")
               or fo.get("sender_user_name")
               or "ไม่ทราบที่มา")
        entry.append(f"*(forward จาก {src})*")

    if msg.get("photo"):
        stem = f"tg-{ts:%Y%m%d-%H%M%S}-{msg['message_id']}"
        try:
            name = download(msg["photo"][-1]["file_id"], stem)
            entry.append(f"![[แนบ/{name}]]")
        except Exception:
            entry.append("*(มีรูปแนบ แต่ดาวน์โหลดไม่สำเร็จ — เปิดดูใน Telegram)*")

    if msg.get("document"):
        doc = msg["document"]
        entry.append(f"*(ไฟล์แนบ: {doc.get('file_name', 'document')} — เปิดดูใน Telegram)*")

    if text:
        entry.append(text)

    if len(entry) > 1:
        with open(day_file, "a", encoding="utf-8") as f:
            f.write("\n".join(entry) + "\n\n")
        try:
            api("sendMessage", chat_id=msg["chat"]["id"],
                reply_to_message_id=msg["message_id"], text="✅ เข้า vault แล้ว")
        except Exception:
            pass

STATE.write_text(json.dumps(state))
