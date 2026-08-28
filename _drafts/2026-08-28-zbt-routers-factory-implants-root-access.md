---
title: "China-Made ZBT Routers Ship With Factory Implants Giving Unauthenticated Root Access"
date: 2026-08-28 10:58:29 +0000
categories: [Daily Signal]
tags: [supply-chain, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/china-made-zbt-routers-ship-with-two.html
---

VulnCheck disclosed two previously undocumented factory-installed implants,
named SPEAKINGSTONE and DARKLANTERN, in firmware for routers made by
Shenzhen Zhibotong Electronics (ZBT). Both implants, tracked as
CVE-2026-74232 and CVE-2026-74233, give an unauthenticated remote attacker
the ability to run commands as root on affected devices. Because the
implants ship from the factory rather than being added post-deployment,
this is a hardware supply chain compromise rather than a conventional
software vulnerability. Organizations using ZBT-built routers should
identify affected devices and take them off internet-facing networks until
a fix is available.
