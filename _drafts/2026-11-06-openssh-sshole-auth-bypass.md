---
title: "OpenSSH Rushes Patches for 'SSHole' Authentication Bypass"
date: 2026-11-06 12:07:42 +0000
categories: [Daily Signal]
tags: [vulnerability, cve]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/openssh-rushes-patches-for-sshole-authentication-bypass/
---

A flaw dubbed "SSHole" affects OpenSSH on Linux distributions that use
musl libc without PAM. On affected systems, some accounts accept any
password between 257 and 1024 characters, effectively bypassing
authentication.

OpenSSH has rushed out patches. Administrators running musl-libc-based
distributions without PAM (common on Alpine Linux and similar minimal
images) should patch immediately and audit SSH access logs for anomalous
long-password logins.
