---
title: "Cloudflare Fixes Flaw Letting Containers Read Other Customers' Leftover Disk Data"
date: 2026-09-25 04:49:22 +0000
categories: [Daily Signal]
tags: [cloud-security, container-security, vulnerability]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/cloudflare-fixes-flaw-that-let-one.html
---

Cloudflare patched a flaw in its Containers product that let one paying
customer's container read data left behind by another customer's container
on the same server.

The exposed data came from disk space that earlier containers had used and
released, not from any live workload, and an attacker could not choose whose
leftover data they accessed, according to Cloudflare.

The source summary does not specify how long the flaw existed or how many
customers were affected.
