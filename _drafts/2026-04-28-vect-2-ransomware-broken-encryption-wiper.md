---
title: "VECT 2.0 Ransomware Permanently Destroys Large Files Due to Broken Encryption"
date: 2026-04-28 21:25:57 +0000
categories: [Daily Signal]
tags: [ransomware, malware]
severity: medium
must_know: false
sources:
  - name: BleepingComputer
    url: https://www.bleepingcomputer.com/news/security/broken-vect-20-ransomware-acts-as-a-data-wiper-for-large-files/
---

Researchers have found that VECT 2.0 ransomware improperly reuses encryption nonces, causing it to permanently destroy large files rather than encrypt them. Victims who pay the ransom will still be unable to recover their large files because the data is overwritten, not locked.

Incident responders encountering VECT 2.0 should treat the infection as a destructive attack from the outset — engage backup recovery procedures immediately and do not assume payment will restore large files. This is a useful reminder that ransomware code quality is variable, and decryption is never guaranteed even when a ransom is paid.
