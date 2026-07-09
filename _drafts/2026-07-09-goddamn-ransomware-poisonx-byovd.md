---
title: "GodDamn Ransomware Uses PoisonX Driver to Disable Endpoint Defenses"
date: 2026-07-09 10:43:09 +0000
categories: [Daily Signal]
tags: [ransomware, malware, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html
---

A new ransomware family called GodDamn has been identified using the
PoisonX kernel driver to disable endpoint security software before
encrypting files — a bring-your-own-vulnerable-driver (BYOVD) technique.
Symantec's Threat Hunter Team assesses GodDamn to be a rebrand of the
previously known Beast ransomware, first spotted in the wild on May 21,
2026. The signed kernel driver lets the ransomware operate with elevated
privileges that bypass many EDR/AV protections.
