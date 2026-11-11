---
title: "eMudhra Revokes 8 More CAs It Previously Declared Unaffected by Key Compromise"
date: 2026-11-11 12:00:53 +0000
categories: [Daily Signal]
tags: [vulnerability, data-breach]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/emudhra-revokes-8-more-cas-it.html
---

eMudhra has revoked 8 additional intermediate certificate authorities tied
to its October key-compromise incident, after previously stating those CAs
were unaffected. A flaw in a single line of the in-house script used to
generate the CAs is behind this second round of revocations.

Each intermediate CA has its own private signing key; the newly revoked
set did not have weakened keys but was still deemed to have a disqualifying
issue.

This is the second round of CA revocations stemming from the same
incident, raising questions about the scope of eMudhra's initial review.
