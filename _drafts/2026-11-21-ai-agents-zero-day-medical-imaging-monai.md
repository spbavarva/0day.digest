---
title: "Attackers' AI Agents Found a Zero-Day in Medical-Imaging Software and Gained Root Access"
date: 2026-11-21 11:03:17 +0000
categories: [Daily Signal]
tags: [zero-day, rce, ai-safety, vulnerability]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html
---

Suspected China-linked hackers reportedly used autonomous AI agents to
discover a previously unknown flaw in MONAI Label, an open-source
medical-imaging server, and used it to gain root access to a university
server, according to Amazon's threat intelligence team.

The flaw lets an unauthenticated attacker write files outside the server's
storage folder, affecting MONAI Label 0.8.5 and earlier in its default
configuration.

No CVE identifier or patched version was mentioned in available reporting.
Operators running MONAI Label should review their exposure until a fix is
confirmed.
