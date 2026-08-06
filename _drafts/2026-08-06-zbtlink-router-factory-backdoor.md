---
title: "Chinese-Made Zbtlink Routers Ship With Factory Backdoor for Unauthenticated Root Access"
date: 2026-08-06 08:05:22 +0000
categories: [Daily Signal]
tags: [supply-chain, vulnerability, privilege-escalation]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/chinese-made-zbtlink-routers-ship-with.html
---

VulnCheck disclosed a factory-shipped backdoor present in at least 20
Zbtlink router models, spanning all 21 firmware images currently available
and more than two years of releases.

The backdoor starts automatically on boot and attempts to beacon out to
infrastructure in China, and it can be used to open an unauthenticated root
shell on affected devices. Because the implant ships in the firmware itself
rather than being added post-deployment, every unit running the affected
firmware is exposed by default.

Organizations using Zbtlink hardware should treat these devices as
compromised, isolate them from sensitive networks, and evaluate
replacement.
