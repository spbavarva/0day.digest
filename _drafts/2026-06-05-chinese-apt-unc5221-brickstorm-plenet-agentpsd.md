---
title: "Chinese APT UNC5221 Deploys New Malware Families Plenet and AgentPSD Against Microsoft 365"
date: 2026-06-05 18:09:47 +0000
categories: [Daily Signal]
tags: [malware, apt, microsoft, iam]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/chinese-apt-deploys-new-malware-to-keep-access-to-hacked-networks/
---

Chinese espionage group UNC5221 has been linked to the Brickstorm backdoor and two previously
undocumented malware families — Plenet and AgentPSD — used to maintain persistent access inside
Microsoft 365 environments. The actor targets government and critical infrastructure organizations,
leveraging cloud-native persistence mechanisms to survive remediation attempts. Defenders should audit
M365 conditional access policies, review OAuth application grants for anomalous delegated permissions,
and check sign-in logs for unusual service principal activity. Hunting for Brickstorm, Plenet, and
AgentPSD IOCs across email and identity layers is recommended.
