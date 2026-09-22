---
title: "Hidden Meta Muse Setting Lets On-Device Malware Turn the AI Assistant Into a Backdoor"
date: 2026-09-22 06:33:57 +0000
categories: [Daily Signal]
tags: [ai-safety, llm, malware]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html
---

Security researcher Patrick Wardle published a proof-of-concept showing
that malware already running on a Mac can quietly take over Meta's Muse
AI assistant by changing a hidden setting.

Once changed, when the user taps the microphone and dictates a prompt,
the spoken words are redirected to the attacker instead of Meta. The
technique requires an existing malware foothold on the device — it's a
post-compromise persistence method, not a standalone remote exploit.
