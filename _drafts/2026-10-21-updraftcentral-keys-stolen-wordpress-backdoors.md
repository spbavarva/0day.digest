---
title: "Stolen UpdraftCentral Keys Used to Backdoor WordPress Sites"
date: 2026-10-21 09:01:12 +0000
categories: [Daily Signal]
tags: [supply-chain, wordpress, credential-theft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/attackers-abuse-updraftcentral-keys-to.html
---

Attackers breached the website of TeamUpdraft, the developer behind the
UpdraftPlus WordPress backup plugin (4M+ active installs), and
potentially obtained customer connection keys for UpdraftCentral,
UpdraftVault, and UpdraftClone. UpdraftCentral is a remote management
service that can send commands to connected WordPress sites, and the
stolen keys were used to plant backdoors on sites managed through it.

Site owners using UpdraftCentral should rotate their connection keys and
audit connected sites for unauthorized plugins, files, or admin accounts.
