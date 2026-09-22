---
title: "Linux Kernel Flaw Lets ARM64 KVM Guests Read/Write Host Memory (CVE-2026-89775)"
date: 2026-09-22 11:38:40 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html
---

A flaw in the Linux kernel's KVM virtualization code for ARM64 leaves a
freed region of host memory exposed to guest VMs on hosts with nested
virtualization enabled. Tracked as CVE-2026-89775, the bug lets a guest
read and write host kernel memory.

The researcher who found it says it can be used to escape the guest and
execute code on the host machine. Affects ARM64 hosts running nested KVM
virtualization.
