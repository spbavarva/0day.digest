---
title: "Red Team Case Study: Social Engineering to Tunneling Attacks Against a Government AI Chatbot"
date: 2026-05-18 12:00:00 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, appsec]
severity: medium
must_know: false
sources:
  - name: SentinelOne Labs
    url: https://www.sentinelone.com/blog/red-teaming-a-government-edubot/
---

SentinelOne's red team published a case study on attacking a government education AI chatbot, escalating from social engineering to advanced tunneling attacks in a single engagement. The exercise revealed that AI deployments inherit the attack surface of their underlying infrastructure — traditional network exploitation techniques remain viable even against AI-fronted systems. AI-specific defenses like content moderation and prompt filtering were bypassed through indirect methods. The study's central lesson: AI safety hardening that focuses only on content moderation leaves the underlying system exposed to practitioners who can route around content-layer controls.
