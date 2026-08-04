---
title: "Greatness PhaaS Adds Device Code Phishing to Bypass MFA and Steal Tokens"
date: 2026-08-04 17:27:39 +0000
categories: [Daily Signal]
tags: [phishing, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html
---

The commercial phishing-as-a-service toolkit Greatness has added device
code phishing, abusing the legitimate OAuth 2.0 Device Authorization
Grant to bypass MFA and seize control of accounts.

Greatness already supports adversary-in-the-middle (AiTM) credential and
session token theft, so this update gives its customers another route
past MFA protections. Organizations should watch for anomalous device
code authorization requests and restrict or conditional-access-gate the
device code flow where it isn't needed.
