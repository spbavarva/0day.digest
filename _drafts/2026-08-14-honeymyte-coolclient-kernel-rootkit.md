---
title: "APT Group HoneyMyte Adds Kernel-Level Windows Rootkit to CoolClient Backdoor"
date: 2026-08-14 09:00:14 +0000
categories: [Daily Signal]
tags: [malware, privilege-escalation, rootkit]
severity: high
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/
---

Kaspersky researchers identified a new variant of the CoolClient backdoor
used by the HoneyMyte APT group, now bundled with a kernel-mode rootkit
driver. The driver hides malicious processes, files, and network connections
from security tools and analysts.

Kernel-level rootkit components significantly complicate detection and
incident response, since they operate below the visibility of most endpoint
security tooling.
