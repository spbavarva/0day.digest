---
title: "FamousSparrow APT Targets Azerbaijani Oil and Gas Firm via Microsoft Exchange"
date: 2026-05-13 13:00:00 +0000
categories: [Daily Signal]
tags: [vulnerability, microsoft, rce, apt]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/azerbaijani-energy-firm-hit-by-repeated.html
  - name: Dark Reading
    url: https://www.darkreading.com/cyberattacks-data-breaches/china-famoussparrow-apt-south-caucasus-energy-firm
---

Bitdefender has attributed a multi-wave intrusion against an unnamed Azerbaijani
oil and gas company to FamousSparrow (UAT-9244), a China-linked APT. Attacks
ran from late December 2025 through late February 2026, using repeated
Microsoft Exchange exploitation as the initial access vector. FamousSparrow
historically targeted hospitality, telecom, and government sectors — this
marks an expansion into critical energy infrastructure. The group's persistence
and repeated-access pattern suggests intelligence gathering rather than
ransomware objectives. Organizations running OT or ICS environments adjacent to
IT networks should audit Exchange exposure and review lateral movement paths
between IT and operational segments.
