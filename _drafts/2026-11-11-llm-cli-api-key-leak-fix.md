---
title: "llm 0.37.2 Patches API Key Leak to Third-Party Endpoints"
date: 2026-11-11 17:19:52 +0000
categories: [Daily Signal]
tags: [vulnerability, llm, appsec]
severity: medium
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Nov/11/llm/
---

The `llm` CLI tool shipped version 0.37.2, fixing a security issue
reported by Daniel de Araujo (GHSA-v9h7-jj4g-f862, GHSA-r639-rr7r-x72w).
The bug affects `llm`'s `extra-openai-models.yaml` mechanism for adding
OpenAI-compatible endpoints from other providers: under two
conditions — an unset `api_key_name`, or running a `responses: true`
model with `-o chat_completions 1` — the tool could send a user's
configured OpenAI API key to a different, unintended provider.

Users of `llm` with custom OpenAI-compatible endpoints should upgrade
to 0.37.2.
