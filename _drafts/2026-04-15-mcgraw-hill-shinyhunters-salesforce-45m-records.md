---
title: "ShinyHunters Claims 45 Million McGraw Hill Records via Salesforce Misconfiguration"
date: 2026-04-15 14:28:00 +0000
categories: [Daily Signal]
tags: [data-breach, cloud-security]
severity: critical
must_know: true
sources:
  - name: The Record (Recorded Future)
    url: https://therecord.media/mcgraw-hill-data-leak-tied-to-salesforce-misconfiguration
---

Educational publisher McGraw Hill has confirmed a data leak tied to a Salesforce
misconfiguration after ShinyHunters claimed to have stolen 45 million Salesforce records and
threatened to publish the data by April 14 if a ransom was not paid. McGraw Hill attributed the
exposure to a misconfiguration in its Salesforce environment rather than a direct breach of core
systems.

The incident underscores the risk of Salesforce misconfiguration at scale, particularly in
organizations managing large volumes of student and customer data. ShinyHunters has a track
record of monetizing bulk cloud data extractions, making follow-on credential stuffing and
phishing a likely downstream risk for affected individuals.

Organizations using Salesforce at scale should audit object-level sharing rules, guest user
access, and field-level security configurations via Salesforce's Security Health Check and
monitor event logs for anomalous bulk data export activity.
