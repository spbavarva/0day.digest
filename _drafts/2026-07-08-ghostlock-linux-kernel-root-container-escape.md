---
title: "15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros"
date: 2026-07-08 06:16:44 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation, container-security]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html
---

Researchers at Nebula Security disclosed GhostLock (CVE-2026-43499), a
15-year-old Linux kernel flaw that lets any logged-in local user gain full
root control on an unpatched machine. The vulnerable code has shipped by
default in essentially every mainstream Linux distribution since 2011.
Exploitation requires no special permissions, unusual configuration, or
network access, and the flaw also enables container escape. Teams running
multi-user Linux hosts or container fleets should prioritize patching once
updates are available.
