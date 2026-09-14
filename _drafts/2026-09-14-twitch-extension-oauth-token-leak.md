---
title: "Malicious Twitch Browser Extension Leaks OAuth Tokens From ~31,000 Users"
date: 2026-09-14 07:24:39 +0000
categories: [Daily Signal]
tags: [data-breach, malware]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/09/malicious-twitch-browser-extension.html
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/twitch-extension-with-30k-installs-exposes-users-oauth-tokens/
---

A cross-store browser extension called "Twitch Enhanced Viewer |
JeetBot," available on the official Chrome and Firefox add-on stores,
sends users' Twitch OAuth session tokens to a commercial bot service
operated out of Russia. BleepingComputer separately put install counts
around 30,000.

Users who installed the extension should remove it and revoke Twitch
session tokens via account security settings, since a leaked OAuth
token can be used to act on the victim's account without their
password.
