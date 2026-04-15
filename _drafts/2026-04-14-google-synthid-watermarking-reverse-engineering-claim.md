---
title: "Developer Claims to Reverse-Engineer Google SynthID AI Watermarking; Google Disputes"
date: 2026-04-14 13:53:53 +0000
categories: [Daily Signal]
tags: [google, ai-safety, llm]
severity: medium
must_know: false
sources:
  - name: The Verge AI
    url: https://www.theverge.com/ai-artificial-intelligence/911579/google-synthid-ai-watermarking-system-reverse-engineered
---

A software developer going by "Aloshdenny" claims to have reverse-engineered Google DeepMind's
SynthID watermarking system for AI-generated images, enabling removal of watermarks from
AI-generated content or their insertion into non-AI images. The developer has open-sourced the
methodology on GitHub. Google disputes the claim, stating the approach does not accurately
reverse-engineer SynthID.

Whether or not this specific claim is accurate, the episode illustrates the fundamental fragility
of watermark-based AI provenance systems: once an algorithm's behavior is observable at scale,
it can be modeled and subverted. Watermark removal and forgery are active research areas with
meaningful adversarial incentives.

Content authenticity systems should not rely solely on a single watermarking layer. C2PA
cryptographic metadata chains, model output logging, and provenance at the generation layer
provide stronger guarantees than perceptual watermarks alone.
