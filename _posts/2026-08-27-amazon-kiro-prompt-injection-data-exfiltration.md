---
title: "Amazon Kiro Prompt Injection Flaw Can Exfiltrate Data via Kiro Powers"
date: 2026-08-27 13:39:56 +0000
categories: [Daily Signal]
tags: [llm, appsec, aws, ai-safety]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/amazon-kiro-prompt-injection-can.html
---

Researchers at Mindguard disclosed a vulnerability in Amazon Kiro, an
AI-powered agentic IDE, that can facilitate data exfiltration via prompt
injection combined with Kiro Powers. The flaw affects Kiro IDE 0.7.45 on
Windows and does not have an assigned CVE identifier.

Teams using agentic IDEs with tool or plugin access should review how
untrusted content (files, web content, third-party outputs) can reach
tool-invocation contexts, since that's the path this attack abuses.
