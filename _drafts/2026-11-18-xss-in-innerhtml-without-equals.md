---
title: "PortSwigger Research: XSS in innerHTML Without Using the Equals Sign"
date: 2026-11-18 14:39:45 +0000
categories: [Daily Signal]
tags: [xss, appsec]
severity: medium
must_know: false
sources:
  - name: PortSwigger Research
    url: https://portswigger.net/research/achieving-the-impossible-xss-in-innerhtml-without-equals
---

PortSwigger published new web security research, contributed by guest
researcher Masato Kinugawa, demonstrating a technique for achieving
cross-site scripting through innerHTML assignment without using the equals
sign — a case previously assumed to be safe from this class of injection.

The finding matters for anyone building sanitizers or filters that assume
equals-sign-based assignment is the only path to innerHTML-driven XSS.
