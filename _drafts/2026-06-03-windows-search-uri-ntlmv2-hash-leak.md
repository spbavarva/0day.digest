---
title: "Unpatched Windows Search URI Flaw Leaks NTLMv2 Hashes"
date: 2026-06-03 10:18:52 +0000
categories: [Daily Signal]
tags: [vulnerability, zero-day, microsoft, cve]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/06/unpatched-windows-search-uri.html
---

Huntress researchers disclosed an unpatched flaw in the Windows search: URI handler that can coerce NTLMv2 hash disclosure from any user who clicks a crafted link, requiring no further interaction. The vulnerability mirrors CVE-2026-33829, which abused the ms-screensketch: URI handler in the Snipping Tool. Captured NTLMv2 hashes can be cracked offline or relayed in pass-the-hash attacks for lateral movement. Microsoft has not yet issued a patch. Recommended mitigations include blocking outbound NTLM over SMB at the network perimeter, enforcing SMB signing across the environment, and treating unexpected search: URI links as phishing vectors.
