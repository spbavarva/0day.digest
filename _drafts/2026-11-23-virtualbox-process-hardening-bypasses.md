---
title: "VirtualBox Process Hardening on Windows: New Bypasses Found Nearly a Decade Later"
date: 2026-11-23 08:00:00 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability]
severity: medium
must_know: false
sources:
  - name: Google Project Zero
    url: https://projectzero.google/2026/11/virtualbox-process-hardening.html
---

Google Project Zero revisited Oracle VirtualBox's Windows
process-hardening mechanism, which restricts who can open the kernel
driver to prevent privilege escalation against VM host processes. The
researcher previously found three bypasses in 2017 plus a related COM
runtime issue reported in 2020.

Returning to the same mechanism in 2026, the researcher found three
new bypasses, showing the protection model has proven difficult to
fully close off across multiple review cycles.
