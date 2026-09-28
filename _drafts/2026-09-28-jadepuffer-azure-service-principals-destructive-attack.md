---
title: "JADEPUFFER Attackers Used Compromised Azure Service Principals to Delete Cloud Resources"
date: 2026-09-28 09:08:21 +0000
categories: [Daily Signal]
tags: [ransomware, azure, cloud-security, malware]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html
---

A threat actor tracked as JADEPUFFER (Microsoft: Storm-3168) used
compromised Azure service principals to carry out a destructive attack
against an Azure tenant, deleting cloud-based storage, applications,
and databases, according to Microsoft research covered by The Hacker
News.

The attack took place over roughly 18 hours in early June 2026 and
involved reconnaissance, credential theft, and destructive operations
against core Azure resources. Microsoft calls it an evolution of the
actor's tradecraft. Organizations should audit service principal
credentials and permissions for signs of compromise.
