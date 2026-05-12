---
title: "Mini Shai-Hulud Worm Hits TanStack, Mistral AI, Guardrails AI and More in Fresh Supply Chain Spree"
date: 2026-05-12 08:50:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, pypi, malware, appsec, devsecops]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html
---

TeamPCP, the threat actor behind the original Shai-Hulud supply chain campaign, has compromised npm
and PyPI packages belonging to TanStack, UiPath, Mistral AI, OpenSearch, and Guardrails AI in a new
wave dubbed Mini Shai-Hulud. Affected npm packages were modified to include an obfuscated JavaScript
file (`router_init.js`) designed to profile the execution environment before delivering a payload.

The cross-ecosystem reach — hitting both npm and PyPI — and the targeting of AI framework packages
(Mistral AI, Guardrails AI) makes this particularly high-risk for AI/ML development pipelines.
Developers using any of the named packages should pin to a known-good version, audit build logs for
unexpected network calls, and treat any CI artifact produced since the compromise window as suspect.
Check the TeamPCP attribution thread for IOCs and affected version ranges.
