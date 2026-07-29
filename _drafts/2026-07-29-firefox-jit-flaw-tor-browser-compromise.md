---
title: "Patched Firefox JIT Flaw Used to Compromise Tor Browser via Single Webpage Visit"
date: 2026-07-29 11:57:00 +0000
categories: [Daily Signal]
tags: [rce, vulnerability, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/researchers-show-single-malicious.html
---

Researchers at Nebula Security disclosed CVE-2026-10702, a Firefox JIT
vulnerability that provides arbitrary code execution in the browser's
renderer process simply by visiting a malicious webpage, with no further
user interaction required. The bug was also used to compromise Tor Browser,
which is built on Firefox. Mozilla rated the flaw High severity and fixed
it in Firefox 151.0.3. Tor Browser users should confirm they are running a
version built on the patched Firefox release, given the anonymity-focused
browser is a higher-value target for this class of exploit.
