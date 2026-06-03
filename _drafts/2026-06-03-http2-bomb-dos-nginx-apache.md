---
title: "HTTP/2 Bomb: Remote DoS Hits NGINX, Apache, IIS, Envoy, and Cloudflare by Default"
date: 2026-06-03 08:33:35 +0000
categories: [Daily Signal]
tags: [vulnerability, appsec, cloud-security]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html
---

Researchers disclosed HTTP/2 Bomb, a remote denial-of-service technique that chains an HTTP/2 compression bomb with a Slowloris-style connection hold to exhaust server resources in seconds. The vulnerable behavior exists in the default HTTP/2 configuration of NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora — covering the majority of production web infrastructure. Notably, the vulnerability was discovered using OpenAI Codex, adding an AI-assisted research angle. Organizations should apply vendor-issued patches as they become available and consider interim hardening measures including HTTP/2 connection timeout reductions and rate limiting on HEADERS frames. No authentication or special privileges are required to trigger the exploit.
