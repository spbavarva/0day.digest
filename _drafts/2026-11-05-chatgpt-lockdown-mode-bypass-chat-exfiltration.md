---
title: "Researchers Bypass ChatGPT Lockdown Mode to Exfiltrate Chats Without User Interaction"
date: 2026-11-05 16:42:32 +0000
categories: [Daily Signal]
tags: [llm, openai, ai-safety, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/researchers-bypass-chatgpt-lockdown.html
---

Security researchers disclosed a now-patched vulnerability that could
bypass Lockdown Mode protections in OpenAI's ChatGPT, allowing chat data to
be exfiltrated without any user interaction. Lockdown Mode was introduced in
June 2026 as an optional setting to reduce data exfiltration risk from
prompt injection.

The flaw could have enabled silent chat data theft and phishing via prompt
injection before it was patched. Teams relying on Lockdown Mode as a
prompt-injection mitigation should confirm they're on a patched ChatGPT
version.
