---
title: "Malicious Sicoob NuGet Package Steals Banking Credentials; npm Packages Target Cloud Secrets"
date: 2026-05-29 09:11:25 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, npm]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/malicious-sicoob-nuget-steals-banking.html
---

Socket researchers found that NuGet package `Sicoob.Sdk` (versions 2.0.0–2.0.4) impersonates the legitimate C# SDK for Sicoob, one of Brazil's largest cooperative banking networks. The malicious versions exfiltrate client IDs and PFX certificates used for banking authentication.

In a separate but simultaneous campaign, npm packages were found targeting cloud secrets — specifically harvesting credentials from developer environments. Both attacks hit the software supply chain at the dependency level, activating silently during normal development workflows.

Developers working with Brazilian banking SDKs should audit their NuGet dependencies immediately and verify package authenticity. Both campaigns underscore the need for dependency scanning in CI pipelines that can detect typosquatting and malicious payload injection beyond simple version pinning.
