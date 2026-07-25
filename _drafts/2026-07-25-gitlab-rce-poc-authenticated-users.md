---
title: "Researcher Publishes GitLab RCE PoC Letting Authenticated Users Run Commands as Git"
date: 2026-07-25 08:34:15 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/researcher-publishes-gitlab-rce-poc.html
---

Researcher Yuhang Wu (depthfirst) published a working PoC exploiting
unpatched self-managed GitLab 18.11.3 servers to execute commands as the
`git` user. The chain is triggered by an ordinary authenticated user
committing two crafted Jupyter notebooks and requesting their diff — no
admin rights or CI runner access required. Self-managed GitLab admins
should confirm patch status and review notebook-diff handling exposure.
