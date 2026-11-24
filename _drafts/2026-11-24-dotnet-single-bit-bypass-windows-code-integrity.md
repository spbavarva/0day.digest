---
title: "Google Researcher Shows Single-Bit .NET File Change Bypasses Windows Code Integrity"
date: 2026-11-24 12:02:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html
---

Google Project Zero researcher James Forshaw showed that a quirk in how the
.NET Framework loads a program file lets a local attacker run untrusted code
past two separate Windows protections designed to block it.

The same loading behavior also bypassed Oracle VirtualBox's process
hardening on Windows hosts, tracked as CVE-2026-87268, as well as Windows
code integrity protections.
