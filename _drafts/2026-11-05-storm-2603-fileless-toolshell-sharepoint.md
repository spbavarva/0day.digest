---
title: "Fileless SharePoint Breach by Storm-2603 Abused ToolShell Exploit"
date: 2026-11-05 10:00:11 +0000
categories: [Daily Signal]
tags: [rce, malware, vulnerability]
severity: high
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/storm-2603-fileless-toolshell-attack/121467/
---

Kaspersky's GReAT team analyzed an intrusion by the threat actor Storm-2603
that used ToolShell exploitation against SharePoint to gain initial access,
then operated entirely in memory rather than dropping files to disk.

The fileless approach, combined with runtime process subversion, was
designed to evade disk-based detection. Kaspersky's writeup includes
guidance for detecting this class of memory-resident intrusion.
