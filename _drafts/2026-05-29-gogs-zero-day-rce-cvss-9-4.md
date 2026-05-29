---
title: "Unpatched Gogs Zero-Day (CVSS 9.4) Enables Remote Code Execution via Pull Requests"
date: 2026-05-29 12:59:37 +0000
categories: [Daily Signal]
tags: [zero-day, rce, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/gogs-zero-day-exposes-servers-to-remote-code-execution/
---

A critical argument injection flaw in Gogs — the self-hosted Git service — allows authenticated attackers to achieve remote code execution by crafting pull requests with malicious branch names. The vulnerability carries a CVSS score of 9.4 and has no patch at time of disclosure.

Gogs is widely used by organizations self-hosting code repositories as a lightweight GitHub alternative. Authenticated RCE via the pull request workflow means any contributor with repo access could compromise the underlying server.

Until a patch is released, administrators should restrict who can open pull requests on Gogs instances, isolate Gogs servers from internal networks, and monitor for anomalous process execution. Consider migrating critical repositories to maintained alternatives if no patch timeline is confirmed.
