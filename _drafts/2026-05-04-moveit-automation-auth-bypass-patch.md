---
title: "Progress Patches Critical Authentication Bypass in MOVEit Automation"
date: 2026-05-04 12:18:57 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/progress-patches-critical-moveit.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/moveit-automation-customers-warned-to-patch-critical-auth-bypass-flaw/
---

Progress Software has released patches for two vulnerabilities in MOVEit Automation (formerly MOVEit Central), including a critical authentication bypass. MOVEit Automation is an enterprise managed file transfer solution used to schedule and automate file workflows without custom scripting.

Given MOVEit's track record — the 2023 CL0P campaign exploited a related SQLi flaw to breach hundreds of organizations and expose data belonging to tens of millions of individuals — authentication bypass vulnerabilities in this product warrant urgent remediation regardless of whether active exploitation has been confirmed.

Organizations running MOVEit Automation should apply available patches immediately, review transfer logs for anomalous activity, and check for unauthorized user accounts. Ransomware operators are well-acquainted with MOVEit's attack surface.
