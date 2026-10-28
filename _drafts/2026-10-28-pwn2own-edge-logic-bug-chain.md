---
title: "Pwn2Own Edge Sandbox Escape Chain Relied on Logic Bugs Alone"
date: 2026-10-28 16:23:34 +0000
categories: [Daily Signal]
tags: [vulnerability, privilege-escalation, microsoft]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/researcher-reveals-how-logic-bugs-alone.html
---

Orange Tsai of DEVCORE published the full technical writeup of a logic-flaw
chain — involving no memory corruption — that turns a malicious web page
into code execution outside Microsoft Edge's sandbox. The chain won
$175,000 at Pwn2Own Berlin in May 2026; Microsoft fixed the underlying bugs
the day after the contest, so no unpatched systems remain exposed. The
writeup is a useful reference for defenders studying logic-bug exploitation
patterns in browser sandboxes.
