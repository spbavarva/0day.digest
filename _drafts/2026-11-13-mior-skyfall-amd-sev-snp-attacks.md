---
title: "New Mior and Skyfall Attacks Steal Secrets From AMD SEV-SNP VMs"
date: 2026-11-13 15:27:05 +0000
categories: [Daily Signal]
tags: [cloud-security, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html
---

Researchers disclosed two attacks, Mior and Skyfall, that let a malicious
cloud host read data from inside AMD SEV-SNP-protected virtual machines,
which are designed to keep the server operator out. Mior can additionally
modify a VM's memory and forge the signed attestation report describing
which software the VM is running.

Both attacks require control of the server's hypervisor, and Mior
additionally requires control of the server's BIOS, limiting exploitation to
hosts already compromised at a deep level. Cloud providers relying on
SEV-SNP for tenant isolation should review hypervisor and BIOS hardening
against this class of attack.
