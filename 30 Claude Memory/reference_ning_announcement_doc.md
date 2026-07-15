---
name: ning-announcement-doc
description: "Ning's real-world CS announcement templates for Thunder Solution & EasyCRM. Source of truth for team voice/tone. Google Doc shared 2026-07-02."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 53119bdc-53f9-462d-9243-6ac7c70c15f2
---

**Google Doc "รวมประกาศ"** — real production announcement templates from the CS team.

- **URL:** https://docs.google.com/document/d/1WAjPPVmd2zCmwr-urQe40H3NzAHMWZLsUS6upQ44fJ0/edit
- **Owner:** ninigchoptam@gmail.com (**หนิง / Ning** — CS lead)
- **Shared with user:** 2026-07-02
- **Copied verbatim into Obsidian:** `~/SecondBrain/03 Resources/CS Announcement Framework/30-ประกาศจริง-Thunder-EasyCRM.md`

**What's in it (13,344 chars):**
- Intake flow for slip-not-verified problems (Line Chat BOT + ThunderAPI)
- Real Thunder Solution templates: KTB QR mismatch (with ITMX escalation language), general slowdown, high-traffic window (19:00–20:00), planned maintenance, KBank slip issue (open/update-with-ETA/close × 2 variants), Login slowdown, Cloudflare outage (open + close), generic bank issue (fill-in), LINE OA down (3 variants + close)
- Real EasyCRM templates: 3 maintenance announcements + 2 completion variants
- **EasySlip + BoostSMS sections are empty** in the doc (not covered yet)

**Team routing (from the doc):**
- Coordination group: **Dav X Support** — ping **@หนิง / @โด้ / @พี่แบงค์** together
- **โด้** = CS support overflow helper
- **พี่แบงค์** = technical
- Announce publicly ONLY when many customers report — channels: FB Page + LINE OA broadcast

**Support phone numbers (verified from real announcements):**
- Thunder Solution: **02-114-8806** and **02-114-8423**
- EasyCRM: **02-124-3423**

**Voice signature (recognize by these — use these when drafting new ones):**
- End with "ค่ะ / นะคะ" (feminine CS tone)
- 🙏 emoji after brand name (Thunder signature)
- ⚠️ / ✅ / 📢 / 📌 / ⏰ as header markers
- Explicit "ไม่ใช่ปัญหาที่ระบบเรา" when the fault is upstream (bank / LINE / Cloudflare)
- Workaround suggestion "ตรวจ SMS หรือประวัติธุรกรรมในแอปธนาคาร" during outages
- Close-of-incident: ✅ + normal-use confirmation + support phone
- Stock closing line: "ขออภัยในความไม่สะดวกมา ณ ที่นี้ 🙏"

**Gaps vs the framework SOP:**
- Doc doesn't declare target segments (broadcasts to all, no "4 groups" concept)
- Doc doesn't declare approvers (some appear to be sent by CS directly — reconcile with T1/T2/T3 SOP)
- No log/audit trail in the doc — team should adopt `21-Log-ประกาศ.md`
- Watch for typos in the source: "บแทเช็คสลิป", "Thunder Solutio" — verify before copying

**How to apply:** when drafting a new announcement for Thunder or EasyCRM, START from a matching template in this file, NOT from the abstract templates in `10-13`. The abstract templates give structure; Ning's real ones give the voice. When the user says "ร่างประกาศ" for these brands, cross-reference this file first.

Related: [[CS Announcement Framework (-announce)|cs-announcement-framework]] (the sibling framework — abstract SOP + generic templates).
