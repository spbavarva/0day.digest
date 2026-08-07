---
title: "New NatJack Attacks Hijack TCP Sessions and Spoof DNS by Manipulating NAT Tables"
date: 2026-08-07 10:58:38 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/new-natjack-attacks-hijack-tcp-sessions.html
---

Security researcher Malcolm Stagg disclosed a new attack class called
NatJack that manipulates NAT connection state to hijack active TCP
sessions, spoof DNS responses, expose mapped ports, and exhaust NAT tables.
Presented at Black Hat USA 2026, the research found the underlying weakness
across independently developed implementations, including Windows. The
available summary does not include patch status.
