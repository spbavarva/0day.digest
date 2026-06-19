---
title: "DragonForce-Linked Actors Abuse Microsoft Teams Relays to Hide Backdoor.Turn C2 Traffic"
date: 2026-06-18 13:30:07 +0000
categories: [Daily Signal]
tags: [ransomware, malware, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/dragonforce-hackers-abuse-microsoft.html
---

Threat actors associated with the DragonForce ransomware operation have
been observed using a custom Go-based RAT called Backdoor.Turn to conceal
command-and-control traffic inside Microsoft Teams relay infrastructure.
The technique was identified by Broadcom-owned Symantec and Carbon Black,
which observed the backdoor deployed against a major U.S. services firm.
Hiding C2 inside legitimate collaboration-platform traffic makes detection
harder for defenders relying on conventional network monitoring.
