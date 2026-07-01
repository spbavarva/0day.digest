---
title: "Azure CLI Password Spray Campaign Tops 81 Million Login Attempts"
date: 2026-07-01 05:46:03 +0000
categories: [Daily Signal]
tags: [azure, cloud-security, iam]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
---

Huntress reports a large-scale, automated password-spray campaign against
Microsoft's Azure CLI, generating more than 81 million login attempts
between June 12 and June 26 and compromising at least 78 accounts. The
traffic originates from an IPv6 range controlled by hosting provider LSHIY
LLC (AS32167). The scale and automation suggest a broad credential-stuffing
operation rather than a targeted attack. Azure customers should review
sign-in logs for the affected IP range and enforce MFA on CLI-capable
accounts if not already required.
