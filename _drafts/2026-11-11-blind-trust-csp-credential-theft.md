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

PortSwigger researchers detail a technique for turning HTML injection into
credential theft even when a page is protected by a Content Security
Policy. The attack works when a CSP allow-lists a third-party domain that
can itself be abused to exfiltrate data, defeating the protection the
policy is meant to provide.

This is a reminder that CSP allow-list entries are only as trustworthy as
what they host — a single permissive entry can reopen the credential-theft
path CSP was adopted to close. Teams should audit their CSP allow-lists for
domains capable of receiving attacker-controlled content or redirects.
