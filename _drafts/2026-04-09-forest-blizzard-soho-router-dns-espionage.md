---
title: "Russia's APT28 Conducts Malwareless Espionage via SOHO Router DNS Hijack"
date: 2026-04-09 01:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, malware, cloud-security, apt]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/threat-intelligence/russia-forest-blizzard-logins-soho-routers
---

Russia's APT28 (Forest Blizzard / GRU Unit 26165) is harvesting credentials from global organizations without deploying any malware — by modifying a single DNS setting on vulnerable SOHO routers to route victim traffic through attacker-controlled infrastructure.

The technique is fileless and leaves minimal forensic trace on endpoint systems. Affected organizations span multiple sectors globally. End-of-life routers with exposed remote management interfaces are the primary attack surface.

Defenders should audit SOHO router DNS configurations, disable remote management where not required, and replace end-of-life hardware. The FBI subsequently conducted a court-authorized operation to disrupt the campaign.
