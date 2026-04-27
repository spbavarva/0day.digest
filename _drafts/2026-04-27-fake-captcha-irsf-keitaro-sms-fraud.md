---
title: "Fake CAPTCHA Campaign Linked to 120 Keitaro Instances Drives Large-Scale IRSF SMS Fraud"
date: 2026-04-27 06:33:00 +0000
categories: [Daily Signal]
tags: [phishing, malware, fraud]
severity: medium
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/fake-captcha-irsf-scam-and-120-keitaro.html
---

Infoblox researchers uncovered a large-scale telecom fraud operation using fake CAPTCHA pages to trick users into triggering international text messages, generating illicit revenue through International Revenue Share Fraud (IRSF). The operation is linked to approximately 120 Keitaro traffic distribution system instances.

IRSF exploits premium-rate phone number schemes where the attacker earns revenue per international SMS triggered by the victim. The fake CAPTCHA causes victims to unknowingly initiate the SMS. Telecom providers and enterprises with SMS-capable infrastructure should monitor for unexpected international messaging volume. Block known Keitaro domains and apply rate limiting on SMS-triggering user actions.
