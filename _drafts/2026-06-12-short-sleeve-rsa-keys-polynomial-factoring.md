---
title: "Trail of Bits Finds 'Short-Sleeve' RSA Keys Factorable via Polynomial Attack"
date: 2026-06-12 11:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec]
severity: high
must_know: false
sources:
  - name: Trail of Bits
    url: https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/
---

Trail of Bits, working with Hanno Böck of the badkeys project, identified
hundreds of unique RSA keys in the wild whose private-key bits are heavily
biased toward 0 rather than randomly generated — a class of weak key they call
"short-sleeve" keys.

The bias is structured enough that the researchers developed a
polynomial-based factoring technique capable of recovering the private key
from the public key for affected keys.

They also identified the underlying bug responsible for generating many of
these weak keys and tracked the issue across historical key data.
Organizations should check their RSA keys against the badkeys database and
regenerate any keys that are flagged.
