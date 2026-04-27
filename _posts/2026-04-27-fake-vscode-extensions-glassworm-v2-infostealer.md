---
title: "73 Fake VS Code Extensions on Open VSX Deliver GlassWorm v2 Infostealer"
date: 2026-04-27 11:23:00 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, developer-tools]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/researchers-uncover-73-fake-vs-code.html
---

Researchers flagged 73 fake Visual Studio Code extensions on the Open VSX repository linked to a persistent infostealer campaign dubbed GlassWorm. The extensions are cloned versions of legitimate ones; six are confirmed malicious, with the rest acting as distribution infrastructure.

Open VSX is used by VS Code-compatible editors including VSCodium and Eclipse Theia, making it a target distinct from the official VS Code Marketplace. Developers using these editors should audit installed extensions, cross-reference publisher identities against official Marketplace listings, and remove anything recently installed from Open VSX that cannot be verified. GlassWorm v2 targets developer credentials and secrets stored in IDE configuration.
