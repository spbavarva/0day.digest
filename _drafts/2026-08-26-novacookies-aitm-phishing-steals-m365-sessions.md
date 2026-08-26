---
title: "NovaCookies Campaigns Abuse Genuine Docusign Notifications to Steal Microsoft 365 Sessions"
date: 2026-08-26 13:44:31 +0000
categories: [Daily Signal]
tags: [phishing, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/novacookies-campaigns-abuse-genuine.html
  - name: Dark Reading
    url: https://www.darkreading.com/endpoint-security/novacookies-steals-microsoft-365-sessions-320-a-month
---

Researchers disclosed a new adversary-in-the-middle phishing toolkit
called NovaCookies that abuses genuine Docusign notifications to
redirect Microsoft 365 sign-ins through an attacker-controlled proxy,
capturing authenticated sessions in the process. Island reports the
subscription-based service is sold for $320 a month.

Because the toolkit steals live session cookies rather than just
credentials, it can bypass MFA on affected accounts. Treat unusual
Docusign-branded sign-in prompts as a possible AitM vector and monitor
for anomalous M365 session reuse.
