---
title: "New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands"
date: 2026-07-29 07:47:19 +0000
categories: [Daily Signal]
tags: [rce, cve, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html
---

Gitea has patched a critical remote code execution vulnerability, tracked
as CVE-2026-60004 (CVSS 9.8), affecting self-hosted Gitea versions 1.17 and
later before 1.27.1. A user with only ordinary repository write access -
not an administrator - can craft patch content that gets turned into a live
Git hook, letting them run shell commands as the Gitea service account.
There is no indication of active exploitation in the wild. Gitea operators
should update to 1.27.1 and audit repository write permissions in the
meantime.
