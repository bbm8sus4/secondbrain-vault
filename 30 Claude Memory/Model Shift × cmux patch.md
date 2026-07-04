---
name: project-modelshift-cmux
description: "Model Shift (gear-lever model switcher) patched to also target cmux surfaces, not just tmux panes"
metadata: 
  node_type: memory
  type: project
  originSessionId: 13b494b3-94d0-42e7-8cdb-97fa23d26b24
---

**Model Shift + cmux backend** (patched 2026-07-03)

- Model Shift = Electron floating gear-lever widget that sends `/model <x>` into Claude Code sessions. Original (milind-soni/stickshift-claude) is tmux-only.
- Patched `main.js` to add a cmux backend: lists surfaces via `cmux --json --id-format both tree --all` (defensive recursive walk), sends via `cmux send --surface <uuid>` + `cmux send-key --surface <uuid> enter`, kill button maps to `close-surface`. tmux + cmux targets merged in one picker, claude-likely first.
- Working copy: `~/Code/modelshift-cmux/src/` → pack with `npx @electron/asar pack src app.asar` → copy to `/Applications/Model Shift.app/Contents/Resources/app.asar` → `codesign --force --deep -s -` (ad-hoc; original Developer ID signature is gone).
- Debug log: `~/gearshift.log` (logs raw cmux JSON head when 0 surfaces found).
- Known issue 2026-07-03: cmux socket gives Broken pipe when app process is a stale build running across a brew upgrade — restart cmux.app fixes it. Related: [[คู่มือ - Cmux|reference-cmux]]
- cmux CLI facts: key name is lowercase `enter`; global flags go before the command (`cmux --json tree --all`); `cmux version` works without socket.
- **Effort bank added 2026-07-03**: row of 5 drive-mode buttons (LOW/MED/HIGH/XHI/MAX) between LCD and shifter — sends `/effort <low|medium|high|xhigh|max>` to the selected session via the same send path as `/model`. Window grew 530→564px (both main.js BrowserWindow and #chrome CSS must match). Last-sent level persists in localStorage `gearshift-settings.effort`. Tach sweeps with effort level (max ≈ redline).
- Claude Code CLI fact: `/effort <low|medium|high|xhigh|max>` is a real slash command (verified via strings on the 2.1.185 binary); xhigh/max availability depends on model.
- **Auto-follow backend (2026-07-04)**: `AUTO` button (was `ALL`) = follow the frontmost terminal. IPC `frontmost` returns bundle id via `System Events get bundle identifier of first process whose frontmost is true`; renderer maps `dev.warp.Warp-Stable`→warp, `com.cmuxterm.app`→cmux (tmux can't be told from bundle id). Switches backend only when the frontmost app *changes* (`lastBid` guard), so a manual pin sticks while you stay in one window. Clicking a specific backend = manual pin (autoFollow off); clicking AUTO resumes. Model Shift is `focusable:false` so it's never itself frontmost.
- **Warp backend + terminal selector (2026-07-04)**: added a `ALL/cmux/Warp/tmux` button row to filter targets by backend (empty backends greyed via `.beBtn.empty`). Warp has NO CLI/socket and no useful AppleScript dict (`warp-cli` = Cloudflare VPN, not the terminal) — driven via System Events keystroke into the ACTIVE Warp tab (`osascript`: `tell application "Warp" to activate` → `keystroke cmd` → `key code 36`). Needs Accessibility permission for Model Shift; error 1002/-25211 → `no-access` code → UI says enable Accessibility. Can't target a specific Warp tab, only the focused one; kill button is a no-op for Warp. Each pane now carries a `backend` field ('tmux'/'cmux'/'warp'). Window 564→590px. NOT tested live (would type into own Warp session).
