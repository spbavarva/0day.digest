---
title: "Trail of Bits Open-Sources SequenceHash for Secure Multihashing"
date: 2026-10-02 11:00:00 +0000
categories: [Daily Signal]
tags: [appsec, devsecops]
severity: informational
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/
---

Trail of Bits introduced SequenceHash and a companion construction,
SequenceMAC, open hash constructions aimed at bringing secure
multihashing to developers using hash functions other than Keccak.

The goal is to help cryptographers and developers avoid attacks that
take advantage of ambiguous input encodings when combining multiple
hashes. The specification is open.
