---
title: "Atlassian Rovo AI Assistant Tricked Into Leaking Jira and Confluence Data"
date: 2026-08-08 08:54:50 +0000
categories: [Daily Signal]
tags: [llm, prompt-injection, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html
---

Security researchers at PromptArmor and Varonis independently found that
Atlassian's Rovo AI assistant can be manipulated by attacker-controlled
instructions hidden in content it reads, such as an uploaded file. Once
triggered in a one-click attack, Rovo can be made to collect Jira or
Confluence data the signed-in user has access to and send it to an outside
server. The two firms discovered the issue via different routes; per the
report, only one of those routes has been confirmed closed by Atlassian.
Organizations using Rovo should review what external content it's permitted
to ingest and monitor for unexpected outbound data flows.
