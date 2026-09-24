---
title: "SolarWinds Patches Critical Unauthenticated RCE Flaws in Observability Self-Hosted"
date: 2026-09-24 10:40:40 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/solarwinds-patches-critical-rce-flaws-in-observability-self-hosted/
---

SolarWinds patched two critical remote code execution vulnerabilities,
tracked as CVE-2026-28324 and CVE-2026-28325, in its self-hosted
Observability product.

Both flaws can be exploited without authentication, meaning a remote
attacker doesn't need valid credentials to attempt exploitation.

Administrators running SolarWinds Observability Self-Hosted should apply
the patches immediately.
