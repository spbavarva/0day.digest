---
title: "Gremlin Stealer Evolves With Resource-File Obfuscation, Crypto Clipping, and Session Hijacking"
date: 2026-05-15 10:00:00 +0000
categories: [Daily Signal]
tags: [malware]
severity: medium
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/
---

Unit 42 analyzed an updated Gremlin stealer variant that embeds malicious code inside application resource files to evade static detection, adds a cryptocurrency clipboard hijacker that redirects transactions to attacker-controlled wallets, and includes session token theft for account takeover. The resource-file obfuscation technique reduces detection rates for environments relying on signature-based scanning. Organizations should ensure endpoint security tools are updated with signatures for this variant and monitor for anomalous clipboard modification activity in environments handling cryptocurrency or sensitive authenticated sessions.
