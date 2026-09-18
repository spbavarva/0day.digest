---
title: "Trail of Bits: Using AI to Build Custom Tooling Before Code Review Begins"
date: 2026-09-18 11:00:00 +0000
categories: [Daily Signal]
tags: [llm, appsec, devsecops]
severity: informational
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/
---

Trail of Bits published a methodology piece on using AI agents to build
custom tooling and formal models before code review even starts, rather
than only for agentic code review itself. The team applied the approach
to an audit of Miden VM, a zero-knowledge VM with a custom assembly
language and almost no existing developer tooling. The post argues that
AI-assisted tooling generation is an underexplored use case compared to
the widely-publicized "point an agent at a codebase" bug-hunting posts.
