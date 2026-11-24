---
title: "GLM-5.4: Toward Generalized Coding with Our First Loop Transformer"
date: 2026-11-23 23:40:49 +0000
categories: [Daily Signal]
tags: [model-release, llm, ai-launch]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Nov/23/glm-54/
---

Chinese AI lab Z.ai released GLM-5.4, its first model built on a looped
transformer architecture. Instead of running each layer once per forward
pass, a group of weight-shared layers runs for multiple iterations,
refining hidden states from the previous pass without increasing parameter
count.

It's the second looped-transformer release noted in the past week,
following Inkling 2 Mini, suggesting growing interest in the architecture
as a way to add depth without inflating model size.
