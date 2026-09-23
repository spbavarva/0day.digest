---
title: "Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI"
date: 2026-09-23 13:52:46 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, pypi, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html
---

Threat actors compromised two legitimate MemTensor packages —
distributed across both the npm and PyPI registries — to push a
cross-platform Go-based implant dubbed "sckit," targeting Windows,
Linux, and macOS. The compromise was identified by multiple firms,
including Aikido, SafeDep, Socket, and StepSecurity.

The affected package includes
@memtensor/memos-cloud-openclaw-plugin. Consumers of MemTensor
packages on npm or PyPI should audit installed versions and rotate
any credentials that may have been exposed.
