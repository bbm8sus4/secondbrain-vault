---
tags: [project, tool, single-file-html, seating]
project: Office Seating Plan
created: 2026-07-02
version: 3.8.0
---

## v3.7.0–3.8.0 · audit fixes (2026-07-03)
Two-round exhaustive multi-agent adversarial review (Workflow, 7 dimensions, 40 confirmed findings) → fixed 24 in v3.7.0 (11) + v3.8.0 (13). Backup pre-fix: `~/Desktop/_archive/office-seating-overview-v3.6.4-pre-audit-fix-*.html`. Every fix Chrome-MCP-verified on live tab (session on port 12306).

**Fixed (security/data-loss/a11y/perf):**
- Stored XSS via imported `person.photo` — 2 sinks (dashboard onboarding L1664, org node L2498) missed the `_photoBg()` escape helper. Added `_photoBg(photo,col)` canonical escaper.
- H2: `switchOrgCompany`/`loadTpl`(org)/`importOrgJSON` never cleared `orgUndoStack/orgRedoStack` → one Undo wrote one company's chart over the other silently. Clear stacks on company change.
- `promptSaveView` + `reserveSeat` still used `window.prompt` (Chrome silently suppresses) → converted to `openInputModal`.
- `render()` rebuilt all 5 views every mutation → gated to visible view; `setView` now calls `render()` after class toggle so switching re-renders target fresh. Added `_activeView()`.
- `renderSettings` re-parsed both org localStorage blobs O(4N)/call → hoisted to one Map build. `settingsSearch` debounced 140ms.
- Ghost cells `+ เพิ่ม`/`+ เพิ่มเลน` were `<div onclick>` → `<button>` (keyboard/touch). `.prow-ctl` lane controls hover-only → added `@media(hover:none){opacity:1}`. Org node boxes: added Enter/Space → `editOrgNode`.
- `savePerson` assigned `product` without reconciling `lane` → invisible member of laneless product. Now reconciles lane + `fillProductSelect` filters out laneless products.
- `deletePerson` left dangling org `personId` links (stale baked name) → `_unlinkPersonFromAllOrg`.
- `toastUndo` button called generic view-aware `undo()` → could hit org stack. Now `_toastUndoAction` forces seating stack.
- `importOrgJSON` overwrote current company silently → reads `__company`, confirms, switches if needed.
- **Export ทั้งหมด / Import ทั้งหมด (bundle)**: `exportAll`/`importAll` package state+both org charts+templates+`osp.views.v1` in one file — fixes "machine move" (views had NO export path before). Quota banner now points to it.
- `migrate` toasts when it kicks laneless-product people. `validateState` checks products/lanes shape. Search (top-nav + Manage) now matches product/lane names.
- Removed dead `toggleOrgRisk`/`orgRiskOn`, `renderUtilization` (no #utilization target). `HISTORY_CAP` 50→20. `onResize` rAF-throttled. Quota % cached (invalidated per save).

**Consciously deferred (cosmetic / nil-impact / needs-decision):**
- Full EN-mode localization (many hardcoded Thai in prefs/lane/modal — large, EN is secondary).
- Dead i18n keys (~22×2), orphaned CSS blocks, `renderSavedLine` no-op stub, `.risk-on` CSS remnants (harmless; keeps risk badges hidden).
- Avatar markup dedup (6 divergent builders — refactor risk; buggy photo part already unified via `_photoBg`).
- Terminology drift โปรเจกต์/โปรดักส์/`.pj-*` (cosmetic).
- `_withSaveRollback` pushUndo-before-mutate phantom-undo on throw (rare); undo/redo ignore save() return; merge-import dup-by-id; presentation cross-tab org sync (LOW edges).
- Dashboard project/lane analytics, template-load lane-revert warning (feature requests).
- computeHR 2×/render, dashboard O(seats×people), photo-pool for undo snapshots (nil impact at 30 people; photo-in-localStorage deferred by owner earlier).
- **resetAll restores 7 hardcoded fake NEW-hire people** — needs owner decision (open 5-vs-7 question).
---

# Office Seating Plan

Single-file HTML app จัดการผังที่นั่ง + ผังองค์กร + product board + master directory ของ Thunder Solution + Easy Slip (Floor 2, ~30 คน)

## Files

- **Live file:** `~/Desktop/office-seating-overview.html`
- **Legacy archive:** `~/Desktop/_archive/office-seating-planner-v2.0-LEGACY.html`
- **Backup v2.4.0:** `~/Desktop/_archive/office-seating-overview-v2.4.0-backup-20260702-133516.html`

## Storage keys (localStorage)

| Key | Content |
|---|---|
| `osp.v2` | main state (people, rooms, holds, products) |
| `osp.v2.lkg` | last-known-good state backup |
| `osp.org.v1` | Thunder org chart |
| `osp.org.easyslip.v1` | Easy Slip org chart |
| `osp.org.v1.lkg` / `osp.org.easyslip.v1.lkg` | org LKG backups |
| `osp.templates.v1` | seating + org scenario templates |
| `osp.views.v1` | saved filter views (v2.7.1+) |
| `osp.locked` / `osp.theme` / `osp.lang` | user prefs |
| IDB `osp-backups` | ring of 15 snapshots (state + org) |

## Architecture

- **Tabs:** ผังที่นั่ง · ผังองค์กร · แดชบอร์ด · โปรดักส์ · จัดการ (Manage)
- **Master data source (v2.6.0+):** `state.people` in "จัดการ" tab; other tabs render from it
- **Org nodes:** independent list but each node has optional `personId` → hydrates name/company/photo from `state.people`
- **Undo/redo:** separate stacks for seating (`undoStack`) and org (`orgUndoStack`), Cmd+Z is view-aware
- **Global error boundary:** `window.onerror` + `unhandledrejection` → red banner + LKG restore + report download

## Changelog

### v2.4.0 (baseline — 24 bug fixes from prior session)
- import validate + seatCount guard (Bug 1)
- org chart drag cap (Bug 3)
- template/org save error surfacing (Bug 4)
- Lock mode coverage: undo/redo, org, reset, import, add-person/room (Bug 5)
- LKG + IDB ring backup for org
- CSS quota warning fix, PDF name fix (POOM NOI, NONG)
- Isolate + archive legacy planner (osp.v2 → osp.v2.legacy)

### v2.5.0 (adversarial regression fix — 38 findings)
Fixed 50 confirmed regressions from 5-agent adversarial verify workflow:
- **Root cause A:** `save()`/`saveOrg()`/`saveTpls()` now return bool + `toastError()` variant + toast queue
- **Root cause B:** All mutation callers gate success toast on save return + snapshot rollback (~20 sites)
- **State validation** added to `restoreFromIDB`/`restoreLKG`/`loadTpl`
- **Lock coverage gaps closed:** storage-event guard, product mutations, editPerson/editRoom Lock feedback
- **Org drop guard:** ancestor check + descendant lv check
- **Cycle detection** in `validateOrg`, `isAncestor` bumped 60→10000 with seen-set
- **Restore UI** for org LKG/IDB (new button in org toolbar)
- **Canvas roster:** H auto-grows to fit all rows (no truncation), Thai font fallback (Noto Sans Thai, Sarabun)
- **POOM NOI/NONG:** one-shot `nameFix250` migration → fullName corrected for existing users

### v2.6.0 (Settings tab / Master directory)
- New "ตั้งค่าบุคคล" tab with master person table (30 people)
- 8-column view: person · role · company · status · seat · product · org · actions
- Search + filter (company / status)
- Stats bar (total / active / new-hire / on-leave / seated / linked)
- **Link Person to Org:** modal that binds `state.people.id` → `orgState.node.personId`
- `_resolveOrgNode()` hydrates node from state when linked — org node shows current name/photo/company from master
- Linked org nodes get green border + 🔗 badge

### v2.6.1 (Quick wins from CRUD-basic audit)
- **XSS escape:** `attr()` helper for JSON.stringify inside HTML attributes; ~10 sites (renderSettings, openLinkOrgModal, renderSeat, renderUnassigned, etc.)
- **Global error boundary:** window.onerror + unhandledrejection → red banner (Restore LKG / Download report / Reload)
- **maxlength on inputs:** nickname 40 / fullName 120 / role 80 / team 40 / task 120 / room name 60 / room num 8 / o_name 120 / tplName 80 / search 60 · plus `FIELD_CAP=1024` in `stripEmoji`

### v2.7.0 (Toolbar Phase 1+2 — unified contextual)
- Move toolbar out of `#seatingView` → top-level (visible all tabs)
- `data-view="..."` attribute on toolbar items → CSS auto-hide unless matches current view
- Delete separate `#orgView` toolbar (consolidate)
- New overflow menu ⋯ with 4 sections: seating data · org data · print/restore · ⚠ danger

### v2.7.1 (Filter bar Hybrid D)
- Views dropdown (5 built-in + custom saved to `osp.views.v1`): ทั้งหมด · NEW hires · รอจัดที่นั่ง · Thunder Solution · Easy Slip
- Company + Status as segmented controls (few options)
- Room / Team / Placement as popover buttons (with checkbox lists, search when >6)
- Active-filter summary + "บันทึกเป็น view" button

### v2.8.0 (Slim KPI hero — later removed)
- Added `.hero-slim` bar with 📍 title + KPIs (30 คน · seated ratio · awaiting · companies)
- Status badges on right: 🔒 Locked · ⚠ Dirty · 💾 saved timestamp
- **Removed entirely in v2.8.2** (user feedback)

### v2.8.1 (Utility cluster relocated + Manage tab)
- Utility cluster (ไทย/EN · 🌙 · 🔒 · ⛶ · ⋮) moved from toolbar → **top nav** (right of tabs)
- Tab renamed: "ตั้งค่าบุคคล" → **"จัดการ"** (Manage)
- Create buttons moved: +Person / +Room / Templates → into Manage view action row
  - Renamed labels: "เพิ่มพนักงาน", "เพิ่มห้อง", "เทมเพลต / มุมมองที่บันทึกไว้"

### v2.8.2 (Removed slim hero, status → top nav)
- `.hero-slim` block + all `.hs-*` CSS deleted
- Status indicators (Lock badge, Dirty badge, Saved line) moved into top nav between tabs and utility cluster
- Saved ~44px vertical space

### v2.8.3 (Search + Undo/Redo → top nav)
- Search input moved from toolbar → top nav (with inline search icon)
- Undo/Redo moved from toolbar → top nav
- Toolbar **auto-hides** when no visible children (Seating/Dashboard/Manage views show no toolbar)

### v2.8.4 (Remove saved timestamp — current)
- Removed 💾 saved timestamp indicator from top nav
- Kept Lock + Dirty badges
- `renderSavedLine()` neutered to no-op

## UI hierarchy (current v2.8.4)

```
┌─ Top nav (sticky) ────────────────────────────────────────────────────┐
│ [Tabs · 5] [🔍 Search] [↶↷] [🔒][⚠]        ไทย EN · 🌙 · 🔒 · ⛶ · ⋮  │
├─ Toolbar (contextual, hidden for seating/dashboard/manage) ───────────┤
│   Org: [+เพิ่มคน] [Thunder|EasySlip] [⚠risk]                          │
│   Product: [+โปรดักส์]                                                │
├─ Filter bar (seating only) ───────────────────────────────────────────┤
│ [Views ▾] │ [Company seg] [Status seg] │ [ห้อง▾][ทีม▾][ที่นั่ง▾] │ Clear │
├─ View content ────────────────────────────────────────────────────────┤
│ Seating: floor plan + onboarding tray                                 │
│ Org: chart with lv/col grid + drag                                    │
│ Dashboard: KPI chips + donuts + tables                                │
│ Product: lanes + drag cards                                           │
│ Manage: [+person][+room][templates] + directory table                 │
└───────────────────────────────────────────────────────────────────────┘
```

## Open questions (from earlier session)

- **จำนวน NEW hires:** seed มี 7 คน (PM, COO+, SALE, MKTX, PO, CFO, CSMG) — พี่ยังไม่ยืนยันว่า 5 หรือ 7
- **Bob (COO):** seed มี `nh-coo` = "COO (incoming, replaces Bob)" — พี่ยังไม่บอกว่าย้ายไปตำแหน่งไหน

## Related notes

- [[feedback_secondbrain_vs_work_folder]] — SecondBrain vs Work folder split convention
- Adversarial verify workflow output: `/private/tmp/claude-501/-Users-aexgee/27a1612c-22b0-4899-8090-0137499b2074/tasks/w0j656k27.output`
