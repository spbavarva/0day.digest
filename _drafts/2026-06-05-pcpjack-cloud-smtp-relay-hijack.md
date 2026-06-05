---
title: "PCPJack Hijacks 230 AWS, GCP, and Azure Servers to Build Covert SMTP Relay Network"
date: 2026-06-05 05:34:19 +0000
categories: [Daily Signal]
tags: [cloud-security, aws, gcp, azure, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/pcpjack-hijacks-230-aws-google-cloud.html
---

The threat actor PCPJack has compromised 230 cloud servers across AWS, Google Cloud, and
Azure, quietly converting business compute instances into SMTP proxies to form a covert
email relay network. Compromised servers span the US, Europe, and Asia; each is verified
for mail relay capability and synced to downstream consumers every five minutes, enabling
high-volume spam or phishing operations that appear to originate from legitimate business
infrastructure. Cloud operators should audit outbound SMTP egress (ports 25, 465, 587),
review IAM for unexpected service accounts, and check compute inventories for instances
they didn't provision.
