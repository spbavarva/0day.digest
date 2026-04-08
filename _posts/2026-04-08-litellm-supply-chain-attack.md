---
title: "LiteLLM Supply Chain Attack — PyPI Packages Compromised"
date: 2026-04-08 09:30:00 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, llm, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/
---

TeamPCP compromised LiteLLM versions 1.82.7 and 1.82.8 on PyPI, injecting an
infostealer that harvested plaintext API keys, SSH credentials, and `.env` files
from developer machines. Both versions have been yanked. If your CI installed
LiteLLM in the last 36 hours, rotate every secret in scope and audit egress
logs. This is exactly why dependency pinning and hash verification matter.
