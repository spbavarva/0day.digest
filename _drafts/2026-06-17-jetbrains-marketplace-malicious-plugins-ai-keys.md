---
title: "Malicious JetBrains Plugins Steal AI API Keys, Chrome Extensions Capture Chatbot Chats"
date: 2026-06-17 09:38:46 +0000
categories: [Daily Signal]
tags: [supply-chain, malware, llm]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html
---

Researchers flagged a coordinated campaign on the JetBrains Marketplace
publishing at least 15 malicious plugins posing as AI coding assistants
built on DeepSeek and other LLMs, offering chat, commit messages, code
review, and bug-finding features while exfiltrating victims' AI provider API
keys. A parallel set of malicious Chrome extensions captures full chatbot
conversation logs from browser-based AI tools. Developers should audit
installed JetBrains plugins and Chrome extensions for unfamiliar AI-assistant
tools and rotate any API keys used on affected machines.
