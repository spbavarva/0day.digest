---
title: "phpBB Patches Decade-Old Authentication Bypass Allowing Admin Takeover"
date: 2026-06-12 18:19:34 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/phpbb-forum-fixes-auth-bypass-bug-lurking-for-a-decade/
---

A decade-old authentication bypass vulnerability in phpBB forum software has
been patched. The flaw allowed an attacker to log in as any user, including
administrators, without valid credentials.

The bug reportedly went unnoticed for roughly ten years before being
identified and fixed.

Forum administrators running phpBB should update to the patched version as
soon as possible, since a successful exploit grants full administrative
access to the forum.
