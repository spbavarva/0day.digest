---
title: "PortSwigger Turns HTTP Header Injection Critical With a Single Prompt"
date: 2026-11-04 15:12:29 +0000
categories: [Daily Signal]
tags: [appsec, vulnerability]
severity: medium
must_know: false
sources:
  - name: PortSwigger Research
    url: https://portswigger.net/research/making-http-header-injection-critical-with-one-prompt
---

PortSwigger researchers detailed a technique for escalating HTTP header
injection into a CRLF-powered desync attack capable of serving a redirect
to an attacker-controlled Collaborator endpoint. The technique can now be
triggered via a single Burp Scanner prompt, and PortSwigger has shipped a
new scan check for it.

This lowers the bar for finding and demonstrating impact of header
injection bugs that were previously treated as low severity.
