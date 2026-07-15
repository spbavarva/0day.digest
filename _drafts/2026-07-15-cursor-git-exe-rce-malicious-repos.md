---
title: "Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution"
date: 2026-07-15 10:55:22 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html
  - name: SecurityWeek
    url: https://www.securityweek.com/unpatched-cursor-vulnerability-exposes-users-to-code-execution/
---

If a file named git.exe sits in the project root of a repository opened in
the Cursor editor on Windows, Cursor automatically executes it — no click,
approval dialog, or warning that anything in the folder is about to run.
The binary executes with the user's own permissions, including access to
SSH keys and cloud tokens, and Cursor keeps re-running it for as long as the
project stays open. The flaw was unpatched at the time of reporting.
