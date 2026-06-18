---
title: "F5 Patches Two Critical NGINX Open Source RCE Flaws"
date: 2026-06-18 17:32:14 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, appsec]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html
---

F5 released security updates addressing two critical vulnerabilities in
NGINX Open Source that could be exploited to achieve remote code
execution. The most severe, CVE-2026-42530 (CVSS v4 score 9.2), is a
use-after-free in the ngx_http_v3_module that can be triggered by a
remote, unauthenticated attacker. Given the unauthenticated remote attack
vector, organizations running NGINX Open Source should prioritize
patching immediately.
