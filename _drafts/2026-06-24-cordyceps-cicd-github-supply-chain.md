---
title: "Cordyceps CI/CD Flaws Expose 300+ GitHub Repositories to Supply-Chain Attacks"
date: 2026-06-24 12:48:11 +0000
categories: [Daily Signal]
tags: [supply-chain, github, vulnerability, cve]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/cordyceps-cicd-flaws-expose-300-github.html
  - name: SecurityWeek
    url: https://www.securityweek.com/exploitable-ci-cd-vulnerabilities-expose-millions-of-repositories-to-hijacking/
---

Researchers at Novee Security disclosed a new class of CI/CD workflow
weakness, codenamed Cordyceps, that lets attackers hijack GitHub Actions
workflows and gain full control of affected repositories. The "critical
exploitable pattern" reportedly impacts 300+ repositories at major
organizations including Microsoft, Google, and Apache. The flaw class
threatens the open-source supply chain broadly, since compromised CI/CD
pipelines can be used to inject malicious code into downstream builds.
