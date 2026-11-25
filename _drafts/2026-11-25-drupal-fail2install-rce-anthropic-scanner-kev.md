---
title: "Critical Drupal RCE Flaw Found by Anthropic Scanner Added to CISA KEV Amid Active Exploitation"
date: 2026-11-25 08:01:06 +0000
categories: [Daily Signal]
tags: [rce, cve, vulnerability, anthropic]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/drupal-flaw-found-by-anthropic-scanner-exploited-in-attacks/
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/drupal-fail2install-exploit-details.html
---

A critical remote code execution flaw in Drupal core, tracked as
CVE-2026-132165 and nicknamed "Fail2Install" (CVSS 9.8), was originally
surfaced by a scanner built by Anthropic. The flaw is now under active
exploitation.

CISA added the vulnerability to its Known Exploited Vulnerabilities catalog
and gave federal agencies until November 27, 2026 to patch. Any organization
running unpatched Drupal core should treat this as an emergency given the
combination of a maximum-impact CVSS score and confirmed in-the-wild attacks.
