---
title: "Attackers Exploit AhsayCBS Flaws to Deploy Sandbox-Evading Python Backdoor"
date: 2026-11-10 16:00:55 +0000
categories: [Daily Signal]
tags: [rce, cve, malware, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/attackers-exploit-ahsaycbs-flaws-to.html
---

Researchers at Huntress disclosed an attack chain that exploited two
now-patched vulnerabilities in AhsayCBS, tracked as CVE-2026-105133 and
CVE-2026-105134, to bypass authentication and execute arbitrary commands.
The exploitation, observed in early October 2026, was used to deliver a
Python-based backdoor designed to evade sandbox analysis. Patches for
both vulnerabilities are available. Organizations running AhsayCBS should
confirm patches are applied and check for signs of the backdoor if they
haven't already updated.
