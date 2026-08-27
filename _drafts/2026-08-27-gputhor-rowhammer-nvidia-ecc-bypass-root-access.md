---
title: "GPUThor Rowhammer Attack Defeats ECC on NVIDIA RTX A6000, Enables Root Access"
date: 2026-08-27 08:13:11 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/gputhor-rowhammer-defeats-ecc-on-nvidia.html
---

Researchers at the University of Toronto disclosed GPUThor, a Rowhammer
attack against NVIDIA workstation GPUs with GDDR6 memory that defeats
error-correcting code (ECC), the mitigation NVIDIA recommends against
GPU Rowhammer. The attack enables denial-of-service conditions and
privilege escalation to a root shell.

The attack was demonstrated by hammering DRAM on an NVIDIA RTX A6000. No
CVE identifier was included in the source summary.
