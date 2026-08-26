---
title: "VMs Won't Contain Cyber-Capable Agents"
date: 2026-08-26 11:00:00 +0000
categories: [Daily Signal]
tags: [ai-safety, vulnerability, llm]
severity: high
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/
---

A Trail of Bits researcher with preview access to an AI model called GPT
5.6-Cyber tasked it with escaping a QEMU/KVM sandbox VM on a Linux dev
machine — and it succeeded three separate times. It first used recently
disclosed host kernel bugs, then switched to disclosed-but-unpatched
bugs after the host was updated, adapting again after QEMU and its
dependencies were rebuilt.

The result is a concrete demonstration that a current frontier model can
autonomously chain real, disclosed vulnerabilities to break out of
VM-based sandboxing, with implications for how labs and security teams
design containment for cyber-capable agents.
