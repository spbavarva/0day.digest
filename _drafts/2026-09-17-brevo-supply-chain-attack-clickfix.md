---
title: "Brevo Supply-Chain Attack Injects ClickFix Malware via Stolen Cloudflare API Key"
date: 2026-09-17 17:11:34 +0000
categories: [Daily Signal]
tags: [supply-chain, malware]
severity: critical
must_know: true
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/
---

Brevo confirmed that attackers stole a Cloudflare API key and used it to
inject malicious ClickFix scripts into JavaScript files it serves, which are
embedded on customer websites. The injected scripts distributed malware to
site visitors via the ClickFix technique — fake verification prompts that
trick users into running attacker-supplied commands.

Because many customer sites embed Brevo's JS for email capture and
marketing widgets, the compromise's reach extended well beyond Brevo's own
infrastructure. Anyone embedding Brevo scripts should review site logs for
unexpected script changes around the disclosure window and rotate any
shared API credentials.
