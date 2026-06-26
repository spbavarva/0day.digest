---
title: "New 'DirtyClone' Linux Kernel Flaw Lets Local Users Gain Root"
date: 2026-06-26 11:51:35 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html
---

DirtyClone, tracked as CVE-2026-43503 (CVSS 8.8), is a new Linux kernel
privilege escalation in the DirtyFrag family. It lets a local user corrupt
file-backed memory through a cloned network packet and gain root. JFrog
Security Research published a working exploit walkthrough on June 25, the
first public demonstration for this variant. A patch has already landed
upstream.
