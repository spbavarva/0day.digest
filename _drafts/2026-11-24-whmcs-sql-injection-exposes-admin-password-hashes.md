---
title: "WHMCS SQL Injection Flaw Exposes Customer Data and Admin Password Hashes Without Login"
date: 2026-11-24 08:34:20 +0000
categories: [Daily Signal]
tags: [sqli, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/whmcs-sql-injection-flaw-could-expose.html
---

A SQL injection flaw in WHMCS's shopping cart module lets anyone on the
internet retrieve customer records and administrator password hashes from
an installation's database — no authentication required. WHMCS is widely
used by web hosting companies to run billing and automation.

The company disclosed the flaw alongside two additional issues that require
an authenticated client account. Hosting providers running WHMCS should
apply the available patch immediately.
