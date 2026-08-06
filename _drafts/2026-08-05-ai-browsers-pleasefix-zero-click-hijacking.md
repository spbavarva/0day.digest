---
title: "AI Browsers Vulnerable to 'PleaseFix' Zero-Click Agent Hijacking"
date: 2026-08-05 23:30:00 +0000
categories: [Daily Signal]
tags: [llm, appsec, vulnerability]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cyber-risk/ai-browsers-zero-click-agent-hijacking
  - name: Dark Reading
    url: https://www.darkreading.com/application-security/no-perfect-fix-ai-browser-prompt-injection-flaws
---

Researchers disclosed a class of zero-click attacks, dubbed PleaseFix, that
let attackers take control of AI browser agents through malicious
instructions hidden in content the browser is asked to process, with no
user interaction required.

Follow-up research found AI browsers from top vendors remain vulnerable to
prompt injection despite multiple layers of guardrails, and there is no
simple or complete fix for the underlying problem.

Organizations piloting AI browser agents should treat any content the agent
reads — web pages, emails, documents — as untrusted input capable of
issuing commands.
