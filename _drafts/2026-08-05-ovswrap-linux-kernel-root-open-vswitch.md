---
title: "New OVSwrap Linux Kernel Flaw Lets Local Users Gain Root via Open vSwitch"
date: 2026-08-05 11:43:27 +0000
categories: [Daily Signal]
tags: [cve, privilege-escalation, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/new-ovswrap-linux-kernel-flaw-lets.html
---

A memory corruption flaw in the Linux kernel's Open vSwitch datapath,
tracked as CVE-2026-64531 (CVSS 7.8) and codenamed OVSwrap, gives ordinary
local users a path to root on a broad set of default-configured
distributions.

A public exploit already ships with pre-built records covering roughly 800
kernel builds, lowering the bar for exploitation. Any system running Open
vSwitch — including many virtualization and container networking stacks —
should prioritize patching.
</content>
