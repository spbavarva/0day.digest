---
title: "Over 16,000 Misconfigured Supabase Databases Expose PII, Passwords, Auth Tokens"
date: 2026-09-28 18:50:59 +0000
categories: [Daily Signal]
tags: [cloud-security, data-breach, appsec]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/misconfigured-supabase-apps-expose-data-in-over-16-000-databases/
---

Researchers found more than 16,000 misconfigured Supabase databases
with readable tables exposing personally identifiable information,
passwords, and authentication tokens, according to BleepingComputer.

The exposures stem from misconfiguration on the customer side rather
than a Supabase platform vulnerability. Teams running Supabase should
review row-level security and access policies on production tables.
