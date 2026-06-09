---
title: "FROST: New SSD Timing Side-Channel Lets Websites Track Browser History and Open Apps"
date: 2026-06-09 09:50:41 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec, xss]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/new-frost-attack-lets-websites-track.html
---

Researchers at Graz University of Technology developed FROST, a JavaScript-only side-channel attack that infers which websites a user has visited and which applications are open by monitoring SSD I/O contention timing from inside a browser tab.
The attack requires no native code, no browser extension, and no user permission; a page left open in a background tab can passively profile user activity.
FROST works by observing how drive access latency changes when the OS accesses files associated with specific apps or cached resources from specific sites.
This is a passive, hard-to-detect technique; browser vendors will need to address SSD timing resolution similar to how speculative execution side-channels were mitigated in hardware.
