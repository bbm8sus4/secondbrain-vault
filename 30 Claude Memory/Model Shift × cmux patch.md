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
