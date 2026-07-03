---
title: "How We Added WebAuthn to a Browser-Based RDP Client"
date: 2026-07-02 22:00:39 +0000
categories: [Daily Signal]
tags: [appsec]
severity: informational
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/webauthn-added-to-browser-based-rdp/
---

Unit 42 researchers detailed the reverse-engineering process behind adding
WebAuthn redirection support to a browser-based RDP client, reportedly the
first such client outside Windows to support it. WebAuthn redirection lets
hardware security keys and platform authenticators be used for
authentication inside remote desktop sessions. The write-up focuses on
protocol-level reverse engineering rather than a new vulnerability or
exploit.
