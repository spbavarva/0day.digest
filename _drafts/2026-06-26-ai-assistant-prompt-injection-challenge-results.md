---
title: "2,000 People Tried to Hack an AI Email Assistant — None Succeeded"
date: 2026-06-26 18:33:14 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, prompt-injection]
severity: informational
must_know: false
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/#atom-everything
---

Fernando Irarrázaval ran a public challenge at hackmyclaw.com, inviting
anyone to email his OpenClaw test instance and try to extract secrets it
held. Across roughly 6,000 attempts from about 2,000 participants — costing
$500 in token spend and triggering a Google account suspension from inbound
email volume — nobody managed to leak the secret. The underlying model was
Claude Opus 4.6, running with explicit system instructions barring it from
revealing credentials or modifying its own configuration files based on
email content.
