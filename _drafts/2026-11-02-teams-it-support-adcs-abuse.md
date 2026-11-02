---
title: "Attackers Pose as IT Support on Microsoft Teams to Abuse AD CS and Steal Data"
date: 2026-11-02 11:08:45 +0000
categories: [Daily Signal]
tags: [privilege-escalation, microsoft]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/11/attackers-pose-as-it-support-on.html
---

Microsoft found attackers posing as IT support staff over Microsoft Teams
to convince employees to hand over remote control of their PCs.

Once inside, the attackers exploited insecure Active Directory Certificate
Services configurations to obtain login certificates for privileged
accounts, including one belonging to a domain controller. Microsoft
investigated two such intrusions, one of which led to a company-wide
compromise.
