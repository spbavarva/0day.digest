---
title: "TanStack Supply Chain Attack Compromised Two OpenAI Employee Devices, Credentials Stolen"
date: 2026-05-15 10:54:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, openai, malware, appsec]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html
  - name: SecurityWeek
    url: https://www.securityweek.com/openai-hit-by-tanstack-supply-chain-attack/
---

OpenAI disclosed that two employee devices in its corporate environment were compromised via the Mini Shai-Hulud malware delivered through the TanStack supply chain attack. Credential material from OpenAI code repositories was stolen; OpenAI states no user data, production systems, or intellectual property were compromised or modified. The company investigated, contained the incident, and pushed macOS updates to affected devices. This demonstrates the downstream blast radius of npm supply chain attacks reaching into high-value corporate environments. Organizations using TanStack packages should audit for Mini Shai-Hulud indicators and rotate any credentials from developer machines that may have installed affected versions.
