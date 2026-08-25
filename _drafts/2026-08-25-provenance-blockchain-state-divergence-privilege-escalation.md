---
title: "State Divergence Enables Unauthorized Access"
date: 2026-08-25 11:00:00 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability]
severity: high
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access/
---

Trail of Bits found and reported a bug in Provenance Blockchain, a public
proof-of-stake chain built on Cosmos SDK, that let any user grant themselves
admin control over marker accounts without holding a single token.
Provenance underpins financial services including on-chain tokenized loans,
private equity tokens, bridged assets, and asset registries, and the bug
affected 82 markers representing live financial assets on mainnet. Trail of
Bits found the issue in versions before 1.28.0 in March 2026 and reported it
on April 1; it was mitigated in PR #2627 (commit c81fd65). No evidence of
exploitation was mentioned in the available summary.
