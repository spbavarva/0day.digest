---
title: "Critical TeamCity Flaw Lets Attackers Run OS Commands Without Logging In"
date: 2026-07-28 08:11:22 +0000
categories: [Daily Signal]
tags: [rce, devsecops, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html
---

JetBrains disclosed CVE-2026-63077 (CVSS 9.8), a critical vulnerability
affecting all on-premises versions of TeamCity that allows unauthenticated
attackers to run arbitrary OS commands. The issue is fixed in versions
2025.11.7 and 2026.1.3; TeamCity Cloud instances are unaffected.
Organizations running on-prem TeamCity — a CI/CD server used to build and
deploy software — should patch immediately given the exposure of build
infrastructure.
