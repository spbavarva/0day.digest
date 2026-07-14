---
title: "Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity"
date: 2026-07-14 06:19:24 +0000
categories: [Daily Signal]
tags: [iam, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html
---

Microsoft mapped three distinct attack paths used against Salesforce
environments over the past year by activity consistent with the extortion
group ShinyHunters. None of the paths exploited a platform vulnerability —
attackers instead abused the trust already extended through OAuth
connections linking Salesforce to third-party apps and vendors. That
trusted access let attackers reach environments without triggering typical
intrusion signals. Organizations should audit connected OAuth apps and
third-party Salesforce integrations for unnecessary scope or unrecognized
grants.
