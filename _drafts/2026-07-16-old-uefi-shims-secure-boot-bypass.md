---
title: "Old UEFI Shims Expose Systems to Secure Boot Bypass"
date: 2026-07-16 07:59:22 +0000
categories: [Daily Signal]
tags: [vulnerability, microsoft]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/old-uefi-shims-expose-systems-to-secure-boot-bypass/
---

Outdated UEFI shim bootloaders, signed by Microsoft, can be abused to
bypass Secure Boot on any system regardless of operating system. Because
the shims carry a valid Microsoft signature, they pass boot-chain trust
checks despite containing known vulnerabilities, letting an attacker with
the right access load untrusted code before the OS starts. Organizations
should ensure vulnerable shim revocations are applied via UEFI Secure Boot
DBX updates rather than relying on OS-level patching alone.
