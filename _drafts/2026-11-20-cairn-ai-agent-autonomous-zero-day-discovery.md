---
title: "Chinese-Nexus Actor's Autonomous AI Agents Found a Zero-Day on Their Own"
date: 2026-11-20 17:30:13 +0000
categories: [Daily Signal]
tags: [zero-day, llm, malware, vulnerability]
severity: critical
must_know: true
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/
---

Amazon Threat Intelligence investigated a Chinese-nexus threat actor that
gave autonomous AI agents, built on the open-source Cairn penetration-testing
framework, a single goal: obtain shell access to a target.

With minimal human involvement, the agents discovered a previously unknown
vulnerability in an open-source application and used it to gain full access
to the target system.

Separate reporting ties the same Cairn-based campaign to attacks on at least
two universities, with one case possibly involving the same zero-day. This
is one of the more concrete examples yet of an AI agent autonomously finding
and weaponizing a zero-day rather than just assisting a human operator.

Amazon has not named the vulnerable application. Organizations running
autonomous AI red-team or pentest tooling should treat agent-discovered
findings with the same urgency as human-reported ones.
</content>
