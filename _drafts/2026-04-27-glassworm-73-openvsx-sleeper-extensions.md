---
title: "GlassWorm Returns: 73 Sleeper Extensions Planted in OpenVSX Registry"
date: 2026-04-27 21:41:01 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/glassworm-malware-attacks-return-via-73-openvsx-sleeper-extensions/
---

A new wave of the GlassWorm campaign has seeded 73 malicious "sleeper" extensions into the OpenVSX registry — the open-source extension marketplace used by VSCodium, Eclipse Che, Gitpod, and other VS Code-compatible editors. The extensions behave legitimately at install time and turn malicious after a subsequent update, making static analysis at install insufficient to catch them.

Developers and CI/CD pipelines running VS Code-compatible editors backed by OpenVSX should audit all recently installed extensions and cross-reference against the published list of 73 known-bad identifiers once released. Pinning extension versions in automated environments is the primary mitigation until affected extensions are removed from the registry. This is the second confirmed GlassWorm wave in the past week; the previous campaign targeted the VS Code Marketplace directly.
