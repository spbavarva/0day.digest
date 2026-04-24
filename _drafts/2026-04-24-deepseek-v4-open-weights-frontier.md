---
title: "DeepSeek Releases V4 Preview: Largest Open-Weights Model at 1.6T Parameters Under MIT License"
date: 2026-04-24 06:01:00 +0000
categories: [Daily Signal]
tags: [deepseek, ai-launch, model-release, llm]
severity: medium
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Apr/24/deepseek-v4/#atom-everything
---

DeepSeek released two preview models from their V4 series: DeepSeek-V4-Pro (1.6T total / 49B
active parameters, Mixture-of-Experts) and DeepSeek-V4-Flash (284B total / 13B active). Both
support 1M token context windows and are released under the MIT license, making them available
for unrestricted commercial use and self-hosting. V4-Pro is now the largest open-weights model
available, surpassing Kimi K2.6 (1.1T) and the prior DeepSeek V3.2 (685B).

The combination of frontier-class scale, open weights, and MIT licensing continues to challenge
closed-model economics. The V4-Flash variant (13B active parameters) is particularly interesting
for inference-cost-sensitive deployments. Security-relevant implication: unrestricted access to
very large open-weights models increases capability availability for both defensive tooling and
adversarial AI-assisted attack research.
