---
title: "Critical GitLab Flaw (CVSS 10.0) Allows Unauthenticated RCE Across 12 Years of Releases"
date: 2026-10-21 18:57:34 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html
---

GitLab released fixes on October 21 for a critical, unauthenticated remote
code execution flaw (CVSS 10.0) affecting every version of GitLab going back
to 7.0, released in 2014 — roughly 12 years of releases. The flaw lets an
attacker run code on a self-managed server without logging in.

Administrators who patched nine days earlier are still exposed: the October
12 update only covered versions 19.2 and later, while the newly fixed
versions sit one patch above it.
