---
title: "Research: Trusted Execution Environments Can Undermine MPC Threshold Signatures"
date: 2026-09-25 11:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: informational
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/
---

Trail of Bits published research on how running multi-party computation
(MPC) threshold-signature schemes inside trusted execution environments
(TEEs) can introduce subtle security issues.

MPC is meant to distribute trust across independent parties, while TEEs root
trust in hardware attestation — but the combination can fail if the
untrusted host isn't accounted for, for example by manipulating the TEE's
environment.

The research is aimed at engineering teams designing threshold-signature
systems on TEE-backed infrastructure.
