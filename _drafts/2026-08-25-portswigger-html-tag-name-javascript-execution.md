---
title: "What's in a Tag Name? JavaScript, Apparently"
date: 2026-08-25 14:24:32 +0000
categories: [Daily Signal]
tags: [xss, appsec]
severity: informational
must_know: false
sources:
  - name: PortSwigger Research
    url: https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently
---

PortSwigger's research team explored which characters browsers actually
accept in HTML tag names beyond the required a-zA-Z prefix, going past
commonly assumed character restrictions. The post walks through browser
parsing quirks that allow unexpected characters in tag names, which is
relevant to filter and sanitizer bypass techniques for XSS. The findings are
aimed at researchers building or evading HTML sanitization filters. See the
source for the full technical breakdown and affected browser behavior.
