---
title: "Researchers Detail Novel XSS Technique: innerHTML Injection Without Equals Signs"
date: 2026-11-18 14:39:45 +0000
categories: [Daily Signal]
tags: [xss, appsec]
severity: medium
must_know: false
sources:
  - name: PortSwigger Research
    url: https://portswigger.net/research/achieving-the-impossible-xss-in-innerhtml-without-equals
---

PortSwigger Research published a new XSS technique from guest
researcher Masato Kinugawa showing how attackers can trigger script
injection via innerHTML assignment without using an equals sign, a
construct many sanitization and detection approaches assume is
required.

The technique matters for defenders building XSS filters or CSP-based
mitigations that pattern-match on common injection syntax, since it
exposes a gap in those assumptions.

Teams maintaining custom HTML sanitizers or WAF rules for XSS should
review whether their detection logic depends on the presence of an
equals sign in injected markup.
