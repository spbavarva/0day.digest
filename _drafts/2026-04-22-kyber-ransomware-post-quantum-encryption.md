---
title: "Kyber Ransomware Gang Experiments with Post-Quantum Encryption on Windows and VMware ESXi"
date: 2026-04-22 18:52:29 +0000
categories: [Daily Signal]
tags: [ransomware, malware, vulnerability]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/kyber-ransomware-gang-toys-with-post-quantum-encryption-on-windows/
---

A new ransomware operation named Kyber is targeting Windows systems and VMware ESXi endpoints,
with at least one variant implementing Kyber1024 post-quantum key encapsulation. Post-quantum
encryption in ransomware closes a recovery avenue that has occasionally helped victims when
operators used weak key generation — decryption without the attacker's private key would be
computationally infeasible even against future quantum hardware.

The dual targeting of Windows hosts and ESXi hypervisors follows a pattern seen in several
recent ransomware groups prioritizing hypervisor-level encryption to maximize blast radius.
Organizations should maintain tested offline backups and monitor for mass file encryption
activity across both Windows endpoints and virtualization infrastructure.
