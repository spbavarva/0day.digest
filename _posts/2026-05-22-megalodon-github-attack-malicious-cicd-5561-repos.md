---
title: "Megalodon GitHub Attack Injects Malicious CI/CD Workflows into 5,561 Repos"
date: 2026-05-22 11:55:24 +0000
categories: [Daily Signal]
tags: [supply-chain, github, malware, devsecops]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html
---

An automated campaign called Megalodon pushed 5,718 malicious commits to 5,561 GitHub repositories in a six-hour window. Throwaway accounts with forged bot identities (build-bot, auto-ci, ci-bot, pipeline-bot) injected GitHub Actions workflows containing base64-encoded bash payloads designed to exfiltrate CI/CD secrets. The scale and automation suggest a systematic, opportunistic supply chain poisoning operation. Repository owners should immediately audit recent CI/CD workflow additions and rotate any secrets that may have been exposed.
