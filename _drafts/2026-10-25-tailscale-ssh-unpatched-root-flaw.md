---
title: "Unpatched Tailscale SSH Flaws Could Let a Hacked Device Reach Root on Other Servers"
date: 2026-10-25 17:44:09 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/unpatched-tailscale-ssh-flaws-could-let.html
---

A security researcher disclosed that a single compromised device on a
Tailscale network can be used to gain root access on other servers the
network's access rules permit it to reach.

The attack requires Tailscale SSH configured to allow port forwarding, plus
an attacker who already controls a device the tailnet's ACLs allow to
connect to the target. The flaw is unpatched as of publication.

Admins running Tailscale SSH should review ACLs and disable port
forwarding where it isn't strictly needed until a fix ships.
