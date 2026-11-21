---
title: "China-Linked Hackers Used AI Agents to Exploit Zero-Day in Medical Imaging Software"
date: 2026-11-21 11:03:17 +0000
categories: [Daily Signal]
tags: [zero-day, llm, rce, privilege-escalation]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html
  - name: SecurityWeek
    url: https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/
---

Suspected China-linked hackers used autonomous AI agents to discover a
previously unknown vulnerability in MONAI Label, an open-source
medical-imaging server, and used it to gain root access to a university
server, according to Amazon Threat Intelligence.

The flaw lets an unauthenticated attacker write files outside the server's
designated storage folder in the default configuration, and affects MONAI
Label 0.8.5 and earlier. The incident is a concrete example of AI agents
being used autonomously to find and weaponize a zero-day rather than just
assist a human operator.
