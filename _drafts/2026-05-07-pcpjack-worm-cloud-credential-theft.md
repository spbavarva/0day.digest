---
title: "PCPJack Worm Steals Cloud Credentials While Evicting TeamPCP"
date: 2026-05-07 18:35:50 +0000
categories: [Daily Signal]
tags: [malware, cloud-security]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/new-pcpjack-worm-steals-credentials-cleans-teampcp-infections/
---

PCPJack is a new malware framework targeting exposed cloud infrastructure to steal credentials while
actively removing TeamPCP infections from compromised hosts — effectively displacing a rival botnet
to claim the resource. It makes innovative use of parquet files for stealthy, pre-validated target
discovery across AWS, GCP, and Azure environments. The credential theft and multi-cloud targeting
make PCPJack a direct threat to cloud-native organizations. Teams should audit IAM credential
exposure, rotate any cloud secrets stored in accessible locations, and review CloudTrail or
equivalent logs for anomalous API access patterns.
