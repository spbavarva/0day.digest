---
title: "Eight Malicious npm Packages Downloaded 40,767 Times Deliver Overlord RAT and Stealer"
date: 2026-10-07 17:43:20 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html
---

Researchers at CloudSEK and Checkmarx disclosed a long-running npm supply
chain campaign, codenamed MALFEX, that pushes information-stealing and
remote access trojan malware to compromised hosts.

A single threat actor appears to have published 12 malicious packages since
August 2023, eight of which were downloaded a combined 40,767 times before
being identified.

Teams should audit recent npm installs against known-malicious package names
from this campaign and treat any host that pulled them as potentially
compromised by the Overlord RAT or an associated stealer.
</content>
