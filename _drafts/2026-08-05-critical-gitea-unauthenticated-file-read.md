---
title: "Critical Gitea Flaw Let Unauthenticated Attackers Read Server Files via Org-Mode Markup"
date: 2026-08-05 11:04:23 +0000
categories: [Daily Signal]
tags: [cve, vulnerability, appsec]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/critical-gitea-flaw-let-unauthenticated.html
---

An unauthenticated attacker can read any file the service account can
access on Gitea, the self-hosted Git platform, in versions 1.22.1 through
1.27.0. No login and no repository write access are required — a public
repository and crafted Org-mode markup are enough.

The flaw is tracked as CVE-2026-59774 (CVSS 9.8) and is fixed in Gitea
1.27.1. Self-hosted Gitea instances with any public repositories should
patch immediately.
</content>
