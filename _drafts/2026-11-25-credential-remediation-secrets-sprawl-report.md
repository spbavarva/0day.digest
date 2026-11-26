---
title: "Credential Remediation Is Slow When You Don't Know What Will Break"
date: 2026-11-25 11:51:48 +0000
categories: [Daily Signal]
tags: [appsec, devsecops]
severity: informational
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/credential-remediation-is-slow-when-you.html
---

GitGuardian's State of Secrets Sprawl 2026 report highlights how slow teams
are to revoke exposed credentials.

More than 64% of valid secrets discovered in 2022 were still working as of
January 2026, largely because teams are unsure what will break if they
revoke them.

The report also found that validity-only triage misses 46% of critical
secrets, arguing teams should prioritize by what a credential can access
and whether it leaked publicly, not just whether it still validates.
