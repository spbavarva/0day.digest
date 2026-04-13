---
title: "OpenAI Revokes macOS App Certificate After Axios Supply Chain Compromise"
date: 2026-04-13 06:50:00 +0000
categories: [Daily Signal]
tags: [supply-chain, openai, github, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html
---

A GitHub Actions workflow used to sign OpenAI's macOS applications pulled a malicious
version of the Axios library on March 31, part of a broader Axios supply chain
compromise. OpenAI detected the issue, revoked the affected code-signing certificate,
and states that no user data or internal systems were compromised.

The incident shows that CI/CD signing pipelines are high-value targets: a compromised
dependency at signing time can cascade into distribution of tampered binaries. Teams
using GitHub Actions for app signing should audit dependency pinning, enforce hash
verification or lockfiles, and restrict which workflow steps have access to signing
credentials. OpenAI has indicated it is hardening its certificate issuance process.
