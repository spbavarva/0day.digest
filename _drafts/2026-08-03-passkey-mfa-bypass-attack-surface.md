---
title: "Novel Attack Surface Found in Passwordless Authentication"
date: 2026-08-03 10:00:35 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec, authentication]
severity: medium
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/
---

Unit 42 researchers detail a gap in how relying parties implement passkey-based
passwordless authentication: many fail to validate the "User Verified" flag
returned during the passkey ceremony. Where that check is skipped, a passkey
meant to combine possession and biometric/PIN factors is effectively reduced
to a single factor. The finding applies broadly across FIDO2/WebAuthn
deployments rather than one specific product. Practitioners should confirm
their relying-party code explicitly checks the UV flag rather than assuming
the authenticator enforces it.
