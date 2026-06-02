---
title: "Meta AI Confused Deputy Flaw Enables High-Profile Instagram Account Takeovers"
date: 2026-06-02 10:48:00 +0000
categories: [Daily Signal]
tags: [meta, llm, ai-safety, data-breach, phishing]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/meta-ai-hands-over-high-profile-instagram-accounts-to-hackers/
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/instagram-users-locked-out-after-meta-ai-abused-to-steal-accounts/
---

Attackers hijacked multiple high-profile Instagram accounts by exploiting a confused deputy weakness in Meta's AI-powered customer support chatbot. The attack was straightforward: the adversary asked the AI to link the target account to a new email address, successfully impersonating the legitimate owner without meaningful verification. Once linked, the attacker locked out the real owner. The flaw exposes a fundamental trust problem in AI-mediated account management — the model executed account-modification requests without sufficient identity validation. Meta has not confirmed a patch at time of writing; account owners should verify recovery options are set to personal, attacker-inaccessible contacts.
