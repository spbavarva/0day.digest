---
title: "Fake OpenAI Repository on Hugging Face Delivers Infostealer Malware"
date: 2026-05-09 14:26:03 +0000
categories: [Daily Signal]
tags: [malware, supply-chain, openai, hugging-face, phishing]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/fake-openai-repository-on-hugging-face-pushes-infostealer-malware/
---

A malicious Hugging Face repository impersonating OpenAI's "Privacy Filter" project reached the platform's trending list before being flagged, exposing a large number of visitors to Windows infostealer malware. Users who cloned and executed the repository may have had credentials, browser session tokens, and other locally stored secrets exfiltrated.

The incident is a textbook AI-platform supply chain attack: brand impersonation of a high-trust name (OpenAI) combined with social proof via trending placement to maximize downloads. Teams that clone Hugging Face repositories in dev or CI environments should audit recent activity and enforce repository allowlists or signature verification where possible.
