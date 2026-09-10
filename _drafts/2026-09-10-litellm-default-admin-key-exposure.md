---
title: "Nearly 1 in 10 Exposed LiteLLM Gateways Still Use the Default 'sk-1234' Admin Key"
date: 2026-09-10 07:12:55 +0000
categories: [Daily Signal]
tags: [llm, cspm, wiz, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/nearly-1-in-10-exposed-litellm-gateways.html
---

Wiz Research scanned internet-facing LiteLLM gateways in February and found
that nearly one in ten accepted "sk-1234," the example admin key published
in LiteLLM's own setup guide. LiteLLM is an open-source AI gateway that sits
between applications and the model providers a company pays for, and the
admin key grants full access to traffic passing through it.

Anyone holding the key on an exposed gateway can read requests and
responses, and potentially rack up usage on the victim's model provider
account. Operators should rotate the default admin key and restrict network
access to their LiteLLM gateways.
