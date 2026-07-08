---
title: "GhostLock: 15-Year-Old Linux Kernel Flaw Enables Root and Container Escape"
date: 2026-07-08 06:16:44 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, privilege-escalation, rce]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html
---

Researchers at Nebula Security disclosed GhostLock (CVE-2026-43499), a
Linux kernel flaw that has shipped by default in essentially every
mainstream distribution since 2011. Any logged-in user can exploit it to
gain full root control on an unpatched machine, with no special
permissions or unusual settings required. The flaw also enables container
escape. Admins should prioritize patching across all Linux fleets given
the 15-year exposure window and broad default-install footprint.
