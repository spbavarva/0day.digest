---
title: "$10 Domain Registration Could Have Handed Attackers 25K Endpoints in OT and Gov Networks"
date: 2026-04-15 10:58:00 +0000
categories: [Daily Signal]
tags: [malware, vulnerability]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/10-domain-could-have-handed-hackers-25k-endpoints-including-in-ot-and-gov-networks/
---

Researchers discovered that registering a $10 domain could have granted control over approximately
25,000 endpoints already infected with adware, including systems on operational technology (OT)
and government networks. The adware in question is capable of disabling cybersecurity products and
pushing more dangerous secondary payloads to compromised hosts.

The finding illustrates a dormant-domain takeover risk: malware already on target systems calls
home to a domain whose registration lapsed or was never claimed. A researcher registering it for
a trivial cost becomes the de facto C2 operator for thousands of infected machines.

The presence of OT and government network hosts in the beacon pool is particularly alarming.
Security teams in those sectors should hunt for the implicated adware family and audit external
domains being contacted by endpoints, especially any that resolve to recently registered or
newly-transferred domains.
