---
title: "Opera GX Flaw Let Malicious Sites Auto-Install Mods to Steal Data From Visited Pages"
date: 2026-07-06 07:27:50 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/opera-gx-flaw-let-malicious-sites-auto.html
---

Researchers found a flaw in Opera GX, the gaming-focused version of the
Opera browser, that let a malicious website silently install a browser
add-on and use it to read data from pages the victim later visits, with no
click required. In a proof of concept, they reconstructed a signed-in user's
full Gmail address from a single site visit. Opera has patched the issue and
says it has found no evidence of in-the-wild exploitation. The bug is
notable for being a zero-click, cross-site data exposure triggered purely by
visiting a malicious page.
