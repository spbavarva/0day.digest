---
title: "ShinyHunters Leaks Rockstar Games Analytics Data Stolen via Anodot Breach"
date: 2026-04-13 20:08:10 +0000
categories: [Daily Signal]
tags: [data-breach, malware]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/stolen-rockstar-games-analytics-data-leaked-by-extortion-gang/
---

The ShinyHunters extortion group has begun publicly leaking analytics data stolen from
Rockstar Games. The breach originated at Anodot, a third-party cloud analytics platform
used by Rockstar. After Rockstar declined to pay the ransom demand, ShinyHunters posted
the data to their leak site.

The incident highlights third-party supply chain risk through cloud analytics vendors:
Rockstar's data was not exfiltrated directly, but through a downstream provider. Organizations
using cloud analytics or data warehousing platforms should audit what production data is
accessible to those vendors, ensure breach notification obligations are clearly scoped in
vendor contracts, and evaluate whether sensitive business data should be masked or
pseudonymized before forwarding to third-party analytics systems.
