---
title: "Placeholder third-party[.]com Domain Referenced in 1,700+ Repos Now Serves Malicious Content"
date: 2026-09-24 15:27:32 +0000
categories: [Daily Signal]
tags: [phishing, supply-chain, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/placeholder-third-partycom-referenced.html
---

The domain third-party[.]com, long used as a generic documentation
placeholder — filling the same role as example.com — has been observed
serving a ClickFix malware lure to Windows browsers.

According to Manifold Security's Ax Sharma, the domain shows a harmless
decoy page to non-Windows visitors while serving the malicious lure to
Windows users.

The domain is referenced across more than 1,700 public repositories,
meaning any live code, config, or documentation still pointing at it
could now expose users to malware. Unlike example.com, third-party[.]com
was never reserved as a non-resolving placeholder.
