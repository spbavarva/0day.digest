---
title: "Cisco Warns of Max-Severity ISE Zero-Day (CVSS 10.0) Under Active Exploitation"
date: 2026-09-17 06:39:40 +0000
categories: [Daily Signal]
tags: [zero-day, cve, iam]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html
---

Cisco disclosed CVE-2026-76460 (CVSS 10.0), an unauthenticated
authentication bypass in Identity Services Engine (ISE) caused by
insufficient authentication control on an API endpoint. Cisco confirmed
attackers are actively exploiting the flaw in the wild.

ISE is widely deployed for network access control and identity policy
enforcement, so a full auth bypass is especially dangerous. Cisco has
released patches; apply them immediately given confirmed active
exploitation. No public IOCs were included in the initial disclosure.
