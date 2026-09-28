---
title: "Carbonato Botnet Deploys Hermes AI Agent on Hacked Docker Hosts"
date: 2026-09-28 11:46:00 +0000
categories: [Daily Signal]
tags: [malware, container-security, llm]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html
---

A botnet called Carbonato is compromising exposed Docker daemons to
deploy an open-source AI agent framework called Hermes Agent, according
to research from ThreatDown covered by The Hacker News.

The implant installs the Hermes framework unmodified, then overwrites
its SOUL.md persona file with a 39-line prompt directing it to execute
commands received over Telegram. The botnet also steals AI API keys
from the compromised hosts. Exposed Docker daemons should not be
reachable from the internet.
