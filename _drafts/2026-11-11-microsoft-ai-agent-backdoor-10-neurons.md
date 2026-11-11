---
title: "Microsoft Researchers Show AI Agents Can Be Backdoored by Editing Fewer Than 10 Neurons"
date: 2026-11-11 07:21:05 +0000
categories: [Daily Signal]
tags: [ai-safety, llm, vulnerability]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/microsoft-researchers-show-ai-agents.html
---

Microsoft researchers demonstrated that an AI model can be given a hidden
backdoor by editing fewer than 10 of its rarely used neurons, without
retraining the model. When a chosen trigger appears in the input, the
backdoored model outputs an attacker's command, which an agent using that
model would then execute with the agent's own permissions.

The attack requires the ability to modify the model's weights, which
limits it to scenarios involving a compromised model supply chain or a
malicious insider rather than a remote attacker.

This adds to a growing body of research on how agentic AI systems inherit
new attack surface from the models underneath them.
