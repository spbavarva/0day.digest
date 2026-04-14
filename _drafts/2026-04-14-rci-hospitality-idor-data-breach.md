---
title: "RCI Hospitality Discloses Data Breach via IDOR Vulnerability in Internet Services Platform"
date: 2026-04-14 09:35:06 +0000
categories: [Daily Signal]
tags: [data-breach, vulnerability, appsec]
severity: medium
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/nightclub-giant-rci-hospitality-reports-data-breach/
---

RCI Hospitality Holdings disclosed a data breach in an SEC filing, attributing it to an IDOR
(Insecure Direct Object Reference) vulnerability in RCI Internet Services. The flaw exposed
contractor data stored on the platform.

IDOR vulnerabilities allow attackers to access data belonging to other users or entities simply
by manipulating predictable identifiers in requests — no authentication bypass required beyond
an active session. The disclosure via SEC filing indicates the company deemed it material.

The breach scope appears limited to contractor data based on available disclosure, but IDOR
flaws affecting internet-facing services warrant review. Organizations should ensure IDOR
testing is part of their standard web application security assessments.
