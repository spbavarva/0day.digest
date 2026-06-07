---
title: "C0XMO Botnet Exploits DD-WRT Router Flaw, Kills Rival Malware on Infected Devices"
date: 2026-06-07 14:17:46 +0000
categories: [Daily Signal]
tags: [malware, vulnerability, iot]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/c0xmo-botnet-spreads-via-dd-wrt-router-flaw-kills-rival-malware/
---

A new Gafgyt botnet variant called C0XMO is spreading by exploiting a flaw in
DD-WRT router firmware and can move laterally to other device types across
multiple CPU architectures. Once it gains a foothold, C0XMO actively kills
competing malware on the infected device to claim exclusive control.

Operators of DD-WRT-based routers and other embedded devices should apply
available firmware updates and review devices for unexpected processes or
outbound connections, since IoT botnets typically feed into DDoS-for-hire
operations once a device population is established.
