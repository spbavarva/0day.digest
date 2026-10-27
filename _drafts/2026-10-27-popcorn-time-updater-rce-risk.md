---
title: "Dead Popcorn Time Updater Put Millions of Computers at Risk of Takeover"
date: 2026-10-27 09:44:50 +0000
categories: [Daily Signal]
tags: [supply-chain, vulnerability, rce]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/dead-popcorn-time-updater-put-millions-of-computers-at-risk-of-takeover/
---

An abandoned Popcorn Time updater component continued running at system
boot and periodically polling its update domain, ready to execute
whatever code was served with full system privileges. Because the
software was defunct, the update domain was unmonitored and could
theoretically have been taken over by an attacker to push malicious code
to all remaining installations.

The report doesn't indicate the domain was actually seized by a
malicious actor, but it highlights a latent supply-chain risk from
abandoned software with live update mechanisms. Anyone with Popcorn Time
still installed should remove it rather than assume it's dormant and
harmless.
