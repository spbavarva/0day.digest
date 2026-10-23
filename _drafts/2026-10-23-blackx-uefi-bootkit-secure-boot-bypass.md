---
title: "BlackX UEFI Bootkit Bypasses Secure Boot via Missing Revocations"
date: 2026-10-23 18:50:13 +0000
categories: [Daily Signal]
tags: [malware, privilege-escalation, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/blackx-uefi-bootkit-bypasses-secure.html
---

Kaspersky reported a new UEFI bootkit, BlackX, used against diplomatic
organizations in Tajikistan, Uzbekistan, and Turkmenistan in early
2026. The campaign is suspected to be the work of China-linked APT41.

BlackX bypasses Secure Boot on patched Windows systems that haven't
applied certificate revocations, letting it load before the OS and
persist beneath standard security tooling. Organizations should verify
UEFI revocation lists (DBX) are current, not just that Secure Boot is
enabled.
