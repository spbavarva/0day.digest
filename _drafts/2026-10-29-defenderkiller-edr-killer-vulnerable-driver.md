---
title: "DefenderKiller Tool Abuses Vulnerable Driver to Disable Endpoint Security"
date: 2026-10-29 20:04:21 +0000
categories: [Daily Signal]
tags: [malware, privilege-escalation, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: Flashpoint
    url: https://flashpoint.io/blog/defenderkiller-how-vulnerable-drivers-are-being-abused-to-disable-endpoint-security/
---

Flashpoint analysts detailed DefenderKiller, an open-source "EDR killer" tool
that abuses a legacy Microsoft driver to terminate endpoint security
processes. The technique is a classic bring-your-own-vulnerable-driver
(BYOVD) attack, and modified variants of the original proof-of-concept are
already circulating.

Defenders should watch for unexpected loading of the abused driver and
unexplained termination of security agents, since EDR-killer tools are a
common precursor step before ransomware deployment.
