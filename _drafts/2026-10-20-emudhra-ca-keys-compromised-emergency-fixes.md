---
title: "Eight eMudhra CA Keys Compromised, Triggering Emergency Fixes Across Browsers and Go"
date: 2026-10-20 17:09:53 +0000
categories: [Daily Signal]
tags: [vulnerability, pki]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html
---

The private keys of eight eMudhra intermediate certificate authority (CA)
certificates are compromised, Mozilla and Google's Chrome Root Program
confirmed on October 20. An intermediate CA key lets anyone holding it issue
a certificate for any website that browsers would trust.

Go shipped emergency releases (1.27.3 and 1.26.10) that make its certificate
verifier reject any chain passing through the affected keys; browser vendors
are expected to follow with similar distrust actions. The identity of the
affected certificate authority was not disclosed at time of writing.
