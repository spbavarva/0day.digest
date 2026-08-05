---
title: "Leaked n8n API Tokens Exposed Live Instances to Credential Theft"
date: 2026-08-05 10:35:29 +0000
categories: [Daily Signal]
tags: [data-breach, github]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/leaked-n8n-api-tokens-exposed-live.html
---

GitGuardian researchers scanned public GitHub commits and found 321 live
n8n instances accepting API tokens that had been exposed in those commits.
In total they identified 4,576 unique credentials tied to 1,255 hostnames.

The researchers demonstrated four ways attackers could use the leaked
tokens to reach sensitive data and downstream credentials — without
exploiting any software vulnerability. Teams running n8n should rotate any
tokens that may have touched a public repository and audit workflow
credentials for downstream exposure.
</content>
