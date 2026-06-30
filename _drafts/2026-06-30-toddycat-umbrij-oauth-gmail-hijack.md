---
title: "ToddyCat APT Hijacks Gmail via OAuth Tokens with New Umbrij Tool"
date: 2026-06-30 10:00:13 +0000
categories: [Daily Signal]
tags: [malware, iam, google]
severity: high
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/toddycat-apt-umbrij-tool-and-oauth/120251/
---

Kaspersky's GReAT team detailed a new tool, Umbrij, used by the ToddyCat
APT group to compromise corporate Gmail accounts. Rather than stealing
passwords, the attack targets OAuth authorization tokens, letting the
group access victims' Google services without needing credentials or
triggering typical login alerts. The research is the latest installment
in Kaspersky's ongoing coverage of the campaign. Organizations should
audit OAuth app authorizations granted to third-party tools and revoke
any unrecognized grants.
