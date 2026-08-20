---
title: "Spectre Attack Leaks JWTs From Co-Located Cloudflare Workers"
date: 2026-08-19 19:02:40 +0000
categories: [Daily Signal]
tags: [vulnerability, cloud-security, appsec]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html
---

Researchers disclosed a remote Spectre-class side-channel attack against
Cloudflare Workers that leaked a JSON Web Token from a co-located Worker
running in Cloudflare's production environment.

The leak rate reached up to 12 bits per second — roughly 360 times faster
than an earlier 2021 demonstration of the same attack class. The
end-to-end experiment used an attacker Worker and a victim Worker, both
controlled by the researchers, running on shared infrastructure.

The result shows Spectre-based cross-tenant leakage remains practical
against modern serverless/edge platforms, even at low bitrates. Teams
storing sensitive tokens in memory on multi-tenant edge compute should
track Cloudflare's response and mitigation guidance.
