---
title: "PCPJack Hijacks 230 AWS, Azure, and GCP Servers to Build Covert SMTP Relay Network"
date: 2026-06-05 05:34:19 +0000
categories: [Daily Signal]
tags: [malware, cloud-security, aws, azure, gcp]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/pcpjack-hijacks-230-aws-google-cloud.html
---

Threat actor PCPJack has compromised approximately 230 cloud servers across AWS, Google Cloud, and
Azure, quietly converting them into SMTP proxy nodes for a covert email relay network. Compromised
servers are synced to a downstream consumer every five minutes, enabling high-volume spam or phishing
at scale behind legitimate cloud provider IP ranges. The attack pattern is consistent with credential
stuffing or API key exposure followed by lateral movement within the tenant. Cloud teams should audit
SMTP egress on port 25/587, review compute instances for unexpected processes, and rotate cloud
credentials if anomalous activity is detected.
