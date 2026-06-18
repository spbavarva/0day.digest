---
title: "Atlassian, Splunk Patch Critical Vulnerabilities"
date: 2026-06-18 10:59:50 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, llm, appsec]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/atlassian-splunk-patch-critical-vulnerabilities/
---

Splunk patched an OS command injection vulnerability in its AI Toolkit
add-on, which could let an attacker run arbitrary commands on the host.
Atlassian separately fixed dozens of flaws across its products, most of
which trace back to vulnerable third-party dependencies rather than
first-party code. Both vendors have shipped patches and no active
exploitation has been reported. Teams running Splunk's AI Toolkit or
Atlassian products should update to the latest fixed versions.
