---
title: "24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages"
date: 2026-08-25 11:52:43 +0000
categories: [Daily Signal]
tags: [npm, supply-chain, phishing]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html
---

Researchers disclosed a campaign using a cluster of 24 npm packages as free
phishing infrastructure, hosting fake Cloudflare CAPTCHA pages that redirect
to ClickFix-style social engineering flows. The malicious payload is a
single HTML page bundled inside each package — the threat actor isn't
trying to infect developers who install the packages, but is instead
abusing npm's public unpkg CDN mirror to host and distribute the phishing
page at no cost. This is a supply chain abuse pattern distinct from typical
malicious-package attacks: the registry becomes free hosting infrastructure
rather than a code-execution vector.
