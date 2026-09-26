---
title: "Compromised GitHub Actions Re-Enabled With Mini Shai-Hulud Payload Still Live"
date: 2026-09-26 14:19:46 +0000
categories: [Daily Signal]
tags: [supply-chain, github, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/
---

Two third-party GitHub Actions previously compromised in the Mini
Shai-Hulud supply chain campaign were re-enabled by their maintainer and
remained publicly accessible for more than a week, despite still pointing
to malicious code.

Any workflow that referenced these actions during that window may have
executed the malicious payload. Repository owners using third-party GitHub
Actions should audit which actions and pinned commit SHAs they depend on.
