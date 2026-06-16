---
title: "China-Linked SprySOCKS Backdoor Gets Windows Variants, Targets Government Orgs"
date: 2026-06-16 09:44:34 +0000
categories: [Daily Signal]
tags: [malware, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/china-linked-sprysocks-backdoor-expands.html
---

ESET researchers discovered two previously undocumented Windows variants of SprySOCKS — a backdoor previously believed to be Linux-only — internally named WIN_DRV and WIN_PLUS. Both variants use driver-based stealth techniques and support communication over TCP and UDP with hardcoded C2 configurations. The China-nexus malware has been used to attack government organizations in at least four countries, according to BleepingComputer. The Windows expansion significantly broadens SprySOCKS' targeting surface beyond the Linux server environments where it was previously observed. Security teams should review ESET's indicators of compromise and scan for driver-level rootkit artifacts on Windows endpoints in government and defense environments.
