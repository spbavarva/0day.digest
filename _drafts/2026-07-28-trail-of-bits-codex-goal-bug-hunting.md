---
title: "Trail of Bits Uses Codex's /goal to Find Bugs in Rust, curl, and zlib"
date: 2026-07-28 11:00:00 +0000
categories: [Daily Signal]
tags: [appsec, llm, openai]
severity: informational
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/
---

Trail of Bits detailed how it uses OpenAI Codex's /goal feature — an
open-ended, objective-driven agent mode — to hunt for bugs as part of
Patch the Planet, its joint initiative with OpenAI targeting widely used,
heavily audited codebases like Rust, curl, and zlib. The team found that
getting useful results from /goal depends heavily on prompt design, scope,
and the number of outcomes requested per run.
