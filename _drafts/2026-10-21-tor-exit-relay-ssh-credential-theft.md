---
title: "Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections"
date: 2026-10-21 10:30:27 +0000
categories: [Daily Signal]
tags: [malware, data-breach]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html
---

A researcher found that attackers hijacked more than 300 Tor exit relays in
early October and used them to intercept and redirect SSH connections,
stealing login passwords from users who authenticated to SSH servers over Tor
with a password between October 1 and 5.

Exit relays are the last hop before traffic leaves the Tor network, giving a
malicious relay operator visibility into connections routed through it.
Anyone who used password-based SSH login over Tor in that window should
rotate credentials.
