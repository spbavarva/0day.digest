---
title: "Malicious PyPI Packages Give Attackers Control of Telegram Bot Servers"
date: 2026-06-30 21:02:55 +0000
categories: [Daily Signal]
tags: [supply-chain, pypi, malware]
severity: high
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/malicious-pypi-packages-give-hackers-control-of-telegram-bot-servers/
---

A supply chain campaign active since last November has targeted Python
developers building Telegram bots with trojanized forks of the Pyrogram
library distributed via PyPI. The malicious packages give attackers the
ability to read arbitrary files on compromised servers. Developers who
installed Pyrogram-based Telegram bot dependencies from PyPI should audit
their dependency trees for the trojanized forks and rotate any credentials
that may have been exposed.
