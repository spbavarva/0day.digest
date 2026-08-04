---
title: "How Legitimate Cloud Platforms Enable Phishers to Bypass MFA"
date: 2026-08-04 12:00:12 +0000
categories: [Daily Signal]
tags: [phishing, cloud-security]
severity: medium
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/cloud-platforms-in-phishing/120832/
---

Securelist details an adversary-in-the-middle (AitM) phishing scenario
that leverages service workers and the Ultraviolet proxy toolkit,
hosted on legitimate cloud platforms including Cloudflare Workers,
Vercel, Netlify, GitHub Pages, and IPFS.

Hosting phishing infrastructure on trusted platforms helps attackers
evade domain reputation and blocklist-based defenses. Defenders should
extend AitM and session-token-theft detection to cover traffic proxied
through these legitimate hosting services.
