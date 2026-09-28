---
title: "Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent"
date: 2026-09-28 11:46:00 +0000
categories: [Daily Signal]
tags: [malware, container-security, llm, ai-safety]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html
---

A new botnet called Carbonato targets exposed Docker daemons and deploys
Hermes Agent, an open-source AI agent framework, according to ThreatDown.
The malware installs the framework unmodified, then overwrites its
persona file (SOUL.md) with a 39-line prompt that directs the agent to
execute tasks received over Telegram.

Using an unmodified legitimate AI agent framework as post-exploitation
tooling is a notable technique — it blends attacker logic into normal
agent behavior rather than shipping custom malware. Administrators should
ensure Docker daemons are not exposed to the internet without
authentication.
