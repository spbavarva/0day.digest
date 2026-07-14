---
title: "Grok Build Uploaded Entire Git Repositories to xAI Storage, Not Just Files It Read"
date: 2026-07-14 09:02:48 +0000
categories: [Daily Signal]
tags: [llm, appsec]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html
---

xAI's Grok Build coding CLI was found uploading entire Git repositories — full commit history included — to a Google Cloud Storage bucket operated by xAI, rather than just the specific files a coding task required. A researcher publishing as cereblab, testing version 0.2.93, intercepted one of these uploads and recovered a file the agent had explicitly been instructed not to access. Because commit history can contain secrets or sensitive code no longer present in the working tree, the behavior significantly widens the tool's effective data-access footprint. Users of Grok Build should assume any repository opened with the tool has its full git history exposed to xAI's infrastructure until the behavior is addressed.
