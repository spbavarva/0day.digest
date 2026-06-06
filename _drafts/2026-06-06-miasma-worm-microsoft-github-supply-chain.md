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

A self-replicating worm called Miasma has compromised 73 repositories across four
of Microsoft's GitHub organizations — Azure, Azure-Samples, Microsoft, and
MicrosoftDocs. GitHub has disabled access to the affected repositories while
remediation is underway, per OpenSourceMalware.

This is part of an ongoing Miasma campaign targeting public GitHub repositories via
self-replication through forks and CI/CD mechanisms. Any pipeline that consumes
dependencies from the affected repos should be treated as potentially compromised
until Microsoft confirms clean bills of health. Audit your GitHub Actions workflows
and dependency lockfiles for unexpected changes originating from these organizations.
