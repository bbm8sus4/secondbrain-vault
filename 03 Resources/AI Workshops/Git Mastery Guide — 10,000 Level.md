# Git Mastery Guide — 10,000 Level

> ทุกเรื่องที่ต้องรู้เพื่อใช้ Git ได้อย่างมั่นใจ ตั้งแต่ internal model ไปจนถึง recovery, forensics, และ workflow ขั้นสูง
> HTML version: `git-mastery-guide.html` (same folder)

## 12 Chapters

1. [Git Object Model](#ch01) — blob/tree/commit/tag, content-addressable storage
2. [Three Trees](#ch02) — working dir / staging / HEAD, partial staging
3. [Reflog](#ch03) — ตาข่ายนิรภัย, กู้ทุกอย่างได้ 90 วัน
4. [Reset Demystified](#ch04) — soft/mixed/hard ต่างกันยังไง
5. [Interactive Rebase](#ch05) — reword/squash/fixup/edit/drop, autosquash
6. [Cherry-pick & Revert](#ch06) — ศัลยกรรม commit, revert merge
7. [Bisect](#ch07) — binary search หา commit ที่ทำพัง
8. [Stash ขั้นสูง](#ch08) — partial stash, stash branch, apply vs pop
9. [Log Forensics](#ch09) — pickaxe, blame -C -C, shortlog
10. [Recovery Recipes](#ch10) — 9 สถานการณ์ + วิธีกู้
11. [Hooks & Automation](#ch11) — pre-commit, share hooks, aliases
12. [Worktrees & Performance](#ch12) — sparse checkout, shallow clone, bundle

---

## CH01: Git Object Model

Git เก็บทุกอย่างเป็น 4 ประเภท object ใน `.git/objects/`:

| Object | เก็บอะไร | Key Insight |
|--------|---------|-------------|
| `blob` | เนื้อหาไฟล์ (ไม่มีชื่อไฟล์) | ไฟล์เนื้อหาเหมือนกัน = blob เดียวกัน |
| `tree` | directory listing (ชื่อ + mode + pointer) | track directory structure |
| `commit` | tree pointer + parent(s) + author + message | เก็บ snapshot ทั้งก้อน ไม่ใช่ diff |
| `tag` | pointer ไป commit + tagger + message | annotated tag เท่านั้นที่เป็น object |

```bash
# ดูประเภทของ object
git cat-file -t HEAD

# ดูเนื้อหาของ commit
git cat-file -p HEAD

# ดูเนื้อหาของ tree
git cat-file -p HEAD^{tree}
```

> **Teaching Point:** Git ไม่ได้เก็บ diff ระหว่าง version — ทุก commit = snapshot ทั้งหมด แต่ถ้าไฟล์ไม่เปลี่ยน มัน point ไป blob เดิม (content-addressable)

### Refs = แค่ text file

```bash
cat .git/refs/heads/main    # → SHA ของ commit
cat .git/HEAD               # → ref: refs/heads/main
```

Branch = pointer 41 bytes ไม่ copy อะไรเลย — branching ถูกมาก

---

## CH02: Three Trees

```
Working Dir → git add → Staging (Index) → git commit → HEAD
                                                         │
Working Dir ← git checkout / git restore ←───────────────┘
```

```bash
git diff --cached     # staging vs HEAD (จะ commit อะไร)
git diff              # working vs staging (ยัง unstaged)
git diff HEAD         # working vs HEAD (ทุกอย่างที่เปลี่ยน)
```

### Partial Staging

```bash
git add -p file.js    # เลือก add ทีละ hunk
# y=stage, n=skip, s=split smaller, e=edit hunk
```

> **Workshop Tip:** `git add -p` แยกมือใหม่กับมือโปร — commit สะอาด เรื่องเดียวต่อ commit

---

## CH03: Reflog — ตาข่ายนิรภัย

บันทึกทุกการเคลื่อนไหวของ HEAD + branches เก็บ 90 วัน

```bash
git reflog                      # ดูทั้งหมด
git reflog show feature/payment # เฉพาะ branch
git reflog --date=relative      # พร้อมเวลา
```

### กู้ commit ที่ "หายไป"

```bash
# เผลอ reset --hard → ดู reflog → reset กลับ
git reflog
git reset --hard HEAD@{4}

# ลบ branch ไปแล้ว → กู้จาก reflog
git branch recovered-branch HEAD@{7}
```

> **Rule:** เผลอทำอะไรพัง → หยุด → `git reflog` → 99% กู้ได้

---

## CH04: Reset — สาม mode

| Mode | HEAD | Staging | Working Dir | ใช้เมื่อ |
|------|------|---------|-------------|---------|
| `--soft` | เลื่อน | ไม่แตะ | ไม่แตะ | squash commits |
| `--mixed` (default) | เลื่อน | reset | ไม่แตะ | undo git add |
| `--hard` | เลื่อน | reset | reset | ทิ้งทุกอย่าง |

```bash
# Squash 3 commits
git reset --soft HEAD~3 && git commit -m "Clean feature"

# Undo git add
git reset HEAD file.js   # หรือ: git restore --staged file.js
```

> **Danger:** `--hard` ทำให้ uncommitted changes หายถาวร reflog ช่วยไม่ได้ → stash ก่อนเสมอ

---

## CH05: Interactive Rebase

```bash
git rebase -i HEAD~5
```

| Command | ทำอะไร |
|---------|--------|
| `pick` (p) | เก็บ commit |
| `reword` (r) | แก้ message |
| `edit` (e) | หยุดให้แก้ไข |
| `squash` (s) | รวม commit + รวม message |
| `fixup` (f) | รวม commit + ทิ้ง message |
| `drop` (d) | ลบ commit |

### Autosquash

```bash
git commit --fixup=abc1234           # สร้าง fixup commit
git rebase -i --autosquash HEAD~5   # เรียงให้อัตโนมัติ
git config --global rebase.autosquash true
```

> **Golden Rule:** ห้าม rebase commit ที่ push + คนอื่นใช้อยู่ — history จะพัง

---

## CH06: Cherry-pick & Revert

```bash
# Cherry-pick
git cherry-pick abc1234                  # หยิบ commit เดียว
git cherry-pick --no-commit abc1234      # หยิบมาไม่ commit

# Revert (safe for shared branches)
git revert abc1234                       # ย้อน commit
git revert -m 1 abc1234                  # ย้อน merge commit
```

| ใช้เมื่อ | คำสั่ง |
|---------|--------|
| ต้องการบาง commit จาก branch อื่น | cherry-pick |
| ถอน commit บน shared branch | revert |
| ลบ commit จาก local branch | reset |

---

## CH07: Bisect — Binary Search หาบั๊ก

```bash
git bisect start
git bisect bad                  # ปัจจุบันพัง
git bisect good v2.0.0          # commit เก่าที่ยังดี
# ทดสอบ → good/bad → ซ้ำจนเจอ
git bisect reset                # กลับมา

# อัตโนมัติ:
git bisect start HEAD v2.0.0
git bisect run npm test
```

> **Pro Move:** เขียน test ที่ reproduce บั๊ก → `bisect run` → หา commit ที่ทำพังอัตโนมัติ

---

## CH08: Stash ขั้นสูง

```bash
git stash push -m "WIP: payment"           # stash + ข้อความ
git stash push -m "config" -- config.js     # เฉพาะบางไฟล์
git stash push -p                           # เฉพาะบาง hunk
git stash push -u -m "with new files"       # รวม untracked
git stash show -p stash@{1}                 # ดูว่าเปลี่ยนอะไร
git stash apply stash@{1}                   # apply ไม่ลบ (safe)
git stash branch new-feature stash@{0}      # สร้าง branch จาก stash
```

> **Tip:** ใช้ `apply` แทน `pop` — ถ้า conflict stash ยังอยู่

---

## CH09: Log Forensics

```bash
git log --oneline --graph --all --decorate  # graph สวย
git log --oneline -- src/payment.js         # history ของไฟล์
git log --grep="payment"                    # ค้น message
git log -S "calculateTotal"                 # pickaxe: ค้นใน code
git log -G "TODO|FIXME"                     # regex ใน code change
git log --author="John" --since="2024-01-01"
git log --follow -- old-name.js             # ติดตามแม้ rename

# Blame
git blame -L 50,70 src/payment.js           # เฉพาะบรรทัด
git blame -w -C -C src/payment.js           # ข้าม whitespace + code move

# Shortlog
git shortlog -sn --all                       # สรุป commits ต่อคน
```

> `git log -S` (pickaxe) = undervalued ที่สุด — หาว่า function ถูกเพิ่ม/ลบใน commit ไหน

---

## CH10: Recovery Recipes

| สถานการณ์ | วิธี |
|----------|------|
| ย้อน commit (ยังไม่ push) | `git reset --soft HEAD~1` |
| ย้อน commit (push แล้ว) | `git revert abc1234` |
| commit ผิด branch | `git branch feature` → `git reset --hard HEAD~1` → `git checkout feature` |
| เผลอ reset --hard | `git reflog` → `git reset --hard HEAD@{N}` |
| ลบ branch แล้ว | `git reflog` → `git branch recovered SHA` |
| Rebase/merge conflict เยอะ | `git rebase --abort` / `git merge --abort` |
| push secret ขึ้นไป | **Revoke ทันที** → `bfg --delete-files` → gc |
| กู้ไฟล์ที่ถูกลบ | `git log --diff-filter=D -- path` → `git checkout SHA^ -- path` |

---

## CH11: Hooks & Automation

| Hook | เมื่อไหร่ | ใช้ทำอะไร |
|------|---------|----------|
| `pre-commit` | ก่อน commit | lint, format, ตรวจ secrets |
| `commit-msg` | หลังเขียน message | ตรวจ format |
| `pre-push` | ก่อน push | test, branch protection |
| `post-merge` | หลัง merge/pull | npm install ถ้า package.json เปลี่ยน |

```bash
# Share hooks กับทีม
git config core.hooksPath .githooks
```

### Must-have Aliases

```bash
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
```

---

## CH12: Worktrees & Performance

```bash
# Worktree: ทำงานหลาย branch พร้อมกัน
git worktree add ../hotfix hotfix/payment
git worktree list
git worktree remove ../hotfix

# Sparse checkout: clone เฉพาะ folder
git clone --filter=blob:none --sparse <url>
git sparse-checkout set src/frontend

# Shallow clone
git clone --depth=1 <url>

# Bundle: ส่ง repo แบบไม่ต้องมี server
git archive --format=zip HEAD -o code.zip
```

---

## Cheat Sheet — คำสั่งที่คนส่วนใหญ่ไม่รู้

| Command | ทำอะไร |
|---------|--------|
| `git diff --word-diff` | diff ระดับคำ |
| `git clean -fd` | ลบ untracked ทั้งหมด |
| `git commit --allow-empty -m "trigger CI"` | commit เปล่า trigger CI |
| `git rev-list --count HEAD` | นับ commits ทั้งหมด |
| `git diff --name-only main..HEAD` | ชื่อไฟล์ที่เปลี่ยน |
| `git grep "pattern"` | grep เฉพาะ tracked files |
| `git log --left-right main...feature` | commits ที่ต่างกัน 2 branches |
| `git rerere` | จำวิธีแก้ conflict → auto next time |
| `git notes add -m "note" HEAD` | แปะโน้ตไม่แก้ commit |