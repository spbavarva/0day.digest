---
title: "GitHub Breach Traced to Poisoned Nx Console VS Code Extension in TanStack Supply Chain Attack"
date: 2026-05-21 06:54:01 +0000
categories: [Daily Signal]
tags: [supply-chain, github, npm, data-breach]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/
---

GitHub confirmed that threat actors breached approximately 3,800 of its internal repositories via a compromised employee device. The initial vector was a malicious version of the Nx Console VS Code extension (`nrwl.angular-console`), itself poisoned as part of last week's TanStack npm supply chain attack. An Nx developer's machine was compromised first, enabling the attackers to trojanize the extension and pivot through any developer who had it installed. The breach was claimed by the threat actor group TeamPCP. GitHub has notified affected teams and is auditing repository access logs.
