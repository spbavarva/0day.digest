---
title: "Hackers Abuse GSocket for Persistent Access on Linux Servers"
date: 2026-11-12 09:38:00 +0000
categories: [Daily Signal]
tags: [malware, appsec]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-plant-gsocket-on-linux-servers-for-persistent-access/
---

Multiple threat actors are abusing GSocket, a legitimate open-source
remote access tool, to keep persistent access to Linux servers even after
the vulnerabilities used for initial access have been patched.

Because GSocket is a legitimate tool, its traffic can blend in with normal
administrative activity, making it a useful technique for attackers to
retain footholds that survive routine patching. Defenders should check for
unexpected GSocket processes or outbound connections on internet-facing
Linux hosts.
