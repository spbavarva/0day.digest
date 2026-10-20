---
title: "WAGO OS Linux Flaws Let Low-Privilege Users Bypass Authorization Boundaries"
date: 2026-10-20 12:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, privilege-escalation]
severity: medium
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-293-02
---

CISA disclosed two vulnerabilities (CVE-2026-80466, CVE-2026-88850) in the
Web-Based Management interface of several WAGO controllers (CC100, PFC100
G2, PFC200 G2, TP600, Edge Controller, WP400), affecting firmware from
1.0.0 up to below 4.10.0.

An authenticated low-privileged user can bypass intended privilege
boundaries in both routing configuration and PROFIBUS authorization.
Operators should apply WAGO's firmware updates once available and restrict
WBM interface access in the meantime.
