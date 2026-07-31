---
title: "Device Code Phishing Emerges as a Fast-Growing OAuth Abuse Technique"
date: 2026-07-31 11:24:59 +0000
categories: [Daily Signal]
tags: [phishing, iam]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/6-reasons-why-device-code-phishing-is.html
---

Abuse of the OAuth 2.0 device authorization grant — designed for
input-constrained devices like smart TVs and printers — has moved from a
niche red-team technique to an increasingly common attack path over the
past six months.

The flow's broad adoption across apps that weren't originally built for
constrained-input scenarios has widened the attack surface for token theft.
Attackers use the technique to trick users into approving a device login
that hands over a valid access token. Organizations allowing device code
flow should restrict it to genuinely input-constrained scenarios and
monitor for anomalous device authorization requests.
