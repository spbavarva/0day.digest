---
title: "Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers"
date: 2026-10-28 06:20:37 +0000
categories: [Daily Signal]
tags: [privilege-escalation, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/tailscale-patches-ssh-flaws-that-could.html
---

Tailscale released version 1.104.4 to fix flaws in its built-in SSH server
that could let an attacker reach services and files on other servers that
only the root user should be able to access.

The flaws are in how Tailscale SSH forwards network connections, a function
the Tailscale background process performs with root privileges.

Tailscale users should update to 1.104.4 or later.
