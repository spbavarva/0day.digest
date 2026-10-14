---
title: "Trail of Bits: Most Package Managers Don't Verify Package Integrity by Default"
date: 2026-10-14 11:00:00 +0000
categories: [Daily Signal]
tags: [supply-chain, appsec, devsecops]
severity: medium
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/10/14/package-managers-have-an-integrity-problem/
---

Trail of Bits tested 25 popular package managers to see whether they detect
a compromised repository injecting malicious code into legitimate packages.

Fewer than half used lockfiles that check for tampering by default, and only
two of the 25 verified the integrity of every package they downloaded.

The researchers note the gap is solvable with cryptographic hashes or
signatures, but most ecosystems still leave the door open to repository-level
supply chain compromise even when a project's own dependencies haven't been
directly tampered with.
