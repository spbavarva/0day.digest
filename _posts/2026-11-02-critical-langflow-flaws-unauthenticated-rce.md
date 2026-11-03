---
title: "Critical Langflow Flaws Let Unauthenticated Attackers Run Code on AI Agent Servers"
date: 2026-11-02 11:50:00 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, llm]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html
---

Two critical vulnerabilities in Langflow, an open-source framework for
building AI agents and workflows, let a remote attacker with no
account bypass authentication or execute arbitrary code on the
server. Every release from 1.0.0 through 1.12.8 is affected; the only
fix is upgrading to 1.13.0.

The flaws were reported to IBM, which handles Langflow's vulnerability
disclosures, and neither is yet listed in CISA's Known Exploited
Vulnerabilities catalog. Anyone running Langflow should upgrade
immediately given the unauthenticated, no-account-required attack
path.
