---
title: "New Threat Actor UNC6783 Steals Enterprise Zendesk Tickets via BPO Supply Chain"
date: 2026-04-08 21:46:27 +0000
categories: [Daily Signal]
tags: [data-breach, phishing, supply-chain]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/google-new-unc6783-hackers-steal-corporate-zendesk-support-tickets/
---

Google's threat intelligence team is tracking UNC6783, a new threat actor that compromises business process outsourcing (BPO) providers to pivot into high-value enterprise targets across multiple sectors. The group specifically exfiltrates Zendesk support tickets, which frequently contain sensitive customer data, internal credentials, and unredacted incident details.

The BPO vector bypasses normal third-party security controls because outsourced support providers are granted broad access to helpdesk systems by design. Enterprises should scope Zendesk access granted to outsourced providers, enable audit logging on support ticket exports, and include BPO partners in third-party risk reviews.
