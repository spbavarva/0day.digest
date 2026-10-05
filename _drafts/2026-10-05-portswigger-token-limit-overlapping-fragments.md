---
title: "PortSwigger Research: Smashing the Token Limit With Overlapping Fragments"
date: 2026-10-05 15:04:55 +0000
categories: [Daily Signal]
tags: [appsec, vulnerability]
severity: medium
must_know: false
sources:
  - name: PortSwigger Research
    url: https://portswigger.net/research/smashing-the-token-limit
---

PortSwigger researchers published a technique for exfiltrating larger
tokens than previously demonstrated, by exploiting overlapping fragment
handling. The work was developed in collaboration with a fellow
PortSwigger researcher and builds on prior tooling like DOM Invader.
No specific target application or CVE was named in the available
summary. Teams building request-parsing or token-validation logic
should review PortSwigger's full writeup once the technical details
are public.
