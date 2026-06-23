---
title: "Research Frames Prompt Injection as Role Confusion"
date: 2026-06-22 23:59:53 +0000
categories: [Daily Signal]
tags: [ai-safety, llm]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything
---

New research from Charles Ye, Jasmine Cui, and Dylan Hadfield-Menell frames
prompt injection as a role-confusion problem: models struggle to reliably
distinguish their own privileged text (wrapped in tags like `<system>`,
`<think>`, `<assistant>`) from untrusted input wrapped in `<user>` tags.
Framing the issue this way ties prompt injection to a structural weakness in
how LLMs process role-tagged context, rather than treating each injection as
a one-off prompt-engineering trick. The paper is accompanied by a more
accessible blog-style writeup covering the same findings.
