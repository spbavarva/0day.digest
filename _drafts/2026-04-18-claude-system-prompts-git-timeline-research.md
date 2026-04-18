---
title: "Claude System Prompts Visualized as a Git Timeline"
date: 2026-04-18 12:25:00 +0000
categories: [Daily Signal]
tags: [anthropic, llm, ai-safety]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Apr/18/extract-system-prompts/#atom-everything
---

Simon Willison used Claude Code to parse Anthropic's publicly published system prompts
page — which covers Claude chat and various model families — and restructure the content
into individual files with synthetic git commit timestamps. The result is a browsable
git history that lets anyone diff how Claude's instructions have evolved across model
versions.

The project surfaces concrete changes in Claude's behavior constraints, tone guidelines,
and capability framing over time. For practitioners building on top of Claude, this
timeline is a practical reference for understanding what shifted and when. The underlying
system prompts are already public; this work makes them navigable.
