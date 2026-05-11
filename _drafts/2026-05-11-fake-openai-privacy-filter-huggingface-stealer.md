---
title: "Fake OpenAI Privacy Filter on Hugging Face Delivers Infostealer to 244K Downloaders"
date: 2026-05-11 07:05:00 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, openai]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/fake-openai-privacy-filter-repo-hits-1.html
---

A malicious Hugging Face repository (`Open-OSS/privacy-filter`) impersonated OpenAI's legitimate
`openai/privacy-filter` model — copying its README and metadata — and climbed to the #1 trending position on
the platform before being flagged. It accumulated 244K downloads and delivered a Rust-based information stealer
to Windows users via the disguised download.

This is a significant supply chain event for the AI/ML ecosystem: Hugging Face's trending algorithm actively
amplified the malicious repo, exposing a model-distribution trust gap analogous to npm typosquatting. Anyone
who downloaded `Open-OSS/privacy-filter` should treat the host as compromised, scan for the Rust infostealer
binary, and rotate all credentials accessible from the affected environment.
