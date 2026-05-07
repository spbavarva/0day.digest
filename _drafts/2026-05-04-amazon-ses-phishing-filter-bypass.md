---
title: "Amazon SES Increasingly Abused in Phishing Campaigns to Bypass Email Security"
date: 2026-05-04 20:03:28 +0000
categories: [Daily Signal]
tags: [phishing, aws, cloud-security]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/amazon-ses-increasingly-abused-in-phishing-to-evade-detection/
---

Threat actors are routing phishing campaigns through Amazon SES to inherit the service's strong sender reputation and render standard reputation-based email security filters ineffective. Because SES is a legitimate, high-volume AWS service, blocklists targeting its IP ranges are not a practical defense.

Email security teams should supplement reputation-based controls with URL inspection, content analysis, and link-rewriting for all inbound mail. The trend of abusing trusted cloud sending services reflects a broader attacker shift toward infrastructure that organizations hesitate to block outright.
