---
title: "Microsoft Attributes Mastra npm Supply Chain Attack to North Korean Hackers"
date: 2026-06-20 14:09:19 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/microsoft-links-mastra-ai-supply-chain-attack-to-north-korean-hackers/
---

Microsoft has attributed the Mastra AI npm supply chain attack, which
compromised more than 140 packages under the "@mastra/*" namespace, to
Sapphire Sleet, a North Korean hacking group also tracked as BlueNoroff.
The attack was previously reported on June 17 as the "easy-day-js"
compromise, carried out via a single hijacked npm account. This is a new
attribution on an already-disclosed incident rather than evidence of a new
compromise. Teams that pulled affected Mastra packages should continue
auditing lockfiles and rotating credentials exposed to affected build
environments.
