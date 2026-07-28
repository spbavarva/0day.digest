---
title: "24,650 Internet-Exposed BMCs Disclose IPMI Password Hashes Before Login"
date: 2026-07-28 14:41:36 +0000
categories: [Daily Signal]
tags: [vulnerability, iam]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/24650-internet-exposed-bmcs-disclose.html
---

Researchers found more than 36,800 internet-exposed Baseboard Management
Controller (BMC) interfaces running IPMI, of which 24,650 disclose
password-derived authentication hashes before any login attempt. An
attacker who captures these hashes can attempt offline cracking to gain
administrative access to the underlying server hardware. Organizations
should audit BMC/IPMI interfaces for internet exposure and firewall the
management network where possible.
