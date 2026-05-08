---
title: "PamDOORa: New Linux Backdoor Abuses PAM Modules for Persistent SSH Access"
date: 2026-05-08 08:41:00 +0000
categories: [Daily Signal]
tags: [malware, vulnerability, linux]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html
---

PamDOORa is a new Linux backdoor advertised on the Rehub Russian cybercrime forum for $1,600 that
abuses Pluggable Authentication Modules (PAM) to maintain persistent SSH access via a hardcoded
magic password and specific TCP port combination. The PAM abuse technique survives reboots and
standard credential rotation, making detection and removal non-trivial. It is being marketed as a
post-exploitation toolkit for maintaining long-term stealthy access. Defenders should audit PAM
configurations, review entries in `/etc/pam.d/`, and monitor for unexpected SSH authentication
behavior.
