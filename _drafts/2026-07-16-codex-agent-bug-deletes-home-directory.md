---
title: "Codex Coding Agent Bug Can Delete a User's Home Directory"
date: 2026-07-16 17:45:59 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, openai]
severity: medium
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything
---

OpenAI has acknowledged reports of Codex, running on GPT-5.6, unexpectedly
deleting user files. The failure surfaces when Codex operates in full access
mode without sandboxing protections and with auto review disabled. In the
observed pattern, the model attempts to redirect the $HOME environment
variable to a temporary directory and instead deletes the real $HOME. The
bug was surfaced publicly by Thibault Sottiaux. Anyone running Codex or
similar coding agents in unsandboxed, full-access configurations should
treat this as a reminder to sandbox agent file operations.
