---
title: "Compromised Nx Console 18.95.0 Delivers Credential Stealer to 2.2M VS Code Users"
date: 2026-05-19 07:49:23 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, credential-theft, appsec, devsecops]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
---

A malicious version of the Nx Console extension (`rwl.angular-console` v18.95.0) was published to the VS Code Marketplace, targeting developers using VS Code, Cursor, and JetBrains.
The extension has more than 2.2 million installations, making the blast radius substantial.
Version 18.95.0 contained a credential stealer designed to harvest secrets accessible from the developer's environment.
Developers who installed or auto-updated to version 18.95.0 should remove it immediately, audit for exfiltrated credentials, and rotate any API keys, tokens, or secrets stored in the affected environment.
The incident follows a pattern of supply chain attacks targeting developer tooling distributed via extension marketplaces.
