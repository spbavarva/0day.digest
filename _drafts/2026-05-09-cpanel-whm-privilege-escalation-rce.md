---
title: "cPanel and WHM Patch Privilege Escalation, Code Execution, and DoS Vulnerabilities"
date: 2026-05-09 07:16:00 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, privilege-escalation, rce]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html
---

cPanel has released patches for three vulnerabilities in cPanel and Web Host Manager (WHM) covering privilege escalation, arbitrary code execution, and denial-of-service. CVE-2026-29201 (CVSS 4.3) involves insufficient input validation in the `feature::LOADFEATUREFILE` adminbin call; the remaining two CVEs carry higher severity with code execution and privilege escalation impact.

cPanel and WHM power a significant share of shared web hosting infrastructure globally. Hosting providers and managed service providers running these products should apply the updates immediately. No active exploitation has been reported yet, but privilege escalation + RCE primitives in widely deployed hosting panels attract rapid post-patch weaponization.
