---
title: "VS Code Zero-Day Lets Attackers Steal GitHub Tokens in One Click"
date: 2026-06-03 06:50:30 +0000
categories: [Daily Signal]
tags: [zero-day, vulnerability, github, microsoft]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/
---

A security researcher published working exploit code for an unpatched Visual Studio Code vulnerability that allows GitHub authentication token theft by tricking a user into clicking a single malicious link. The flaw abuses a URI handler in VS Code and requires no extensions or elevated privileges — only VS Code with an active GitHub session. GitHub tokens obtained this way grant full access to every repository and organization the victim can reach, making this a significant developer supply chain risk. Microsoft has not issued a patch; developers should treat unexpected VS Code URI links as phishing and avoid opening them from untrusted sources until a fix is available.
