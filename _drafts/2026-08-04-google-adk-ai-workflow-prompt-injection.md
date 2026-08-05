---
title: "Google Deletes 3 ADK AI Workflows After Malicious GitHub Issue Could Trigger Privileged Agent"
date: 2026-08-04 11:16:23 +0000
categories: [Daily Signal]
tags: [llm, privilege-escalation, ai-safety, google]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/google-deletes-3-adk-ai-workflows-after.html
---

Google removed three AI agent workflows from its Agent Development Kit
(ADK) Python repository after Pillar Security showed that a public
GitHub issue could manipulate a low-privilege triage agent into
invoking a privileged code-fixing agent.

The researchers prompt-injected the public-facing agent into posting a
"/adk-issue-fix" comment as the adk-bot account, which the bot's
collaborator status treated as authorized. Teams building multi-agent
workflows should treat any user-controllable input reaching a
privileged agent as an injection vector, not just direct chat prompts.
