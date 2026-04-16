---
title: "UAC-0247 Targets Ukrainian Clinics and Government with AgingFly Espionage Malware"
date: 2026-04-16 06:20:00 +0000
categories: [Daily Signal]
tags: [malware, data-breach]
severity: high
must_know: false
sources:
  - name: The Hacker News
    url: https://thehackernews.com/2026/04/uac-0247-targets-ukrainian-clinics-and.html
  - name: The Record (Recorded Future)
    url: https://therecord.media/aging-fly-espionage-campaign-targets-ukraine-emergency-services
---

CERT-UA has disclosed a campaign attributed to UAC-0247 targeting Ukrainian government
bodies and municipal healthcare institutions — primarily emergency clinics and hospitals —
between March and April 2026. The campaign deploys a newly documented malware family called
AgingFly, capable of stealing sensitive data from Chromium-based browsers and WhatsApp.

The targeting of healthcare and emergency services aligns with observed Russian cyber
operations against Ukrainian critical infrastructure. The data-theft focus on browsers and
messaging apps suggests the goal is credential and communication intelligence collection
rather than destructive impact.

CERT-UA IOCs and detection rules are available in the advisory. Organizations in Ukraine's
public sector should review endpoint telemetry for AgingFly indicators and enforce WhatsApp
Desktop restrictions on government-managed systems.
