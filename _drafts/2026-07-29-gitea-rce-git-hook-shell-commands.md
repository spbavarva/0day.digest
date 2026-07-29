---
title: "Critical Gitea RCE Lets Repository Writers Run Shell Commands via Git Hook"
date: 2026-07-29 07:47:19 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html
---

Gitea, the self-hosted Git platform, patched a critical remote code
execution vulnerability tracked as CVE-2026-60004 (CVSS 9.8). A user with
ordinary repository write access — not admin — can craft attacker-controlled
patch content that gets turned into a live Git hook, letting them run shell
commands as the Gitea service account. This makes the flaw exploitable by
any contributor with write access rather than requiring privileged access.
It affects Gitea versions 1.17 and later before 1.27.1, fixed in 1.27.1.
Administrators should upgrade and audit recent repository write activity
for signs of hook abuse.
