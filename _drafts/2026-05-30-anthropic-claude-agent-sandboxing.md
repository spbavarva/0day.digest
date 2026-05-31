---
title: "How Anthropic Sandboxes Claude Agents Across Products"
date: 2026-05-30 21:36:24 +0000
categories: [Daily Signal]
tags:
  - ai-safety
  - llm
  - anthropic
  - appsec
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything
---

Anthropic published a detailed overview of the containment techniques applied to
Claude agents across Claude.ai, Claude Code, and Cowork. The mechanisms include
process sandboxes, virtual machines, filesystem boundaries, and network egress
controls to hard-limit what an agent can reach.

The key design principle: if credentials never enter the sandbox, they cannot be
exfiltrated. Anthropic's documentation is notable for being more thorough than
most vendor sandboxing write-ups, which typically omit implementation specifics.

Practitioners building agentic systems on top of Claude or other LLMs should
review this as a reference architecture for agent isolation — the same techniques
(VM-per-session, egress allowlisting, no credential passthrough) apply broadly.
