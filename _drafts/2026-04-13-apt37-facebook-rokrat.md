---
title: "North Korea's APT37 Weaponizes Facebook Friendships to Deliver RokRAT"
date: 2026-04-13 09:15:00 +0000
categories: [Daily Signal]
tags: [malware, phishing, apt]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/north-koreas-apt37-uses-facebook-social.html
---

APT37 (ScarCruft), a North Korean state-sponsored threat group, ran a multi-stage
Facebook social engineering campaign: operators sent friend requests to targets, built
rapport over time, then leveraged the established trust as a delivery channel for
RokRAT — a full-featured Windows RAT used for espionage.

RokRAT exfiltrates documents, captures screenshots, and supports cloud-based C2 via
legitimate services. Routing initial contact through mainstream social platforms reduces
the effectiveness of traditional network-layer controls. Targets in policy, defense,
journalism, and research — APT37's typical focus areas — should treat unsolicited
social media connection requests as a potential threat vector.
