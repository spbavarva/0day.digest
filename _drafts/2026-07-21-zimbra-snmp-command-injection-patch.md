---
title: "Zimbra Patches Critical SNMP Command Injection and Four XSS Vulnerabilities"
date: 2026-07-21 13:18:31 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec, xss]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/zimbra-patches-critical-snmp-command.html
---

Zimbra 10.1.20 patches nine security vulnerabilities, the most severe being
a command injection flaw in the SNMP monitoring component that triggers
when SNMP notifications are enabled. The update also addresses four XSS
issues among the other patched flaws. Zimbra administrators should update
to 10.1.20 and confirm SNMP notification settings on any systems that
haven't yet been patched.
