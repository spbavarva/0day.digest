---
title: "16-Year-Old Linux Kernel Flaw Enables VM Escape on Intel and AMD"
date: 2026-07-07 10:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce, privilege-escalation]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/linux-kernel-vulnerability-allows-vm-escape-on-intel-and-amd-systems/
---

A flaw dubbed "Januscape," present in Linux's KVM hypervisor for a reported
16 years, allows an attacker with access to a guest VM to escape the VM
boundary and potentially execute code on the underlying host. The flaw
affects both Intel and AMD systems running KVM-based virtualization. No
active exploitation has been reported. Operators of KVM hypervisors should
watch for distro kernel patches and apply them once available.
