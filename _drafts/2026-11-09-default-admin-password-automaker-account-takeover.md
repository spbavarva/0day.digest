---
title: "Default 'admin:admin' Password Let Researchers Hack Two Automakers' Connected Cars"
date: 2026-11-09 11:27:53 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/default-adminadmin-server-password.html
---

Two security researchers found that the login systems behind two car
brands' mobile apps could be fully taken over due to a default
'admin:admin' server password.

Both apps signed customers in through ForgeRock, an identity platform
now part of Ping Identity. Access to those servers let the researchers
reach any customer's account and, for owners with a connected car,
unlock the doors and start the engine remotely.

The finding highlights how a single default credential on a backing
identity provider can cascade into physical-world impact for
connected-vehicle customers.
