---
title: "VS Code Vulnerability Enables One-Click GitHub Token Theft"
date: 2026-06-04 08:14:52 +0000
categories: [Daily Signal]
tags: [vulnerability, github, microsoft]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/vs-code-vulnerability-allows-one-click-github-token-theft/
  - name: The Record (Recorded Future)
    url: https://therecord.media/researcher-publishes-github-token-stealing-exploit-microsoft
---

Researcher Ammar Askar published full technical details and a proof-of-concept exploit for a VS Code vulnerability that allows stealing a victim's GitHub authentication token with a single click. The researcher gave Microsoft approximately one hour's notice before public disclosure, citing frustration with the disclosure process. Developers using VS Code with GitHub integration should apply available patches immediately and rotate any GitHub tokens that may have been accessible from affected installations.
