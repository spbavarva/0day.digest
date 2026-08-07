---
title: "Malware Can Abuse Windows Hello for Business Keys for Persistent Entra ID Access"
date: 2026-08-07 08:52:11 +0000
categories: [Daily Signal]
tags: [privilege-escalation, iam, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/08/malware-can-abuse-windows-hello-for.html
---

Entra ID researcher Dirk-jan Mollema demonstrated that malware already
running in a signed-in Windows session can silently use the victim's
Windows Hello for Business key to authenticate to Microsoft Entra ID. The
attacker can then establish longer-term cloud access, register a
device it controls, and obtain a Primary Refresh Token. Depending on
tenant policy, the attacker may also add further authentication methods.
