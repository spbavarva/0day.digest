---
title: "101 Malicious npm Packages Add Developers to WhatsApp Groups Without Consent"
date: 2026-09-29 13:45:10 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/101-malicious-npm-packages-add.html
---

OX Security researchers identified a cluster of 101 npm packages, dubbed
PhantomSub, that abuse the open-source "Baileys" WhatsApp library to add
developers to WhatsApp groups without their consent. The campaign appears
aimed at building subscriber lists rather than delivering destructive
payloads. Developers who installed affected packages should audit their
WhatsApp account for unexpected group memberships and review dependencies
pulling in Baileys-based packages from untrusted sources.
