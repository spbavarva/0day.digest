---
title: "Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports"
date: 2026-09-14 17:58:16 +0000
categories: [Daily Signal]
tags: [vulnerability, xss]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html
---

A flaw in Telegram Desktop allowed a bot's message to plant hidden
JavaScript inside chats that users later exported to HTML files,
according to a writeup by security researchers at ExPatch published
September 12.

The malicious message looked ordinary in the app, but the embedded
script ran only when someone opened the exported HTML file in a web
browser, letting it copy every message in that export. Users who
export Telegram chat history to HTML should avoid opening those files
directly in a browser until Telegram addresses the issue.
