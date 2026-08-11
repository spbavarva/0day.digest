---
title: "Mozilla Revokes Firefox and Thunderbird Linux Signing Key After Key Lands in Private Repo"
date: 2026-08-11 12:04:51 +0000
categories: [Daily Signal]
tags: [github, supply-chain, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/mozilla-revokes-firefox-and-thunderbird.html
---

Mozilla has revoked the cryptographic key used to sign Firefox and
Thunderbird downloads for Linux after discovering an unencrypted copy had
been mistakenly committed to one of its own private code repositories.
The key is what lets users and Linux distributions verify that a
downloaded browser tarball genuinely came from Mozilla and wasn't
tampered with. Mozilla has issued a new signing key; downstream packagers
will need to update accordingly.
