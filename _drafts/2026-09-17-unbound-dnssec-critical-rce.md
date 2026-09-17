---
title: "Critical Unbound DNSSEC Validator Flaw Enables RCE via Malicious DNS Zone"
date: 2026-09-17 12:30:00 +0000
categories: [Daily Signal]
tags: [rce, cve, vulnerability]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html
---

Every release of the Unbound DNS resolver before 1.26.1 has a critical
heap overflow in its DNSSEC validator, according to an NLnet Labs
advisory. An attacker who controls a malicious DNS zone can trigger the
overflow by getting a vulnerable resolver to query it, leading to remote
code execution. The bug is tracked as CVE-2026-81642.

NLnet Labs shipped the fix, version 1.26.1, the same day the advisory was
published. No active exploitation has been reported, but resolver
operators should patch promptly given the RCE impact.
