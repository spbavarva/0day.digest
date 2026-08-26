---
title: "Hackers Abuse npm Mirrors to Host Phishing Redirect Pages"
date: 2026-08-25 21:39:01 +0000
categories: [Daily Signal]
tags: [npm, phishing, supply-chain]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/hackers-abuse-npm-mirrors-to-host-phishing-redirect-pages/
---

Threat actors are abusing npm and its public mirrors to host malicious HTML
pages that impersonate Cloudflare CAPTCHA challenges. Visitors who land on
these pages are redirected to attacker-controlled sites.

Because the pages are served from trusted npm mirror infrastructure, they
can evade domain-reputation filtering that would otherwise flag a
newly-registered phishing domain.
