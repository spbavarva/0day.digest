---
title: "Grafana Confirms Data Breach Claimed by Coinbase Cartel"
date: 2026-05-18 08:34:59 +0000
categories: [Daily Signal]
tags: [data-breach, grafana]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/
---

Grafana has confirmed a data breach after the Coinbase Cartel — a cybercrime group linked to
ShinyHunters, Scattered Spider, and Lapsus$ — claimed to have stolen data. Grafana's observability
platform is widely deployed for infrastructure dashboards and monitoring across engineering and
security teams, making its credential and configuration data a valuable target.

The scope of exfiltrated data has not been fully detailed publicly. Organizations using Grafana Cloud
or Grafana Enterprise should review and rotate API tokens, service account credentials, and any
secrets stored in Grafana datasource configurations. The Coinbase Cartel's known TTPs include
credential theft and SIM swapping.
