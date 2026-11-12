---
title: "Google Cloud Warns Three AMD Turin CPU Flaws Could Leak Data Across VMs"
date: 2026-11-12 12:09:14 +0000
categories: [Daily Signal]
tags: [cloud-security, vulnerability, gcp]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html
---

Google Cloud warned that three CPU side-channel flaws in AMD Turin
processors could let an attacker with code running on the same processor
core infer data from other processes or the kernel inside a VM. Affected
VMs need a guest OS patch and a stop-and-start to apply the mitigation.

Google says it has already applied mitigations against attacks between
VMs, and between VMs and the host — the residual risk is intra-VM,
cross-process leakage.
