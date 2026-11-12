---
title: "Hackers Plant GSocket on Linux Servers for Persistent Access"
date: 2026-11-12 09:38:00 +0000
categories: [Daily Signal]
tags: [malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-plant-gsocket-on-linux-servers-for-persistent-access/
---

Multiple threat actors are abusing GSocket, a legitimate open-source
remote access tool, to maintain access to Linux servers even after the
vulnerabilities used for initial access have been patched.

Because GSocket is a legitimate tool, its presence can blend in with
normal administrative activity — defenders should treat unexpected GSocket
usage as a persistence indicator worth investigating.
