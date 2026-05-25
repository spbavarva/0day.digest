---
title: "TrapDoor Supply Chain Attack Targets npm, PyPI, and Crates.io"
date: 2026-05-25 05:59:13 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, pypi, malware, crates-io]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html
---

TrapDoor is a coordinated cross-ecosystem campaign distributing
credential-stealing malware across npm, PyPI, and Crates.io. Researchers
identified 34+ malicious packages spanning 384+ versions, with activity
recorded in waves starting May 22, 2026.

The simultaneous targeting of three major registries is unusual and suggests
a well-resourced actor. Developers should audit dependency trees for any
packages published or updated since May 22 from unknown or low-reputation
maintainers, and rotate credentials if affected packages were installed.
