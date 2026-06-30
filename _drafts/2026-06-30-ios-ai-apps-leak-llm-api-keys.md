---
title: "282 iOS AI Chatbot Apps Found Leaking LLM API Keys"
date: 2026-06-30 13:49:34 +0000
categories: [Daily Signal]
tags: [vulnerability, llm, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/282-ios-apps-found-leaking-llm-api-keys.html
---

Researchers tested 444 AI chatbot apps for iPhone and found that 282 —
nearly two-thirds — exposed paid AI API access through their network
traffic. The exposure took the form of plaintext API keys, reusable
tokens, or backend servers accepting requests with no key at all. An
attacker who captures these credentials can send model requests billed to
the developer's account, abusing the underlying LLM access at the
developer's expense.
