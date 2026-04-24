---
title: "Anthropic Postmortem: Three Claude Code Harness Bugs Caused Two Months of Quality Degradation"
date: 2026-04-24 01:31:00 +0000
categories: [Daily Signal]
tags: [anthropic, llm]
severity: medium
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/#atom-everything
---

Anthropic published a postmortem confirming that three separate bugs in the Claude Code harness
caused material quality degradation over the past two months — the models themselves were not at
fault. One notable issue: a March 26 change cleared Claude's accumulated "thinking" from sessions
idle for over an hour to reduce latency, inadvertently discarding context critical for complex
multi-step tasks.

The incident is a useful case study for teams building agentic AI systems: harness-level changes
can silently degrade task performance in ways that look like model regressions. Organizations
using Claude Code for automated workflows should review the postmortem to understand which
task types were most affected and verify current behavior against their benchmarks.
