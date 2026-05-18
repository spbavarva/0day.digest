---
title: "SHub Reaper macOS Stealer Bypasses Apple Mitigations, Plants Persistent Backdoor"
date: 2026-05-18 13:00:00 +0000
categories: [Daily Signal]
tags: [malware, phishing, appsec, macos]
severity: high
must_know: false
sources:
  - name: SentinelOne Labs
    url: https://www.sentinelone.com/blog/shub-reaper-macos-stealer-spoofs-apple-google-and-microsoft-in-a-single-attack-chain/
---

SentinelOne researchers have detailed SHub Reaper, a macOS infostealer that simultaneously impersonates Apple, Google, and Microsoft within a single attack chain. The malware bypasses Apple's Terminal mitigation controls, exfiltrates credentials and documents from the victim system, and installs a persistent backdoor for continued post-infection access. Spoofing three trusted brand identities in one campaign maximizes the probability of user engagement compared to single-brand lures. macOS users in enterprise environments should treat unexpected authentication prompts from any of the three vendors with heightened suspicion and verify software provenance before execution.
