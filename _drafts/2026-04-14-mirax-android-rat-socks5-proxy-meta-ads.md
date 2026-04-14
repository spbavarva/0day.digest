---
title: "Mirax Android RAT Converts Devices into SOCKS5 Proxies via Meta Ad Campaigns"
date: 2026-04-14 10:20:00 +0000
categories: [Daily Signal]
tags: [malware, rce]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/mirax-android-rat-turns-devices-into.html
---

A newly identified Android remote access trojan called Mirax is actively targeting
Spanish-speaking users, distributing via paid advertisements on Facebook, Instagram, Messenger,
and Threads. The campaign has reached over 220,000 Meta accounts.

Once installed, Mirax grants attackers full device control and silently converts infected
devices into SOCKS5 proxies — effectively routing attacker traffic through victim devices to
obscure origin and resist blocklists.

The use of Meta's advertising infrastructure for delivery is notable: it provides targeting
capabilities, reach, and an appearance of legitimacy. Users in affected regions should be
cautious of apps promoted via social media ads, and enterprise MDM policies should restrict
sideloading and enforce app source validation.
