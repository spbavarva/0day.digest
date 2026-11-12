---
title: "Critical Red Hat Quay Flaw Lets Attackers Read and Overwrite All Private Container Images"
date: 2026-11-12 16:27:01 +0000
categories: [Daily Signal]
tags: [container-security, vulnerability, cve, supply-chain]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/critical-red-hat-quay-flaw-lets.html
---

A critical flaw in Red Hat Quay allows an attacker who can access a Quay
registry to read and overwrite private container images across every
repository in that registry. Quay enables anonymous access by default; if
anonymous access is left on, no account is required to exploit the flaw.

Even with anonymous access disabled, any user with a valid account can
still exploit it. Red Hat has released fixed builds for eight Quay
versions — teams running Quay should patch immediately and audit registry
access controls.
