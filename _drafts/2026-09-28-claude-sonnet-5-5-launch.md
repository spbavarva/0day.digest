---
title: "Anthropic Releases Claude Sonnet 5.5"
date: 2026-09-28 22:07:38 +0000
categories: [Daily Signal]
tags: [ai-launch, model-release, anthropic, llm]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/
---

Anthropic released Claude Sonnet 5.5 today, an update to its mid-range
model. The company says it runs 30%+ faster and costs up to 30% less to
run than Sonnet 5, while pricing stays the same and benchmark results
improve across the board.

Early testing by Simon Willison found the same quirk seen in Opus 5.5:
at the "max" thinking-effort setting, Sonnet 5.5 burned through 128,000
thinking tokens without completing a simple SVG-generation task. At the
"xhigh" setting it completed the same task in 41 seconds.
