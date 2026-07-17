---
title: "GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft"
date: 2026-07-17 16:39:16 +0000
categories: [Daily Signal]
tags: [supply-chain, data-breach, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/goldeneyedog-subgroup-linked-to.html
---

Researchers at Expel have attributed the April 2026 DigiCert security incident, which involved theft of code-signing certificates, to a threat cluster dubbed CylindricalCanine — a sub-group of GoldenEyeDog (aka APT-Q-27, Dragon Breath, Miuuti Group), a Chinese cybercrime group historically focused on gambling and gaming targets. Stolen code-signing certificates let attackers sign malware so it appears trusted by endpoint defenses, creating downstream supply-chain risk for anyone who trusts binaries signed under the compromised certs. Organizations should review code-signing trust policies and watch for revocations tied to this incident.
