---
title: "GoBalance Flaw Lets Attackers Hijack .onion Addresses via Tor Key Recovery"
date: 2026-10-09 09:03:24 +0000
categories: [Daily Signal]
tags: [vulnerability, tor]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/gobalance-flaw-lets-attackers-hijack.html
---

A flaw in GoBalance, a tool many dark-web sites use to stay reachable during
attacks, lets anyone compute the secret key that controls a site's .onion
address using only publicly available information, then take that address
over.

Searchlight Cyber, which disclosed the flaw on October 8, says an attacker
who recovers the key can redirect a site's visitors to a copy of the site
under the attacker's control.
