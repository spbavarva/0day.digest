---
title: "OpenAI Agents SDK Adds Native Sandbox Execution and Model-Native Harness"
date: 2026-04-15 10:00:00 +0000
categories: [Daily Signal]
tags: [llm, openai, appsec]
severity: medium
must_know: false
sources:
  - name: OpenAI Blog
    url: https://openai.com/index/the-next-evolution-of-the-agents-sdk
---

OpenAI has released a major update to its Agents SDK introducing native sandbox execution and a
model-native harness for building long-running agents that operate across files and tools. The
update targets enterprise developers building secure, persistent agent pipelines.

Native sandbox execution is the most security-relevant addition: it constrains an agent's blast
radius by limiting what tools, filesystem paths, and network resources it can access during a
run. The model-native harness standardizes tool interaction in ways that reduce opportunities
for prompt injection through inconsistent tool handling—a significant source of AI agent
vulnerability in earlier frameworks.

Developers building on the OpenAI Agents SDK should upgrade and review sandbox configuration
options to determine appropriate constraints for their deployment. The SDK documentation covers
tool permission scoping and execution boundary settings.
