---
title: "Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws"
date: 2026-07-10 14:19:50 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, vulnerability, rce, privilege-escalation]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/researcher-details-whatsapp-to-host.html
---

A researcher detailed an attack chain combining three now-patched flaws
in OpenClaw, a personal AI assistant, that together could let an attacker
move from a WhatsApp message to credential theft, privilege escalation,
and arbitrary code execution on the host machine. One of the flaws,
GHSA-hjr6-g723-hmfm, carries a CVSS score of 8.8. All three issues have
been fixed in current releases. Users of OpenClaw should confirm they are
on a patched version, since the chain illustrates how AI assistants with
messaging and host-level integrations can widen the attack surface.
