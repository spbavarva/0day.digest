---
title: "SprySOCKS Gets a Windows Port: FishMonger APT Abuses Kernel Drivers to Evade Detection"
date: 2026-06-16 20:11:00 +0000
categories: [Daily Signal]
tags: [malware, apt, microsoft, vulnerability]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/threat-intelligence/sprysocks-windows-variant-kernel-drivers
---

FishMonger, a China-nexus threat group, has deployed an undocumented Windows variant of the SprySOCKS backdoor—previously known only as a Linux implant—against government targets in Honduras, Taiwan, Thailand, and Pakistan. The new variant abuses signed kernel drivers to evade endpoint detection. The campaign targets government entities across multiple regions, suggesting a sustained and broadening espionage focus. Defenders should monitor for anomalous kernel driver loads, review FishMonger IOCs in threat intel platforms, and ensure EDR visibility into kernel-level activity.
