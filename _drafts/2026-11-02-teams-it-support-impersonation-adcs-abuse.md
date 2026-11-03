---
title: "Attackers Pose as IT Support on Microsoft Teams, Abuse AD CS to Steal Credentials"
date: 2026-11-02 11:08:45 +0000
categories: [Daily Signal]
tags: [privilege-escalation, phishing, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/attackers-pose-as-it-support-on.html
---

Microsoft disclosed a social-engineering campaign in which attackers
posed as IT support on Microsoft Teams to convince employees to grant
remote control of their PCs. Once inside, the attackers exploited
insecure Active Directory Certificate Services (AD CS) configurations
to obtain login certificates for privileged accounts, including one
for a domain controller.

Microsoft investigated at least two such intrusions, one of which led
to further compromise. Organizations should review AD CS template
permissions and train staff to verify IT support requests
out-of-band.
