---
title: "Git Patches Flaw Allowing Code Execution via Recursive Clones"
date: 2026-11-10 19:23:10 +0000
categories: [Daily Signal]
tags: [rce, cve, vulnerability, github]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/git-patches-flaw-that-lets-malicious.html
---

A vulnerability in Git, tracked as CVE-2026-111760, can let a malicious
repository execute an attacker's code on a machine that recursively clones
it along with its submodules. The flaw is an integer truncation bug in how
Git handles its index. The Git project shipped fixes this week in Git
2.56.1, with matching backports for the 2.50 through 2.55 series. Anyone
who recursively clones untrusted repositories, including in CI pipelines,
should update immediately.
