---
title: "VS Code Vulnerability Enables One-Click GitHub Token Theft via Extensions"
date: 2026-06-04 08:14:52 +0000
categories: [Daily Signal]
tags: [vulnerability, github, cve]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/vs-code-vulnerability-allows-one-click-github-token-theft/
---

A researcher disclosed full details and a public PoC for a VS Code
vulnerability that allows a malicious extension to steal a developer's GitHub
access token with a single user interaction — without notifying Microsoft in
advance. A stolen token could grant access to private repositories, GitHub
Actions pipelines, and any service that trusts it for authentication. VS Code
extensions are commonly auto-installed through project recommendation files
(`.vscode/extensions.json`), broadening the attack surface. Developers should
audit installed extensions, prefer verified-publisher extensions only, and
rotate any GitHub personal access tokens that may have been exposed.
