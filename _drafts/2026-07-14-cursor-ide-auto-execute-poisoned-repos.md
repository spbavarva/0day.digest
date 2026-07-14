---
title: "Cursor IDE Auto-Executes Malicious Code in Poisoned Repos"
date: 2026-07-14 13:00:00 +0000
categories: [Daily Signal]
tags: [rce, ai-safety, appsec]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/application-security/cursor-ide-malicious-code-poisoned-repos
---

Researchers disclosed a vulnerability in the Cursor AI coding IDE that allows malicious code to auto-execute when a developer opens a poisoned repository. The flaw was reported to Cursor in December but reportedly remains unpatched, meaning the popular AI coding platform is still exploitable via crafted repositories. The attack requires no explicit action beyond opening the repo in Cursor, making it a real risk for developers who clone untrusted code. Until a fix ships, developers should avoid opening unfamiliar repositories directly in Cursor and use an isolated environment for first review.
