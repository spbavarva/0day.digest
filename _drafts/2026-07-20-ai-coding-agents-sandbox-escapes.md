---
title: "AI Coding Agents Cursor, Codex, Gemini CLI Hit by Sandbox Escapes"
date: 2026-07-20 21:14:42 +0000
categories: [Daily Signal]
tags: [llm, appsec, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/
---

Security researchers escaped the sandboxes of four popular AI coding
agents — Cursor, Codex, Gemini CLI, and Antigravity — using a technique
where the AI agent writes files inside the sandbox that trusted host-side
tooling later reads and executes outside of it. The finding resulted in
multiple CVEs and vendor patches, though Google downgraded the severity of
two of the reported Antigravity issues. The pattern highlights a recurring
trust-boundary bug class in agentic coding tools: sandboxing the agent's
actions isn't sufficient if host tooling later trusts agent-written output.
