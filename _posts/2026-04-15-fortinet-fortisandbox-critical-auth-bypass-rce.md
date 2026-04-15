---
title: "Fortinet Patches Critical FortiSandbox Vulnerabilities Enabling Auth Bypass and RCE"
date: 2026-04-15 09:37:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce]
severity: critical
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/fortinet-patches-critical-fortisandbox-vulnerabilities/
---

Fortinet has released patches for critical vulnerabilities in FortiSandbox that allow remote
attackers to bypass authentication or execute arbitrary code and commands via HTTP requests.
No CVE identifiers were published in the feed summary, and Fortinet has not yet confirmed
active exploitation.

FortiSandbox is a network sandboxing appliance widely deployed as a last-line malware analysis
layer in enterprise and government environments. An auth bypass in this component is especially
high-risk because compromising it could let attackers whitelist malicious samples.

Administrators running FortiSandbox should apply the patches immediately and review appliance
access logs for unusual HTTP activity. Check Fortinet's PSIRT advisory for affected version
ranges and the specific CVEs.
