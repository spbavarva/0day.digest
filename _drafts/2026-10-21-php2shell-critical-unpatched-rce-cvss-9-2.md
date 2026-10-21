---
title: "PHP2Shell: Critical Unpatched PHP RCE Flaws (CVSS 9.2) Trigger Emergency Patch"
date: 2026-10-21 10:36:53 +0000
categories: [Daily Signal]
tags: [rce, cve, vulnerability, zero-day]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/php2shell-what-actually-protects-you.html
  - name: SecurityWeek
    url: https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/
---

PHP's security team shipped an out-of-cycle release at 14:00 UTC on
October 21 for two critical flaws — tracked as CVE-2026-109618 and
CVE-2026-109619 — rated 9.2 on the CVSS v4.0 scale. Dubbed PHP2Shell, the
bugs could lead to unauthenticated remote code execution.

Details leaked ahead of the official advisory, and a security firm that
initially suggested a stopgap mitigation later said the workaround alone
is not enough to fully block exploitation. PHP did not publish its own
interim mitigation before the patch landed. Organizations running PHP
should prioritize applying the emergency release as soon as possible.
