---
title: "Linux KVM Flaw Lets Guest VMs Read Host Memory on AMD Clouds"
date: 2026-11-20 12:20:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, cloud-security, linux]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html
---

A flaw in KVM, the hypervisor built into the Linux kernel, let researchers
read about 127 GB of a cloud server's memory from inside a VM of their own
on DigitalOcean. Tracked as CVE-2026-99312, the bug affects only hosts
with AMD processors and nested virtualization enabled.

On a shared server, the exposed memory can include other customers'
virtual machines. Fixed kernels have already shipped; cloud operators
running AMD hosts with nested virtualization should confirm they're
patched.
