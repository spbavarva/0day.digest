---
title: "CISA Adds BerriAI LiteLLM SQL Injection to Known Exploited Vulnerabilities"
date: 2026-05-08 12:00:00 +0000
categories: [Daily Signal]
tags: [sqli, cve, vulnerability, llm]
severity: high
must_know: false
sources:
  - name: CISA Alerts
    url: https://www.cisa.gov/news-events/alerts/2026/05/08/cisa-adds-one-known-exploited-vulnerability-catalog
---

CISA added CVE-2026-42208, a SQL injection vulnerability in BerriAI's LiteLLM, to its Known
Exploited Vulnerabilities catalog, confirming active exploitation in the wild. LiteLLM is a
widely-used open-source proxy layer that routes calls across multiple LLM providers, making it
common infrastructure in AI-heavy environments. SQL injection at this layer could expose LLM API
keys, request logs, and prompt histories. Organizations running LiteLLM should update immediately
and audit any instances accessible over the internet.
