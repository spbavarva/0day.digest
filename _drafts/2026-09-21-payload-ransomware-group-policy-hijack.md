---
title: "Group Policy Hijacked: PAYLOAD Ransomware Weaponizes Active Directory GPO"
date: 2026-09-21 10:00:40 +0000
categories: [Daily Signal]
tags: [ransomware, privilege-escalation]
severity: high
must_know: false
sources:
  - name: Securelist (Kaspersky GReAT)
    url: https://securelist.com/tr/payload-ransomware-via-group-policy/121335/
---

Kaspersky's GERT team analyzed PAYLOAD ransomware, an operation that
departs from typical ransomware design: it is encryptionless and
binary-less.

Instead of deploying an encryption payload, the operators abuse Active
Directory's Group Policy Object (GPO) management mechanisms to achieve
their objectives across a compromised environment.

Further technical detail on the specific GPO abuse techniques and
detection guidance was not included in the source summary.
