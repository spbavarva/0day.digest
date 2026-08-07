---
title: "18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers"
date: 2026-08-07 11:10:33 +0000
categories: [Daily Signal]
tags: [privilege-escalation, container-security, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/18-year-old-linux-sctp-flaw-could-let.html
---

A use-after-free bug in Linux's SCTP networking code, present since 2008,
can be turned into full root access on a host. Tencent researchers say they
used it to escape a container and reach the underlying machine. Fixes
shipped in stable kernels 7.1.6, 6.18.42, 6.12.101, and 6.6.148, released
August 3. Anyone running an older kernel with SCTP reachable should update.
