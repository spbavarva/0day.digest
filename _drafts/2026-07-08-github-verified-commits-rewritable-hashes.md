---
title: "GitHub 'Verified' Commits Can Be Rewritten Into New Hashes Without Breaking Signatures"
date: 2026-07-08 11:51:24 +0000
categories: [Daily Signal]
tags: [github, supply-chain, appsec]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/github-verified-commits-can-be.html
---

New research shows that a signed Git commit's hash is not the unique
identifier the software supply chain assumes it to be. Given any signed
commit, someone without the signing key can mint a second commit with the
same files, author, and date that carries a different hash but still
displays "Verified" on GitHub. Everything a reviewer would normally check
matches except the hash itself. Teams that pin dependencies or releases
by commit hash should be aware hash-based pinning alone doesn't guarantee
the content a signature originally attested to.
