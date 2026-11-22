---
title: "OpenRouter Drops 3 Providers After Researchers Catch Months of Prompt Theft at AI Hosting Firms"
date: 2026-11-22 05:06:55 +0000
categories: [Daily Signal]
tags: [llm, data-breach, ai-safety]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html
---

Researchers at Dragos found that attackers had been stealing data from
inside three AI inference providers for months, undetected by the
providers themselves. OpenRouter, which routes customer requests to a pool
of inference providers, dropped all three after being notified.

Some of the stolen requests had been flagged as Zero Data Retention,
a setting meant to guarantee prompts are never stored. The incident
highlights that ZDR commitments are only as strong as the hosting
provider's actual infrastructure controls.
