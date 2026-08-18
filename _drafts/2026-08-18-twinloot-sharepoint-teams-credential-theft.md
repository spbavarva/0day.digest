---
title: "TWINLOOT Abuses SharePoint and Teams to Steal Credentials and Move Across Networks"
date: 2026-08-18 12:38:20 +0000
categories: [Daily Signal]
tags: [malware, cloud-security, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/twinloot-abuses-sharepoint-and-teams-to.html
---

Security researchers at Ontinue disclosed TWINLOOT, a modular,
PyArmor-hardened Python implant framework that runs its entire
command-and-control infrastructure inside trusted Microsoft services.
Tasking flows through SharePoint Online files and Microsoft Teams, letting
the malware blend into normal enterprise traffic.

The framework steals credentials and moves laterally across victim networks
using living-off-the-land techniques. Because C2 traffic rides on SharePoint
and Teams rather than attacker-owned infrastructure, defenders should watch
for anomalous file and API activity within those services rather than rely
on network-layer indicators alone.
