---
title: "Project Glasswing: Anthropic's AI Model Restricted Due to Autonomous Vulnerability Discovery"
date: 2026-04-23 11:30:00 +0000
categories: [Daily Signal]
tags: [anthropic, ai-safety, llm, vulnerability, appsec]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/project-glasswing-proved-ai-can-find.html
---

Anthropic announced Project Glasswing, built on the Mythos Preview model, which proved so
effective at autonomously discovering software vulnerabilities that the company delayed its public
release. Instead of open access, Anthropic gave the model to Apple, Microsoft, Google, Amazon, and
a coalition of technology companies for coordinated pre-disclosure bug finding and patching. The
model reportedly found real vulnerabilities during its controlled deployment period.

This establishes a new pattern for offensive-capable AI systems: "responsible AI capability
disclosure" analogous to responsible disclosure in traditional vulnerability research. The
precedent has significant implications for how AI labs should handle models that reach a threshold
of autonomous vulnerability discovery capability — releasing such a model publicly without
coordination could provide immediate offensive uplift before defenders patch the findings.
