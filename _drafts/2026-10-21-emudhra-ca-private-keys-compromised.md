---
title: "Browsers Block eMudhra Intermediate CAs Over Recoverable Private Keys"
date: 2026-10-21 11:22:05 +0000
categories: [Daily Signal]
tags: [data-breach, vulnerability]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/browsers-block-emudhra-intermediate-cas-over-recoverable-private-keys/
---

Browsers and root certificate programs are blocking several eMudhra
intermediate certificate authorities after the private keys for eight
certificates were found to be recoverable and were compromised. Root trust
stores have moved to revoke trust in the affected CAs.

Organizations relying on certificates issued by the affected eMudhra
intermediates should check for renewal needs, as browsers may begin rejecting
them.
