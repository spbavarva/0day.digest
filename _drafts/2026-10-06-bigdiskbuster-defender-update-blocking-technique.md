---
title: "'BigDiskBuster' Technique Leaves Microsoft Defender Running While Blocking Its Updates"
date: 2026-10-06 16:59:24 +0000
categories: [Daily Signal]
tags: [malware, microsoft, appsec]
severity: medium
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/application-security/bigdiskbuster-microsoft-defender-running-blocking-updates
---

A newly disclosed proof-of-concept technique dubbed "BigDiskBuster" can block
Microsoft Defender from receiving updates while leaving the service itself
running, creating a silent gap in virus detection. Unlike typical EDR-killer
techniques, this approach doesn't require an exploit — Defender appears
active and healthy to the user and to basic health checks, while its
detection capability is effectively stale. The technique is a proof of
concept; no evidence of in-the-wild use was reported.
