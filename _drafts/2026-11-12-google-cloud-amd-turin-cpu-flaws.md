---
title: "Google Cloud Warns AMD Turin CPU Flaws Can Leak Data Across VM Processes"
date: 2026-11-12 12:09:14 +0000
categories: [Daily Signal]
tags: [cloud-security, vulnerability, gcp]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html
---

Google Cloud is warning that three CPU side-channel flaws in AMD Turin
processors could let an attacker with code running on the same processor
core infer data from other processes or the kernel inside a VM.

Google says it has already applied mitigations against attacks between
VMs and between VMs and the host, but customers on affected Turin-based VM
types still need to apply a guest OS patch and stop/start the instance to
close the intra-VM data leak path.
