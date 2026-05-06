---
title: "Cisco Crosswork Network Controller DoS Flaw Requires Manual Reboot to Recover"
date: 2026-05-06 18:06:21 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-cisco-dos-flaw-requires-manual-reboot-to-revive-devices/
---

Cisco patched a denial-of-service vulnerability in Crosswork Network Controller and Network Services Orchestrator (NSO) that can be exploited to crash affected devices, requiring manual physical or console-based reboot for recovery. The flaw is particularly disruptive in environments where these network automation platforms manage large-scale infrastructure.

Network operations teams running Crosswork or NSO should apply the available patch and review their incident response procedures to account for scenarios where automated recovery mechanisms are unavailable. Prioritize patching in environments where manual reboot access is limited or operationally costly.
