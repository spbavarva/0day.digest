---
title: "Malicious npm Package 'imgdecode' Hides Shellcode Loader in Windows Native Addon"
date: 2026-10-17 11:11:56 +0000
categories: [Daily Signal]
tags: [npm, supply-chain, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/malfex-npm-package-imgdecode-hides.html
---

Researchers uncovered a malicious npm package named "imgdecode" tied to a
supply chain campaign dubbed MALFEX. It was uploaded on September 30, 2026 by
a user named "malfexteste8" and has been downloaded 979 times. The package
ships a Windows native addon that conceals a shellcode loader. It remained
live on npm at the time of disclosure. Developers who installed "imgdecode"
should treat any Windows hosts that ran it as potentially compromised.
