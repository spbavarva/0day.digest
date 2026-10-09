---
title: "GoBalance Flaw Lets Attackers Recover Tor Keys and Hijack .onion Addresses"
date: 2026-10-09 09:03:24 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/gobalance-flaw-lets-attackers-hijack.html
---

A flaw in GoBalance, a load-balancing tool many dark-web sites use to stay
reachable during DDoS attacks, lets anyone recover the secret key
controlling a site's .onion address using only publicly available
information, according to Searchlight Cyber, which disclosed the bug
October 8.

An attacker who recovers the key can take over the .onion address and
redirect the site's visitors to a lookalike page they control, enabling
phishing or credential theft against the original site's users.

The flaw undermines a core assumption of Tor hidden services — that only
the legitimate operator can control a given .onion address — for any site
relying on GoBalance for resilience.
