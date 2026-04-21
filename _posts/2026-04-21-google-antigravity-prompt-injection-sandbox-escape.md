---
title: "Google Antigravity AI IDE: Prompt Injection Chained to Sandbox Escape and Code Execution"
date: 2026-04-21 10:22:00 +0000
categories: [Daily Signal]
tags: [llm, rce, appsec, ai-safety, vulnerability, google]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html
  - name: Dark Reading
    url: https://www.darkreading.com/vulnerabilities-threats/google-fixes-critical-rce-flaw-ai-based-antigravity-tool
---

Google's AI-native IDE Antigravity contained a vulnerability that chained prompt injection with
insufficient input sanitization in the built-in `find_by_name` file-searching tool to escape the
program's strict-mode sandbox and achieve arbitrary code execution. No user interaction was
required beyond the IDE processing a malicious file.

The attack pattern is a concrete example of the emerging agentic security risk class: when an
LLM agent is granted filesystem or tool access, insufficient sanitization of any tool's input
can become an OS-level code execution primitive. Antigravity's case is notable because the
sandbox was explicitly designed to prevent this — yet a single insufficiently validated tool call
undermined it.

Google has patched the flaw. Developers using AI-native IDEs or building agentic tools with
filesystem access should treat every tool call as a potential injection surface. This vulnerability
pattern is highly likely to recur in other AI-assisted development environments.
