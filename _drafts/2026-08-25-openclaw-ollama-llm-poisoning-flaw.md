---
title: "Networking Flaw in NVIDIA's OpenClaw Allows LLM Poisoning via Ollama API"
date: 2026-08-25 19:50:16 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, vulnerability]
severity: high
must_know: false
sources:
  - name: Dark Reading
    url: https://www.darkreading.com/cyber-risk/nemo-claw-networking-llm-poisoning-openclaw
---

A security bug dubbed "Nemo(Claw)" in NVIDIA's OpenClaw lets attackers gain
unauthenticated access to the local model server through the Ollama API.
That access can be used to persistently corrupt an AI agent running on the
affected host.

The issue stems from how OpenClaw exposes networking to the local Ollama
instance rather than a flaw in Ollama itself. Deployments running OpenClaw
alongside Ollama should restrict network exposure to the API until a fix is
available.
