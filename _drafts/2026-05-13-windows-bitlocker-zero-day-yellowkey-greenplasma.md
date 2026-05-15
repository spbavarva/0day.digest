---
title: "Unpatched Windows BitLocker Zero-Days YellowKey and GreenPlasma: PoC Released"
date: 2026-05-13 16:37:49 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, privilege-escalation, microsoft, cve]
severity: critical
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/
---

A researcher has published proof-of-concept exploits for two unpatched Windows
vulnerabilities: YellowKey, a BitLocker bypass granting read access to
protected drives, and GreenPlasma, a local privilege-escalation flaw. Neither
has a patch from Microsoft as of disclosure. With public PoC code in the wild,
exploitation window is narrow. Organizations relying on BitLocker for
data-at-rest protection should treat this as elevated risk until a patch ships.
Physical or local low-privilege access is likely required — exact prerequisites
are still being assessed by the community. Monitor for a Microsoft
out-of-band advisory and apply any patch immediately on release.
