---
title: "April Windows 11 Update KB5083769 Breaks Third-Party Backup Software on 24H2 and 25H2"
date: 2026-04-30 15:23:03 +0000
categories: [Daily Signal]
tags: [microsoft, vulnerability]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/april-kb5083769-windows-11-update-causes-backup-software-failures/
---

Microsoft's April 2026 KB5083769 security update breaks third-party backup applications from multiple vendors on systems running Windows 11 24H2 and 25H2. Microsoft has acknowledged the issue but has not released a fix. The failure mode is not yet fully documented, meaning some organizations may have silent backup failures without obvious error reporting.

Backup failures resulting from a security patch directly undermine disaster recovery posture — especially if backups appear to run but produce corrupted or incomplete output. Organizations on the affected Windows versions should immediately verify that backup jobs are completing and producing valid output, and consider temporarily pausing automated backups until Microsoft issues a fix if jobs are failing.
