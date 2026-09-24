---
title: "Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions"
date: 2026-09-24 18:10:18 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html
---

Security researcher Rasmus Moorats chained two flaws in OnePlus's own
software to root a OnePlus 15 running the latest OxygenOS, using a
malicious app that requests no special permissions.

OnePlus confirmed the same flaws affect many more of its own devices as
well as OPPO devices, which share code, but has not yet shipped patches
for the broader device set.

Any app a user installs could exploit the chain to gain full root access,
the highest level of control on the device. Users should be cautious
installing apps from outside official stores until a fix ships.
