---
title: "Brevo Supply Chain Attack Injects Malware Into 100,000 Websites"
date: 2026-09-18 09:46:57 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, cloud-security]
severity: critical
must_know: true
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/brevo-supply-chain-attack-injects-malware-into-100000-websites/
---

Attackers used a compromised Brevo API key to deploy a malicious
Cloudflare Worker that injected malicious scripts into roughly 100,000
websites using Brevo's marketing/email services. The compromise is a
supply chain attack at the platform level, affecting downstream sites
rather than Brevo's core infrastructure directly. Organizations using
Brevo should rotate API keys and audit any Cloudflare Worker deployments
tied to their account.
