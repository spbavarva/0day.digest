---
title: "Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify, and Other Apps for API Keys"
date: 2026-11-16 07:34:21 +0000
categories: [Daily Signal]
tags: [llm, aws, agentic-ai]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html
---

Amazon's threat intelligence team used decoy servers to capture records of
attacker-run AI agents hunting for weak spots in internet-exposed AI apps,
including LiteLLM, One API, and Dify. The agents searched for AI provider
API keys stored inside these self-hosted apps.

Once stolen, the keys were used to run AI models that powered further
searches for additional keys, creating a self-sustaining attack loop.
