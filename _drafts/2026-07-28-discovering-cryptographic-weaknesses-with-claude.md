---
title: "Discovering Cryptographic Weaknesses With Claude"
date: 2026-07-28 22:45:37 +0000
categories: [Daily Signal]
tags: [anthropic, llm, ai-safety]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/#atom-everything
---

Anthropic researchers used Claude Mythos to find mathematical weaknesses in
both the HAWK cipher and a deliberately weakened version of AES, according
to a write-up highlighted by Simon Willison. Neither result has a practical
impact on current production systems, since the AES variant tested was
intentionally reduced in strength. The most notable part of the disclosure
is the shared prompting process, which required substantial iterative
guidance to get the model to attempt novel cryptanalysis rather than assume
the problem was unsolvable - a concrete data point on using frontier LLMs
as a cryptanalysis research aid.
