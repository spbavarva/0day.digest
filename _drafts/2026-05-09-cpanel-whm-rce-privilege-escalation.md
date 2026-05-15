---
title: "cPanel and WHM Patch Three Vulnerabilities Including RCE and Privilege Escalation"
date: 2026-05-09 07:16:00 +0000
categories: [Daily Signal]
tags: [cve, rce, privilege-escalation, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html
---

cPanel has released security updates addressing three vulnerabilities in cPanel and Web Host Manager (WHM). The flaws could be exploited individually or in combination to achieve privilege escalation, remote code execution, and denial-of-service on affected hosting systems.

CVE-2026-29201 (CVSS 4.3) involves insufficient input validation of the feature file name in the `feature::LOADFEATUREFILE` adminbin call. Details on the remaining two CVEs were not fully disclosed in the available summary. Admins running cPanel/WHM should apply the latest updates immediately — hosting control panels are routinely targeted in opportunistic attacks and are high-value footholds for lateral movement into hosted customer environments.
