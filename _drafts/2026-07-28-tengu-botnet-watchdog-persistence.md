---
title: "Tengu Botnet Reboots Compromised Linux Devices When Defenders Kill Its Process"
date: 2026-07-28 15:01:33 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/tengu-botnet-reboots-compromised-linux.html
---

Nozomi Networks Labs disclosed Tengu, a new Mirai-derived Linux botnet that
abuses a compromised device's hardware watchdog to force a reboot when
defenders kill its main process. The reboot gives Tengu's other persistence
mechanisms another chance to relaunch it, undermining simple process-kill
remediation. The dropper was observed reaching honeypots via Telnet
credential brute force, and the botnet supports at least 25 distributed
denial-of-service methods.
