---
title: "Miasma Worm Compromises 73 Microsoft GitHub Repositories in Supply Chain Attack"
date: 2026-06-06 06:58:04 +0000
categories: [Daily Signal]
tags: [supply-chain, github, microsoft, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html
---

The Miasma self-replicating worm has compromised 73 repositories across four Microsoft GitHub organizations: Azure, Azure-Samples, Microsoft, and MicrosoftDocs. GitHub has disabled access to affected repositories. The attack is part of an ongoing Miasma supply chain campaign, not an isolated incident. Downstream consumers — developers using Azure SDK samples or docs repos — should audit any dependencies, Actions workflows, or scripts pulled during the impact window. Pin to known-good commit SHAs and inspect CI/CD pipelines referencing the affected organizations. The breadth of Microsoft repositories involved makes this a high-priority supply chain event.
