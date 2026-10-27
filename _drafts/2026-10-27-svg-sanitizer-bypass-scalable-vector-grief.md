---
title: "Researcher Bypasses Six of Eight Popular SVG Sanitizers"
date: 2026-10-27 14:29:26 +0000
categories: [Daily Signal]
tags: [xss, appsec, vulnerability]
severity: high
must_know: false
sources:
  - name: PortSwigger Research
    url: https://portswigger.net/research/scalable-vector-grief
---

PortSwigger Research tested eight popular SVG sanitizers and found
bypasses for six of them. The research shows how a crafted response
header can execute JavaScript in Firefox even when the response body
itself is harmless XML, sidestepping sanitization that only inspects the
body.

The technique highlights a blind spot in sanitizer design: validating
document content without accounting for how headers influence browser
parsing behavior. Teams relying on SVG sanitization for user-uploaded
content should review whether their sanitizer accounts for
response-header-driven content-type confusion.
