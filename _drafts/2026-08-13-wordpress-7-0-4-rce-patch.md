---
title: "WordPress 7.0.4 Patches Remote Code Execution Vulnerability"
date: 2026-08-13 12:53:56 +0000
categories: [Daily Signal]
tags: [vulnerability, rce, cve, appsec]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/wordpress-7-0-4-patches-remote-code-execution-vulnerability/
---

WordPress 7.0.4 patches a remote code execution vulnerability exploitable
by attackers who already hold Author-level user permissions or higher, via
maliciously crafted Postscript files.

The elevated-privilege requirement limits the blast radius compared to an
unauthenticated RCE, but sites allowing untrusted Author-level accounts
should update promptly.
