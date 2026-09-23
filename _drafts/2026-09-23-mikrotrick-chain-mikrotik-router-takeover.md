---
title: "MikroTrick Chain Lets Attackers Take Over MikroTik Routers Without Authentication"
date: 2026-09-23 16:06:41 +0000
categories: [Daily Signal]
tags: [rce, privilege-escalation, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html
---

CERT Polska disclosed MikroTrick, an attack chain combining an SSH
state-machine flaw (CVE-2026-67279) with an argument-injection bug in
the RouterOS login process (CVE-2026-86060). Chained together, the
two vulnerabilities let attackers gain full administrative control of
internet-exposed MikroTik routers without a password, SSH key, or
completed authentication.

Operators of internet-facing MikroTik RouterOS devices should apply
available patches and restrict management-plane exposure.
