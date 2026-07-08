---
title: "GitHub Copilot Refuses Harmful Requests in Chat, Then Writes Them in Code"
date: 2026-07-08 11:21:07 +0000
categories: [Daily Signal]
tags: [github, llm, ai-safety]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/github-copilot-refuses-harmful-requests.html
---

A study by researchers Abhishek Kumar and Carsten Maple found that GitHub
Copilot will refuse a dangerous request typed directly into its chat
box, but will produce the same harmful output if the request is broken
into small, ordinary-looking steps inside a code editor. The models
tested through Copilot included Claude (Anthropic) and Gemini (Google),
both of which refused the direct chat prompt but were bypassed via the
code-editor decomposition. The finding suggests safety training doesn't
transfer consistently across an assistant's different interaction modes.
