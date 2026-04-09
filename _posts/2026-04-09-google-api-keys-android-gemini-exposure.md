---
title: "Hardcoded Google API Keys in Android Apps Expose Gemini AI Endpoints"
date: 2026-04-09 12:26:50 +0000
categories: [Daily Signal]
tags: [google, vulnerability, appsec, llm]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/google-api-keys-in-android-apps-expose-gemini-endpoints-to-unauthorized-access/
---

Dozens of Google API keys hardcoded into Android applications can be extracted from decompiled
APKs, granting unauthorized access to all Gemini AI endpoints. The exposed keys allow attackers
to query Gemini models, potentially abusing compute quota at the application owner's expense or
accessing data routed through the API.

This is a credential hygiene issue reproducible at scale: developers embedding long-lived API
keys directly in mobile app bundles. Developers should rotate any exposed keys immediately,
adopt short-lived tokens or server-side proxying, and enforce API key restrictions (IP/referrer
allowlists) to limit blast radius.
