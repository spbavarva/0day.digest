---
title: "Unpatched Shark Vacuum Flaw Allows Region-Wide Takeover of Other Devices"
date: 2026-07-16 09:23:19 +0000
categories: [Daily Signal]
tags: [vulnerability, iot]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/unpatched-shark-vacuum-flaw-could-let.html
---

A researcher publishing as tokay0 found that extracting the certificate
from a Shark RV2320EDUS robot vacuum's flash storage allows running root
commands against other Shark vacuums in the same AWS region — including
viewing the onboard camera, driving the robot, reading a map of the
victim's home, and retrieving the Wi-Fi password in plaintext. The method
was published without vendor coordination and has reportedly only been
tested against the researcher's own devices, but the underlying flaw
appears unpatched. Owners of affected Shark vacuums should treat the
devices' camera and network access as untrusted until a fix is issued.
