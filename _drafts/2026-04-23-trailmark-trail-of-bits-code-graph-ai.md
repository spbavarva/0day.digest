---
title: "Trail of Bits Open-Sources Trailmark: Code Graph Library for AI-Assisted Security Analysis"
date: 2026-04-23 12:00:00 +0000
categories: [Daily Signal]
tags: [appsec, devsecops, llm]
severity: informational
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/04/23/trailmark-turns-code-into-graphs/
---

Trail of Bits released Trailmark (`uv pip install trailmark`), an open-source library that parses
source code into a queryable call graph exposing functions, classes, call relationships, and
semantic metadata through a Python API designed for Claude skills. The project is grounded in John
Lambert's observation that defenders think in lists while attackers think in graphs — Trailmark
aims to give AI-assisted analysis graph-native reasoning over codebases rather than flat file
traversal.

Security researchers and tool builders can integrate Trailmark into AI-powered code review and
vulnerability discovery workflows to enable structural queries like "find all functions that reach
this sink" or "show call paths from external input to authentication checks." The library is
directly usable with Claude's tool-use API.
