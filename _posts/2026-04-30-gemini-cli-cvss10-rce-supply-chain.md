---
title: "Google Patches CVSS 10 Gemini CLI RCE Enabling Supply-Chain Code Execution"
date: 2026-04-30 07:07:00 +0000
categories: [Daily Signal]
tags: [rce, supply-chain, npm, github, google, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html
---

Google patched a maximum-severity (CVSS 10) vulnerability in Gemini CLI — the official `@google/gemini-cli` npm package and the `google-github-actions/run-gemini-cli` GitHub Actions workflow. The flaw allowed an unprivileged external attacker to force malicious content to load as Gemini configuration, enabling arbitrary command execution on host systems.

This is a supply-chain attack surface: any CI/CD pipeline consuming the official npm package or the GitHub Actions workflow was potentially exposed to remote code execution without privilege. Developers using either artifact should update immediately. Audit any recent pipeline runs that may have executed untrusted external content under Gemini configuration scope, and treat affected runner environments as potentially compromised.
