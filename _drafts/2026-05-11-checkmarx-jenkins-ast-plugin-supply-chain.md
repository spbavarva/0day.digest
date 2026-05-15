---
title: "Checkmarx Jenkins AST Plugin Poisoned in Supply Chain Attack"
date: 2026-05-11 09:34:55 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, devsecops, github]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/
---

A malicious version of the Checkmarx Jenkins AST (Application Security Testing) plugin was
published to the official Jenkins Plugin Marketplace late last week. The poisoned plugin can
silently intercept or manipulate security scan results within CI/CD pipelines, potentially
allowing attackers to suppress findings and pass malicious code through automated gates.

Any Jenkins instance with the AST plugin installed should verify the installed version and
its checksum against known-good values immediately. This follows a pattern of CI/CD tooling
being targeted to undermine security scanning rather than simply deliver malware — a more
subtle and persistent form of supply chain compromise. Teams using Checkmarx SAST through
Jenkins should treat scan results from affected time windows as potentially unreliable.
