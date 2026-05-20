---
title: "Microsoft Rolls Out Mitigations for YellowKey BitLocker Bypass"
date: 2026-05-20 15:39:00 +0000
categories: [Daily Signal]
tags: [vulnerability, microsoft, cve]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/microsoft-rolls-out-mitigations-for-yellowkey-bitlocker-bypass/
---

Microsoft has released mitigations for YellowKey, a BitLocker bypass that allows attackers to circumvent full-disk encryption by exploiting the Windows Recovery Environment (WinRE). The fix works by preventing the FsTx Auto Recovery Utility from launching when the WinRE image starts.

Organizations relying on BitLocker for data protection at rest should apply the available update promptly. The bypass is relevant in scenarios involving physical or bootable-media access to a device, making it particularly relevant for endpoint security policies covering laptops and unattended workstations.
