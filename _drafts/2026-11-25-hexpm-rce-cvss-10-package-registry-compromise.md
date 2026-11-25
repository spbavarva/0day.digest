---
title: "Attacker Exploits 10-Year-Old CVSS 10.0 Hex.pm Flaw to Compromise Package Registry Servers"
date: 2026-11-25 09:06:59 +0000
categories: [Daily Signal]
tags: [supply-chain, rce, cve, vulnerability]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/hackers-exploited-cvss-100-hexpm-rce.html
---

An attacker ran operating system commands on six production servers of
Hex.pm, the package registry that Elixir and Erlang developers use to fetch
dependencies. The exploited flaw, rated CVSS 10.0, had existed in the
registry's code since February 2016.

The Hex.pm team got every affected server onto a patched build within about
15 minutes of the first malicious request. Given the scale of the Elixir and
Erlang ecosystem's reliance on the registry, this was a direct supply chain
compromise of shared infrastructure, not an isolated application bug.
