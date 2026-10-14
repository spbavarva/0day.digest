---
title: "Researchers Run Code Inside Windows SmartScreen's Protected VBS Enclave"
date: 2026-10-14 05:52:28 +0000
categories: [Daily Signal]
tags: [microsoft, vulnerability, appsec]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/10/four-byte-write-and-timing-bug-let.html
---

Security researchers used a four-byte write combined with a timing bug to
execute their own code inside a Windows VBS enclave, an isolated memory
region designed to stay sealed off even if the rest of the machine is
compromised.

The specific enclave they broke into handles passwords for a Windows
anti-phishing feature. The work was demonstrated in a lab as a proof of
concept rather than observed in the wild.
