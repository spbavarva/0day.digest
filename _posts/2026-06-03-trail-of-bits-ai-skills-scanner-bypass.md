---
title: "Trail of Bits: Malicious AI Skills Bypass Every Public Skill Scanner"
date: 2026-06-03 11:00:00 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, appsec, supply-chain]
severity: high
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/
---

Trail of Bits researchers bypassed ClawHub's malicious skill detector, Cisco's agent skill scanner, and all three scanners integrated into skills.sh — each in under an hour — using four malicious skills capable of stealing credentials, exfiltrating data, and hijacking AI agents. Public skill marketplaces for AI agents are being flooded with attacker-controlled skills, and the scanner ecosystem designed to catch them does not work against even basic evasion techniques. The finding mirrors early npm and PyPI supply chain dynamics: a fast-moving distribution channel with security tooling that lags far behind. Organizations deploying AI agents should treat third-party skills with the same scrutiny as third-party code dependencies and prefer skills from verified publishers over marketplace installs.
