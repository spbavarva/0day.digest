---
title: "Checkmarx Jenkins AST Plugin Compromised in Supply Chain Attack"
date: 2026-05-11 09:34:55 +0000
categories: [Daily Signal]
tags: [supply-chain, devsecops, appsec]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/
---

A malicious version of the Checkmarx Jenkins AST Plugin was published to the Jenkins Marketplace late last week.
The compromised plugin is used in CI/CD pipelines for application security testing, giving the attacker
foothold in build environments that routinely hold source code, secrets, and pipeline credentials.

This is the second Checkmarx-adjacent supply chain compromise in recent weeks, following the April compromise
of Bitwarden CLI and KICS. Teams using the Jenkins AST plugin should treat any environment where the affected
version executed as compromised, rotate all secrets accessible from those pipelines, and verify plugin integrity
before resuming scans. Consult the Jenkins Security Advisory for the specific compromised version.
