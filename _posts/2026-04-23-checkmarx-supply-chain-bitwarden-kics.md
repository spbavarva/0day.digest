---
title: "Checkmarx Supply Chain Attack Compromises Bitwarden CLI and KICS Analysis Tool"
date: 2026-04-23 13:42:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, cve, appsec, devsecops]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/bitwarden-cli-compromised-in-ongoing.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-checkmarx-supply-chain-breach-affects-kics-analysis-tool/
---

An ongoing supply chain campaign has compromised `@bitwarden/cli@2026.4.0` on npm with malicious
code embedded in `bw1.js`, designed to harvest credentials from developer environments. The same
campaign backdoored Docker images and VSCode/Open VSX extensions for the Checkmarx KICS
infrastructure-as-code analysis tool, which is widely used in CI/CD pipelines for security
scanning. Research from JFrog and Socket confirmed the active compromise.

Developers using either tool should treat any environment where the affected versions ran as
compromised. Remove `@bitwarden/cli@2026.4.0` immediately and rotate all secrets and credentials
accessible from those environments. Review Docker image provenance for KICS and audit any
extensions pulled from Open VSX. Both affected codepaths should be treated with the same urgency
as a direct credential theft incident.
