---
title: "xAI's Grok Build Coding Tool Was Uploading Users' Full Codebases to Cloud Storage"
date: 2026-07-14 19:25:00 +0000
categories: [Daily Signal]
tags: [llm, appsec]
severity: high
must_know: false
sources:
  - name: The Verge AI
    url: https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload
---

Security researchers at Cereblab found that xAI's Grok Build coding tool was
uploading users' entire code repositories to Google Cloud storage, including
files the tool had been explicitly told not to open. The Register reported
the finding before xAI disabled the behavior.

The incident highlights the risk of undisclosed data exfiltration in AI
coding assistants that operate with broad filesystem access.
