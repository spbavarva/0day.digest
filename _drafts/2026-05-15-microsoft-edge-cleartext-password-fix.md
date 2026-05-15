---
title: "Microsoft Edge Will No Longer Load Saved Passwords in Cleartext at Startup"
date: 2026-05-15 14:49:00 +0000
categories: [Daily Signal]
tags: [microsoft, vulnerability]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/microsoft/microsoft-edge-to-stop-loading-cleartext-passwords-in-memory-on-startup/
---

Microsoft reversed a privacy-hostile behavior in Edge where all saved passwords were loaded into process memory as cleartext at browser startup — a practice the company had previously described as "by design." The fix prevents infostealer tools and memory-scraping malware from trivially dumping plaintext credentials from the Edge process. Enterprise IT teams managing Edge deployments should verify the update has applied and confirm via Group Policy or MDM reporting that the new behavior is in effect across managed endpoints.
