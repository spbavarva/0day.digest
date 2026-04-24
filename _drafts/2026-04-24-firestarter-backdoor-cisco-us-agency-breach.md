---
title: "FIRESTARTER Backdoor Gave Attackers Persistent Access to US Agency via Cisco Vulnerability"
date: 2026-04-24 19:03:00 +0000
categories: [Daily Signal]
tags: [malware, vulnerability, data-breach, cve, microsoft]
severity: high
must_know: false
sources:
  - name: The Record (Recorded Future)
    url: https://therecord.media/cisa-us-agency-breached-cisco-vulnerability-backdoor
---

CISA disclosed that an unnamed US government department was breached via a Cisco vulnerability and
subsequently infected with a custom backdoor called FIRESTARTER. The malware allowed attackers to
re-enter the compromised Cisco device through March 2026 without re-exploiting the original
vulnerability — a classic persistence-over-re-exploitation pattern associated with nation-state
operators. CISA's disclosure does not name the threat actor or the specific Cisco CVE used for
initial access.

Organizations running internet-exposed Cisco network appliances should audit devices for
FIRESTARTER indicators of compromise and verify patch status. The ability of the attackers to
maintain persistent access through a custom implant on a network device underscores the risk of
treating network gear as lower-priority targets for endpoint detection.
