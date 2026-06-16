---
title: "DragonForce Ransomware Hides C2 Traffic Inside Microsoft Teams Infrastructure"
date: 2026-06-16 10:18:48 +0000
categories: [Daily Signal]
tags: [ransomware, malware, microsoft]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/ransomware-gang-abuses-microsoft-teams-relays-to-hide-malicious-traffic/
---

The DragonForce ransomware group deployed custom malware named 'Backdoor.Turn' that tunnels command-and-control traffic through Microsoft Teams relay infrastructure. By blending malicious traffic into legitimate Teams relay connections, attackers can bypass network defenses that allowlist Microsoft services. Organizations cannot simply block Teams relay traffic without disrupting business communications. The technique follows a growing trend of threat actors abusing trusted enterprise platforms — including OneDrive and Slack — for C2 to evade detection. Security teams should monitor for anomalous Teams relay behavior and deploy endpoint detections for Backdoor.Turn indicators rather than relying solely on network-level filtering.
