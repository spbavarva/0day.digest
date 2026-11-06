---
title: "Hackers Hide Linux Backdoor in Control Web Panel Server to Execute Commands Without Logs"
date: 2026-11-06 05:58:54 +0000
categories: [Daily Signal]
tags: [malware, vulnerability]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html
---

Researchers at QiAnXin's XLab found a backdoor hidden inside the web
server that runs Control Web Panel (CWP), a free Linux hosting management
panel. The backdoored server executes attacker-sent commands without
those requests ever appearing in its access logs.

Installing the backdoor requires root access, meaning attackers must
already control the server — this is a post-compromise persistence and
anti-forensics tool rather than an initial-access vulnerability.
Administrators of CWP-managed servers should audit for unexpected root
access and unexplained outbound activity.
