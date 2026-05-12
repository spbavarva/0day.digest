---
title: "Fortinet Patches Critical RCE Flaws in FortiSandbox and FortiAuthenticator"
date: 2026-05-12 18:23:09 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-rce-flaws-in-fortisandbox-and-fortiauthenticator/
---

Fortinet has released patches for two critical vulnerabilities in FortiSandbox and
FortiAuthenticator. Both flaws could allow attackers to execute commands or arbitrary
code remotely. FortiAuthenticator is commonly deployed as part of RADIUS and single
sign-on infrastructure, making it a high-value target in enterprise environments.
Patches are available in the May 2026 Fortinet security advisories. Organizations
should prioritize these updates, particularly for any FortiAuthenticator instance
reachable from untrusted networks.
