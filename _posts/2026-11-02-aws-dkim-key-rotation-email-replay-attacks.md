---
title: "AWS Details Email Replay Attacks That Bypass DKIM Key Rotation"
date: 2026-11-02 18:06:28 +0000
categories: [Daily Signal]
tags: [phishing, cloud-security, aws]
severity: informational
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/beyond-dkim-key-rotation-understanding-email-replay-attacks/
---

AWS Security published guidance on "email replay attacks," where
previously legitimate, DKIM-signed messages are resent from
unauthorized IP addresses, causing DMARC reports to show passing DKIM
verification for mail the domain owner never sent. Rotating the DKIM
key alone doesn't fix this, since the replayed message was signed
before rotation.

The post outlines detection signals in DMARC aggregate reports and
mitigation guidance for domain administrators running DKIM/DMARC
email authentication.
