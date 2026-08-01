---
title: "HollowFrame Loader Deploys Matryoshka Backdoor in Law Firm Spear-Phishing Attack"
date: 2026-07-31 16:39:31 +0000
categories: [Daily Signal]
tags: [malware, phishing]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html
---

Researchers at Blackpoint Cyber documented a previously undocumented
Go-based loader, HollowFrame, deploying a Rust-based backdoor family called
Matryoshka in a targeted attack on a law firm. The intrusion began with a
spear-phishing message linking to an encrypted archive containing a
malicious Windows Shortcut (LNK) file.

Executing the LNK triggers a multi-stage infection chain leading to backdoor
deployment. The use of two previously undocumented tooling families suggests
active development by the threat actor behind the campaign.
