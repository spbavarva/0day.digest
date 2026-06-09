---
title: "Unit 42: Attackers Impersonate IT Support in Microsoft Teams Phishing Campaigns"
date: 2026-06-08 23:00:45 +0000
categories: [Daily Signal]
tags: [phishing, microsoft, social-engineering]
severity: medium
must_know: false
sources:
  - name: Unit 42 (Palo Alto)
    url: https://unit42.paloaltonetworks.com/microsoft-teams-phishing/
---

Unit 42 documents an escalating pattern of attackers using Microsoft Teams to
impersonate internal IT support personnel, exploiting the implicit trust users
extend to messages arriving on corporate collaboration platforms. The technique
bypasses traditional email-based phishing defenses and is effective against
users trained to scrutinize email but not internal chat. Defenders should
configure Teams to restrict or flag external tenant messaging, enable
conditional-access policies for Teams login, and train users to verify any
credential or remote-access request through a second, out-of-band channel
regardless of which platform it arrives on.
