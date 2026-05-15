---
title: "TanStack npm Supply Chain Attack Hits Multiple AI Companies"
date: 2026-05-14 20:26:00 +0000
categories: [Daily Signal]
tags: [supply-chain, npm, pypi, openai, appsec]
severity: critical
must_know: true
sources:
  - name: The Record (Recorded Future)
    url: https://therecord.media/openai-asks-macos-users-to-update-tanstack-npm
---

The popular open-source TanStack JavaScript library has been compromised as part of an expanding
supply chain campaign. The attack also affects additional npm and PyPI packages linked to multiple
AI companies. OpenAI has asked its macOS users to update their software as a precautionary measure
in response to the incident.

TanStack is widely used for data tables, routing, and query management in JavaScript applications,
giving the compromise broad reach across the developer ecosystem. Organizations using TanStack or
the affected AI company packages should audit their dependency trees and rotate any credentials
or secrets that may have been exposed through compromised build pipelines.
