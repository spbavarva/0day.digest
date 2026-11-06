---
title: "Experts Demonstrate Barracuda Email Security Gateway Chain Enabling Root Access Without Login"
date: 2026-11-06 05:39:10 +0000
categories: [Daily Signal]
tags: [rce, privilege-escalation, vulnerability, cve]
severity: critical
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/experts-demonstrate-barracuda-email.html
---

Two flaws in Barracuda's Email Security Gateway can be chained to let an
unauthenticated attacker run commands as root, the appliance's highest
privilege level. One of the flaws, CVE-2026-116606, is an authorization
bypass that lets an attacker restore access without logging in.

Barracuda released patches on Monday, and security firm watchTowr detailed
the full attack chain on Thursday. Organizations running the Email
Security Gateway should confirm patches are applied immediately given the
no-login requirement.
