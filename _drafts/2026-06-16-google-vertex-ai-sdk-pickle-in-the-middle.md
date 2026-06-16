---
title: "Google Vertex AI SDK 'Pickle in the Middle' Flaw Allowed ML Model Hijacking via Bucket Squatting"
date: 2026-06-16 19:05:00 +0000
categories: [Daily Signal]
tags: [vulnerability, supply-chain, google, gcp, cloud-security, llm]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html
---

Unit 42 discovered a flaw in the Google Cloud Vertex AI SDK for Python enabling "Pickle in the Middle": an attacker with no access to a victim's project could preemptively register the cloud storage bucket Vertex AI expects for model uploads. Once the bucket is squatted, the victim's ML model upload lands in attacker-controlled storage, allowing arbitrary code execution inside Google's model-serving infrastructure via Python pickle deserialization. Google patched the issue through its bug bounty program; Unit 42 confirmed no exploitation in the wild. Teams using Vertex AI for custom model uploads should update to the latest SDK version and audit bucket naming conventions for predictable patterns.
