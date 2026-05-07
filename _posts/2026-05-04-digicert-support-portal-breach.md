---
title: "DigiCert Support Portal Hacked via Malware; Certificates Revoked"
date: 2026-05-04 12:46:53 +0000
categories: [Daily Signal]
tags: [malware, data-breach, pki]
severity: high
must_know: false
sources:
  - name: SecurityWeek
    url: https://www.securityweek.com/digicert-revokes-certificates-after-support-portal-hack/
---

Attackers breached DigiCert's internal customer support portal after delivering malware through a customer chat channel that infected a support analyst's system. DigiCert subsequently revoked customer certificates as a precautionary measure following the portal compromise.

DigiCert is one of the largest certificate authorities globally; its support portal contains customer account data and certificate management interfaces. Certificate revocations can cause service disruptions for affected customers if replacement certificates are not reissued promptly. Organizations using DigiCert should verify whether their certificates were among those revoked, reissue if necessary, and monitor for any unauthorized certificate operations during the breach window.

The attack vector — malware delivered through a legitimate customer support chat — is a reminder that support channel interactions are an underappreciated initial access surface.
