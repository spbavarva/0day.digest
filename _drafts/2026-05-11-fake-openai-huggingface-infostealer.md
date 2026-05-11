---
title: "Fake OpenAI Privacy Filter Repo Tops Hugging Face Trending, Delivers Infostealer"
date: 2026-05-11 07:05:00 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, openai, llm]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/fake-openai-privacy-filter-repo-hits-1.html
---

A malicious Hugging Face repository named `Open-OSS/privacy-filter` impersonated OpenAI's
legitimate `openai/privacy-filter` open-weight model, copying its description verbatim and
gaming the platform's trending algorithm to reach the #1 spot. The repository accumulated
244,000 downloads before detection, and delivered a Rust-based information stealer to
Windows users.

The attack demonstrates that AI model hosting platforms face the same typosquatting and
impersonation risks as package registries. Hugging Face does not currently enforce the same
publisher verification mechanisms as npm or PyPI. Any Windows system that downloaded from
`Open-OSS/privacy-filter` should be considered compromised and investigated for credential
and session-token theft. Organizations consuming Hugging Face models in automated pipelines
should pin by commit hash and verify publisher identity before ingestion.
