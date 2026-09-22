---
title: "Meta Patches Muse Zero-Day That Let Attackers Hijack the AI Assistant"
date: 2026-09-22 11:53:58 +0000
categories: [Daily Signal]
tags: [zero-day, meta, llm, vulnerability]
severity: high
must_know: false
sources:
  - name: The Verge AI
    url: https://www.theverge.com/tech/998679/meta-muse-patch-zero-day-exploit-ai-agent
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html
---

Security researcher Patrick Wardle found a zero-day in Meta's Muse macOS
app that let malware already running on a Mac quietly take over the AI
assistant, using the broad access its owner had granted the app.

The exploit worked by flipping a hidden, undocumented setting so that when
a user dictated a prompt via microphone, the words went to the attacker
instead of Meta's servers. Meta has issued a patch after the PoC was
released on September 21.
