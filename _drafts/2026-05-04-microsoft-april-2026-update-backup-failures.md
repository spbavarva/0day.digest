---
title: "Microsoft April 2026 Updates Break Third-Party Backup Apps via Driver Block"
date: 2026-05-04 10:40:11 +0000
categories: [Daily Signal]
tags: [microsoft, vulnerability]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-backup-failures-caused-by-vulnerable-driver-block/
---

Microsoft confirmed that April 2026 security updates are causing failures in third-party backup applications that rely on the psmounterex.sys driver. The update's vulnerable driver blocklist prevents the driver from loading, breaking backup operations for affected tools.

Backup integrity is a critical ransomware resilience control — failed backup jobs that go undetected leave organizations without recovery options. Administrators should immediately verify that backup jobs are completing successfully post-update, coordinate with their backup vendor for a patched driver version, and consider temporary compensating controls (such as additional snapshot-based backups) until the issue is resolved. Microsoft has confirmed the issue; watch for an out-of-band fix or KB update.
