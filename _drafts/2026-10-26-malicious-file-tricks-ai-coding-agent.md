---
title: "Malicious File Planted in Downloads Folder Tried to Trick AI Coding Agent Into Installing Malware"
date: 2026-10-26 06:03:48 +0000
categories: [Daily Signal]
tags: [llm, ai-safety, malware, npm]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/malicious-file-in-downloads-folder.html
---

Security firm Forever Security reported catching a malicious instruction
file planted in a developer's Downloads folder that attempted to make
their AI coding agent install a known-malicious npm package.

The company caught the attempt on a real customer's machine and stopped
the agent before any code ran. It could not determine how the file got
into the folder. The case illustrates how untrusted local files can
influence AI coding agent behavior.
