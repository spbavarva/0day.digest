---
title: "Node2Shell: Brotli Decoder Flaw Triggers Patching Across Node.js, .NET, Python, and Microsoft Products"
date: 2026-10-26 10:21:57 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, rce, microsoft]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/node2shell-brotli-flaw-triggers-patching-across-microsoft-node-js-python-packages/
---

An out-of-bounds write in Google's Brotli decompression library, tracked
as Node2Shell, affects Node.js, .NET, PowerShell, and Python packages that
bundle the decoder, and can lead to code execution.

Microsoft and other vendors have issued patches across affected products.
Teams should check whether their dependency trees bundle Brotli and update
to patched versions.
