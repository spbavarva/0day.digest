---
title: "CPUID Supply Chain Attack Poisons CPU-Z and HWMonitor Downloads"
date: 2026-04-10 13:12:42 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/supply-chain-attack-at-cpuid-pushes-malware-with-cpu-z-hwmonitor/
---

Hackers compromised an API for CPUID, the developer behind CPU-Z and HWMonitor, and
modified official download links to serve malicious executables in place of the
legitimate tools. The attack targeted users downloading from the official CPUID website
during the compromise window. CPU-Z and HWMonitor are among the most widely used
Windows hardware diagnostics utilities, making the potential exposure broad. Any
executable downloaded from the official site during the affected period should be
treated as suspect. Users should re-download from a verified clean source and check
hashes against any known-good values published by CPUID post-remediation.
