---
title: "McGraw-Hill Confirms Data Breach via Salesforce Misconfiguration"
date: 2026-04-14 18:07:07 +0000
categories: [Daily Signal]
tags: [data-breach, cloud-security]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/mcgraw-hill-confirms-data-breach-following-extortion-threat/
---

Educational publisher McGraw-Hill has confirmed a data breach after hackers exploited a
Salesforce misconfiguration to access internal data. The breach was disclosed following an
extortion threat. The full scope of compromised data has not been disclosed.

Salesforce misconfigurations — particularly around object-level sharing, guest user permissions,
and externally accessible org settings — have become a recurring initial access vector in
enterprise breaches. Unlike direct exploitation, these attacks abuse legitimate platform features
that were simply configured insecurely.

Organizations using Salesforce should audit sharing rules, guest user access settings, and
profile/permission set configurations. Focus on public-accessible objects, Connected App OAuth
policies, and any externally shared reports or dashboards. This incident joins a growing list of
high-profile breaches originating from SaaS misconfigurations rather than traditional exploits.
