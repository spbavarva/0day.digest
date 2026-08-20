---
title: "Simon Willison Tests smolmachines as a Sandbox for Untrusted LLM-Generated Code"
date: 2026-08-19 23:16:00 +0000
categories: [Daily Signal]
tags: [llm, appsec]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/
---

Simon Willison tasked Claude, running in Claude Code for web, with
evaluating smolmachines/smolvm as a fast, secure sandbox for executing
untrusted Python and JavaScript.

The goal was running user-provided code with limits on RAM and CPU time,
no network access, and filesystem access restricted to designated files —
a common requirement for agents that execute LLM-generated code for tasks
like data transformation.

This is relevant to teams building agentic tools that need to safely
execute model-generated code without full sandbox infrastructure.
