---
title: "New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens"
date: 2026-07-17 17:12:23 +0000
categories: [Daily Signal]
tags: [malware, cloud-security, iam, kubernetes]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/new-nadmesh-botnet-hunts-exposed-ai.html
---

A Go-based botnet called NadMesh, first spotted in early July, is scanning the internet via Shodan for exposed AI infrastructure — ComfyUI, Ollama, n8n, Open WebUI, Langflow, and Gradio instances that teams stand up quickly and firewall late. The operator's own dashboard claims 3,811 unique stolen AWS keys, alongside harvested Kubernetes tokens. Teams running local model runners or workflow builders should confirm these services aren't exposed to the internet without authentication, and rotate any credentials that may have been reachable.
