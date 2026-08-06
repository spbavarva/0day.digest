---
title: "AWS, Google, and Vercel Patch Agent Flaws That Let Attackers Trigger Tools Without the Model"
date: 2026-08-06 08:57:30 +0000
categories: [Daily Signal]
tags: [llm, appsec, aws, google, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/aws-google-and-vercel-patch-agent-flaws.html
---

Security researchers disclosed flaws in agent infrastructure from AWS,
Google, and Vercel that allowed untrusted or forged instructions to reach an
agent's tools without any check that a model turn had actually authorized
the action.

In several of the attack paths, the underlying model never ran at all,
meaning system prompts, content filters, and model-level guardrails had no
opportunity to intervene.

All three vendors have patched the affected products. Teams building on
agent frameworks from these providers should confirm they're on patched
versions and review whether their own tool-invocation paths assume a model
turn always precedes execution.
