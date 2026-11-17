---
title: "'Sleeper Agent' Tactic Hides Payloads in Open-Weight AI Models"
date: 2026-11-16 19:10:03 +0000
categories: [Daily Signal]
tags: [malware, supply-chain, llm]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/vulnerabilities-threats/sleeper-agent-tactic-payloads-open-weight-ai-models
---

Researchers describe a "sleeper agent" technique that hides malicious
payloads inside open-weight AI models, with malware occupying as little as
0.00001% of a neural network's parameters. At that scale, the hidden
payload is effectively undetectable through casual inspection of model
weights.

The technique raises the stakes for anyone downloading open-weight models
from public repositories, since standard file-level scanning is unlikely
to catch a payload embedded at the weight level. Teams should prioritize
provenance and signed-checksum verification over content scanning alone.
