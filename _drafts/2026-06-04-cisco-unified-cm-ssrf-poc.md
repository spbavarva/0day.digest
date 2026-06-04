---
title: "Cisco Unified CM Critical SSRF Flaw Gets Public PoC — Patch Urgently"
date: 2026-06-04 08:44:08 +0000
categories: [Daily Signal]
tags: [ssrf, cve, vulnerability]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/cisco-warns-of-available-poc-for-critical-unified-cm-vulnerability/
---

Cisco has issued a warning that a public proof-of-concept exploit now exists
for a critical server-side request forgery (SSRF) vulnerability in Cisco
Unified Communications Manager (Unified CM). The flaw is exploitable remotely
without authentication, allowing attackers to force the server to reach internal
network resources. Cisco Unified CM is widely deployed enterprise telephony
infrastructure, making this a high-value target. With a public PoC circulating,
exploitation attempts against unpatched systems are likely imminent. Admins
should apply the available Cisco patch immediately and review network
segmentation controls around Unified CM to limit SSRF blast radius.
