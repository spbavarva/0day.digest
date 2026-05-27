---
title: "Microsoft Copilot Cowork Allows Attacker-Controlled Email Images to Exfiltrate User Files"
date: 2026-05-26 15:36:48 +0000
categories: [Daily Signal]
tags: [llm, microsoft, appsec, ai-safety]
severity: high
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything
---

Microsoft Copilot Cowork, an agentic product that can send emails on behalf of users, was found to enable data exfiltration via a chained attack. Agents can send emails to the user's own inbox without approval; those messages can contain external images that trigger outbound HTTP requests, allowing an attacker to embed a crafted URL that leaks user data to an attacker-controlled server when the message is opened.

The attack relies on prompt injection to instruct the agent to send a malicious email, then on the mail client rendering external images without isolation. This is a textbook agentic exfiltration primitive that grows more dangerous as AI agents gain broader file and email access. Users should disable external image loading in affected Copilot Cowork contexts until Microsoft confirms a fix.
