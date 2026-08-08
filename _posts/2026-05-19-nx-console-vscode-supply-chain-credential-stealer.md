---
title: "Compromised Nx Console VS Code Extension Installed Credential Stealer on 2.2M Developer Machines"
date: 2026-05-19 07:49:23 +0000
categories: [Daily Signal]
tags: [supply-chain, credential-stealer, malware, github]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html
---

A compromised version of the Nx Console extension (`rwl.angular-console` v18.95.0)
was published to the VS Code Marketplace, targeting the extension's 2.2 million
installed users across VS Code, Cursor, and JetBrains. The malicious version
deployed a credential stealer aimed at developer credentials and secrets
accessible within the IDE environment.

Affected developers should remove version 18.95.0 immediately, update to the
latest clean release, and rotate any credentials, API keys, or tokens that
may have been accessible in their development environment. This is the latest
in a string of developer tooling supply chain attacks that treat IDE extensions
as a high-value distribution vector.
