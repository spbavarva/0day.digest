---
title: "Critical Langflow Flaws Allow Unauthenticated Remote Code Execution"
date: 2026-11-02 11:50:00 +0000
categories: [Daily Signal]
tags: [rce, llm, vulnerability]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html
---

Two critical vulnerabilities in Langflow, an open-source tool for building
AI agents and workflows, could let an unauthenticated attacker bypass
authentication or run arbitrary code on the server.

Every release from 1.0.0 through 1.12.8 is affected; version 1.13.0
contains the fix. IBM, which handles Langflow's vulnerability reports,
disclosed the flaws. Neither is currently listed in CISA's Known Exploited
Vulnerabilities catalog.
