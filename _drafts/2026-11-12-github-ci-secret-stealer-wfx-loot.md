---
title: "Hijacked GitHub Accounts Plant CI Secret Stealer in 1,800+ Repositories"
date: 2026-11-12 06:42:47 +0000
categories: [Daily Signal]
tags: [supply-chain, github, data-breach]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html
  - name: SecurityWeek
    url: https://www.securityweek.com/attacker-targets-60000-github-repositories-in-credential-theft-campaign/
---

Starting Tuesday, an attacker used stolen credentials for 4,837 GitHub
accounts to plant a CI secret stealer, dubbed wfx-loot by researchers at
Aikido Security, in any repository those accounts could write to.

The stealer ran in at least 1,806 repositories, harvesting secrets and
cloud credentials reachable from each repo's CI workflows. SecurityWeek
reports the campaign targeted roughly 60,000 repositories in total.
Organizations should rotate CI/CD secrets and cloud credentials for any
repos tied to compromised contributor accounts and audit workflow runs
from this week.
