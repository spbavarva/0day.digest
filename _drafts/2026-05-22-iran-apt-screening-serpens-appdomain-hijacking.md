---
title: "Iranian APT Screening Serpens Uses AppDomainManager Hijacking in 2026 Espionage Campaigns"
date: 2026-05-22 13:00:42 +0000
categories: [Daily Signal]
tags: [malware, privilege-escalation]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/
---

Unit 42 published detailed tracking of Screening Serpens, an Iran-linked APT actively targeting technology and defense sector organizations in 2026. The group employs AppDomainManager hijacking — abusing .NET's application domain configuration to load attacker-controlled DLLs without dropping obvious malware — alongside new remote access trojan variants. The combination of a living-off-the-land technique with custom tooling complicates detection. Defenders in tech and defense verticals should review .NET AppDomainManager configurations and monitor for unexpected DLL loading.
