---
name: feedback_topup_analysis
description: "How to analyze top-up/wallet transaction data — don't over-index on manual/admin credit; define churn from real cadence not a guess"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 21184b42-831d-4358-b3b8-24a89577ab5e
---

Guidance from the COO when building dashboards from top-up/wallet transaction logs (e.g. `topup 6 เดือน.csv`, 3-page dashboard set on Desktop: topup_dashboard / crm_dashboard / monthly_dashboard).

**1. Don't over-emphasize manual (admin) vs auto top-ups.** The "เพิ่มโดยแอดมิน" type is still real money (customer paid offline / by transfer, staff credits the wallet). Treat total top-up as THE revenue number. Do NOT front-load a "40% is admin-credit / may not be real cash / ตรวจที่มา" caveat or split organic-vs-gross everywhere — the user said it's "ไม่ค่อยสำคัญ" and it made the whole dashboard read wrong. Keep concentration/whale risk (that IS valid), just drop the admin framing.

**Why:** I initially treated 40% admin-credit + a whale that was 100% admin as a red flag; the COO corrected that it's normal. **How to apply:** report total as revenue; at most a one-line neutral note that admin+auto are combined.

**2. Define "ลูกค้าหายไป (churned)" from real behavior, not a guessed number.** Method that worked: compute the distribution of gaps between consecutive top-ups, then set the churn line past the normal band. For this data: median gap 11d, 96% of repeat top-ups within 45d, 98% within 60d → **churn = silent >60 days** (not the 90 I first guessed, which was too loose). At-risk = 45–60d. Always split churn into **never-activated** (1 top-up, onboarding problem) vs **lapsed repeater** (≥2 then stopped — the painful, high-value one). Cohort churn is only reliable for cohorts with ≥90 days of observation (with 6 months of data, only the first ~3 months' cohorts). See `churn_analyze.py` / `crm_analyze.py` on Desktop.

This top-up data = **EasySlip API** credit top-ups (not lotto). Related: [[EasySlip API Customer Dashboard|project_easyslip_api_dashboard]], [[No emoji in HTML outputs|feedback_no_emoji]], [[กติกา - Deploy ใช้ stable URL|feedback_deploy_link]].
