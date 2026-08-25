---
title: "Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin Access"
date: 2026-08-25 08:34:07 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html
---

Attackers are actively exploiting two unauthenticated authentication bypass
vulnerabilities in the Xecurify miniOrange SAML 2.0 Single Sign-On plugin
for WordPress, allowing sign-in as any user including administrators. The
flaws, disclosed by Patchstack, are tracked as CVE-2026-61979 (CVSS 8.1, an
unauthenticated privilege escalation) and CVE-2026-15981. Sites running the
miniOrange SAML SSO plugin should update immediately and check for
unauthorized admin accounts or unexpected plugin and theme changes.
