---
title: "DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing"
date: 2026-09-14 18:02:13 +0000
categories: [Daily Signal]
tags: [vulnerability, cloud-security]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html
---

Researchers have disclosed DDRop, a hardware attack that breaks memory
protection in Intel and AMD confidential computing by silently
dropping writes to a server's memory, so the processor keeps reading
old encrypted data as if it were current.

The attack requires an attacker who already controls the server's
software and can briefly access the machine physically to insert a
small circuit. This limits DDRop to attackers with privileged access
and physical proximity, but it undermines a core guarantee of Intel
TDX and AMD SEV-SNP confidential computing offerings used in cloud
environments.
