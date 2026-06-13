---
name: Chrome MCP × Google Docs editing playbook
description: Operational know-how for editing Google Docs (canvas-rendered) via Chrome MCP — what works, what doesn't, and the safe workflow
type: reference
originSessionId: 96d71952-78a0-4d27-acda-df50391f7f45
---
Google Docs uses canvas rendering, so Chrome MCP behaves very differently from a normal HTML page. This is the working playbook learned the hard way.

**Why this matters:** Going in blind, almost everything fails — clicks land on the wrong tab, keyboard shortcuts do nothing, and clipboard writes get blocked. Without this playbook, attempting to edit a Google Doc via Chrome MCP wastes a lot of cycles before realizing what won't work.

## What WORKS

1. **`mcp__chrome-mcp__chrome_switch_tab`** — REQUIRED before any chrome_computer interaction. Without it, OS focus is wrong and clicks land on the wrong window. **Even after switch_tab succeeds, `chrome_computer` action=`type` may still target the previously-active tab if the OS hasn't actually transferred focus.** ALWAYS verify with `chrome_javascript` (`location.href` + `document.hasFocus()`) on the target tabId BEFORE typing, AND type a small `TEST_MARKER` first then verify via mobilebasic that it landed in the right doc. The cost of a 2-second verify is nothing compared to spraying 6000 chars into the wrong file (happened once on user's expense spreadsheet — see incident note below).
2. **`mcp__chrome-mcp__chrome_computer` action=`type`** — inserts Unicode text (Thai works) at cursor position via CDP `Input.insertText`. Handles 3000+ chars per call reliably.
3. **`mcp__chrome-mcp__chrome_computer` action=`left_click`** on doc canvas — places cursor (after switch_tab).
4. **Reading doc content** via `fetch('/document/d/<ID>/mobilebasic', {credentials: 'include'})` — returns full HTML with all body text. Strip tags and you have the content. (gdrive MCP is blocked by auth.)
5. **Find & Replace dialog** — opens via menu click on `#docs-edit-menu` then "ค้นหาและแทนที่". Inputs are real HTML (`#c5` find, `#c8` replace). Set values via React-friendly setter:
   ```js
   const setter = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(input), 'value').set;
   setter.call(input, value);
   input.dispatchEvent(new Event('input', {bubbles: true}));
   ```
   Then `.click()` the button whose `textContent.trim() === 'แทนที่ทั้งหมด'`.
6. **Find & Replace regex with `\n`** — the regex checkbox enables multi-paragraph matching. `\n.*` chains work up to ~7-8 lines reliably; longer patterns may silently fail to match.
7. **Version History restore** — File menu → ประวัติเวอร์ชัน → ดูประวัติเวอร์ชัน. Click the version row, then "คืนค่าเวอร์ชันนี้" button (top toolbar), then "คืนค่า" in confirm dialog. This is the safety net for damage.
8. **Undo button** in toolbar (`[aria-label*="เลิกทำ"]`) — clickable via JS, but bounded by the doc's undo history.

## What DOES NOT work

1. **Cmd+A, Cmd+End, Cmd+Home, Cmd+Z** via `chrome_computer` action=`key` or `chrome_keyboard` — modifier+key combos do not reach Google Docs' shortcut handlers. The events fire but the doc ignores them.
2. **Backspace, Delete, arrow keys** via chrome_computer — also don't move the cursor or delete in the doc.
3. **Edit menu → Select All click** — the menu opens, the item is clickable, but the action does not actually select.
4. **`navigator.clipboard.writeText`** — fails with "Document is not focused" even after switch_tab.
5. **`document.execCommand('copy')`** — returns false (no user gesture).
6. **`gdrive_read_file` MCP** — 403 unregistered caller.
7. **`/export?format=txt`** opened in a new window — gets a "ข้อผิดพลาด" page (transient auth/redirect token).
8. **Synthetic KeyboardEvent dispatch** — Google Docs filters by `isTrusted`.
9. **Cross-paragraph regex with `(?=...)` lookahead or `[\s\S]*?` matching the whole doc** — fails. The F&R engine seems to operate per-paragraph or with limited multi-line support; only explicit `\n.*` chains work.
10. **F&R regex checkbox toggle via real coordinate click** — sometimes the kix canvas captures clicks inside the dialog area at hit-test level (`elementFromPoint` returns `kix-page-paginated` instead of the dialog widget), so coord-based clicks fall through. Setting `regexCb.checked = true` via React setter only flips the DOM input — does NOT actually enable regex mode in F&R's engine. If you cannot get a real user click on the regex checkbox, plan as if regex is unavailable.
11. **F&R replace input with literal `\n` to insert paragraph breaks** — without regex mode the `\n` is searched as literal backslash-n text, not a paragraph break. So you cannot turn a single-paragraph blob into multi-paragraph via F&R replace alone.

## CRITICAL pitfall: regex during cleanup must be OLD-only

When the doc has BOTH versions present (e.g., old draft on top + new formal version below), do **not** use generic patterns like `ข้อ N\..*\n.*\n.*` — they match BOTH versions and silently destroy the new one. Symptoms: doc shrinks, sections vanish, you don't notice until verifying.

**Safe approach when both versions coexist:**
- Anchor on phrases that exist ONLY in the old draft. Examples from EasyBOT contract: `(template)`, single-quote chars `‘…’` (NEW uses double quotes), `บริษัทแต่งตั้ง`, `ในฐานะ Founder และ Chairman`, `(ก) 'EasyBOT'` definition format.
- After each Replace All, fetch mobilebasic and verify NEW markers (e.g., `END OF FORMAL VERSION`, `1356/2549`, key article headings) still exist before continuing.

**Safer overall workflow:** delete OLD *first* (when only OLD exists in doc), THEN type NEW. This way every regex you fire is unambiguously safe — there's nothing else to damage.

## Standard workflow for "replace doc body wholesale"

1. Save the new content to a local `.md` file as backup (cheap insurance).
2. `switch_tab` to focus the doc tab.
3. `left_click` on doc canvas at any visible page position to place cursor.
4. Open Find & Replace via Edit menu → ค้นหาและแทนที่ (use real coord click on `#docs-edit-menu`, then real coord click on the menuitem rect — JS `.click()` on the menuitem does not actually fire the action).
5. Enable regex checkbox if you can get a real user click on it. If the dialog is being shadowed by the kix canvas at `elementFromPoint` level, regex mode is effectively unavailable — switch to "literal F&R per paragraph" plan B.
6. **Plan A (regex available):** Use the JS-driven setter + click pattern (above) to wipe the OLD content. Iterate with chunks of 4–8 lines: `<unique-anchor>.*\n.*\n.*\n.*\n.*`. Verify after each round.
   **Plan B (literal F&R only):** Fetch mobilebasic, parse out each paragraph's exact text, sort by length DESC (longer/more-specific first), then F&R each paragraph → empty via the React setter pattern. ~30s per batch of ~35 paragraphs (each loop iteration sleeps ~250ms after Replace All click). Re-fetch mobilebasic between batches; 100+ paragraphs typically needs 3 batches.
7. Once mobilebasic shows the doc near-empty, close Find & Replace.
8. `switch_tab` again, `left_click` on canvas, then `chrome_computer` action=`type` with the new content in chunks of ~3000 chars. Newlines in the `text` argument become real paragraph breaks (CDP `Input.insertText` injects them as actual `\n` chars at cursor position).
9. Verify via mobilebasic that all expected markers/sections are present.

**Caveat with Plan B (literal F&R):** Each paragraph deletion leaves an empty paragraph behind. After ~100 deletions you have ~100 trailing blank paragraphs that you cannot remove (Backspace/Delete don't reach the editor via MCP). Document content is correct but visually has lots of trailing whitespace — flag this to the user and recommend manual cleanup with Cmd+End → Backspace.

## When in doubt: restore via Version History

If anything looks wrong (sections missing, wrong text), File → ประวัติเวอร์ชัน → ดูประวัติเวอร์ชัน → pick a known-good version → คืนค่าเวอร์ชันนี้ → คืนค่า. This is non-destructive (creates a new version on top) and recovers from any damage.
