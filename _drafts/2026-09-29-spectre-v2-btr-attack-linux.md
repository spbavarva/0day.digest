---
title: "New Spectre v2 'BTR' Attack Recovers Linux Root Password Hashes in Minutes"
date: 2026-09-29 17:10:11 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-spectre-v2-attack-variant-leaks-linux-root-password-hash-in-minutes/
---

Researchers disclosed a new Spectre v2 variant, dubbed Branch Target Reuse
(BTR), that can recover root password hashes on Intel systems running Linux
in an average of 3-5 minutes. The attack targets JIT engines used by
browsers, language runtimes, and the OS kernel, and works despite existing
Spectre mitigations. It requires local code execution to exploit, consistent
with other Spectre-class side channels. Expect follow-up guidance from CPU
vendors and Linux distros on additional mitigations.
