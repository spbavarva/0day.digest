---
title: "ChatGPhish: ChatGPT's Trust in Markdown Enables Prompt Injection and Phishing"
date: 2026-05-29 18:07:12 +0000
categories: [Daily Signal]
tags: [phishing, llm, vulnerability, openai, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html
---

Permiso Security disclosed a vulnerability dubbed ChatGPhish: the ChatGPT web renderer implicitly trusts Markdown-rendered links and images, allowing attacker-controlled web content summarized by ChatGPT to inject malicious Markdown into the response and redirect users to phishing pages.

The attack path involves a user asking ChatGPT to summarize a malicious web page; the page's content embeds Markdown that ChatGPT faithfully renders, including links and images pointing to attacker infrastructure. Because the final output appears within chatgpt.com, users are less likely to scrutinize the embedded links.

This is a classic indirect prompt injection scenario. Until OpenAI adds server-side sanitization of rendered Markdown, users should avoid asking ChatGPT to summarize untrusted URLs, particularly in contexts where the model has access to sensitive sessions or tools.
