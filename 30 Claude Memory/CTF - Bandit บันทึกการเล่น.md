---
name: CTF writeup — OverTheWire Bandit (running log)
description: Bandit wargame writeup — levels solved, techniques used, defensive lessons mapped to user's own systems. Append new levels as they're solved.
type: project
originSessionId: a4b8f59d-a5ce-4b36-8841-d300a1cb3ac2
---
OverTheWire Bandit (https://overthewire.org/wargames/bandit/) — classic Linux/SSH/CLI wargame. Used as the first hands-on CTF lab for the user's hacker learning track. Each level reveals a password to the next via a Linux-CLI puzzle.

**Connection pattern:**
```
sshpass -p <password> ssh -o StrictHostKeyChecking=no -p 2220 banditN@bandit.labs.overthewire.org '<remote command>'
```

**Why sshpass:** non-interactive password auth. Default OpenSSH refuses to accept password on stdin for security; sshpass spawns ssh under a pty and feeds the password.

---

## Level 0 → 1 — Recon, baby

**Creds:** `bandit0 / bandit0`
**Solve:** `cat ~/readme`
**Lesson:** First instinct on any new shell: read every README, motd, .profile. Many CTFs and real-world boxes hand you the next step in plain text — you just have to look.
**Mapped to defense:** On your Cloud Run / CF Worker instances, never leave `README`, `.env.example`, `notes.md` in deployed image. Attackers' first move = ls / cat the obvious.

---

## Level 1 → 2 — File named `-`

**Goal:** Read a file named `-` (single dash).
**Why hard:** Most CLI tools treat `-` as stdin/stdout sentinel. `cat -` waits for stdin forever.
**Solve:** `cat ./-` (relative path defeats the dash interpretation).
**Lesson (SO#14 edge state):** Every CLI tool has reserved tokens. Filename = `-`, `--`, leading-`-`, NUL byte, newline, etc. all break naive parsing. Defenders should:
- Validate uploaded filenames at the HTTP layer (reject `^-`, `--`, control chars)
- Always use `--` separator before user-supplied paths in shell (`rm -- "$user_file"`)

**Mapped to your systems:**
- **Friday AI bot:** if you ever shell out to handle user-uploaded files (Telegram file_id), an attacker-named `-rf /` wreaks havoc with naive `rm $file`.
- **OCR Bot:** Cloud Run handler must NOT pass filenames to subprocess without `--` and quoting.

---

## Level 2 → 3 — Combo: spaces + dashes

**Goal:** Read file named `--spaces in this filename--`.
**Why hard:** Combined edge cases — leading `--` (parsed as end-of-options), interior spaces (need quoting).
**Solve:** `cat "./--spaces in this filename--"`
**Lesson:** Attackers chain edge cases. A single defense doesn't cover combinations.
**Note:** I (Claude) initially failed this level because the Bandit team updated the filename to combine BOTH attacks. Standing Order #19 (time-box pivot) kicked in — instead of retrying the same broken command, I pivoted to recon (`ls -la`) and saw the combo. **Pivoting on failure beats persisting.**

---

## Level 3 → 4 — Hidden file, multi-dot prefix

**Goal:** Read `~/inhere/...Hiding-From-You`.
**Why hard:** Three-dot prefix invisible to default `ls`. Also looks like `..` (parent) at glance.
**Solve:** `ls -la ~/inhere/` to spot it, then `cat "./inhere/...Hiding-From-You"`.
**Lesson:** Default tool views hide things. Always `ls -la`, `ps auxf`, `netstat -tulpn`, `find / -newer` for full visibility.
**Mapped to defense:** Adversaries leave persistence in `.` files. On any compromised box, `find /home -name '.*' -type f -mtime -7` to spot recent dot-files.

---

## Level 4 → 5 — File type by content, not extension

**Goal:** In `~/inhere/`, 10 files named `-file00`...`-file09`. Only one is human-readable text. Find it.
**Why hard:** Filenames don't tell you content. `.txt` extension means nothing.
**Solve:**
```bash
file ~/inhere/* | grep "ASCII text" | cut -d: -f1 | xargs cat
```
The `file` command reads magic bytes / heuristics to identify content type independent of extension.
**Lesson:** Trust content over metadata. Extensions, MIME types, Content-Type headers all lie.
**Mapped to defense:**
- **Invoice Control Hub:** when users upload "invoice.pdf", run `file` on actual bytes server-side. PDF magic = `%PDF`. If header doesn't match, reject — even if extension/MIME claims PDF.
- **OCR Bot:** same — Telegram-sent files; verify magic bytes before passing to Tesseract/Gemini.
- **R2 / S3 buckets:** strip user-controlled Content-Type on upload, set it server-side from sniffed bytes.

---

## Standing Orders activated this session

- **SO#13 Recon-first** — every level started with `ls -la` or `file` command before action. Saved time at Level 2 when the trick changed.
- **SO#14 Edge state hunting** — every Bandit level IS an edge case. The whole game is "what shell quirks exist?"
- **SO#19 Time-box and pivot** — Level 2 retry returned empty; immediately pivoted to recon instead of retrying same broken command.
- **SO#21 Read memory actively** — next session should grep this file before starting Bandit Level 5+ to pick up where left off without re-explaining.

---

## Resume point

**Current state:** Level 5 password obtained: `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`
**Next level:** Bandit Level 5 → 6
**Hint preview (Level 5):** Find file in `inhere/` matching: human-readable, 1033 bytes, not executable. Use `find -size -user -perm -readable -executable`.

Pick up here next time without re-running 0–4.
