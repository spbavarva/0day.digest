---
title: "Attackers Weaponize Amazon SES to Send Phishing Emails That Pass Security Filters"
date: 2026-05-04 10:00:23 +0000
categories: [Daily Signal]
tags: [phishing, aws, cloud-security]
severity: medium
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/
---

Kaspersky's GReAT team documented phishing and business email compromise campaigns abusing Amazon Simple Email Service (SES) to send malicious messages that bypass traditional email security controls. Because SES is a legitimate AWS cloud service with established sending reputation, emails routed through it have a higher likelihood of passing SPF, DKIM, and DMARC authentication checks.

The technique reduces attacker infrastructure costs and improves deliverability over self-hosted mail servers, which typically carry low reputation scores. Security teams should move beyond authentication-only email filtering and add behavioral analysis, anomaly detection on sender patterns, and elevated scrutiny for SES-originated messages targeting employees with financial authority or system access. Training users to recognize the SES routing as a possible indicator is also advisable.
