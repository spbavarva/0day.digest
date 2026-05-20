---
title: "GitHub Confirms 3,800 Internal Repos Breached via Malicious VS Code Extension"
date: 2026-05-20 09:28:53 +0000
categories: [Daily Signal]
tags: [supply-chain, github, malware, data-breach]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/github-confirms-hack-impacting-3800-internal-repositories/
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/
---

GitHub confirmed that roughly 3,800 internal repositories were compromised after a GitHub employee
installed a malicious VS Code extension. The threat actor, TeamPCP, exfiltrated private source code
and internal organization data, which was subsequently listed for sale on a cybercrime forum.

GitHub says there is currently no evidence of impact to customer repositories or data stored outside
GitHub's internal systems. The breach vector — a trojanized developer tool installed by a privileged
employee — underscores the supply chain risk of unvetted IDE extensions in sensitive environments.

Organizations should audit approved VS Code extension lists, restrict marketplace installs to curated
sets, and review whether any developer tooling with privileged access is exposed to unreviewed
third-party plugins.
