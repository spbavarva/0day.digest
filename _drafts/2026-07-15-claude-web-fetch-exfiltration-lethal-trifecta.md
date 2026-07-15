---
title: "Researcher Finds Hole in Claude's Web Fetch Data Exfiltration Protections"
date: 2026-07-15 14:21:54 +0000
categories: [Daily Signal]
tags: [anthropic, llm, ai-safety, vulnerability]
severity: high
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything
---

Researcher Ayush Paul found a hole in the design Anthropic built to stop
Claude's web_fetch tool from being used for data exfiltration. Regular Claude
chat carries "lethal trifecta" risk: it has access to private data (memories
of past interactions), and a tool that can both read hostile instructions
from fetched content and reach out to attacker-controlled URLs. Anthropic's
protection restricts web_fetch to exact URLs the user has already seen, but
Paul demonstrated a way around that restriction.
