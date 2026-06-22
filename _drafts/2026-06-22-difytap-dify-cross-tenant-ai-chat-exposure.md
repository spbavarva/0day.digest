---
title: "DifyTap Flaws in Dify Expose AI Chats Across Tenants"
date: 2026-06-22 16:13:28 +0000
categories: [Daily Signal]
tags: [llm, vulnerability, data-breach, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/researchers-detail-difytap-flaws-in.html
---

Zafran Security disclosed four vulnerabilities, collectively named DifyTap, in Dify, an open-source agentic workflow platform with more than 146,000 GitHub stars. The flaws could let an attacker stealthily read AI conversations from other customers' applications without authentication, exposing cross-tenant chat data on shared Dify deployments. Organizations self-hosting Dify should apply available patches and review tenant-isolation configuration on any multi-tenant deployment.
