---
title: "MuddyWater Uses Microsoft Teams for False Flag Ransomware Attack"
date: 2026-05-06 13:00:00 +0000
categories: [Daily Signal]
tags: [ransomware, phishing, malware, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/muddywater-uses-microsoft-teams-to.html
---

Iranian state-sponsored group MuddyWater (Mango Sandstorm / Seedworm) used Microsoft Teams-based social engineering to gain initial access in an intrusion documented by Rapid7 in early 2026. After establishing persistence and exfiltrating data, the attackers deployed Chaos ransomware as a false flag designed to redirect incident responders while the underlying espionage activity completed.

The false flag tactic is significant: defenders responding to the ransomware event may miss the credential harvesting and data theft that preceded it. Organizations using Microsoft Teams should enforce strict external contact policies, block or alert on unexpected cross-tenant messages, and review Teams channel membership. MuddyWater historically targets telecommunications, defense, and government sectors in the Middle East and Western countries.
