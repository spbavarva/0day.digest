---
title: "xAI Open-Sources Grok CLI After It Silently Uploaded Users' Files to the Cloud"
date: 2026-07-15 23:59:30 +0000
categories: [Daily Signal]
tags: [data-breach, llm, ai-safety]
severity: critical
must_know: true
sources:
  - name: Simon Willison
    url: https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything
---

xAI's Grok CLI coding agent, recently open-sourced as xai-org/grok-build, drew
backlash after users discovered that running it inside a directory could
upload the entire directory's contents to xAI's Google Cloud buckets. One
user reported running the tool in their home directory and having it upload
their SSH keys, password manager database, documents, photos, and videos.
xAI has not published an official technical explanation for the behavior.
Elon Musk responded to the backlash, stating that previously uploaded user
data would be handled "as a precautionary measure," though further
remediation details were not available in reporting. Anyone who has run the
Grok CLI in a directory containing credentials, SSH keys, or other sensitive
files should treat that data as exposed and rotate it.
