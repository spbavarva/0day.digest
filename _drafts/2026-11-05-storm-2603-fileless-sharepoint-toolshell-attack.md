---
title: "Storm-2603 Runs Fileless SharePoint Attack Using ToolShell Exploitation"
date: 2026-11-05 10:00:11 +0000
categories: [Daily Signal]
tags: [malware, rce]
severity: high
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/storm-2603-fileless-toolshell-attack/121467/
---

Kaspersky's GReAT team analyzed a fileless attack by the group tracked as
Storm-2603, which exploited SharePoint via the ToolShell exploit chain and
then subverted the runtime environment to operate without dropping files to
disk. The fileless approach is designed to evade traditional file-based
detection.

Organizations running on-premises SharePoint should confirm ToolShell-related
patches are applied and review detection coverage for in-memory attack
techniques, not just file-based indicators.
