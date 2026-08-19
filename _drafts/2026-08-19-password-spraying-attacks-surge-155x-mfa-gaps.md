---
title: "Password Spraying Attacks Surge 155x as Attackers Exploit MFA Gaps"
date: 2026-08-19 14:00:10 +0000
categories: [Daily Signal]
tags: [iam, mfa-bypass]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/password-spraying-attacks-surge-155x-as-hackers-exploit-mfa-gaps/
---

Huntress observed a 155x increase in password spraying attacks during the
first half of 2026, including a single campaign that generated more than
81 million login attempts in two weeks. The attacks exploited legacy
authentication protocols and gaps in MFA policy coverage that left some
login flows unprotected. Organizations should audit for legacy auth
endpoints still accepting single-factor logins and close MFA enforcement
gaps across all sign-in paths, not just primary ones.
