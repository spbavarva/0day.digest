---
title: "Windows, Linux, and Android File Notification Systems Found to Leak User Activity"
date: 2026-09-25 10:53:32 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/windows-linux-android-file-notification-systems-leak-user-activity/
---

Researchers showed that file-change notification systems on Windows, Linux,
and Android can leak sensitive user activity to unprivileged observers.

The leaked signals reportedly include keystroke timing, browsing activity,
and WhatsApp media events, inferred from patterns in file-system
notification APIs.

The source summary does not specify whether vendors have shipped mitigations
or assigned CVEs for the underlying design issue.
