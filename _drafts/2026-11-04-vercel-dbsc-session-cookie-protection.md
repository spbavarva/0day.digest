---
title: "Vercel Rolls Out Device Bound Session Credentials to Block Session Theft"
date: 2026-11-04 21:31:18 +0000
categories: [Daily Signal]
tags: [cloud-security, appsec]
severity: informational
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/vercel-rolls-out-new-protection-against-stolen-session-cookie-attacks/
---

Vercel has begun gradually rolling out Device Bound Session Credentials
(DBSC) across its platform. DBSC cryptographically binds session cookies to
the device that created them, so a stolen cookie can't be replayed from an
attacker's machine.

The feature is aimed squarely at info-stealer malware, which commonly
exfiltrates session cookies to hijack logged-in accounts without needing
credentials. Rollout is gradual rather than platform-wide at launch.
