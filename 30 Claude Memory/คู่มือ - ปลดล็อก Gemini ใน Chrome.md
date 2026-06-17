---
name: reference-gemini-in-chrome-unlock
description: "How to unlock the Chrome top-right \"✦ Ask Gemini\" button on a Thai Google account (Chrome 148, macOS) — Local State patch + launch flag. Verified working 2026-05-13."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 34edec0e-ba14-4aa3-ab9c-b06cde76d83c
---

**Problem:** Chrome's "✦ Ask Gemini" toolbar button (Gemini in Chrome / GLIC) doesn't appear for Thai-region Google accounts even after enabling `chrome://flags/#glic`. Cause: Chrome caches `variations_country = "th"` in `Local State` and `is_glic_eligible = false` per profile — the flag only enables the *code*, not the field-trial config that surfaces the UI.

**Fix (verified on Chrome 148.0.7778.167, macOS, account `bobbysomporn@gmail.com`):**

1. Enable flags once: `chrome://flags/#glic` + `#glic-actor` → Enabled → Relaunch.
2. `Cmd+Q` Chrome completely.
3. Edit `~/Library/Application Support/Google/Chrome/Local State` (back up first):
   - `variations_country` → `"us"`
   - `variations_permanent_consistency_country` → `[<chrome_ver>, "us"]`
   - `variations_safe_seed_permanent_consistency_country` → `"us"`
   - `variations_safe_seed_session_consistency_country` → `"us"`
   - In `profile.info_cache.*`: set `is_glic_eligible` → `true` for every profile.
4. Relaunch with override flag: `open -a "Google Chrome" --args --variations-override-country=us`
5. If the Gemini panel opens but says "Something went wrong / Gemini isn't available" — **turn OFF any VPN** (Google rejects datacenter IPs for the Gemini service), Cmd+Q, reopen, Try again.
6. If still erroring → server-side account-region gate (account not yet flipped in TH rollout). Switch to another signed-in profile (try the one with Gemini Ultra subscription) — `is_glic_eligible=true` is now set for all profiles so the button appears in all.

**Persistence caveat:** Chrome may overwrite `variations_country` back to `"th"` on the next seed fetch if real IP is Thai. If the button disappears, rerun the patch (PDF at `~/gemini-in-chrome-rootcause.pdf` has the Quick Script — STEP 2–4 in one bash block). Backup at `~/Library/Application Support/Google/Chrome/Local State.backup-glic-<timestamp>`.

**What did NOT work alone:** chrome://flags, VPN (extension or app, even with confirmed US IP 67.213.208.x), Chrome restart, language=English (US), policy clear, signed-in account. UI gate is Variations/Finch country (client-side) — bypass via Local State edit, not via IP/flag alone. Related: [[โปรไฟล์ - สาย Security|user_security_interest]] — pure client-side config edit, low ban risk per references.
