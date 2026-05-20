---
title: "Webworm Deploys EchoCreep and GraphWorm Backdoors via Discord and MS Graph C2"
date: 2026-05-20 12:51:43 +0000
categories: [Daily Signal]
tags: [malware, microsoft, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html
---

China-aligned threat actor Webworm, active since at least 2022, has deployed two new custom backdoors—EchoCreep and GraphWorm—that route command-and-control traffic through Discord and the Microsoft Graph API. Using legitimate cloud services for C2 allows the malware to blend into normal enterprise traffic and evade signature-based detection.

Webworm has historically targeted government agencies. Organizations should review EDR telemetry and proxy logs for unusual outbound connections from unexpected processes to Discord or Graph API endpoints. Restricting Graph API access to authorized applications via Conditional Access policies can reduce the attack surface.
