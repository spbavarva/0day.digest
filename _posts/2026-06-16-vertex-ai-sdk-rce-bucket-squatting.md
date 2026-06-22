---
title: "Vertex AI Python SDK Flaw Allows Cross-Tenant RCE via Bucket Squatting"
date: 2026-06-16 10:00:29 +0000
categories: [Daily Signal]
tags: [rce, cloud-security, gcp, vulnerability, llm]
severity: high
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/
---

Unit 42 disclosed a vulnerability in the Vertex AI Python SDK where predictable GCS bucket naming allows an attacker to pre-claim a bucket and inject a malicious pickle file. When a victim loads a model from Vertex AI, Python's pickle deserialization executes the attacker's payload with the victim's permissions. The attack enables cross-tenant remote code execution in shared Vertex AI environments — an attacker in one GCP tenant can affect users in another. The pickle deserialization vector is well-understood, but its application in a cloud ML context with multi-tenant blast radius is a significant elevation. AI/ML teams using Vertex AI should validate bucket ownership and avoid loading models from shared or untrusted sources.
