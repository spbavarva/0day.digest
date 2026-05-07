---
title: "DAEMON Tools Supply Chain Attack Hits Government and Scientific Targets"
date: 2026-05-06 08:33:40 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/government-scientific-entities-hit-via-daemon-tools-supply-chain-attack/
  - name: The Record (Recorded Future)
    url: https://therecord.media/hackers-compromise-daemon-tools-global-supply-chain-attack
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/daemon-tools-devs-confirm-breach-release-malware-free-version/
---

Attackers compromised DAEMON Tools Lite installers distributed via the software's official website, embedding a backdoor in a global supply chain attack. Kaspersky researchers identified the compromise; Disc Soft Limited (the developer) confirmed the breach and released a clean version.

Although trojanized versions were installed on systems worldwide, the attackers selectively deployed a sophisticated backdoor payload on approximately a dozen targets — primarily government and scientific entities. Users who installed DAEMON Tools Lite recently should verify their version against the new clean release and hunt for persistence mechanisms and unexpected outbound connections from affected hosts.
