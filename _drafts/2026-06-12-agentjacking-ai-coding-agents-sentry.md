---
title: "'Agentjacking' Attack Tricks AI Coding Agents Into Running Malicious Code via Fake Sentry Error Reports"
date: 2026-06-12 12:04:33 +0000
categories: [Daily Signal]
tags: [llm, rce, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html
---

Researchers at Tenet Security disclosed "Agentjacking," described as a new
class of attack that tricks AI coding agents into running arbitrary code on
developer machines.

The attack is triggered via a fake error report crafted using Sentry, the
open-source error-tracking and performance-monitoring platform. When an AI
coding agent processes the malicious report — for example, while autonomously
triaging or fixing bugs — it can be manipulated into executing
attacker-controlled code.

Teams that give AI coding agents access to error-tracking tools or other
external inputs should review what those agents are permitted to act on
automatically, and treat ingested error reports as untrusted input.
