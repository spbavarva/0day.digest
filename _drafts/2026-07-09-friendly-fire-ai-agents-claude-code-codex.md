---
title: "Top AI Agents Built to Catch Malicious Code Can Be Tricked Into Running It"
date: 2026-07-09 05:15:02 +0000
categories: [Daily Signal]
tags: [ai-safety, llm, anthropic, openai]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/friendly-fire-ai-agents-built-to-catch.html
---

The AI Now Institute published a proof-of-concept it calls "Friendly Fire,"
showing that AI coding agents tasked with scanning open-source code for
vulnerabilities can instead be tricked into executing the malicious code
they're supposed to catch. The PoC works against Anthropic's Claude Code
and OpenAI's Codex when either is run in an autonomous mode that approves
its own actions. The risk is specific to autonomous/auto-approve
configurations rather than standard human-in-the-loop use.
