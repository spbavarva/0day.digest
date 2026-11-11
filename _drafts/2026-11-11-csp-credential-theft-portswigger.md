---
title: "Blind Trust: Stealing Credentials Through CSP"
date: 2026-11-11 14:26:01 +0000
categories: [Daily Signal]
tags: [xss, appsec, vulnerability]
severity: medium
must_know: false
sources:
  - name: PortSwigger Research
    url: https://portswigger.net/research/blind-trust-stealing-credentials-through-csp
---

PortSwigger Research details a technique for stealing credentials by
abusing Content Security Policy (CSP) allow-lists. CSP is meant to stop
HTML injection from escalating into full XSS, but when a policy
allow-lists a domain that can itself be abused, that trust can be
turned against the site.

Appsec teams should audit their CSP allow-lists for third-party domains
that could be leveraged by an attacker to defeat the policy's intent.
