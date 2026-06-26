---
title: "Popular Chrome Ad Blocker With 10M+ Installs Found to Have Dormant Script Injection Capability"
date: 2026-06-25 14:12:52 +0000
categories: [Daily Signal]
tags: [supply-chain, vulnerability, xss]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html
---

Researchers at Island found that "Adblock for YouTube" (extension ID
cmedhionkhpnakcndndgjdbohmhepckk), a Chrome Web Store extension with a
Featured badge and more than 10 million installs, has the ability to
execute arbitrary JavaScript on pages it loads. This capability is not
part of the extension's advertised ad-blocking function and was found
dormant rather than actively triggered. Given the install base, this is a
notable browser-extension supply-chain risk — a malicious update or
remote-config flip could weaponize the capability against a large user
population with no new install required.
