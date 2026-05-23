---
title: "Google AI Search Interprets 'Disregard' as a Prompt Injection Instruction"
date: 2026-05-22 16:01:17 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, prompt-injection]
severity: medium
must_know: false
sources:
  - name: The Verge AI
    url: https://www.theverge.com/tech/936176/google-ai-overviews-search-disregard
---

Google's AI Overviews feature is treating the search query "disregard" as an instruction override, returning chatbot-style responses instead of web search results. The term appears to trigger an LLM instruction-following behavior in the AI layer rather than being processed as a literal search token. The incident is a real-world demonstration of prompt injection risk in LLM-augmented interfaces: user-controlled input reaching an LLM can alter the system's intended behavior. Google had not issued a fix as of publication; the behavior was widely reproduced.
