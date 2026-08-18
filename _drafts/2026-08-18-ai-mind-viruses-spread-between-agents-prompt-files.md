---
title: "AI 'Mind Viruses' Can Spread Between Agents Through Persistent Prompt Files"
date: 2026-08-18 12:38:36 +0000
categories: [Daily Signal]
tags: [ai-safety, llm, anthropic, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/ai-mind-viruses-can-spread-between.html
---

Researchers at Anthropic and EPFL demonstrated that self-propagating payloads
can spread between AI agents through the editable system prompt files that
agent harnesses use to carry state across sessions. The technique was tested
in a simulated six-agent coding environment, where an infected agent's prompt
file could pass the payload to peers it interacted with.

The work was released as a preprint on August 10, 2026. It highlights a novel
attack surface in multi-agent systems: shared or persistent prompt/state
files are effectively a writable channel a compromised agent can weaponize
against the rest of a fleet. Teams running multi-agent harnesses with shared
memory files should treat those files as untrusted input.
