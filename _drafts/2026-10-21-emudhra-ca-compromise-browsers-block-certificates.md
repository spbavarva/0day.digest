---
title: "Mozilla, Google, Apple Block Compromised eMudhra Intermediate CA Certificates"
date: 2026-10-21 00:46:42 +0000
categories: [Daily Signal]
tags: [vulnerability, certificate-authority, appsec]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/
  - name: Simon Willison
    url: https://simonwillison.net/2026/Oct/20/emudhra-certificates/
---

Researchers found that the private keys for eight eMudhra intermediate CA
certificates were recoverable almost instantly due to weak cryptography,
letting anyone who found them forge trusted certificates for arbitrary
websites. The certificates chain to roots trusted by Mozilla, Microsoft,
Apple, and Chrome, so the exposure extends to any software bundling those
trust stores. eMudhra revoked the eight certificates, and the major
browsers have moved to block them in their root programs.

Linux distros need to update their ca-certificates packages; in the Python
ecosystem, uv 0.13.4, pip 26.2.2, and certifi 2026.10.19 ship updated
certificate lists. Treat this as a credential compromise at the CA level
and apply trust-store updates promptly.
