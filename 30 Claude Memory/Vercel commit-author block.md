---
name: feedback_vercel_commit_author
description: "Vercel blocks deploys when git commit author email isn't tied to the account (COMMIT_AUTHOR_REQUIRED)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d02346a8-e0db-4158-82d0-70171f7ae46a
---

Vercel deploys show status **BLOCKED** (`readyStateReason: "no git user associated with the commit"`, `blockCode: COMMIT_AUTHOR_REQUIRED`) when the commit **author email** isn't associated with the Vercel account.

**Why:** fresh `git init` on this Mac authors commits as `aexgee@Bob-MacBookPro-M5Pro.local` (machine default) — not a real account email. Vercel's seat-security blocks those.

**How to apply:** before first commit on any repo that will deploy to Vercel, set author to the user's verified email:
`git config user.email "bobbysomporn@gmail.com"` (name `bbm8sus4` = their GitHub). Global config was set 2026-07-14 so new repos inherit it. To fix an already-committed HEAD: `git commit --amend --reset-author --no-edit && git push -f`.

**Also learned:** these Vercel projects auto-deploy on `git push` (GitHub integration active). So **push alone deploys** — do NOT also run `vercel deploy --prod` or you get duplicate deployments (bit me twice on [[TrainerFlow (PT client mgmt)|project_trainerflow]] and [[m-trainer-management|project_m_trainer_management]]). BLOCKED deploys never clear on their own; re-author + push is the fix.

Note: [[TrainerFlow (PT client mgmt)|project_trainerflow]] repo still has the old machine-email author on HEAD — its next push will block until re-authored the same way.
