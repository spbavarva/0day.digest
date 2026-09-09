---
title: "A Lean Proof-Checker Bug Behind Anthropic's Fermat's Last Theorem Formalization"
date: 2026-09-09 11:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, anthropic]
severity: informational
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/
---

Trail of Bits found a bug in the Lean proof checker while examining
Anthropic's recently announced 13-million-line Lean formalization of
Fermat's Last Theorem. The issue affects all stable versions of Lean up to
4.33.1; a patch is incorporated in v4.34.0-rc1.
