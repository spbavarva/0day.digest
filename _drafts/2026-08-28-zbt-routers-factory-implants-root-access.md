---
title: "China-Made ZBT Routers Ship With Factory-Installed Root Access Implants"
date: 2026-08-28 10:58:29 +0000
categories: [Daily Signal]
tags: [supply-chain, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/china-made-zbt-routers-ship-with-two.html
---

VulnCheck has disclosed two previously undocumented factory-installed
implants, named SPEAKINGSTONE and DARKLANTERN, in firmware for routers
built by Shenzhen Zhibotong Electronics (ZBT). Tracked as CVE-2026-74232
and CVE-2026-74233, each implant gives an unauthenticated remote attacker
the ability to run commands as root on affected devices.

Because the implants ship in the factory firmware, every device using the
affected firmware is compromised out of the box. Organizations using
ZBT-based routers, including white-labeled variants, should identify
affected devices and replace or reflash them rather than wait for a
patch.
