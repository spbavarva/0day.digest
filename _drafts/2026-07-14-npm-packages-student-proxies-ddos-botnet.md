---
title: "148 npm Packages Disguised as Student Proxies Turned Browsers Into a DDoS Botnet"
date: 2026-07-14 07:08:36 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/148-npm-packages-disguised-as-student.html
---

JFrog researchers identified a campaign of 148 npm packages disguised as student web proxies that turned visitors' browsers into a distributed denial-of-service botnet for roughly two weeks in May. Rather than targeting developers who installed the packages, the operators used the npm registry as free hosting for a booby-trapped proxy website aimed at students trying to bypass network restrictions. Visitors to the proxy site had their browsers silently conscripted into the DDoS botnet. The campaign illustrates a supply chain abuse pattern where npm is used as hosting infrastructure rather than as a distribution vector for malicious code.
