---
title: "GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution"
date: 2026-10-02 17:33:31 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve, llm]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html
---

A critical flaw (CVSS 9.9) in GitLab's AI Gateway, the service that
connects a self-hosted GitLab instance to AI models, could let a
logged-in user with Duo Agent Platform access run commands on the
gateway under certain conditions.

Only organizations that host their own AI Gateway need to act. The flaw
is fixed in gateway versions 19.2.4, 19.3.2, and 19.4.1.
