---
title: "EngageLab SDK Flaw Exposed 50 Million Android Users Including 30 Million Crypto Wallets"
date: 2026-04-09 17:26:00 +0000
categories: [Daily Signal]
tags: [supply-chain, vulnerability, cve, android]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/engagelab-sdk-flaw-exposed-50m-android.html
---

A now-patched critical vulnerability in EngageLab SDK, a widely used third-party Android SDK,
allowed apps on the same device to bypass Android's security sandbox and access private data
from co-installed applications. Approximately 50 million Android users were affected, including
30 million cryptocurrency wallet users whose private key material and account data were at risk.

Microsoft Defender researchers discovered and disclosed the flaw. The vulnerability's mechanism
let any app embedding the vulnerable SDK version gain unauthorized read access to data stored
by other apps — without requiring any additional permissions. Crypto wallet apps were a high-value
target given the financial sensitivity of the data involved.

Developers using EngageLab SDK should verify they have applied the patched version. Users of
apps that relied on the SDK should review account activity for signs of unauthorized access.
