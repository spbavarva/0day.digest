---
title: "Critical Vulnerabilities Patched With Chrome 151 Update"
date: 2026-08-07 06:56:56 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec, google]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/critical-vulnerabilities-patched-with-chrome-151-update/
---

Google shipped Chrome 151, fixing more than two dozen memory-safety bugs,
including several critical use-after-free vulnerabilities. Use-after-free
flaws in a widely deployed browser are a common target for exploit chains once
the fix is patch-diffed against the prior release. SecurityWeek's report gave
no indication any of the flaws were under active exploitation at time of
disclosure. Practitioners should confirm automatic updates are enabled and
that managed Chrome fleets have picked up the release.
