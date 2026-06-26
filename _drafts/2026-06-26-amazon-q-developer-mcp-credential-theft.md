---
title: "Amazon Q Developer Flaw Allowed Credential Theft via Malicious MCP Configs"
date: 2026-06-26 13:53:00 +0000
categories: [Daily Signal]
tags: [vulnerability, cve, aws, llm]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html
---

A high-severity flaw in Amazon Q Developer, tracked as CVE-2026-12957
(CVSS 8.5), allowed a malicious repository to run commands and steal a
developer's cloud credentials. The flaw sat in how the AI coding assistant
handled Model Context Protocol (MCP) server configurations: a developer
opening a malicious repo and trusting the workspace was enough to trigger
it. AWS has patched the vulnerability and published its own advisory.
