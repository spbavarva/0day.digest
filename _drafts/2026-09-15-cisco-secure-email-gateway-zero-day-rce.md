---
title: "Cisco Secure Email Gateway Zero-Day Exploited in the Wild, Enables Root Command Execution"
date: 2026-09-15 06:11:11 +0000
categories: [Daily Signal]
tags: [zero-day, rce, cve]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html
---

Cisco has warned that a critical zero-day vulnerability in AsyncOS
Software for Cisco Secure Email Gateway, tracked as CVE-2026-76461 with a
CVSS score of 9.8, is under active exploitation in the wild.

The flaw stems from insufficient validation in the email parsing logic
and could allow an unauthenticated, remote attacker to execute commands
as root. Organizations running Secure Email Gateway should apply Cisco's
patch immediately and check for indicators of compromise.
