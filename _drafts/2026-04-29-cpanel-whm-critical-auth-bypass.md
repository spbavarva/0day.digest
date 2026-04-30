---
title: "cPanel and WHM Emergency Patch Fixes Critical Authentication Bypass"
date: 2026-04-29 15:51:44 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation, appsec, cve]
severity: critical
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/cpanel-whm-emergency-update-fixes-critical-auth-bypass-bug/
---

cPanel and WebHost Manager (WHM) received an emergency security update addressing a critical authentication bypass affecting all currently supported versions. The vulnerability allows unauthenticated attackers to gain access to the control panel without valid credentials, potentially compromising every hosted account on a vulnerable server.

Fixed versions are 11.110.0.97, 11.118.0.63, 11.126.0.54, and 11.132.0.29. Hosting providers and managed service providers should apply the emergency update immediately — cPanel manages millions of web hosting accounts globally, making auth bypass vulnerabilities here extremely high-value targets. No active exploitation was mentioned at time of disclosure, but that window will be short.
