---
title: "EnOcean SmartServer Flaws Enable Security Bypass and RCE in Building Management Systems"
date: 2026-04-30 11:57:31 +0000
categories: [Daily Signal]
tags: [vulnerability, rce, ics]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/enocean-smartserver-flaws-expose-buildings-to-remote-hacking/
---

Claroty researchers disclosed two vulnerabilities in the EnOcean SmartServer, a building automation IoT gateway used in commercial and industrial environments for HVAC, lighting, and access control. The flaws allow security control bypass and remote code execution. SmartServers act as protocol bridges between IoT field devices and building management platforms.

Successful exploitation could give attackers control over physical building systems — unlocking access control, manipulating HVAC, or disrupting fire suppression coordination. Patch according to EnOcean's advisory; where patching is not immediately feasible, isolate SmartServer management interfaces from internet-accessible segments and restrict access to known management hosts.
