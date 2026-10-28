---
title: "Critical 16-Year-Old UEFI Flaw in EDK II Allows Pre-Boot Code Execution"
date: 2026-10-28 11:50:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/critical-16-year-old-uefi-flaw-can-run.html
---

A 16-year-old flaw in EDK II, the open-source code most hardware makers use
to build UEFI firmware, can let an attacker run code on a machine before its
operating system loads, bypassing Secure Boot. The flaw only applies while a
machine is booting over the network, limiting exposure to environments using
network/PXE boot. Firmware vendors will need to ship EDK II updates; affected
organizations should restrict network boot to trusted segments in the
meantime.
