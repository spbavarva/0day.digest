---
title: "Polyfill Supply Chain Attack Surfaces Credential-Harvesting Prompts on Toshiba and Muji Sites"
date: 2026-06-05 21:54:42 +0000
categories: [Daily Signal]
tags: [supply-chain, phishing, xss]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/
---

Toshiba and Muji have warned visitors that unexpected sign-in screens appearing on their websites are linked to polyfill script injections and may be harvesting credentials. Both companies flagged the issue after customers reported suspicious prompts on otherwise legitimate pages. Web teams should audit all third-party JavaScript dependencies — particularly any CDN-hosted polyfill scripts — and replace with self-hosted equivalents. End users should be advised not to enter credentials on unexpected prompts and to verify site authenticity before logging in. The continued appearance of polyfill-related attacks on major brand sites indicates many organizations have not yet remediated compromised script includes.
