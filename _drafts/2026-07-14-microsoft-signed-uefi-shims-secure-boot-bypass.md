---
title: "11 Old Microsoft-Signed Linux UEFI Shims Could Let Attackers Bypass Secure Boot"
date: 2026-07-14 12:46:18 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/11-old-microsoft-signed-linux-uefi.html
---

Researchers discovered 11 old, Microsoft-signed Linux UEFI shim applications that can be abused to bypass Secure Boot on most systems using the modern UEFI firmware standard. An attacker exploiting one of these still-trusted shims can execute untrusted code during system boot, enabling deployment of UEFI bootkits or other persistent malware. Because the shims carry a valid Microsoft signature, standard Secure Boot validation does not flag them as malicious. Organizations should check whether their UEFI revocation lists (dbx) have been updated to block the affected shim hashes.
