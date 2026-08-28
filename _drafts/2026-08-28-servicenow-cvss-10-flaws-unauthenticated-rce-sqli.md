---
title: "ServiceNow Patches Three CVSS 10.0 Flaws Allowing Unauthenticated Code Execution and SQL Injection"
date: 2026-08-28 11:20:32 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, rce, sqli]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/servicenow-warns-of-three-max-severity-security-vulnerabilities/
---

ServiceNow released patches for four security flaws in its AI Platform,
three of them rated a maximum CVSS score of 10.0 and exploitable, in certain
circumstances, by an unauthenticated attacker. The flaws can be used for
code injection, SQL injection, and privilege escalation. ServiceNow has
already applied the fix to its hosted instances and provided the update to
partners, but organizations running self-hosted ServiceNow instances need
to apply the patch themselves. Self-hosted ServiceNow AI Platform customers
should patch immediately given the unauthenticated attack path.
