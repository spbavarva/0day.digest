---
title: "CISA Adds Actively Exploited Langflow and Trend Micro Apex One Flaws to KEV"
date: 2026-05-22 05:47:33 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, zero-day, rce]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html
---

CISA added two actively exploited vulnerabilities to its Known Exploited Vulnerabilities catalog:
CVE-2025-34291, a CVSS 9.4 origin validation error in Langflow (the open-source AI workflow
builder), and CVE-2026-34926, a directory traversal flaw in Trend Micro Apex One on-premise
deployments. Both are confirmed under active exploitation in the wild.

Langflow is widely deployed in AI agent pipelines and LLM orchestration stacks, making this
particularly relevant for teams running self-hosted AI infrastructure. Operators of either product
should patch immediately; federal agencies face mandatory remediation under BOD 22-01.
