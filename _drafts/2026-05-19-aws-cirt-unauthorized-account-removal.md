---
title: "AWS CIRT: Attackers Are Removing Accounts from AWS Organizations to Disable Guardrails"
date: 2026-05-19 21:34:25 +0000
categories: [Daily Signal]
tags: [aws, iam, cloud-security]
severity: medium
must_know: false
sources:
  - name: AWS Security Blog
    url: https://aws.amazon.com/blogs/security/cirt-insights-how-to-help-prevent-unauthorized-account-removals-from-aws-organizations/
---

AWS's Customer Incident Response Team has documented a trending attacker tactic: removing member
accounts from AWS Organizations to disable service control policies, break centralized logging, and
isolate blast radius. The post details specific misconfigurations that enable this attack and
architectural recommendations to prevent it, drawn from live incident response engagements.

Organizations using AWS Organizations should restrict the `organizations:RemoveAccountFromOrganization`
action via SCPs and IAM policies, and ensure CloudTrail logging cannot be silenced by account
removal. Treating organization management permissions with the same sensitivity as root credentials
is the core mitigation guidance.
