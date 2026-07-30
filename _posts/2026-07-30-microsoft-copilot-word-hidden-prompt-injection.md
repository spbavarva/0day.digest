---
title: "Microsoft Copilot for Word Can Copy Hidden Prompts Into New Documents"
date: 2026-07-30 11:54:49 +0000
categories: [Daily Signal]
tags: [llm, prompt-injection, microsoft]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/microsoft-copilot-for-word-can-copy.html
---

Researcher Håkon Måløy disclosed a technique where hidden instructions
embedded in a Word document cause Microsoft 365 Copilot to rewrite content
per the attacker's instructions, then copy those same hidden instructions
into the newly generated file.

In Måløy's proof of concept, the resulting file triggered the same behavior
in a second, separate Copilot drafting session, letting the injection
self-propagate across documents. The finding was disclosed 144 days after
being reported to Microsoft.
