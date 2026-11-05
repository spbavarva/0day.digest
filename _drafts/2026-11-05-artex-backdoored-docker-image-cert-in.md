---
title: "Backdoored ARTEX Docker Image Exposes 62 Consoles to Root Access, CERT-In Warns"
date: 2026-11-05 08:42:03 +0000
categories: [Daily Signal]
tags: [supply-chain, container-security, rce]
severity: critical
must_know: true
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/backdoored-docker-image-for-artex-ai.html
---

India's CERT-In disclosed that a threat actor it tracks as Crafty Falcon is
targeting banking, financial services, and insurance organizations in the
country with a backdoored Docker image distributed for the ARTEX AI
platform. The compromised image has exposed 62 management consoles to
root access.

CERT-In describes the campaign as active and ongoing, and notes the actor
is using publicly available AI-driven offensive security tooling.
Organizations running ARTEX should audit their deployed container images
against a trusted source immediately.
