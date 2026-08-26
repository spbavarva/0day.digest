---
title: "New GPUThor Attack Defeats NVIDIA ECC Protection for Root Access"
date: 2026-08-26 18:48:24 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-gputhor-attack-defeats-nvidia-ecc-protection-for-root-access/
---

A newly disclosed Rowhammer-class attack called GPUThor can defeat
error-correcting code (ECC) protections on NVIDIA GPUs. The technique
enables both denial-of-service conditions and root-level privilege
escalation on affected systems.

ECC memory has historically been treated as an effective mitigation
against Rowhammer-style bit-flip attacks, so a working bypass on GPU
hardware is notable. Organizations running NVIDIA GPUs in multi-tenant
or security-sensitive environments should watch for vendor guidance as
more technical detail emerges.
