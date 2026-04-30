---
title: "EtherRAT Campaign Uses GitHub Facades and SEO Poisoning to Target Enterprise Admins"
date: 2026-04-30 11:30:00 +0000
categories: [Daily Signal]
tags: [malware, github, phishing]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/etherrat-distribution-spoofing.html
---

Atos Threat Research Center identified an active campaign distributing EtherRAT through GitHub repositories that convincingly impersonate legitimate administrative utilities. The operation uses SEO manipulation (Search Engine Order poisoning) to surface malicious repos when enterprise administrators, DevOps engineers, and security analysts search for common tools. The campaign specifically targets high-privilege accounts.

EtherRAT provides persistent remote access to compromised hosts. The technique — weaponizing GitHub's trusted reputation combined with SEO to intercept organic search-driven tool downloads — is a notable evolution of the typosquatting model. Organizations should enforce a policy of downloading admin utilities only from verified vendor sources, not arbitrary GitHub repos, and should verify hashes where available.
