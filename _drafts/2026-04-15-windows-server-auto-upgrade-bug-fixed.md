---
title: "Microsoft Patches Bug That Silently Upgraded Windows Server 2019/2022 to Server 2025"
date: 2026-04-15 10:24:00 +0000
categories: [Daily Signal]
tags: [microsoft, vulnerability]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-bug-behind-windows-server-2025-automatic-upgrades/
---

Microsoft has resolved a known issue that was causing Windows Server 2019 and 2022 systems to
unexpectedly upgrade to Windows Server 2025 without administrator intent. The bug had been
affecting production environments where organizations had not licensed or planned to deploy
Server 2025.

Unexpected OS upgrades in production server environments carry real risk: licensing compliance
exposure, application incompatibility, changed security baselines, and invalidation of support
contracts tied to specific OS versions. Environments with automated update pipelines were most
exposed.

Administrators should verify that no unintended upgrades occurred during the window the bug was
active. Systems that auto-upgraded should be assessed for licensing status and application
compatibility before being left in production on Server 2025.
