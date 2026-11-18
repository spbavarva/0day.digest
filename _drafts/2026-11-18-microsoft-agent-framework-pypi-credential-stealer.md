---
title: "Attackers Compromise Microsoft's Agent Framework PyPI Package to Steal Cloud Credentials"
date: 2026-11-18 06:45:26 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, microsoft, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html
  - name: SecurityWeek
    url: https://www.securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer/
---

Threat actors compromised Microsoft's agent-framework package on PyPI,
pushing two malicious versions — 1.26.1 and 1.26.2 — that run a
credential stealer every time Python starts. The versions were
published 33 minutes apart on November 17, 2026.

The malware targets Azure, Azure DevOps, and GitHub Actions
credentials. Multiple security vendors — including Aikido, Chainguard,
Endor Labs, OX Security, Socket, and Google-owned Wiz — independently
flagged the compromise.

Anyone who installed agent-framework 1.26.1 or 1.26.2 should treat
Azure, Azure DevOps, and GitHub Actions credentials on affected
systems as compromised and rotate them immediately.
